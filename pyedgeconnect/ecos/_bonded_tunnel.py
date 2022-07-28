# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# bondedTunnel : Bonded Tunnels
from __future__ import annotations


def get_appliance_bonded_tunnels_state(
    self,
    state_match: str = None,
) -> dict:
    """Get the current list of tunnels and their configuration as well
    as some state information like uptime and operational state

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - bondedTunnel
          - GET
          - /bondedTunnels/state

    :param state_match: Regular expression used to match tunnels state,
        e.g. ``Idle`` or ``Up`` would match all tunnels with ``status``
        of ``Up - Idle``
    :type state_match: str
    :return: Returns dictionary of overlay tunnels with status matched
        from the ``state_match`` parameter \n
        * keyword **<bonded_tunnel_id>** (`dict`): Bonded tunnel object\n
            * keyword **self** (`str`): Tunnel id
            * keyword **oper** (`str`): Status, e.g. ``Up - Idle``
            * keyword **uptime** (`int`): Tunnel uptime in ms
            * keyword **cur_mtu** (`str`): Tunnel MTU, e.g. ``1488``
            * keyword **cur_max_bw** (`str`): Tunnel max bw, Kbps
            * keyword **rem_sys_bw** (`str`): Remaining system bandwidth
            * keyword **quiescence** (`bool`): true,
            * keyword **remote_id** (`int`): Remote ID
            * keyword **state_bin** (`dict`): \n
                * keyword **tun_state** (`str`): Tunnel status,
                  e.g. ``Up - Idle``
                * keyword **uptime** (`int`): Tunnel uptime in ms
                * keyword **cur_mtu** (`str`): Tunnel MTU, e.g. ``1488``
                * keyword **local_id** (`int`): Local ID
                * keyword **bonded** (`bool`): Tunnel bonded state
                * keyword **ipsec_nat_addr** (`str`): ``NONE`` for
                  bonded tunnels
                * keyword **ipsec_nat_port** (`str`): ``NONE`` for
                  bonded tunnels
    :rtype: dict
    """  # noqa: W505
    path = "/bondedTunnels/state"
    if state_match is not None:
        path += f"?state={state_match}"
    return self._get(path)


def get_appliance_multiple_bonded_tunnels_state(
    self,
    tunnel_list: list[str],
) -> dict:
    """Get multiple bonded tunnels state

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - bondedTunnel
          - POST
          - /bondedTunnels/getStateMultiple

    :param tunnel_list: List of tunnel id's to query for
    :type tunnel_list: list[str]
    :return: Returns dictionary of specified tunnels queried \n
        * keyword **<bonded_tunnel_id>** (`dict`): Bonded tunnel object\n
            * keyword **self** (`str`): Tunnel id
            * keyword **oper** (`str`): Status, e.g. ``Up - Idle``
            * keyword **uptime** (`int`): Tunnel uptime in ms
            * keyword **cur_mtu** (`str`): Tunnel MTU, e.g. ``1488``
            * keyword **cur_max_bw** (`str`): Tunnel max bw, Kbps
            * keyword **rem_sys_bw** (`str`): Remaining system bandwidth
            * keyword **quiescence** (`bool`): true,
            * keyword **remote_id** (`int`): Remote ID
            * keyword **state_bin** (`dict`): \n
                * keyword **tun_state** (`str`): Tunnel status,
                  e.g. ``Up - Idle``
                * keyword **uptime** (`int`): Tunnel uptime in ms
                * keyword **cur_mtu** (`str`): Tunnel MTU, e.g. ``1488``
                * keyword **local_id** (`int`): Local ID
                * keyword **bonded** (`bool`): Tunnel bonded state
                * keyword **ipsec_nat_addr** (`str`): ``NONE`` for
                  bonded tunnels
                * keyword **ipsec_nat_port** (`str`): ``NONE`` for
                  bonded tunnels
    :rtype: dict
    """  # noqa: W505
    return self._post(
        "/bondedTunnels/getStateMultiple",
        data=tunnel_list,
    )


def get_appliance_all_bonded_tunnel_ids(
    self,
    state_match: str = None,
) -> list:
    """Get the current list of all bonded tunnels

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - bondedTunnel
          - GET
          - /bondedTunnels/allIDs

    :param state_match: Regular expression used to match tunnels state,
        e.g. ``Idle`` or ``Up`` would match all tunnels with ``status``
        of ``Up - Idle``
    :type state_match: str
    :return: Returns list of all tunnel ids
        e.g. ``["bondedTunnel_370","bondedTunnel_371",...]``
    :rtype: list
    """
    path = "/bondedTunnels/allIDs"
    if state_match is not None:
        path += f"?state={state_match}"
    return self._get(path)


def get_appliance_bonded_tunnel_aliases(
    self,
    limit: int,
    alias_match: str = None,
    state_match: str = None,
) -> list:
    """Find bonded tunnels with matching aliases on appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - bondedTunnel
          - GET
          - /bondedTunnels/aliases

    :param limit: Max number of tunnels to return from query
    :type limit: int
    :param alias_match: Match text of tunnel's alias, paramter is case
        insensitive
    :type alias_match: str
    :param state_match: Regular expression used to match tunnels state,
        e.g. ``Idle`` or ``Up`` would match all tunnels with ``status``
        of ``Up - Idle``
    :type state_match: str
    :return: Returns list of matching tunnels with tunnel ID and alias\n
        * [`dict`]: List of tunnel alias/id pairs \n
            * keyword **alias** (`str`): Tunnel alias
            * keyword **id** (`str`): Tunnel id
    :rtype: list
    """
    path = f"/bondedTunnels/aliases?limit={limit}"
    if alias_match is not None:
        path += f"&matchingAlias={alias_match}"
    if state_match is not None:
        path += f"&state={state_match}"
    return self._get(path)


def get_appliance_bonded_tunnels_config(
    self,
    state_match: str = None,
) -> dict:
    """Get the current list of bonded tunnels and their configuration

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - bondedTunnel
          - GET
          - /bondedTunnels/config

    :param state_match: Regular expression used to match tunnels state,
        e.g. ``Idle`` or ``Up`` would match all tunnels with ``status``
        of ``Up - Idle``
    :type state_match: str
    :return: Returns dictionary of tunnels with status matched from the
        ``state_match`` parameter \n
        * keyword **<tunnel_id>** (`dict`): Tunnel id and object \n
            * keyword **admin** (`str`): Admin state of the tunnel -
              takes two values: ``up`` or ``down``
            * keyword **alias** (`str`): Tunnel alias/name, e.g.
              ``to_<REMOTE_EC_HOSTNAME>_<OVERLAY_NAME>``
            * keyword **auto_mtu** (`bool`): Determines if the tunnel
              should have auto MTU detection
            * keyword **ctrl_pkt** (`dict`): Tunnel health packet
              marking \n
                * keyword **dscp** (`str`): DSCP marking to be used on
                  tunnel keepalive packets to determine if tunnel remote
                  IP address is reachable
            * keyword **gms_marked** (`bool`): ``True`` if configured by
              Orchestrator
            * keyword **gre_proto** (`int`): GRE protocol in the GRE
              header
            * keyword **id2** (`int`): NEEDS DESCRIPTION
            * keyword **ipsec_arc_window** (`str`): IPSec ARC Window,
              not configurable
            * keyword **ipsec_enable** (`bool`): ``True`` if IPSec
              tunnel
            * keyword **presharedkey** (`str`): Tunnel preshared key
            * keyword **ipsec_udp_sport** (`str`): IPSec UDP tunnel
              source port
            * keyword **ipsec_udp_dport** (`str`): IPSec UDP tunnel
              destination port
            * keyword **orch_tid** (`list[int]`): NEEDS DESCRIPTION
            * keyword **max_bw** (`int`): If the tunnel max bandwidth is
              manually configured, use this field and set max_bw_auto to
              ``false``
            * keyword **max_bw_auto** (`bool`): If the tunnel max
              bandwidth needs to be set to auto, this field must be true
            * keyword **max_bw_unshaped** (`bool`): false,
            * keyword **min_bw** (`int`): Tunnel minimum bandwidth
            * keyword **mode** (`str`): Tunnel mode, e.g. ``udp_sp``
            * keyword **mtu** (`str`): Tunnel MTU, e.g. ``1500``
            * keyword **peername** (`str`): Tunnel peer name
            * keyword **nat_mode** (`str`): Tunnel NAT mode, e.g.
              ``auto``, ``none``
            * keyword **pkt** (`dict`): Packet settings object \n
                * keyword **coalesce_enable** (`bool`): Packet
                  coalescing enabled
                * keyword **coalesce_wait** (`int`): Packet coalescing
                  wait timer
                * keyword **fec_enable_str** (`str`): FEC enabled, e.g.
                  ``enable``, ``disable``, or ``auto``
                * keyword **fec_reset_intvl** (`int`): FEC reset
                  interval, e.g. ``1``, ``2``, ``5``, ``10``, or ``20``
                * keyword **fec_max_ratio** (`int`): FEC auto maximum
                  ration, e.g. ``10``
                * keyword **fec_min_ratio** (`int`): FEC auto minimum
                  ration, e.g. ``0``
                * keyword **frag_enable** (`bool`): Enable tunnel packet
                  fragmentation and reassembly
                * keyword **reorder_wait** (`int`): Amount of time in ms
                  to wait for Packet Order Correction algorithm
            * keyword **tag_name** (`str`): Overlay name, e.g.
              ``BulkApps``
            * keyword **threshold** (`dict`): Tunnel fail thresholds \n
                * keyword **fastfail** (`int`): Enable fast fail,
                  increasing the frequency of tunnel health packets,
                  e.g. ``0``, ``1``, or ``2``
                * keyword **fastfail-wait-base** (`int`): 150,
                * keyword **fastfail-wait-rtt** (`int`): 5,
                * keyword **jitter** (`int`): Jitter threshold, ``0`` if
                  not configured
                * keyword **latency** (`int`): Latency threshold, ``0``
                  if not configured
                * keyword **loss** (`int`): Loss threshold, ``0`` if
                  not configured
                * keyword **retry_count** (`int`): How many packets
                  which are sent once per second should be missed before
                  a tunnel is declared down, e.g. ``3``
            * keyword **type** (`str`): e.g. ``bonded``
            * keyword **udp_dest_port** (`int`): If the tunnel is of
              type 'udp', the udp port to use, e.g. ``4163``
            * keyword **udp_flows** (`int`): If tunnel mode is udp, this
              field determines how many different udp flows are used to
              distribute tunnel traffic, e.g. ``256``
            * keyword **local_vrf** (`int`): Local VRF ID, Default
              segment would be ``0``
            * keyword **source** (`str`): Source IP address of tunnel,
              for bonded tunnels this is ``127.0.0.0``
            * keyword **destination** (`str`): Destination IP address of
              tunnel, for bonded tunnels this is ``127.0.0.0``
            * keyword **bound_tun** (`dict`): Tunnels bound to bonded
              tunnel \n
                * keyword **<tunnel_id>** (`str`): Underlay tunnel alias
                  e.g. ``to_<REMOTE_EC_HOSTNAME>_INET1-INET1``
    :rtype: dict
    """
    path = "/bondedTunnels/config"
    if state_match is not None:
        path += f"?state={state_match}"
    return self._get(path)


def configure_appliance_all_bonded_tunnels(
    self,
    tunnel_configuration: dict,
) -> bool:
    """Add/modify overlay tunnels

    .. warning::
        This function would update all overlay tunnels. Existing tunnel
        IDs will be updated, New tunnel IDs will be created.

        Use :func:`~pyedgeconnect.EdgeConnect.get_appliance_bonded_tunnels_config`
        to get current tunnel configuration

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - bondedTunnel
          - POST
          - /bondedTunnels/config


    :param tunnel_configuration: Dictionary structure for configuring
        overlay tunnels on EdgeConnect appliance. See response from
        :func:`~pyedgeconnect.EdgeConnect.get_appliance_bonded_tunnels_config`
        for documentation of data structure
    :type tunnel_configuration: dict
    :return: Returns True/False based on successful call
    :rtype: bool
    """  # noqa:W505,E501
    return self._post(
        "/bondedTunnels/config",
        data=tunnel_configuration,
        return_type="bool",
    )


def get_appliance_single_bonded_tunnel_config(
    self,
    tunnel_id: str,
) -> dict:
    """Get specific overlay tunnel configuration by tunnel id from
    appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - bondedTunnel
          - GET
          - /bondedTunnels/{id}

    :param tunnel_id: Tunnel id of tunnel to retrieve information for,
        e.g. ``bondedTunnel_385``
    :type tunnel_id: str
    :return: Returns dictionary of tunnel configuration for specific
        tunnel \n
        * keyword **admin** (`str`): Admin state of the tunnel -
            takes two values: ``up`` or ``down``
        * keyword **alias** (`str`): Tunnel alias/name, e.g.
            ``to_<REMOTE_EC_HOSTNAME>_<OVERLAY_NAME>``
        * keyword **auto_mtu** (`bool`): Determines if the tunnel
            should have auto MTU detection
        * keyword **ctrl_pkt** (`dict`): Tunnel health packet
            marking \n
            * keyword **dscp** (`str`): DSCP marking to be used on
                tunnel keepalive packets to determine if tunnel remote
                IP address is reachable
        * keyword **gms_marked** (`bool`): ``True`` if configured by
            Orchestrator
        * keyword **gre_proto** (`int`): GRE protocol in the GRE
            header
        * keyword **id2** (`int`): NEEDS DESCRIPTION
        * keyword **ipsec_arc_window** (`str`): IPSec ARC Window,
            not configurable
        * keyword **ipsec_enable** (`bool`): ``True`` if IPSec
            tunnel
        * keyword **presharedkey** (`str`): Tunnel preshared key
        * keyword **ipsec_udp_sport** (`str`): IPSec UDP tunnel
            source port
        * keyword **ipsec_udp_dport** (`str`): IPSec UDP tunnel
            destination port
        * keyword **orch_tid** (`list[int]`): NEEDS DESCRIPTION
        * keyword **max_bw** (`int`): If the tunnel max bandwidth is
            manually configured, use this field and set max_bw_auto to
            ``false``
        * keyword **max_bw_auto** (`bool`): If the tunnel max
            bandwidth needs to be set to auto, this field must be true
        * keyword **max_bw_unshaped** (`bool`): false,
        * keyword **min_bw** (`int`): Tunnel minimum bandwidth
        * keyword **mode** (`str`): Tunnel mode, e.g. ``udp_sp``
        * keyword **mtu** (`str`): Tunnel MTU, e.g. ``1500``
        * keyword **peername** (`str`): Tunnel peer name
        * keyword **nat_mode** (`str`): Tunnel NAT mode, e.g.
            ``auto``, ``none``
        * keyword **pkt** (`dict`): Packet settings object \n
            * keyword **coalesce_enable** (`bool`): Packet
                coalescing enabled
            * keyword **coalesce_wait** (`int`): Packet coalescing
                wait timer
            * keyword **fec_enable_str** (`str`): FEC enabled, e.g.
                ``enable``, ``disable``, or ``auto``
            * keyword **fec_reset_intvl** (`int`): FEC reset
                interval, e.g. ``1``, ``2``, ``5``, ``10``, or ``20``
            * keyword **fec_max_ratio** (`int`): FEC auto maximum
                ration, e.g. ``10``
            * keyword **fec_min_ratio** (`int`): FEC auto minimum
                ration, e.g. ``0``
            * keyword **frag_enable** (`bool`): Enable tunnel packet
                fragmentation and reassembly
            * keyword **reorder_wait** (`int`): Amount of time in ms
                to wait for Packet Order Correction algorithm
        * keyword **tag_name** (`str`): Overlay name, e.g.
            ``BulkApps``
        * keyword **threshold** (`dict`): Tunnel fail thresholds \n
            * keyword **fastfail** (`int`): Enable fast fail,
                increasing the frequency of tunnel health packets,
                e.g. ``0``, ``1``, or ``2``
            * keyword **fastfail-wait-base** (`int`): 150,
            * keyword **fastfail-wait-rtt** (`int`): 5,
            * keyword **jitter** (`int`): Jitter threshold, ``0`` if
                not configured
            * keyword **latency** (`int`): Latency threshold, ``0``
                if not configured
            * keyword **loss** (`int`): Loss threshold, ``0`` if
                not configured
            * keyword **retry_count** (`int`): How many packets
                which are sent once per second should be missed before
                a tunnel is declared down, e.g. ``3``
        * keyword **type** (`str`): e.g. ``bonded``
        * keyword **udp_dest_port** (`int`): If the tunnel is of
            type 'udp', the udp port to use, e.g. ``4163``
        * keyword **udp_flows** (`int`): If tunnel mode is udp, this
            field determines how many different udp flows are used to
            distribute tunnel traffic, e.g. ``256``
        * keyword **local_vrf** (`int`): Local VRF ID, Default
            segment would be ``0``
        * keyword **source** (`str`): Source IP address of tunnel,
            for bonded tunnels this is ``127.0.0.0``
        * keyword **destination** (`str`): Destination IP address of
            tunnel, for bonded tunnels this is ``127.0.0.0``
        * keyword **bound_tun** (`dict`): Tunnels bound to bonded
            tunnel \n
            * keyword **<tunnel_id>** (`str`): Underlay tunnel alias
                e.g. ``to_<REMOTE_EC_HOSTNAME>_INET1-INET1``
    :rtype: dict
    """
    return self._get(f"/bondedTunnels/config/{tunnel_id}")


def delete_appliance_single_bonded_tunnel(
    self,
    tunnel_id: str,
) -> bool:
    """Delete specific overlay tunnel configuration by tunnel id from
    appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - bondedTunnel
          - DELETE
          - /bondedTunnels/config/{id}

    :param tunnel_id: Tunnel id of tunnel to retrieve information for,
        e.g. ``bondedTunnel_385``
    :type tunnel_id: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        f"/bondedTunnels/config/{tunnel_id}",
        return_type="bool",
    )


def get_appliance_multiple_bonded_tunnels_config(
    self,
    tunnel_list: list[str],
) -> dict:
    """Get the configuration of multiple bonded tunnels from appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - bondedTunnel
          - POST
          - /bondedTunnels/getMultiple

    :param tunnel_list: List of tunnel id's to query for
    :type tunnel_list: list[str]
    :return: Returns dictionary of specified tunnels queried \n
        * keyword **<tunnel_id>** (`dict`): Tunnel id and object \n
            * keyword **admin** (`str`): Admin state of the tunnel -
              takes two values: ``up`` or ``down``
            * keyword **alias** (`str`): Tunnel alias/name, e.g.
              ``to_<REMOTE_EC_HOSTNAME>_<OVERLAY_NAME>``
            * keyword **auto_mtu** (`bool`): Determines if the tunnel
              should have auto MTU detection
            * keyword **ctrl_pkt** (`dict`): Tunnel health packet
              marking \n
                * keyword **dscp** (`str`): DSCP marking to be used on
                  tunnel keepalive packets to determine if tunnel remote
                  IP address is reachable
            * keyword **gms_marked** (`bool`): ``True`` if configured by
              Orchestrator
            * keyword **gre_proto** (`int`): GRE protocol in the GRE
              header
            * keyword **id2** (`int`): NEEDS DESCRIPTION
            * keyword **ipsec_arc_window** (`str`): IPSec ARC Window,
              not configurable
            * keyword **ipsec_enable** (`bool`): ``True`` if IPSec
              tunnel
            * keyword **presharedkey** (`str`): Tunnel preshared key
            * keyword **ipsec_udp_sport** (`str`): IPSec UDP tunnel
              source port
            * keyword **ipsec_udp_dport** (`str`): IPSec UDP tunnel
              destination port
            * keyword **orch_tid** (`list[int]`): NEEDS DESCRIPTION
            * keyword **max_bw** (`int`): If the tunnel max bandwidth is
              manually configured, use this field and set max_bw_auto to
              ``false``
            * keyword **max_bw_auto** (`bool`): If the tunnel max
              bandwidth needs to be set to auto, this field must be true
            * keyword **max_bw_unshaped** (`bool`): false,
            * keyword **min_bw** (`int`): Tunnel minimum bandwidth
            * keyword **mode** (`str`): Tunnel mode, e.g. ``udp_sp``
            * keyword **mtu** (`str`): Tunnel MTU, e.g. ``1500``
            * keyword **peername** (`str`): Tunnel peer name
            * keyword **nat_mode** (`str`): Tunnel NAT mode, e.g.
              ``auto``, ``none``
            * keyword **pkt** (`dict`): Packet settings object \n
                * keyword **coalesce_enable** (`bool`): Packet
                  coalescing enabled
                * keyword **coalesce_wait** (`int`): Packet coalescing
                  wait timer
                * keyword **fec_enable_str** (`str`): FEC enabled, e.g.
                  ``enable``, ``disable``, or ``auto``
                * keyword **fec_reset_intvl** (`int`): FEC reset
                  interval, e.g. ``1``, ``2``, ``5``, ``10``, or ``20``
                * keyword **fec_max_ratio** (`int`): FEC auto maximum
                  ration, e.g. ``10``
                * keyword **fec_min_ratio** (`int`): FEC auto minimum
                  ration, e.g. ``0``
                * keyword **frag_enable** (`bool`): Enable tunnel packet
                  fragmentation and reassembly
                * keyword **reorder_wait** (`int`): Amount of time in ms
                  to wait for Packet Order Correction algorithm
            * keyword **tag_name** (`str`): Overlay name, e.g.
              ``BulkApps``
            * keyword **threshold** (`dict`): Tunnel fail thresholds \n
                * keyword **fastfail** (`int`): Enable fast fail,
                  increasing the frequency of tunnel health packets,
                  e.g. ``0``, ``1``, or ``2``
                * keyword **fastfail-wait-base** (`int`): 150,
                * keyword **fastfail-wait-rtt** (`int`): 5,
                * keyword **jitter** (`int`): Jitter threshold, ``0`` if
                  not configured
                * keyword **latency** (`int`): Latency threshold, ``0``
                  if not configured
                * keyword **loss** (`int`): Loss threshold, ``0`` if
                  not configured
                * keyword **retry_count** (`int`): How many packets
                  which are sent once per second should be missed before
                  a tunnel is declared down, e.g. ``3``
            * keyword **type** (`str`): e.g. ``bonded``
            * keyword **udp_dest_port** (`int`): If the tunnel is of
              type 'udp', the udp port to use, e.g. ``4163``
            * keyword **udp_flows** (`int`): If tunnel mode is udp, this
              field determines how many different udp flows are used to
              distribute tunnel traffic, e.g. ``256``
            * keyword **local_vrf** (`int`): Local VRF ID, Default
              segment would be ``0``
            * keyword **source** (`str`): Source IP address of tunnel,
              for bonded tunnels this is ``127.0.0.0``
            * keyword **destination** (`str`): Destination IP address of
              tunnel, for bonded tunnels this is ``127.0.0.0``
            * keyword **bound_tun** (`dict`): Tunnels bound to bonded
              tunnel \n
                * keyword **<tunnel_id>** (`str`): Underlay tunnel alias
                  e.g. ``to_<REMOTE_EC_HOSTNAME>_INET1-INET1``
    :rtype: dict
    """
    return self._post(
        "/bondedTunnels/getMultiple",
        data=tunnel_list,
    )


def delete_appliance_multiple_bonded_tunnels(
    self,
    tunnel_list: list[str],
) -> bool:
    """Delete multiple bonded tunnels from appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - bondedTunnel
          - POST
          - /bondedTunnels/deleteMultiple

    :param tunnel_list: List of tunnel id's to query for
    :type tunnel_list: list[str]
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/bondedTunnels/deleteMultiple",
        data=tunnel_list,
        return_type="bool",
    )


def get_appliance_bonded_tunnel_live_view_info(
    self,
    tunnel_id: str,
) -> dict:
    """Get Live View state information for specific overlay tunnel

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - bondedTunnel
          - POST
          - /liveViewInfo/{id}

    :param tunnel_id: Tunnel id of tunnel to retrieve information for,
        e.g. ``bondedTunnel_385``
    :type tunnel_id: str
    :return: Returns dictionary of Live View state information for
        overlay tunnel queried \n
        * keyword **state_bin** (`dict`): Status object \n
            * keywoord **tun_state** (`str`): Tunnel status, e.g.
              ``Up - Idle``
            * keyword **overlay** (`dict`): Overlay live view stats \n
                * keyword **black_tun_list** (`list[str]`): List of
                  tunnels exlcluded from overlay due to blackout
                  conditions
                * keyword **black_reason_fastfail** (`list[str]`): List
                  of tunnels excluded from overlay due to fast fail
                  blackout
                * keyword **brown_tun_list** (`list[str]`): List of
                  tunnels in brownout status
                * keyword **brown_reason_loss** (`list[str]`): List of
                  tunnels in brownout status because of loss
                * keyword **brown_reason_latency** (`list[str]`): List
                  of tunnels in brownout status because of latency
                * keyword **brown_reason_jitter** (`list[str]`): List of
                  tunnels in brownout status because of jitter
                * keyword **green_tun_list** (`list[str]`): List of
                  underlay tunnels in green status
                * keyword **curr_tun_list** (`list[str]`): List of
                  underlay tunnels currently in use
                * keyword **best_link** (`str`): Current best performing
                  underlay tunnel, e.g. ``tunnel_404``
                * keyword **ts** (`int`): Unix epoch timestamp in ms
                * keyword **bonded_tunnel_state_brown** (`int`):
                  Overall overlay tunnel brownout status, ``0`` for
                  green, ``1`` for brownout
                * keyword **bonded_tunnel_state_brown_lat** (`int`):
                  overlay tunnel brownout status due to latency, ``0``
                  for green, ``1`` for brownout
                * keyword **bonded_tunnel_state_brown_loss** (`int`):
                  overlay tunnel brownout status due to loss, ``0``
                  for green, ``1`` for brownout
                * keyword **bonded_tunnel_state_brown_jit** (`int`):
                  overlay tunnel brownout status due to jitter, ``0``
                  for green, ``1`` for brownout
    """
    return self._get(f"/liveViewInfo/{tunnel_id}")
