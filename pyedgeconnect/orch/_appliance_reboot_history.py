# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# applianceRebootHistory : returns all Appliances reboot history


def get_appliance_reboot_history(
    self,
    action: str = None,
) -> list:
    """Get all appliance reboot history, optionally send reboot reports
    to Cloud Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applianceRebootHistory
          - GET
          - /gms/applianceRebootHistory

    :param action: If None, returns all the appliance history otherwise
        it will send all the reboot reports to portal, defaults to None
    :type action: string, optional
    :return: Returns list of dictionaries for each appliance reboot
        history \n
        [`dict`]: list of reboot history dictionaries \n
            * keyword **nePk** (`str, optional`): This is the primary
              key of the appliance. e.g. ``3.NE``
            * keyword **time** (`int, optional`): Epoch time of
              Appliance reboot Time
            * keyword **version** (`str, optional`): Appliance version
              before it rebooted
            * keyword **rootCause** (`str, optional`): Root cause for
              the reboot. ``Normal`` indicates reboot was initiated by
              user. ``Unexpected shutdown`` - indicates there could be a
              appliance crash
            * keyword **sentToPortal** (`bool, optional`): boolean flag
              to indicate whether the reboot record sent to portal or
              not
    :rtype: list
    """

    path = "/gms/applianceRebootHistory"

    if action is not None:
        path = path + "?action={}".format(action)

    return self._get(path)
