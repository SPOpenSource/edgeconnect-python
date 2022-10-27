.. auth_example:


Authentication
********************************

The following code snippet is an example of handling multiple authentication
methods when connecting to an Aruba Orchestrator instance with pyedgeconnect.

The example scripts provided in the repository use this process in
addition to any other required logic for a particular use-case.

.. note::

    The code referenced in this document and all published examples
    with pyedgeconnect are available from the GitHub repository within the
    `examples <https://github.com/SPOpenSource/edgeconnect-python/tree/main/examples>`_
    folder. Each example script contains logic to authenticate to the
    Orchestrator as documented in the authentication example.

    Clone the repository and download the examples with:

    .. code:: bash

        $ git clone https://github.com/SPOpenSource/edgeconnect-python.git


Environment variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The example script will also look for the following environment variables
related to authenticating to Orchestrator

``ORCH_URL``
``ORCH_API_KEY``
``ORCH_USER``
``ORCH_PASSWORD``

If ``ORCH_URL`` is specified, it will take precedence, otherwise user
will be prompted for input to enter the Orchestrator IP or FQDN

If ``ORCH_API_KEY`` is specified it will take precedence for an
authentication method over user/password authentication. If not found,
the user will be prompted for entering an API key.

.. code-block:: python

    import argparse
    import getpass
    import os

    from pyedgeconnect import Orchestrator

    # Parse runtime arguments to specify an Orchestrator IP or FQDN
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-o",
        "--orch",
        help="specify Orchestrator URL",
        type=str,
    )
    args = parser.parse_args()

    # Set Orchestrator FQDN/IP via arguments, environment variable,
    # or user input if neither in argument or environment variable
    if vars(args)["orch"] is not None:
        orch_url = vars(args)["orch"]
    elif os.getenv("ORCH_URL") is not None:
        orch_url = os.getenv("ORCH_URL")
    else:
        orch_url = input("Orchstrator IP or FQDN: ")

    # Set Orchestrator API Key via environment variable or user input
    # Skipping will fallback to user/password authentication
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
    # printing log messages to terminal, and ``verify_ssl`` to False
    # which will not verify the web https certificate on Orchestrator
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
        # Login to Orchestrator with user/password to check auth before
        # proceeding
        confirm_auth = orch.login(orch_user, orch_pw, mfacode=token)
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