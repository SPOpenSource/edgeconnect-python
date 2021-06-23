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

# retrieve Orchestrator system information
orch_info = orch.get_orchestrator_server_info()

# print Orchestrator information
print(
    """
Orchestrator Information:
-------------------------------------------------------
Hostname: {}
Version: {}
Uptime: {}
-------------------------------------------------------

    """.format(
        orch_info["hostName"],
        orch_info["release"],
        orch_info["uptime"],
    )
)

# retrieve all appliances in Orchestrator
appliances = orch.get_appliances()

print("Appliance Information:")

# print headers for table
print(
    "\n{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(
        "Hostname",
        "Appliance ID",
        "Serial Num",
        "IP Address",
        "Software",
        "Bandwidth",
    )
)

# print horizontal line before appliance data
print("-" * 126)

# print row for each appliance with particular info attributes
for appliance in appliances:

    print(
        "{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(
            appliance["hostName"],
            appliance["nePk"],
            appliance["serial"],
            appliance["IP"],
            appliance["softwareVersion"],
            appliance["systemBandwidth"],
        )
    )

print("\n")

# if not using API key, logout of Orchestrator
if orchestrator_api_key == "":
    orch.logout()
else:
    pass
