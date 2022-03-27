import argparse
import csv
import getpass
import os

from pyedgeconnect import Orchestrator

# Parse runtime arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    "-c",
    "--csv",
    help="Specify source csv file for preconfigs",
    type=str,
    required=True,
)
parser.add_argument(
    "-o",
    "--orch",
    help="specify Orchestrator URL",
    type=str,
)
args = parser.parse_args()

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

# Specify CSV file for generating preconfigs
# This is a mandatory runtime argument
if vars(args)["csv"] is not None:
    csv_filename = vars(args)["csv"]
else:
    print("Source CSV file not specified, exiting")
    exit()


with open(csv_filename, encoding="utf-8-sig") as csvfile:
    csv_dict = csv.DictReader(csvfile)

    # Get all preconfigs from Orchestrator
    all_preconfigs = orch.get_all_preconfig()
    preconfigs_to_delete = []
    ec_hostname_list = []

    # Form list of preconfigs on Orchestrator matching preconfig
    # names from the CSV file
    for row in csv_dict:
        ec_hostname_list.append(row["hostname"])
        for preconfig in all_preconfigs:
            if preconfig["name"] == row["hostname"]:
                # Similar to appliances, preconfigs are identified by
                # an id (e.g. 10) rather than the name/hostname
                preconfigs_to_delete.append(preconfig["id"])
            else:
                pass

# Show user pending preconfigs to be deleted
print("The following Preconfigs are queued for deletion:")
width = 10
print(
    "\n".join(
        "".join(str(preconfigs_to_delete[i : i + width]))
        for i in range(0, len(preconfigs_to_delete), width)
    )
)

# Confirm with user to remove the specified preconfigs
proceed = input("Delete these preconfigs from Orchestrator?(y/n): ")
if proceed == "y" or proceed == "Y":
    for preconfigId in preconfigs_to_delete:
        orch.delete_preconfig(str(preconfigId))
    print("All specified preconfigs deleted from Orchestrator")
else:
    print("Cancelled, no preconfigs deleted from Orchestrator")
