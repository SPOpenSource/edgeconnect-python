# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# scheduleTimezone : Configure the timezone for the scheduled jobs and
# reports


def get_schedule_timezone(
    self,
) -> dict:
    """Get timezone configuration for scheduled jobs and reports to run

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - scheduleTimezone
          - GET
          - /gms/scheduleTimezone

    :return: Returns dictionary of schedule timezone \n
        * keyword **defaultTimezone** (`str`): Timezone of scheduled
          jobs and reports, e.g. ``US/East-Indiana``
    :rtype: dict
    """
    return self._get("/gms/scheduleTimezone")


def set_schedule_timezone(
    self,
    timezone: str,
) -> bool:
    """Updates the schedule timezone used with for the scheduled jobs
    and reports

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - scheduleTimezone
          - POST
          - /gms/scheduleTimezone

    :param timezone: Time zone to set for scheduled jobs and reports.
        Format of Country/Location, e.g. ``US/East-Indiana``
    :type timezone: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {"defaultTimezone": timezone}
    return self._post(
        "/gms/scheduleTimezone",
        data=data,
        expected_status=[204],
        return_type="bool",
    )
