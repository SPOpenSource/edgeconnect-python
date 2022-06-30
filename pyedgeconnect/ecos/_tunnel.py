# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# tunnel : Underlay SDWAN Tunnels
from __future__ import annotations


def get_appliance_tunnels_config_and_state(
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
        * - tunnel
          - GET
          - /tunnelsConfigAndState

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
              ``to_<REMOTE_EC_HOSTNAME>_<LOCAL_LABEL>_<REMOTE_LABEL>``
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
            * keyword **ipsec** (`dict`): IPSec Configuration object \n
                * keyword **security** (`dict`): security settings \n
                    * keyword **ah** (`dict`): \n
                        * keyword **algorithm** (`str`): e.g. ``sha1``
                    * keyword **esp** (`dict`): \n
                        * keyword **algorithm** (`str`): e.g. ``sha1``
                * keyword **mode** (`str`): e.g. ``transport``
                * keyword **exchange_mode** (`str`): e.g. ``main``
                * keyword **ike_aalg** (`str`): IKE Algo, e.g. ``sha1``
                * keyword **ike_ealg** (`str`): e.g. ``default``
                * keyword **dhgroup** (`int`): Diffie-Hellman Group,
                  e.g. ``14``
                * keyword **pfs** (`bool`): e.g. ``true``
                * keyword **pfsgroup** (`str`): e.g. ``14``
                * keyword **id_type** (`str`): e.g. ``address``
                * keyword **ike_version** (`int`): IKE version,
                  e.g. ``1``
                * keyword **esn** (`bool`): e.g. ``true``
                * keyword **id_str** (`str`): "",
                * keyword **dpd_delay** (`int`): e.g. ``10``
                * keyword **dpd_retry** (`int`): e.g. ``3``
                * keyword **ike_lifetime** (`int`): e.g. ``360``
                * keyword **lifetime** (`int`): e.g. ``360``
                * keyword **lifebytes** (`int`): e.g. ``0``
                * keyword **ike_id_local** (`str`): Local IKE ID
                * keyword **ike_id_remote** (`str`): Remote IKE ID
            * keyword **max_bw** (`int`): If the tunnel max bandwidth is
              manually configured, use this field and set max_bw_auto to
              ``false``
            * keyword **max_bw_auto** (`bool`): If the tunnel max
              bandwidth needs to be set to auto, this field must be true
            * keyword **max_bw_unshaped** (`bool`): false,
            * keyword **min_bw** (`int`): Tunnel minimum bandwidth
            * keyword **mode** (`str`): Tunnel mode, e.g. ``ipsec_udp``
            * keyword **mtu** (`str`): Tunnel MTU, e.g. ``1488``
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
            * keyword **tag_name** (`str`): Label ID pairs in string of
              ``<local_label_id>-<remote_label_id>`` e.g. if INET1 has a
              label id of ``5`` then a tunnel between INET1 and INET1
              would have ``tag_name`` of ``5-5``
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
            * keyword **type** (`str`): NEEDS DESCRIPTION
            * keyword **udp_dest_port** (`int`): If the tunnel is of
              type 'udp', the udp port to use, e.g. ``4163``
            * keyword **udp_flows** (`int`): If tunnel mode is udp, this
              field determines how many different udp flows are used to
              distribute tunnel traffic, e.g. ``256``
            * keyword **local_vrf** (`int`): Local VRF ID, Default
              segment would be ``0``
            * keyword **source** (`str`): Source IP address of tunnel
            * keyword **destination** (`str`): Destination IP address of
              tunnel
            * keyword **uptime** (`int`): Tunnel uptime in ms
            * keyword **status** (`str`): Tunnel status,
              e.g. ``Up - Idle``
            * keyword **isRediscoveringMTU** (`bool`): This flag is true
              if auto-mtu discovery is in progress
            * keyword **cur_max_bw** (`str`): Tunnel maximum bandwidth
              can be lower than configured when using dynamic tunnel
              bandwidth feature. This field shows the current tunnel
              bandwidth. It can change every second. Units in Kbps, e.g.
              ``50000`` for 50Mbps
            * keyword **state_bin** (`dict`): Remote NAT \n
                * keyword **ipsec_nat_addr** (`str`): Remote NAT address
                * keyword **ipsec_nat_port** (`str`): Remote NAT port
    :rtype: dict
    """
    path = "/tunnelsConfigAndState"
    if state_match is not None:
        path += f"?state={state_match}"
    return self._get(path)


def get_appliance_tunnels_config(
    self,
    state_match: str = None,
) -> dict:
    """Get the current list of tunnels and their configuration

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnel
          - GET
          - /tunnels

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
              ``to_<REMOTE_EC_HOSTNAME>_<LOCAL_LABEL>_<REMOTE_LABEL>``
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
            * keyword **ipsec** (`dict`): IPSec Configuration object \n
                * keyword **security** (`dict`): security settings \n
                    * keyword **ah** (`dict`): \n
                        * keyword **algorithm** (`str`): e.g. ``sha1``
                    * keyword **esp** (`dict`): \n
                        * keyword **algorithm** (`str`): e.g. ``sha1``
                * keyword **mode** (`str`): e.g. ``transport``
                * keyword **exchange_mode** (`str`): e.g. ``main``
                * keyword **ike_aalg** (`str`): IKE Algo, e.g. ``sha1``
                * keyword **ike_ealg** (`str`): e.g. ``default``
                * keyword **dhgroup** (`int`): Diffie-Hellman Group,
                  e.g. ``14``
                * keyword **pfs** (`bool`): e.g. ``true``
                * keyword **pfsgroup** (`str`): e.g. ``14``
                * keyword **id_type** (`str`): e.g. ``address``
                * keyword **ike_version** (`int`): IKE version,
                  e.g. ``1``
                * keyword **esn** (`bool`): e.g. ``true``
                * keyword **id_str** (`str`): "",
                * keyword **dpd_delay** (`int`): e.g. ``10``
                * keyword **dpd_retry** (`int`): e.g. ``3``
                * keyword **ike_lifetime** (`int`): e.g. ``360``
                * keyword **lifetime** (`int`): e.g. ``360``
                * keyword **lifebytes** (`int`): e.g. ``0``
                * keyword **ike_id_local** (`str`): Local IKE ID
                * keyword **ike_id_remote** (`str`): Remote IKE ID
            * keyword **max_bw** (`int`): If the tunnel max bandwidth is
              manually configured, use this field and set max_bw_auto to
              ``false``
            * keyword **max_bw_auto** (`bool`): If the tunnel max
              bandwidth needs to be set to auto, this field must be true
            * keyword **max_bw_unshaped** (`bool`): false,
            * keyword **min_bw** (`int`): Tunnel minimum bandwidth
            * keyword **mode** (`str`): Tunnel mode, e.g. ``ipsec_udp``
            * keyword **mtu** (`str`): Tunnel MTU, e.g. ``1488``
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
            * keyword **tag_name** (`str`): Label ID pairs in string of
              ``<local_label_id>-<remote_label_id>`` e.g. if INET1 has a
              label id of ``5`` then a tunnel between INET1 and INET1
              would have ``tag_name`` of ``5-5``
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
            * keyword **type** (`str`): NEEDS DESCRIPTION
            * keyword **udp_dest_port** (`int`): If the tunnel is of
              type 'udp', the udp port to use, e.g. ``4163``
            * keyword **udp_flows** (`int`): If tunnel mode is udp, this
              field determines how many different udp flows are used to
              distribute tunnel traffic, e.g. ``256``
            * keyword **local_vrf** (`int`): Local VRF ID, Default
              segment would be ``0``
            * keyword **source** (`str`): Source IP address of tunnel
            * keyword **destination** (`str`): Destination IP address of
              tunnel
    :rtype: dict
    """
    path = "/tunnels"
    if state_match is not None:
        path += f"?state={state_match}"
    return self._get(path)


def configure_appliance_all_tunnels(
    self,
    tunnel_configuration: dict,
) -> bool:
    """Add/delete/modify tunnels

    .. warning::
        This function would update all tunnels. Existing tunnel IDs will
        be updated, New tunnel IDs will be created, missing tunnel IDs
        will be deleted!

        Use :func:`~pyedgeconnect.EdgeConnect.get_appliance_tunnels_config`
        to get current tunnel configuration

        Use :func:`~pyedgeconnect.EdgeConnect.configure_appliance_multiple_tunnels`
        to only add net-new tunnels without having to include existing
        tunnels and avoid accidental tunnel deletions

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnel
          - POST
          - /tunnels


    :param tunnel_configuration: Dictionary structure for configuring
        tunnels on EdgeConnect appliance. See response from
        :func:`~pyedgeconnect.EdgeConnect.get_appliance_tunnels_config`
        for documentation of data structure
    :type tunnel_configuration: dict
    :return: Returns True/False based on successful call
    :rtype: bool
    """  # noqa:W505,E501
    return self._post(
        "/tunnels",
        data=tunnel_configuration,
        return_type="bool",
    )


def get_appliance_single_tunnel_config(
    self,
    tunnel_id: str,
) -> dict:
    """Get specific tunnel configuration by tunnel id from appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnel
          - GET
          - /tunnels/{id}

    :param tunnel_id: Tunnel id of tunnel to retrieve information for,
        e.g. ``tunnel_385``
    :type tunnel_id: str
    :return: Returns dictionary of tunnel configuration for specific
        tunnel \n
        * keyword **admin** (`str`): Admin state of the tunnel -
          takes two values: ``up`` or ``down``
        * keyword **alias** (`str`): Tunnel alias/name, e.g.
          ``to_<REMOTE_EC_HOSTNAME>_<LOCAL_LABEL>_<REMOTE_LABEL>``
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
        * keyword **ipsec** (`dict`): IPSec Configuration object \n
            * keyword **security** (`dict`): security settings \n
                * keyword **ah** (`dict`): \n
                    * keyword **algorithm** (`str`): e.g. ``sha1``
                * keyword **esp** (`dict`): \n
                    * keyword **algorithm** (`str`): e.g. ``sha1``
            * keyword **mode** (`str`): e.g. ``transport``
            * keyword **exchange_mode** (`str`): e.g. ``main``
            * keyword **ike_aalg** (`str`): IKE Algo, e.g. ``sha1``
            * keyword **ike_ealg** (`str`): e.g. ``default``
            * keyword **dhgroup** (`int`): Diffie-Hellman Group,
              e.g. ``14``
            * keyword **pfs** (`bool`): e.g. ``true``
            * keyword **pfsgroup** (`str`): e.g. ``14``
            * keyword **id_type** (`str`): e.g. ``address``
            * keyword **ike_version** (`int`): IKE version,
              e.g. ``1``
            * keyword **esn** (`bool`): e.g. ``true``
            * keyword **id_str** (`str`): "",
            * keyword **dpd_delay** (`int`): e.g. ``10``
            * keyword **dpd_retry** (`int`): e.g. ``3``
            * keyword **ike_lifetime** (`int`): e.g. ``360``
            * keyword **lifetime** (`int`): e.g. ``360``
            * keyword **lifebytes** (`int`): e.g. ``0``
            * keyword **ike_id_local** (`str`): Local IKE ID
            * keyword **ike_id_remote** (`str`): Remote IKE ID
        * keyword **max_bw** (`int`): If the tunnel max bandwidth is
          manually configured, use this field and set max_bw_auto to
          ``false``
        * keyword **max_bw_auto** (`bool`): If the tunnel max
          bandwidth needs to be set to auto, this field must be true
        * keyword **max_bw_unshaped** (`bool`): false,
        * keyword **min_bw** (`int`): Tunnel minimum bandwidth
        * keyword **mode** (`str`): Tunnel mode, e.g. ``ipsec_udp``
        * keyword **mtu** (`str`): Tunnel MTU, e.g. ``1488``
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
        * keyword **tag_name** (`str`): Label ID pairs in string of
          ``<local_label_id>-<remote_label_id>`` e.g. if INET1 has a
          label id of ``5`` then a tunnel between INET1 and INET1
          would have ``tag_name`` of ``5-5``
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
        * keyword **type** (`str`): NEEDS DESCRIPTION
        * keyword **udp_dest_port** (`int`): If the tunnel is of
          type 'udp', the udp port to use, e.g. ``4163``
        * keyword **udp_flows** (`int`): If tunnel mode is udp, this
          field determines how many different udp flows are used to
          distribute tunnel traffic, e.g. ``256``
        * keyword **local_vrf** (`int`): Local VRF ID, Default
          segment would be ``0``
        * keyword **source** (`str`): Source IP address of tunnel
        * keyword **destination** (`str`): Destination IP address of
          tunnel
    :rtype: dict
    """
    return self._get(f"/tunnels/{tunnel_id}")


def configure_appliance_single_tunnel(
    self,
    tunnel_id: str,
    tunnel_configuration: dict,
) -> bool:
    """Modify or Add single tunnel configuration by tunnel id

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnel
          - POST
          - /tunnels/{id}

    :param tunnel_id: Tunnel id of tunnel to retrieve information for,
        e.g. ``tunnel_385``
    :type tunnel_id: str
    :param tunnel_configuration: Dictionary structure for configuring
        tunnel on EdgeConnect appliance. See response from
        :func:`~pyedgeconnect.EdgeConnect.get_appliance_single_tunnel_config`
        for documentation of data structure
    :type tunnel_configuration: dict
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._get(
        f"/tunnels/{tunnel_id}",
        data=tunnel_configuration,
        return_type="bool",
    )


def delete_appliance_single_tunnel(
    self,
    tunnel_id: str,
) -> bool:
    """Delete specific tunnel configuration by tunnel id from appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnel
          - DELETE
          - /tunnels/{id}

    :param tunnel_id: Tunnel id of tunnel to retrieve information for,
        e.g. ``tunnel_385``
    :type tunnel_id: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        f"/tunnels/{tunnel_id}",
        return_type="bool",
    )


def get_appliance_all_tunnel_ids(
    self,
    state_match: str = None,
) -> list:
    """Get the current list of all physical tunnels

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnel
          - GET
          - /tunnelAllIDs

    :param state_match: Regular expression used to match tunnels state,
        e.g. ``Idle`` or ``Up`` would match all tunnels with ``status``
        of ``Up - Idle``
    :type state_match: str
    :return: Returns list of all tunnel ids
        e.g. ``["tunnel_385","default","pass-through",...]``
    :rtype: list
    """
    path = "/tunnelAllIDs"
    if state_match is not None:
        path += f"?state={state_match}"
    return self._get(path)


def get_appliance_tunnel_aliases(
    self,
    limit: int,
    alias_match: str = None,
    state_match: str = None,
) -> list:
    """Find tunnels with matching aliases on appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnel
          - GET
          - /tunnelAliases

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
    path = f"/tunnelAliases?limit={limit}"
    if alias_match is not None:
        path += f"&matchingAlias={alias_match}"
    if state_match is not None:
        path += f"&state={state_match}"
    return self._get(path)


def get_appliance_multiple_tunnels_config(
    self,
    tunnel_list: list[str],
) -> dict:
    """Get the configuration of multiple tunnels from appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnel
          - POST
          - /getMultipleTunnels

    :param tunnel_list: List of tunnel id's to query for
    :type tunnel_list: list[str]
    :return: Returns dictionary of specified tunnels queried \n
        * keyword **<tunnel_id>** (`dict`): Tunnel id and object \n
            * keyword **admin** (`str`): Admin state of the tunnel -
              takes two values: ``up`` or ``down``
            * keyword **alias** (`str`): Tunnel alias/name, e.g.
              ``to_<REMOTE_EC_HOSTNAME>_<LOCAL_LABEL>_<REMOTE_LABEL>``
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
            * keyword **ipsec** (`dict`): IPSec Configuration object \n
                * keyword **security** (`dict`): security settings \n
                    * keyword **ah** (`dict`): \n
                        * keyword **algorithm** (`str`): e.g. ``sha1``
                    * keyword **esp** (`dict`): \n
                        * keyword **algorithm** (`str`): e.g. ``sha1``
                * keyword **mode** (`str`): e.g. ``transport``
                * keyword **exchange_mode** (`str`): e.g. ``main``
                * keyword **ike_aalg** (`str`): IKE Algo, e.g. ``sha1``
                * keyword **ike_ealg** (`str`): e.g. ``default``
                * keyword **dhgroup** (`int`): Diffie-Hellman Group,
                  e.g. ``14``
                * keyword **pfs** (`bool`): e.g. ``true``
                * keyword **pfsgroup** (`str`): e.g. ``14``
                * keyword **id_type** (`str`): e.g. ``address``
                * keyword **ike_version** (`int`): IKE version,
                  e.g. ``1``
                * keyword **esn** (`bool`): e.g. ``true``
                * keyword **id_str** (`str`): "",
                * keyword **dpd_delay** (`int`): e.g. ``10``
                * keyword **dpd_retry** (`int`): e.g. ``3``
                * keyword **ike_lifetime** (`int`): e.g. ``360``
                * keyword **lifetime** (`int`): e.g. ``360``
                * keyword **lifebytes** (`int`): e.g. ``0``
                * keyword **ike_id_local** (`str`): Local IKE ID
                * keyword **ike_id_remote** (`str`): Remote IKE ID
            * keyword **max_bw** (`int`): If the tunnel max bandwidth is
              manually configured, use this field and set max_bw_auto to
              ``false``
            * keyword **max_bw_auto** (`bool`): If the tunnel max
              bandwidth needs to be set to auto, this field must be true
            * keyword **max_bw_unshaped** (`bool`): false,
            * keyword **min_bw** (`int`): Tunnel minimum bandwidth
            * keyword **mode** (`str`): Tunnel mode, e.g. ``ipsec_udp``
            * keyword **mtu** (`str`): Tunnel MTU, e.g. ``1488``
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
            * keyword **tag_name** (`str`): Label ID pairs in string of
              ``<local_label_id>-<remote_label_id>`` e.g. if INET1 has a
              label id of ``5`` then a tunnel between INET1 and INET1
              would have ``tag_name`` of ``5-5``
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
            * keyword **type** (`str`): NEEDS DESCRIPTION
            * keyword **udp_dest_port** (`int`): If the tunnel is of
              type 'udp', the udp port to use, e.g. ``4163``
            * keyword **udp_flows** (`int`): If tunnel mode is udp, this
              field determines how many different udp flows are used to
              distribute tunnel traffic, e.g. ``256``
            * keyword **local_vrf** (`int`): Local VRF ID, Default
              segment would be ``0``
            * keyword **source** (`str`): Source IP address of tunnel
            * keyword **destination** (`str`): Destination IP address of
              tunnel
    :rtype: dict
    """
    return self._post(
        "/getMultipleTunnels",
        data=tunnel_list,
    )


def get_appliance_multiple_tunnels_state(
    self,
    tunnel_list: list[str],
) -> dict:
    """Get the state of multiple tunnels from appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnel
          - POST
          - /getStateMultipleTunnels

    :param tunnel_list: List of tunnel id's to query for
    :type tunnel_list: list[str]
    :return: Returns dictionary of specified tunnels queried \n
        * keyword **<tunnel_id>** (`dict`): Tunnel id and object \n
            * keyword **self** (`str`): Tunnel id, e.g. ``tunnel_385``
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
                * keyword **ipsec_nat_addr** (`str`): Remote NAT address
                * keyword **ipsec_nat_port** (`str`): Remote NAT port
    :rtype: dict
    """
    return self._post(
        "/getMultipleTunnels",
        data=tunnel_list,
    )


def configure_appliance_multiple_tunnels(
    self,
    tunnel_configuration: dict,
) -> bool:
    """Add/modify multiple tunnels at once. Use
    :func:`~pyedgeconnect.EdgeConnect.get_appliance_tunnels_config` to
    get current tunnel configuration for example data structure.


    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnel
          - POST
          - /addMultipleTunnels


    :param tunnel_configuration: Dictionary structure for configuring
        multiple tunnels on EdgeConnect appliance. See response from
        :func:`~pyedgeconnect.EdgeConnect.get_appliance_tunnels_config`
        for documentation of data structure
    :type tunnel_configuration: dict
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/addMultipleTunnels",
        data=tunnel_configuration,
        return_type="bool",
    )


def delete_appliance_multiple_tunnels(
    self,
    tunnel_list: list[str],
) -> bool:
    """Delete multiple tunnels from appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnel
          - POST
          - /deleteMultipleTunnels

    :param tunnel_list: List of tunnel id's to query for
    :type tunnel_list: list[str]
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/deleteMultipleTunnels",
        data=tunnel_list,
        return_type="bool",
    )


def get_appliance_tunnel_source_endpoints(
    self,
) -> list:
    """Get a list of interface IP addresses which can be used as tunnel
    source IP addresses on this appliance.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnel
          - GET
          - /tunnelSourceEndpoints

    :return: Returns list of possible tunnel source IP addresses \n
        * [`list[list[str,int,int]]`]: Tunnel endpoint array \n
            * [`list[str,int,int]`]: Available tunnel endpoint array \n
                * [0] (`str`): IP Address string, e.g. ``192.168.1.1``
                * [1] (`int`): CIDR mask, e.g. ``30``
                * [2] (`int`): VRF/Segment ID, e.g. ``0`` for Default
    :rtype: list

    Example response:

    .. code::

        [
            [
                "192.168.1.1",
                30,
                0,
            ],
        ]
    """
    return self._get("tunnelSourceEndpoints")


def get_appliance_passthrough_tunnel_source_endpoints(
    self,
) -> list:
    """Get a list of interface IP addresses which can be used as
    passthrough tunnel source IP addresses on this appliance.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnel
          - GET
          - /passThroughTunnelSourceEndpoints

    :return: Returns list of possible passthrough tunnel source IP
        addresses \n
        * [`list[list[str,int,int]]`]: Tunnel endpoint array \n
            * [`list[str,int,int]`]: Available tunnel endpoint array \n
                * [0] (`str`): IP Address string, e.g. ``192.168.1.1``
                * [1] (`int`): CIDR mask, e.g. ``30``
                * [2] (`int`): VRF/Segment ID, e.g. ``0`` for Default
    :rtype: list
    """
    return self._get("passThroughTunnelSourceEndpoints")


def start_appliance_tunnel_mtu_discovery(
    self,
    tunnel_list: list[str],
) -> bool:
    """Start MTU discovery on list of of specified tunnels on appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnel
          - POST
          - /tunnelsAutoDiscoverMtu

    :param tunnel_list: List of tunnel id's to query for
    :type tunnel_list: list[str]
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {"tunnels": tunnel_list}
    return self._post(
        "/tunnelsAutoDiscoverMtu",
        data=data,
        return_type="bool",
    )


def apply_appliance_tunnel_template(
    self,
    tunnel_configuration: dict,
) -> bool:
    """Use this method to set a group of properties across all existing
    tunnels on the system. There is an additional property called:
    ``apply_to_default`` which can be used to change the settings of
    'default' tunnel as well. This allows automatically established
    tunnels to come up with these settings.

    .. important::

        You can omit fields from the schema which you do not want to
        change.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnel
          - POST
          - /applyTunnelTemplate

    :param tunnel_configuration: Dictionary structure for configuring
        tunnel template settings on EdgeConnect appliance. \n

        Example data structure:

        .. code::

            tunnel_configuration = {
                "min_bw": 0,
                "max_bw_auto": false,
                "max_bw": 0,
                "admin": "",
                "ipsec_arc_window": "",
                "mode": "",
                "ctrl_pkt": {
                    "dscp": ""
                },
                "destination": "",
                "pkt": {
                    "frag_enable": false,
                    "fec_enable_str": "",
                    "fec_reset_intvl": 0,
                    "fec_min_ratio": 0,
                    "fec_max_ratio": 0,
                    "reorder_wait": 0
                },
                "auto_mtu": false,
                "threshold": {
                    "dbw_aimd": false,
                    "dbw_rserc": false,
                    "retry_count": 0,
                    "fastfail": 0
                },
                "gre_proto": 0,
                "udp_dest_port": 0,
                "source": "",
                "ipsec_enable": false,
                "mtu": 0,
                "options": 0,
                "type": "",
                "udp_flows": 0,
                "local_vrf": 0,
                "ipsec": {
                    "security": {
                    "ah": {
                        "algorithm": ""
                    },
                    "esp": {
                        "algorithm": ""
                    }
                    },
                    "lifetime": 0,
                    "lifebytes": 0,
                    "pfsgroup": "",
                    "pfs": false,
                    "ike_aalg": "",
                    "ike_ealg": "",
                    "dhgroup": "",
                    "dpd_delay": 0,
                    "dpd_retry": 0,
                    "id_type": "",
                    "id_str": "",
                    "exchange_mode": "",
                    "ike_version": 0,
                    "esn": false
                    }
                }
    :type tunnel_configuration: dict
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/applyTunnelTemplate",
        data=tunnel_configuration,
        return_type="bool",
    )


def set_appliance_tunnels_ipsec_psk(
    self,
    tunnels_psk: dict,
) -> bool:
    """Set the ipsec preshared key for multiple tunnels

    .. important::

        You can omit fields from the schema which you do not want to
        change.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnel
          - POST
          - /tunnelsIpsecKey

    :param tunnels_psk: Dictionary structure for configuring
        tunnel pre-shared key settings.
    :type tunnel_configuration: dict

        Example data structure:

        .. code::

            tunnel_configuration = {
                "tunnel_123": {
                    "presharedkey": "mypresharedkeyvalue"
                },
            }

    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/tunnelsIpsecKey",
        data=tunnels_psk,
        return_type="bool",
    )
