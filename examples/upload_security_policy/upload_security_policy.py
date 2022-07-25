import argparse
import csv
import getpass
import os

from pyedgeconnect import Orchestrator

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    "-c",
    "--csv",
    help="specify source csv file for security rules",
    type=str,
    required=True,
)
parser.add_argument(
    "-a",
    "--appliance",
    help="specify appliance name to apply rules to",
    type=str,
)
parser.add_argument(
    "-tg",
    "--templategroup",
    help="specify template group name to apply rules to",
    type=str,
)
parser.add_argument(
    "-dll",
    "--denyloglevel",
    help="log level in template for deny all log events",
    type=int,
)
parser.add_argument(
    "-m",
    "--merge",
    help="merge new rules with any existing rules",
    action=argparse.BooleanOptionalAction,
)
parser.add_argument(
    "-o",
    "--orch",
    help="specify Orchestrator URL",
    type=str,
)
args = parser.parse_args()

# CSV file for generating security rules
csv_filename = vars(args)["csv"]

# Appliance name to apply security rules to
appliance_name = vars(args)["appliance"]

# TemplateGroup to create and apply security rules to
template_group_name = vars(args)["templategroup"]

if vars(args)["denyloglevel"] is not None:
    deny_all_log_level = vars(args)["denyloglevel"]
else:
    deny_all_log_level = 2

# Check if appliance or templategroup has been specified and exit on
# conflicting conditions, can only use one
if appliance_name is None and template_group_name is None:
    print("Must specify appliance or template group to create rules!")
    exit()
elif appliance_name is not None and template_group_name is not None:
    print("Cannot specify appliance and template group at same time!")
    exit()
else:
    pass

# Merge set to ``True`` will merge with existing rules on appliance.
# Rules in same zone pair with same priority will be overwritten even
# with Merge.
if vars(args)["merge"] is not None:
    merge = vars(args)["merge"]
else:
    merge = False

# Set Orchestrator FQDN/IP via arguments, environment variable,
# or user input
if vars(args)["orch"] is not None:
    orch_url = vars(args)["orch"]
elif os.getenv("ORCH_URL") is not None:
    orch_url = os.getenv("ORCH_URL")
else:
    orch_url = input("Orchstrator IP or FQDN: ")

# Set Orchestrator API Key via environment variable or user input
if os.getenv("ORCH_API_KEY") is not None:
    orch_api_key = os.getenv("ORCH_API_KEY")
else:
    orch_api_key_input = input("Orchstrator API Key (enter to skip): ")
    if len(orch_api_key_input) == 0:
        orch_api_key = None
        # Set user and password if present in environment variable
        orch_user = os.getenv("ORCH_USER")
        orch_pw = os.getenv("ORCH_PASSWORD")
    else:
        orch_api_key = orch_api_key_input

# Instantiate Orchestrator with ``log_console`` enabled for
# printing log messages to terminal
orch = Orchestrator(
    orch_url,
    api_key=orch_api_key,
    log_console=True,
    verify_ssl=False,
)

# If not using API key, login to Orchestrator with username/password
if orch_api_key is None:
    # If username/password not in environment variables, prompt user
    if orch_user is None:
        orch_user = input("Enter Orchestrator username: ")
        orch_pw = getpass.getpass("Enter Orchestrator password: ")
    # Check if multi-factor authentication required
    mfa_prompt = input("Are you using MFA for this user (y/n)?: ")
    if mfa_prompt == "y":
        orch.send_mfa(orch_user, orch_pw, temp_code=False)
        token = input("Enter MFA token: ")
    else:
        token = ""
    # Login to Orchestrator
    confirm_auth = orch.login(orch_user, orch_pw, mfacode=token)
    # Check that user/pass authentication works before proceeding
    if confirm_auth:
        pass
    else:
        print("Authentication to Orchestrator Failed")
        exit()
# If API key specified, check that key is valid before proceeding
else:
    confirm_auth = orch.get_orchestrator_hello()
    if confirm_auth != "There was an internal server error.":
        pass
    else:
        print("Authentication to Orchestrator Failed")
        exit()


if appliance_name is not None:
    # retrieve all appliances in Orchestrator to be able correlate
    # specified hostname to respective appliance id
    appliances = orch.get_appliances()

    ne_pk = None
    # Find NEPK of specified appliance
    for appliance in appliances:
        if appliance_name == appliance["hostName"]:
            ne_pk = appliance["nePk"]

    # Check that appliance was found by hostname before continuing
    if ne_pk is None:
        print(
            f"""
            FAILED TO PROCESS:
            Appliance: {appliance_name} was not found in Orchestrator
            """
        )

# Get overlay id's to correlate overlay names if used in security policy
raw_overlays = orch.get_all_overlays_config()
overlays = {}

# Map new dictionary with key/value pair of Overlay name to Overlay id
for overlay in raw_overlays:
    overlays[overlay["name"]] = overlay["id"]

# If template group is chosen set templateApply value base values
if template_group_name is not None:

    # Retrieve existing Template Groups on Orchestrator to check for
    # duplicate names
    existing_template_groups = orch.get_all_template_groups()
    # If Template Group name already exists, exit to avoid any conflict
    # with existing Template Group
    for group in existing_template_groups:
        if template_group_name == group["name"]:
            print(
                f"WARNING: Template Group {template_group_name}"
                "already exists in Orchestrator!"
            )
            if orch_api_key is None:
                orch.logout()
            exit()

    # Instantiate TemplateGroup data object
    template_group = {
        "name": template_group_name,
        "selectedTemplateNames": ["securityMaps"],
        "templates": [{"name": "securityMaps", "valObject": {}}],
    }

    # Initial security policy to add rules to
    security_map = {
        "data": {},
        "options": {
            "merge": merge,
            "templateApply": True,
        },
        "settings": {
            "map1": {
                # Log 'Deny All' Events at Level
                "imp_fw_drop": deny_all_log_level
            }
        },
    }
# Initial direct to appliance security policy to add rules to
else:
    security_map = {
        "data": {},
        "options": {
            "merge": merge,
            "templateApply": False,
        },
    }

# Instantiate dictionary for rules to be inserted to
# This will later be nested into the security map object
map_details = {}

# Process rules from CSV for upload
with open(csv_filename, encoding="utf-8-sig") as csvfile:
    ruleset = csv.DictReader(csvfile)

    # Set initial row number for row identification of data
    # First row is headers
    rule_number = 2

    # Get configured firewall zones for ingesting rules
    raw_zones = orch.get_zones()
    zones = {}

    # Map new dictionary with key/value pair of Zone name to Zone ID
    for zone in raw_zones:
        zones[raw_zones[zone]["name"]] = zone

    # For each row in configuration file, add to security rules
    for rule in ruleset:
        try:
            # Set rule priority
            rule_priority = rule["rule_priority"]

            # Instantiate match criteria for security rule
            match_criteria = {}

            # To identify valid values for each of the security
            # parameters, retrieve an existing appliance security policy
            # either through Orchestrator or directly from an appliance
            #
            # orch.appliance_get_api(
            #     ne_pk=ne_pk,
            #     url="securityMaps",
            # )
            # OR
            #
            # ec.get_appliance_security_policy_map()

            # Check CSV file for all possible security parameters
            # and add to policy object if they exist

            # if acl exists and is not blank, set the value
            if rule.get("acl") and rule.get("acl").strip():
                match_criteria["acl"] = rule["acl"]
            else:
                match_criteria["acl"] = ""
            # if src_ip exists and is not blank, set the value
            if rule.get("src_ip") and rule.get("src_ip").strip():
                match_criteria["src_ip"] = rule["src_ip"]
            else:
                pass
            # if dst_ip exists and is not blank, set the value
            if rule.get("dst_ip") and rule.get("dst_ip").strip():
                match_criteria["dst_ip"] = rule["dst_ip"]
            else:
                pass
            # if src_addrgrp_groups exists and is not blank, set the value
            if (
                rule.get("src_addrgrp_groups")
                and rule.get("src_addrgrp_groups").strip()
            ):
                match_criteria["src_addrgrp_groups"] = rule[
                    "src_addrgrp_groups"
                ]
            else:
                pass
            # if dst_addrgrp_groups exists and is not blank, set the value
            if (
                rule.get("dst_addrgrp_groups")
                and rule.get("dst_addrgrp_groups").strip()
            ):
                match_criteria["dst_addrgrp_groups"] = rule[
                    "dst_addrgrp_groups"
                ]
            else:
                pass
            # if either_addrgrp_groups exists and is not blank, set the value
            if (
                rule.get("either_addrgrp_groups")
                and rule.get("either_addrgrp_groups").strip()
            ):
                match_criteria["either_addrgrp_groups"] = rule[
                    "either_addrgrp_groups"
                ]
            else:
                pass
            # if either_ip exists and is not blank, set the value
            if rule.get("either_ip") and rule.get("either_ip").strip():
                match_criteria["either_ip"] = rule["either_ip"]
            else:
                pass
            # if protocol exists and is not blank, set the value
            if rule.get("protocol") and rule.get("protocol").strip():
                match_criteria["protocol"] = rule["protocol"]
            else:
                pass
            # if src_port exists and is not blank, set the value
            if rule.get("src_port") and rule.get("src_port").strip():
                match_criteria["src_port"] = rule["src_port"]
            else:
                pass
            # if dst_port exists and is not blank, set the value
            if rule.get("dst_port") and rule.get("dst_port").strip():
                match_criteria["dst_port"] = rule["dst_port"]
            else:
                pass
            # if vlan exists and is not blank, set the value
            if rule.get("vlan") and rule.get("vlan").strip():
                match_criteria["vlan"] = rule["vlan"]
            else:
                pass
            # if application exists and is not blank, set the value
            if rule.get("application") and rule.get("application").strip():
                match_criteria["application"] = rule["application"]
            else:
                pass
            # if app_group exists and is not blank, set the value
            if rule.get("app_group") and rule.get("app_group").strip():
                match_criteria["app_group"] = rule["app_group"]
            else:
                pass
            # if dscp exists and is not blank, set the value
            if rule.get("dscp") and rule.get("dscp").strip():
                match_criteria["dscp"] = rule["dscp"]
            else:
                pass
            # if src_dns exists and is not blank, set the value
            if rule.get("src_dns") and rule.get("src_dns").strip():
                match_criteria["src_dns"] = rule["src_dns"]
            else:
                pass
            # if dst_dns exists and is not blank, set the value
            if rule.get("dst_dns") and rule.get("dst_dns").strip():
                match_criteria["dst_dns"] = rule["dst_dns"]
            else:
                pass
            # if either_dns exists and is not blank, set the value
            if rule.get("either_dns") and rule.get("either_dns").strip():
                match_criteria["either_dns"] = rule["either_dns"]
            else:
                pass
            # if src_geo exists and is not blank, set the value
            if rule.get("src_geo") and rule.get("src_geo").strip():
                match_criteria["src_geo"] = rule["src_geo"]
            else:
                pass
            # if dst_geo exists and is not blank, set the value
            if rule.get("dst_geo") and rule.get("dst_geo").strip():
                match_criteria["dst_geo"] = rule["dst_geo"]
            else:
                pass
            # if either_geo exists and is not blank, set the value
            if rule.get("either_geo") and rule.get("either_geo").strip():
                match_criteria["either_geo"] = rule["either_geo"]
            else:
                pass
            # if src_service exists and is not blank, set the value
            if rule.get("src_service") and rule.get("src_service").strip():
                match_criteria["src_service"] = rule["src_service"]
            else:
                pass
            # if dst_service exists and is not blank, set the value
            if rule.get("dst_service") and rule.get("dst_service").strip():
                match_criteria["dst_service"] = rule["dst_service"]
            else:
                pass
            # if either_service exists and is not blank, set the value
            if (
                rule.get("either_service")
                and rule.get("either_service").strip()
            ):
                match_criteria["either_service"] = rule["either_service"]
            else:
                pass
            # if tbehavior exists and is not blank, set the value
            # "Voice", "Video Conferencing", "Bulk Data", etc.
            if rule.get("tbehavior") and rule.get("tbehavior").strip():
                match_criteria["tbehavior"] = rule["tbehavior"]
            else:
                pass
            # if overlay exists and is not blank, set the value
            # Rule uses overlay id rather than name
            if rule.get("overlay") and rule.get("overlay").strip():
                match_criteria["overlay"] = overlays[rule["overlay"]]
            else:
                pass
            # if internet exists and is not blank, set the value
            # ``1`` for internet traffic, ``0`` for for non-internet/internal
            if rule.get("internet") and rule.get("internet").strip():
                match_criteria["internet"] = overlays[rule["overlay"]]
            else:
                pass

            # Check that zones in CSV exist in Orchestrator
            if zones.get(rule["src_zone"]) is not None:
                pass
            else:
                print(
                    f"""
                FAILED TO PROCESS RULE ON ROW {rule_number}:
                Zone: {rule["src_zone"]} does not exist on Orchestrator
                Please define all zones prior to uploading rules

                Rule Details:
                {rule}
                """
                )
                # Skip to next rule in ruleset
                continue
            if zones.get(rule["dst_zone"]) is not None:
                pass
            else:
                print(
                    f"""
                FAILED TO PROCESS RULE ON ROW {rule_number}:
                Zone: {rule["dst_zone"]} does not exist on Orchestrator
                Please define all zones prior to uploading rules

                Rule Details:
                {rule}
                """
                )
                # Skip to next rule in ruleset
                continue

            # Combine source and destination zones into string <srcId_dstId>
            # E.g., 10_10 or 10_12
            zone_pair = f'{zones[rule["src_zone"]]}_{zones[rule["dst_zone"]]}'

            # If this is the first rule with this zone combination,
            # instantiate the zone pair in the map_details and the
            # underlying prio object for adding rules
            if zone_pair not in map_details:
                # Instantiate nested dictionaries for map
                map_details[zone_pair] = {}
                map_details[zone_pair]["prio"] = {}
            else:
                pass

            # Set rule logging enablement
            if rule.get("logging") == "enable":
                logging = "enable"
            else:
                logging = "disable"

            # Set rule logging priority
            if (
                rule.get("logging_priority")
                and rule.get("logging_priority").strip()
            ):
                logging_priority = rule["logging_priority"]
            else:
                logging_priority = "0"

            # Set rule comment
            if rule.get("comment") is not None:
                comment = rule["comment"]
            else:
                comment = ""

            # Form rule structure with respective details
            map_details[zone_pair]["prio"][rule_priority] = {
                "comment": comment,
                "gms_marked": False,
                "match": match_criteria,
                "misc": {
                    "rule": "enable",
                    "logging": logging,
                    "logging_priority": logging_priority,
                },
                "set": {"action": rule["action"]},
            }

            # Increment rule number being processed
            rule_number += 1

        except Exception as e:
            print(f"ERROR ENCOUNTERED WHEN PROCESSING RULE: {rule_number}")
            print(e)

# POST security policy as long as rules are < 1000 (1001 because rule
# count started at 2 accounting for headers in CSV file)
if rule_number <= 1001:

    # Set rule map details into the security map
    security_map["data"]["map1"] = map_details

    # With template group option, create new template group
    # and include security policy
    if template_group_name is not None:
        # Set security map into template group data
        template_group["templates"][0]["valObject"] = security_map
        # Create new TemplateGroup and select templates to include
        orch.create_template_group(template_group)
        orch.select_templates_for_template_group(
            template_group["name"],
            template_group["selectedTemplateNames"],
        )
    # With appliance option, upload rules to appliance through
    # Orchestrator passthrough api
    else:
        orch.appliance_post_api(
            ne_pk=ne_pk,
            url="securityMaps",
            data=security_map,
        )
# If ruleset longer than 1000 do not upload
else:
    print("WARNING - Ruleset too long to upload")


# if not using API key, logout from Orchestrator
if orch_api_key is None:
    orch.logout()
else:
    pass
