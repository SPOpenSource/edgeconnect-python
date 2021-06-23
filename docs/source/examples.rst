.. examples:


================
 Example Usage
================

The following examples are also included as individual .py files in the
repository in the `examples` directory.

Each example file begins with the following code for setting up initial
connection details for Orchestrator:

.. code-block:: python
    :linenos:

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

    # instantiate Orchestrator with debug enabled
    # for printing log messages to terminal
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




Print Appliance Information
===========================

This example retrieves all the appliances currently in Orchestrator
and then prints the appliances and certain attributes into a table in
the terminal output.

.. code-block:: python
    :linenos:

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


Run Packet Capture
==================

This example will run a tcpdump packet capture on the specified
appliance and then upload the file to Orchestrator so that it can be
downloaded by the user or uploaded to support.

.. code-block:: python
    :linenos:

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


Create User
==================

This example will create a new user read-only user
locally on Orchestrator.

.. note::

    As warned in the inline comments, this can update an existing user
    with matching details which is why most of the values are hard-coded
    with generic values such as 'first_name' as a first name, etc.


.. code-block:: python
    :linenos:

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