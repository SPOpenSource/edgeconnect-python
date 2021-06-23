# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# interfaceState : ECOS interfaces


def get_appliance_interface_state(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get interface configuration data for appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - interfaceState
          - GET
          - /interfaceState/{neId}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary of interface configuration \n
        * keyword **sysConfig** (`dict`): system level configuration \n
            * keyword **mode** (`str`): Operation mode, e.g. ``router``
            * keyword **submode** (`str`): Sub-mode, e.g. ``inline``
            * keyword **bonding** (`bool`): Interface bonding enabled
        * keyword **scalars** (`dict`): Many system stats such as
          ``maxWanBandwidth``, ``maxTunnels``, ``maxRouteMapEntries``,
          ``processorCount``, etc.
        * keyword **ifInfo** (`list`): List of interface information \n
            [`dict`]: Interface information object \n
                * keyword **ifname** (`str`): Interface name, e.g.
                  ``wan1``
                * keyword **admin** (`bool`): Interface admin state
                * keyword **oper** (`bool`): Interface operational state
                * keyword **ipv4** (`str`): IPv4 address
                * keyword **ipv4mask** (`str`): IPv4 subnet mask
                * keyword **ipv4dhcp** (`bool`): If IPv4 address from
                  dhcp
                * keyword **ifSpeed** (`str`): Interface speed
                * keyword **ifDuplex** (`str`): Interface duplex
                  setting, e.g. ``auto``
                * keyword **duplex** (`str`): Duplex state, e.g.
                  ``full (auto)``
                * keyword **mtu** (`int`): Interface mtu, e.g. ``1500``
                * keyword **mac** (`str`): Interface mac address
                * keyword **wan-if** (`bool`): Is a WAN interface
                * keyword **lan-if** (`bool`): Is a LAN interface
                * keyword **harden** (`bool`): If interface set to
                  harden
                * keyword **label** (`str`): Interface label id number,
                  e.g. ``2``
                * keyword **publicIp** (`str`): Public IP on interface
                * keyword **supported** (`str`): String listing
                  supported interface speed/duplexes e.g.
                  ``10/full,100/full,1000/full,auto/auto``
                * keyword **vrf** (`int`,optional): VRF id for interface
        * keyword **macIfs** (`list[str]`): Available interfaces on
          appliance
        * keyword **availMACs** (`list[str]`): Available unassigned MAC
          addresses
    :rtype: dict
    """
    return self._get("/interfaceState/{}?cached={}".format(ne_id, cached))
