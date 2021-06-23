# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# peerPriority : Orchestrator peer priority


def get_peer_priority_configuration(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get peer priority configurations from Edge Connect appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - peerPriority
          - GET
          - /appliance/peerPriorityList/{neId}?cached={cached}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary of peer priority configuration
        information \n
        * keyword **peerList** (`dict`): dictionary of each peer and
          related metrics \n
            * keyword **<peer_name>** (`str`): Name of peer \n
                * keyword **peer_weight** (`int`): Configured peer
                  weight
                * keyword **peer_metric** (`int`): Advertised metric
                * keyword **self** (`str`): Name of peer (same as parent
                  dictionary key)
    :rtype: dict
    """
    return self._get(
        "/appliance/peerPriorityList/{}?cached={}".format(ne_id, cached)
    )
