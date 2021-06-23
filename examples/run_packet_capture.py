import time
from getpass import getpass

from pyedgeconnect import Orchestrator

# set value for Orchestrator URL/IP address
orchestrator_url = input("Enter Orchestrator URL or IP address: ")
# set value for Orchestrator API key
orchestrator_api_key = input(
    "Enter API key for Orchestrator (leave blank to use username/password): "
)

# obtain username password if not using API Key
if orchestrator_api_key == "":
    orch_user = input("Enter Orchestrator username: ")
    orch_password = getpass("Enter Orchestrator password: ")
else:
    pass

# instantiate Orchestrator with debug enabled for
# printing log messages to terminal
orch = Orchestrator(
    orchestrator_url,
    api_key=orchestrator_api_key,
    log_console=True,
    verify_ssl=False,
)

# if not using API key, login to Orchestrator
if orchestrator_api_key == "":
    orch.login(orch_user, orch_password)
else:
    pass

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

# if not using API key, logout of Orchestrator
if orchestrator_api_key == "":
    orch.logout()
else:
    pass
