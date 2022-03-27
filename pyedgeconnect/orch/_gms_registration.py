# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# gmsRegistration : Orchestrator registration on appliance setting


def get_orchestrator_registration_setting(
    self,
) -> dict:
    """This configuration determines what appliances will use to connect
    to Orchestrator. If the customDefaultIP is a blank string,
    Orchestrator will send it's internal management IP (returned as
    internalManagementIP) as the default. If any labels are configured,
    it will push that IP/domain instead.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsRegistration
          - GET
          - /gms/gmsRegistration2

    :return: Returns values for Orchestrator registration settings
        pushed to appliances \n
        * keyword **customDefaultIP** (`str`): The user set default
          domain or IP to send to appliances
        * keyword **internalManagementIP** (`str`): The Orchestrator's
          management IP
        * keyword **label** (`dict`): Priority value for label \n
            * keyword **ipOrDns** (`str`): IP or DNS value to reach
              Orchestrator with over this label
            * keyword **labelId** (`int`): Label integer ID
    :rtype: dict
    """
    return self._get("/gms/gmsRegistration2")


def set_orchestrator_registration_setting(
    self,
    custom_default_ip: str = "",
    label_details: dict = {},
) -> dict:
    """This configuration determines what appliances will use to connect
    to Orchestrator. If the customDefaultIP is a blank string,
    Orchestrator will send it's internal management IP (returned as
    internalManagementIP) as the default. If any labels are configured,
    it will push that IP/domain instead. These settings can be found in
    the web UI under ``Administration -> General Settings -> Setup ->
    Orchestrator Reachability``

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsRegistration
          - POST
          - /gms/gmsRegistration2

    .. warning::
        This will overwrite current Orchestrator reachability settings.
        Retrieve the current settings with
        :func:`pyedgeconnect.Orchestrator.get_orchestrator_registration_setting`

    :param custom_default_ip: The user set default domain or IP to send
        to appliances, e.g. ``my-orch-useast1.silverpeak.cloud``
    :type custom_default_ip: str, optional
    :param label_details: Priority and IP/DNS details for specific
        labels for appliances to use to connect to Orchestrator.
        Defaults to blank dictionary ``{}``
        Outlined in structure as follows: \n
        label_details = { \n
            "1": { \n
                "ipOrDns": "", \n
                "labelId": 0 \n
            }, \n
            "2": { \n
                "ipOrDns": "", \n
                "labelId": 0 \n
            } \n
        } \n
    :type label_details: dict, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """  # noqa: W505
    data = {
        "customDefaultIP": custom_default_ip,
        "label": label_details,
    }

    return self._post(
        "/gms/gmsRegistration2",
        data=data,
        return_type="bool",
    )
