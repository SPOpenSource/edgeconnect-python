# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# maintenanceMode : Get or set maintenance mode for appliances


def get_maintenance_mode_appliances(self) -> dict:
    """Get appliances currently in maintenance mode

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - maintenanceMode
          - GET
          - /maintenanceMode

    :return: Returns dictionary of appliances in maintenance mode
    :rtype: dict
    """
    return self._get("/maintenanceMode")


def update_maintenance_mode_appliances(
    self,
    action: str,
    pause_list: list = [],
    alarm_list: list = [],
) -> bool:
    """Update appliances in maintenance mode. Can pause orchestration
    and/or suppress alarms for appliances.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - maintenanceMode
          - POST
          - /maintenanceMode

    :param action: Use the values of ``add`` or ``remove`` to add or
        remove appliances from maintenance
    :type action: str
    :param pause_list: List of appliances to pause orchestration for in
        nePk format, e.g. ``["3.NE","5.NE"]``, defaults to []
    :type pause_list: list, optional
    :param alarm_list: List of appliances to suppress alarms for in nePk
        format, e.g. ``["3.NE","5.NE"]``, defaults to []
    :type alarm_list: list, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "action": action,
        "data": {
            "pauseOrchestration": pause_list,
            "suppressAlarm": alarm_list,
        },
    }

    return self._post(
        "/maintenanceMode",
        data=data,
        expected_status=[204],
        return_type="bool",
    )
