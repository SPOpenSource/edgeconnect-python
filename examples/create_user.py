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

# set user password details
username = "API_CREATED_USER"
password = 1
confirm_password = 2

# confirm password with interactive user
while password != confirm_password:
    print(
        "\nPassword must be at least 8 characters long and contain "
        + "the following items:\n"
        + "upper case letter, lower case letter, "
        + "a number, a special character\n"
    )
    password = getpass("Enter user's password: ")
    confirm_password = getpass("Confirm user's password: ")
    if password != confirm_password:
        print("Passwords do not match, please try again\n\n")

# create user
# THIS FUNCTION ALSO UPDATES EXISTING USERS
# MAKE SURE NOT TO ACCIDENTLY CHANGE DETAILS
# OF AN EXISTING PRODUCTION USER
orch.create_or_update_user(
    new_user=True,
    user_pk="",
    first_name="first_name",
    last_name="last_name",
    phone="",
    email="jdoe@not-a-real-email.com",
    status="Active",
    role="Network Monitor",
    username=username,
    password=password,
    repeat_password=password,
    two_factor_email=False,
    two_factor_app=False,
)

# retrieve and print user details of newly created user
user_details = orch.get_user(username)
for item in user_details.items():
    print(item)

# if not using API key, logout of Orchestrator
if orchestrator_api_key == "":
    orch.logout()
else:
    pass
