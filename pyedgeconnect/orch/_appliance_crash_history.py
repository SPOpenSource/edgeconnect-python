# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# applianceCrashHistory : returns and posts all Appliances crash history


def appliance_crash_history(
    self,
    action: str = None,
):
    """Get appliance crash history. Can optionally send crash reports to
    Cloud Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applianceCrashHistory
          - GET
          - /gms/applianceCrashHistory

    :param action: If this paramter has a value, the appliance crash
        reports will be sent to Cloud Portal, defaults to None
    :type action: str, optional
    :return: Returns True/False based on successful call sending crash
        reports to Cloud Portal. If action is None, will return dict of
        appliance crash history.
    :rtype: bool or dict
    """

    if action is not None:
        return self._get(
            "/gms/applianceCrashHistory?action={}".format(action),
            expected_status=[204],
            return_type="bool",
        )
    else:
        return self._get("/gms/applianceCrashHistory")
