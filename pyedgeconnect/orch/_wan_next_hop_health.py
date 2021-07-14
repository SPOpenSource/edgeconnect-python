# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# wanNextHopHealth : Next hop health config


def get_wan_next_hop_health_config(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get wan next hop health config on the appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - wanNextHopHealth
          - GET
          - /appliance/wanNextHopHealth/{neId}?cached={cached}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary of WAN Next Hop Health configurations \n
        * keyword **enable** (`bool`): Enable or disable health check
        * keyword **hold_down_count** (`int`): Hold down count
        * keyword **interval** (`int`): Interval in seconds
        * keyword **retry_count** (`int`): Retry count
    :rtype: dict
    """
    return self._get(
        "/appliance/wanNextHopHealth/{}?cached={}".format(ne_id, cached)
    )
