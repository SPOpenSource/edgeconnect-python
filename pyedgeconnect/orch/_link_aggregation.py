# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# linkAggregation : Link Aggregation Configuration


def get_link_aggregation_data(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get all link aggregation data on the appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - linkAggregation
          - GET
          - /linkAggregation/{neId}?cached={cached}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary of configured link aggregation \n
        * keyword **<aggregate_interface>** (`dict`): Aggregate
          interface object, e.g. ``blan0`` or ``bwan0`` \n
          * keyword **mtu** (`int`): MTU of Link Aggregation interface
          * keyword **portlist** (`str`): Comma separated list of bonded
            interfaces as string, e.g. ``lan0,lan1``
    :rtype: dict
    """
    return self._get("/linkAggregation/{}?cached={}".format(ne_id, cached))
