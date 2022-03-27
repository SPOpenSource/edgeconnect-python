import argparse
import getpass
import os
import time

from pyedgeconnect import Orchestrator

# Parse runtime arguments
parser = argparse.ArgumentParser()
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

# get appliance and filter information from user
ne_pk = input("Appliance NePk (e.g. 77.NE) to run packet capture on: ")
max_packets = "100"
ip_filter = None
port_filter = None

# initiate packet capture on appliance
# the 'ip' and 'port' parameters are optional as they default to None
# explicity included here for demonstration purposes only
orch.tcpdump_run(
    [ne_pk], max_packet=max_packets, ip=ip_filter, port=port_filter
)
time.sleep(5)

# check and print status of packet capture on appliance
status = orch.tcpdump_status_appliance(ne_pk)
print(status)

# continue to check status of pcap while either in an
# active state or waiting to finish processing
while status["active"] == True or status["lastOneDone"] == False:
    print(
        "Waiting for pcap to complete -- current progress: {}".format(
            status["progress"]
        )
    )
    time.sleep(5)
    status = orch.tcpdump_status_appliance(ne_pk)
    print(status)

# get debug files from appliance
debug_files = orch.get_debug_files_from_appliance(ne_pk)

timestamps = []
# for each packet capture on an appliance, capture the timestamp
for pcap in debug_files["tcpDump"]:
    timestamps.append(pcap["stats"]["ctime"])

# use the filename of the packet capture with the
# most recent (max) timestamp
for pcap in debug_files["tcpDump"]:
    if pcap["stats"]["ctime"] == max(timestamps):
        filename = pcap["name"]
    else:
        pass

print("Uploading {} to Orchestrator from appliance {}".format(filename, ne_pk))

# upload the packet capture to Orchestrator
# where the user can download it
orch.upload_appliance_debug_files_to_orchestrator(
    ne_pk, debug_file_group="tcpDump", debug_filenames=[filename]
)

# if not using API key, logout from Orchestrator
if orch_api_key is None:
    orch.logout()
else:
    pass
