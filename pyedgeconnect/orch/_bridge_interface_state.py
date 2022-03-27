# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# bridgeInterfaceState : ECOS bridge interfaces


def get_appliance_bridge_interface_state(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Lists the Bridge Interfaces State and pass through Tx Interface

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - bridgeInterfaceState
          - GET
          - /appliance/interface/bridge/{neId}?cached={cached}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary of bridge interface configuration. If
        device is in router mode will return dictionary of single item
        ``router`` with value of ``The appliance is currently in Router
        Mode`` \n
        * keyword **bridge** (`dict`): Container for each bridge
          interface \n
            * keyword **<interface_name>** (`dict`): Interface object,
              e.g. ``lan0`` and it's underlying state \n
                * keyword **state** (`str`): Admin state of interface
                * keyword **link_state** (`str`): Link state of
                  interface
                * keyword **pthru_tx_if** (`str`): Transmit destination
                  interface for traffic received on this interface
    :rtype: dict
    """
    return self._get(
        "/appliance/interface/bridge/{}?cached={}".format(ne_id, cached)
    )
