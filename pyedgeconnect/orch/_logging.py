# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# logging : ECOS syslog


def get_appliance_syslog_config(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get logging settings from appliance or gmsdb

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - logging
          - GET
          - /logging/{neId}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary of logging configuration
    :rtype: dict
    """
    return self._get("/logging/{}?cached={}".format(ne_id, cached))
