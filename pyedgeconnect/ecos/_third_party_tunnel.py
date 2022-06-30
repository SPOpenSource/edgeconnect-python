# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# thirdPartyTunnel : Third Party Tunnels
from __future__ import annotations


def get_appliance_3rdparty_tunnels_state(
    self,
    state_match: str = None,
) -> dict:
    """Get the current list of passthrough tunnels state information
    like uptime and operational state

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyTunnel
          - GET
          - /thirdPartyTunnels/state

    :param state_match: Regular expression used to match tunnels state,
        e.g. ``Idle`` or ``Up`` would match all tunnels with ``status``
        of ``Up - Idle``
    :type state_match: str
    :return: Returns dictionary of tunnels with status matched from the
        ``state_match`` parameter \n
        * keyword **<tunnel_id>** (`dict`): Tunnel id and object \n
            * keyword **self** (`str`): Tunnel id, e.g.
              ``passThrough_199``
            * keyword **oper** (`str`): Status, e.g. ``Up - Active``
            * keyword **uptime** (`int`): Tunnel uptime in ms
            * keyword **cur_mtu** (`str`): Tunnel MTU, e.g. ``1500``
            * keyword **cur_max_bw** (`str`): Current tunnel maximum
              bandwidth. Units in Kbps, e.g. ``50000`` for 50Mbps
            * keyword **rem_sys_bw** (`str`): Remaining system bandwidth
            * keyword **quiescence** (`bool`): ``True`` if tunnel is in
              Idle state / quiescence mode
            * keyword **remote_id** (`int`): NEEDS DESCRIPTION
            * keyword **state_bin** (`dict`): \n
                * keyword **tun_state** (`str`): Tunnel status,
                  e.g. ``Up - Active``
                * keyword **uptime** (`int`): Tunnel uptime in ms
                * keyword **cur_mtu** (`str`): Tunnel MTU, e.g. ``1500``
                * keyword **local_id** (`int`): Local ID
                * keyword **bonded** (`bool`): Tunnel bonded state,
                  ``False`` for passthrough tunnels
                * keyword **ipsec_nat_addr** (`str`): ``NONE`` for
                  passthrough tunnels
                * keyword **ipsec_nat_port** (`str`): ``NONE`` for
                  passthrough tunnels
    :rtype: dict
    """
    path = "/thirdPartyTunnels/state"
    if state_match is not None:
        path += f"?state={state_match}"
    return self._get(path)


def get_appliance_multiple_3rdparty_tunnels_state(
    self,
    tunnel_list: list[str],
) -> dict:
    """Get the state of multiple passthrough tunnels from appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyTunnel
          - POST
          - /thirdPartyTunnels/getStateMultiple

    :param tunnel_list: List of tunnel id's to query for
    :type tunnel_list: list[str]
    :return: Returns dictionary of specified tunnels queried \n
        * keyword **<tunnel_id>** (`dict`): Tunnel id and object \n
            * keyword **self** (`str`): Tunnel id, e.g.
              ``passThrough_199``
            * keyword **oper** (`str`): Status, e.g. ``Up - Active``
            * keyword **uptime** (`int`): Tunnel uptime in ms
            * keyword **cur_mtu** (`str`): Tunnel MTU, e.g. ``1500``
            * keyword **cur_max_bw** (`str`): Current tunnel maximum
              bandwidth. Units in Kbps, e.g. ``50000`` for 50Mbps
            * keyword **rem_sys_bw** (`str`): Remaining system bandwidth
            * keyword **quiescence** (`bool`): ``True`` if tunnel is in
              Idle state / quiescence mode
            * keyword **remote_id** (`int`): NEEDS DESCRIPTION
            * keyword **state_bin** (`dict`): \n
                * keyword **tun_state** (`str`): Tunnel status,
                  e.g. ``Up - Active``
                * keyword **uptime** (`int`): Tunnel uptime in ms
                * keyword **cur_mtu** (`str`): Tunnel MTU, e.g. ``1500``
                * keyword **local_id** (`int`): Local ID
                * keyword **bonded** (`bool`): Tunnel bonded state,
                  ``False`` for passthrough tunnels
                * keyword **ipsec_nat_addr** (`str`): ``NONE`` for
                  passthrough tunnels
                * keyword **ipsec_nat_port** (`str`): ``NONE`` for
                  passthrough tunnels
    :rtype: dict
    """
    return self._post(
        "/thirdPartyTunnels/getStateMultiple",
        data=tunnel_list,
    )


def get_appliance_all_3rdparty_tunnel_ids(
    self,
    state_match: str = None,
) -> list:
    """Get the current list of all passthrough tunnels

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyTunnel
          - GET
          - /thirdPartyTunnels/allIDs

    :param state_match: Regular expression used to match tunnels state,
        e.g. ``Idle`` or ``Up`` would match all tunnels with ``status``
        of ``Up - Idle``
    :type state_match: str
    :return: Returns list of all tunnel ids
        e.g. ``["passThrough_320","passThrough_321",...]``
    :rtype: list
    """
    path = "/thirdPartyTunnels/allIDs"
    if state_match is not None:
        path += f"?state={state_match}"
    return self._get(path)


def get_appliance_3rdparty_tunnel_aliases(
    self,
    limit: int,
    alias_match: str = None,
    state_match: str = None,
) -> list:
    """Find passthrough tunnels with matching aliases on appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyTunnel
          - GET
          - /thirdPartyTunnels/aliases

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
    path = f"/thirdPartyTunnels/aliases?limit={limit}"
    if alias_match is not None:
        path += f"&matchingAlias={alias_match}"
    if state_match is not None:
        path += f"&state={state_match}"
    return self._get(path)


def get_appliance_3rdparty_tunnels_config(
    self,
    state_match: str = None,
) -> dict:
    """Get the current list of passthrough tunnels and their
    configuration

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyTunnel
          - GET
          - /thirdPartyTunnels/config

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
              ``AWS_<TGNM_NAME>_Primary_TGNM1`` for AWS TGNM,
              ``<EC_HOSTNAME>_<LABEL>@<REMOTE_IP_ADDRESS>`` for Serivce
              Orchestration endpoint,
              ``ThirdParty_Zscaler_<LABEL>_<Primary/Secondary>_Z#`` for
              ZScaler etc.
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
            * keyword **mode** (`str`): Tunnel mode, e.g. ``ipsec_udp``,
              ``ipsec_ip``, or ``no_encap``
            * keyword **mtu** (`str`): Tunnel MTU, e.g. ``1488``
            * keyword **peername** (`str`): Tunnel peer name, often
              blank, but for BIO local breakout will take form of e.g.
              ``Overlay_RealTime_Primary``
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
            * keyword **tag_name** (`str`): Varies by tunnel type,
              can have label id's (``25-5``), tunnel names for
              ThirdParty name ``Zscaler_25_Primary_Z2``, or interface
              name for local passthrough, ``lan0`` or ``wan0``
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
            * keyword **local_vrf** (`int`): Local VRF ID, Default
              segment would be ``0``
            * keyword **source** (`str`): Source IP address of tunnel
            * keyword **destination** (`str`): Destination IP address of
              tunnel, ``0.0.0.0/0`` for passthrough breakout tunnels
    :rtype: dict
    """
    path = "/thirdPartyTunnels/config"
    if state_match is not None:
        path += f"?state={state_match}"
    return self._get(path)


def configure_appliance_multiple_3rdparty_tunnels(
    self,
    tunnel_configuration: dict,
) -> bool:
    """Add/modify multiple tunnels at once. Use
    :func:`~pyedgeconnect.EdgeConnect.get_appliance_3rdparty_tunnels_config`
    to get current tunnel configuration for example data structure.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyTunnel
          - POST
          - /thirdPartyTunnels/config

    :param tunnel_configuration: Dictionary structure for configuring
        multiple tunnels on EdgeConnect appliance. See response from
        :func:`~pyedgeconnect.EdgeConnect.get_appliance_3rdparty_tunnels_config`
        for documentation of data structure
    :type tunnel_configuration: dict
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/thirdPartyTunnels/config",
        data=tunnel_configuration,
        return_type="bool",
    )


def get_appliance_single_3rdparty_tunnel_config(
    self,
    tunnel_id: str,
) -> dict:
    """Get specific passthrough tunnel configuration by tunnel id from
    appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyTunnel
          - GET
          - /thirdPartyTunnels/config/{id}

    :param tunnel_id: Tunnel id of tunnel to retrieve information for,
        e.g. ``passThrough_385``
    :type tunnel_id: str
    :return: Returns dictionary of tunnel configuration for specific
        tunnel \n
        * keyword **admin** (`str`): Admin state of the tunnel -
          takes two values: ``up`` or ``down``
        * keyword **alias** (`str`): Tunnel alias/name, e.g.
          ``AWS_<TGNM_NAME>_Primary_TGNM1`` for AWS TGNM,
          ``<EC_HOSTNAME>_<LABEL>@<REMOTE_IP_ADDRESS>`` for Serivce
          Orchestration endpoint,
          ``ThirdParty_Zscaler_<LABEL>_<Primary/Secondary>_Z#`` for
          ZScaler etc.
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
        * keyword **mode** (`str`): Tunnel mode, e.g. ``ipsec_udp``,
          ``ipsec_ip``, or ``no_encap``
        * keyword **mtu** (`str`): Tunnel MTU, e.g. ``1488``
        * keyword **peername** (`str`): Tunnel peer name, often
          blank, but for BIO local breakout will take form of e.g.
          ``Overlay_RealTime_Primary``
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
        * keyword **tag_name** (`str`): Varies by tunnel type,
          can have label id's (``25-5``), tunnel names for
          ThirdParty name ``Zscaler_25_Primary_Z2``, or interface
          name for local passthrough, ``lan0`` or ``wan0``
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
        * keyword **local_vrf** (`int`): Local VRF ID, Default
          segment would be ``0``
        * keyword **source** (`str`): Source IP address of tunnel
        * keyword **destination** (`str`): Destination IP address of
          tunnel, ``0.0.0.0/0`` for passthrough breakout tunnels
    :rtype: dict
    """
    return self._get(f"/tunnels/{tunnel_id}")


def delete_appliance_single_3rdparty_tunnel(
    self,
    tunnel_id: str,
) -> bool:
    """Delete specific passthrough tunnel configuration by tunnel id
    from appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyTunnel
          - DELETE
          - /thirdPartyTunnels/config/{id}

    :param tunnel_id: Tunnel id of tunnel to retrieve information for,
        e.g. ``passThrough_385``
    :type tunnel_id: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        f"/thirdPartyTunnels/config/{tunnel_id}",
        return_type="bool",
    )


def get_appliance_multiple_3rdparty_tunnels_config(
    self,
    tunnel_list: list[str],
) -> dict:
    """Get the configuration of multiple passthrough tunnels from
    appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyTunnel
          - POST
          - /thirdPartyTunnels/getMultiple

    :param tunnel_list: List of tunnel id's to query for
    :type tunnel_list: list[str]
    :return: Returns dictionary of specified tunnels queried \n
        * keyword **<tunnel_id>** (`dict`): Tunnel id and object \n
            * keyword **admin** (`str`): Admin state of the tunnel -
              takes two values: ``up`` or ``down``
            * keyword **alias** (`str`): Tunnel alias/name, e.g.
              ``AWS_<TGNM_NAME>_Primary_TGNM1`` for AWS TGNM,
              ``<EC_HOSTNAME>_<LABEL>@<REMOTE_IP_ADDRESS>`` for Serivce
              Orchestration endpoint,
              ``ThirdParty_Zscaler_<LABEL>_<Primary/Secondary>_Z#`` for
              ZScaler etc.
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
            * keyword **mode** (`str`): Tunnel mode, e.g. ``ipsec_udp``,
              ``ipsec_ip``, or ``no_encap``
            * keyword **mtu** (`str`): Tunnel MTU, e.g. ``1488``
            * keyword **peername** (`str`): Tunnel peer name, often
              blank, but for BIO local breakout will take form of e.g.
              ``Overlay_RealTime_Primary``
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
            * keyword **tag_name** (`str`): Varies by tunnel type,
              can have label id's (``25-5``), tunnel names for
              ThirdParty name ``Zscaler_25_Primary_Z2``, or interface
              name for local passthrough, ``lan0`` or ``wan0``
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
            * keyword **local_vrf** (`int`): Local VRF ID, Default
              segment would be ``0``
            * keyword **source** (`str`): Source IP address of tunnel
            * keyword **destination** (`str`): Destination IP address of
              tunnel, ``0.0.0.0/0`` for passthrough breakout tunnels
    :rtype: dict
    """
    return self._post(
        "/thirdPartyTunnels/getMultiple",
        data=tunnel_list,
    )


def delete_appliance_multiple_3rdparty_tunnels(
    self,
    tunnel_list: list[str],
) -> bool:
    """Delete multiple passthrough tunnels from appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyTunnel
          - POST
          - /thirdPartyTunnels/deleteMultiple

    :param tunnel_list: List of tunnel id's to query for
    :type tunnel_list: list[str]
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/thirdPartyTunnels/deleteMultiple",
        data=tunnel_list,
        return_type="bool",
    )
