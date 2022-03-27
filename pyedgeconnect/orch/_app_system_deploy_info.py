# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# appSystemDeployInfo : ECOS deployment


def get_appliance_system_deployment_info(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get appliance system deployment information

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appSystemDeployInfo
          - GET
          - /systemInfo/system/{neId}?cached={cached}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary of appliance deployment info \n
        * keyword **bw** (`dict`): System bandwidth object \n
            * keyword **if_rx_target** (`bool`): Target bandwidth
              enabled
        * keyword **auto_subnet** (`dict`): Auto subnet object \n
            * keyword **self** (`bool`): Flag to enable and disable
              subnet sharing
            * keyword **add_local** (`bool`): Enable automatic
              advertising local subnets. Note: Only applicable for
              appliances whose version is less than 8.1.4.
            * keyword **add_local_lan** (`bool`): Enable automatic
              advertising local subnets for LAN interfaces only. Note:
              Only applicable for appliances whose version is greater
              than or equal to 8.1.4.
            * keyword **add_local_wan** (`bool`): Enable automatic
              advertising local subnets for WAN interfaces only. Note:
              Only applicable for appliances whose version is greater
              than or equal to 8.1.4.
            * keyword **add_local_metric** (`int`): Metric assigned to
              subnets of interfaces on this appliance
            * keyword **redist_bgp** (`bool`): Enable redistribution of
              learned BGP routes via subnet sharing
            * keyword **redist_ospf** (`bool`): Enable redistribution of
              learned OSPF routes via subnet sharing
            * keyword **redist_ospf_filter** (`int`): Filter for OSPF
              routes redistributed to subnet sharing
            * keyword **redist_ospf_metric** (`int`): Add metric to OSPF
              routes to be redistributed to subnet sharing
            * keyword **local_ospf_filter** (`int`): Filter for locally
              learned OSPF routes
        * keyword **nm_fsp_enable** (`bool`): Enable network memory FSP
        * keyword **nat** (`bool`): Enable NAT
        * keyword **auto_syn** (`bool`): Enable auto SYN
        * keyword **bridge_loop_test** (`bool`): Bridge loop test
        * keyword **auto_tunnel** (`bool`): Enable auto tunnel
        * keyword **ipsec_override** (`bool`): SSL IPSec override
        * keyword **auto_ipid** (`bool`): Enable auto IP ID
        * keyword **excess_flow** (`dict`): Excess flow object \n
            * keyword **dscp_marking** (`bool`): Excess flow DSCP
              marking
            * keyword **policy** (`str`): Excess flow policy,
              e.g. ``bypass``
        * keyword **dpc** (`dict`): DPC object \n
            * keyword **tunfail** (`str`): DPC tunnel failover behavior,
              e.g. ``fail-stick``
        * keyword **disk_encrypt_enable** (`bool`): Enable disk
          encryption
        * keyword **igmp_snooping** (`bool`): Bridge multicast IGMP
          snooping
        * keyword **nm_media** (`int`): System network memory media
        * keyword **nm_mode** (`int`): System network memory mode
        * keyword **node_dns** (`dict`): DNS lookup object \n
            * keyword **enable** (`bool`): Enable DNS lookup
            * keyword **ipaddr** (`str`): DNS IP address
        * keyword **smb_signing** (`bool`): SMB signing optimization
        * keyword **udp_inact_time** (`int`): UDP flow timeout in
          seconds range from 1 to 65535
        * keyword **quies_tun_ka_intvl** (`int`): Quiescent-tunnel keep
          alive time range from 1 to 65535
        * keyword **max_tcp_mss** (`int`): Maximum TCP MSS range from
          500 to 9000
        * keyword **int_hairpin** (`bool`): Enable internal hairpinning
        * keyword **auto_pol_lookup_intvl** (`int`): Auto policy lookup
          interval
        * keyword **passthru_to_sender** (`bool`): Disable passthrough
          L2 return to sender
        * keyword **orch_guid** (`str`): Orchestrator GUID
        * keyword **idrc** (`dict`): IDRC object \n
            * keyword **param_delta** (`float`): Parameter delta for
              IDRC
            * keyword **param_g** (`float`): Parameter g for IDRC
            * keyword **param_m** (`float`): Parameter m for IDRC
            * keyword **param_y** (`float`): Parameter y for IDRC
        * keyword **ha_if** (`str`): High availability interface
        * keyword **port_fwd_rules** (`str`): Inbound port forwarding
          rules
        * keyword **udp_ipsec_lcl_ports** (`str`): List of ports used
          locally for UDP IPSec tunnels
        * keyword **udp_ipsec_peer_ports** (`str`): List of ports used
          by peers for UDP IPSec tunnels
        * keyword **network_role** (`int`): Network role,
        * keyword **options** (`int`): Tunnel system level options for
          future
        * keyword **serverMode** (`dict`): Server mode object \n
            * keyword **target_in_thres** (`float`): Interface max link
              threshold
            * keyword **target_out_thres** (`float`): Interface max link
              threshold
            * keyword **in_max_bw** (`int`): Server inbound max
              bandwidth (kbps)
            * keyword **out_max_bw** (`int`): Server outbound max
              bandwidth (kbps)
        * keyword **shaperinbound** (`dict`): Shaper inbound object \n
            * keyword **wan** (`dict`): Shaper interface wan \n
                * keyword **max_bw** (`int`): Shaper max bandwidth
                  (kbps)
                * keyword **dyn_bw_enable** (`bool`): Enable/disable
                  dynamic bandwidth for inbound shaper
                * keyword **self** (`str`): Shaper interface name. It is
                  the same as the parent node key ``wan``
                * keyword **accuracy** (`int`): Shaper accuracy (usec)
                * keyword **enable** (`bool`): Enable/disable inbound
                  shaper
                * keyword **traffic-class** (`dict`): Traffic class \n
                    * keyword **<traffic_class_id>** (`dict`):
                      Traffic class ID, e.g. ``1`` object with nested
                      attributes \n
                        * keyword **max_bw** (`float`): Traffic class
                          max bandwidth %
                        * keyword **min_bw** (`float`): Traffic class
                          min bandwidth %
                        * keyword **max_bw_abs** (`int`): Traffic class
                          max bandwidth (kbps)
                        * keyword **min_bw_abs** (`int`): Traffic class
                          min bandwidth (kbps)
                        * keyword **flow_limit** (`int`): Traffic class
                          flow rate limit
                        * keyword **self** (`int`): Traffic class ID. It
                          is the same as the parent node key
                          ``trafficClassId``
                        * keyword **excess** (`int`): Traffic class
                          excess weight
                        * keyword **priority** (`int`): Traffic class
                          priority
                        * keyword **max_wait** (`int`): Traffic class
                          max wait
    :rtype: dict
    """
    return self._get("/systemInfo/system/{}?cached={}".format(ne_id, cached))


def get_discovered_appliance_system_deployment_info(
    self,
    discovered_id: int,
) -> dict:
    """Get discovered appliance system deployment information

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appSystemDeployInfo
          - GET
          - /systemInfo/systemForDiscovered/{discoveredId}

    :param discovered_id: Discovered appliance id
    :type discovered_id: int
    :return: Returns dictionary of appliance deployment info \n
        * keyword **bw** (`dict`): System bandwidth object \n
            * keyword **if_rx_target** (`bool`): Target bandwidth
              enabled
        * keyword **auto_subnet** (`dict`): Auto subnet object \n
            * keyword **self** (`bool`): Flag to enable and disable
              subnet sharing
            * keyword **add_local** (`bool`): Enable automatic
              advertising local subnets. Note: Only applicable for
              appliances whose version is less than 8.1.4.
            * keyword **add_local_lan** (`bool`): Enable automatic
              advertising local subnets for LAN interfaces only. Note:
              Only applicable for appliances whose version is greater
              than or equal to 8.1.4.
            * keyword **add_local_wan** (`bool`): Enable automatic
              advertising local subnets for WAN interfaces only. Note:
              Only applicable for appliances whose version is greater
              than or equal to 8.1.4.
            * keyword **add_local_metric** (`int`): Metric assigned to
              subnets of interfaces on this appliance
            * keyword **redist_bgp** (`bool`): Enable redistribution of
              learned BGP routes via subnet sharing
            * keyword **redist_ospf** (`bool`): Enable redistribution of
              learned OSPF routes via subnet sharing
            * keyword **redist_ospf_filter** (`int`): Filter for OSPF
              routes redistributed to subnet sharing
            * keyword **redist_ospf_metric** (`int`): Add metric to OSPF
              routes to be redistributed to subnet sharing
            * keyword **local_ospf_filter** (`int`): Filter for locally
              learned OSPF routes
        * keyword **nm_fsp_enable** (`bool`): Enable network memory FSP
        * keyword **nat** (`bool`): Enable NAT
        * keyword **auto_syn** (`bool`): Enable auto SYN
        * keyword **bridge_loop_test** (`bool`): Bridge loop test
        * keyword **auto_tunnel** (`bool`): Enable auto tunnel
        * keyword **ipsec_override** (`bool`): SSL IPSec override
        * keyword **auto_ipid** (`bool`): Enable auto IP ID
        * keyword **excess_flow** (`dict`): Excess flow object \n
            * keyword **dscp_marking** (`bool`): Excess flow DSCP
              marking
            * keyword **policy** (`str`): Excess flow policy,
              e.g. ``bypass``
        * keyword **dpc** (`dict`): DPC object \n
            * keyword **tunfail** (`str`): DPC tunnel failover behavior,
              e.g. ``fail-stick``
        * keyword **disk_encrypt_enable** (`bool`): Enable disk
          encryption
        * keyword **igmp_snooping** (`bool`): Bridge multicast IGMP
          snooping
        * keyword **nm_media** (`int`): System network memory media
        * keyword **nm_mode** (`int`): System network memory mode
        * keyword **node_dns** (`dict`): DNS lookup object \n
            * keyword **enable** (`bool`): Enable DNS lookup
            * keyword **ipaddr** (`str`): DNS IP address
        * keyword **smb_signing** (`bool`): SMB signing optimization
        * keyword **udp_inact_time** (`int`): UDP flow timeout in
          seconds range from 1 to 65535
        * keyword **quies_tun_ka_intvl** (`int`): Quiescent-tunnel keep
          alive time range from 1 to 65535
        * keyword **max_tcp_mss** (`int`): Maximum TCP MSS range from
          500 to 9000
        * keyword **int_hairpin** (`bool`): Enable internal hairpinning
        * keyword **auto_pol_lookup_intvl** (`int`): Auto policy lookup
          interval
        * keyword **passthru_to_sender** (`bool`): Disable passthrough
          L2 return to sender
        * keyword **orch_guid** (`str`): Orchestrator GUID
        * keyword **idrc** (`dict`): IDRC object \n
            * keyword **param_delta** (`float`): Parameter delta for
              IDRC
            * keyword **param_g** (`float`): Parameter g for IDRC
            * keyword **param_m** (`float`): Parameter m for IDRC
            * keyword **param_y** (`float`): Parameter y for IDRC
        * keyword **ha_if** (`str`): High availability interface,
        * keyword **port_fwd_rules** (`str`): Inbound port forwarding
          rules
        * keyword **udp_ipsec_lcl_ports** (`str`): List of ports used
          locally for UDP IPSec tunnels
        * keyword **udp_ipsec_peer_ports** (`str`): List of ports used
          by peers for UDP IPSec tunnels
        * keyword **network_role** (`int`): Network role,
        * keyword **options** (`int`): Tunnel system level options for
          future
        * keyword **serverMode** (`dict`): Server mode object \n
            * keyword **target_in_thres** (`float`): Interface max link
              threshold
            * keyword **target_out_thres** (`float`): Interface max link
              threshold
            * keyword **in_max_bw** (`int`): Server inbound max
              bandwidth (kbps)
            * keyword **out_max_bw** (`int`): Server outbound max
              bandwidth (kbps)
        * keyword **shaperinbound** (`dict`): Shaper inbound object \n
            * keyword **wan** (`dict`): Shaper interface wan \n
                * keyword **max_bw** (`int`): Shaper max bandwidth
                  (kbps)
                * keyword **dyn_bw_enable** (`bool`): Enable/disable
                  dynamic bandwidth for inbound shaper
                * keyword **self** (`str`): Shaper interface name. It is
                  the same as the parent node key ``wan``
                * keyword **accuracy** (`int`): Shaper accuracy (usec)
                * keyword **enable** (`bool`): Enable/disable inbound
                  shaper
                * keyword **traffic-class** (`dict`): Traffic class \n
                    * keyword **<traffic_class_id>** (`dict`):
                      Traffic class ID, e.g. ``1`` object with nested
                      attributes \n
                        * keyword **max_bw** (`float`): Traffic class
                          max bandwidth %
                        * keyword **min_bw** (`float`): Traffic class
                          min bandwidth %
                        * keyword **max_bw_abs** (`int`): Traffic class
                          max bandwidth (kbps)
                        * keyword **min_bw_abs** (`int`): Traffic class
                          min bandwidth (kbps)
                        * keyword **flow_limit** (`int`): Traffic class
                          flow rate limit
                        * keyword **self** (`int`): Traffic class ID. It
                          is the same as the parent node key
                          ``trafficClassId``
                        * keyword **excess** (`int`): Traffic class
                          excess weight
                        * keyword **priority** (`int`): Traffic class
                          priority
                        * keyword **max_wait** (`int`): Traffic class
                          max wait
    :rtype: dict
    """
    return self._get(
        "/systemInfo/systemForDiscovered/{}".format(discovered_id)
    )
