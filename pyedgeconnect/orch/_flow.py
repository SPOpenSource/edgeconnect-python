# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# flow : ECOS current flows


def get_appliance_flows(  # noqa: C901, silences flake8 complexity
    self,
    ne_id: str,
    ip1: str = None,
    mask1: str = None,
    port1: int = None,
    ip2: str = None,
    mask2: str = None,
    port2: int = None,
    ip_either_flag: bool = True,
    port_either_flag: bool = True,
    vrf1: str = None,
    vrf2: str = None,
    vrf_either: str = None,
    application: str = None,
    application_group: str = None,
    protocol: str = None,
    vlan: int = None,
    dscp: str = None,
    overlays: str = None,
    transport: str = None,
    services: str = None,
    zone1: str = None,
    zone2: str = None,
    zone_either: str = None,
    flow_category: str = "all",
    edge_ha: bool = False,
    built_in: bool = False,
    uptime: str = None,
    bytes_transferred: str = "total",
    duration: str = None,
    anytime_slow_flows: str = None,
) -> dict:
    """Get active, inactive, or both types of flows from an appliance
    based on supplied query parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - flow
          - GET
          - /flow/{neId}/q

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param ip1: First IP endpoint, defaults to None
    :type ip1: str, optional
    :param mask1: Mask for ip1 ip address, defaults to None
    :type mask1: str, optional
    :param port1: Port for ip1, defaults to None
    :type port1: int, optional
    :param ip2: Second IP endpoint, defaults to None
    :type ip2: str, optional
    :param mask2: Mask for ip2 ip address, defaults to None
    :type mask2: str, optional
    :param port2: Port for ip2, defaults to None
    :type port2: int, optional
    :param ip_either_flag: Enable directionality for IP parameters.
        ``True`` will treat ip1 as source ip and ip2 as destination ip,
        defaults to True.
    :type ip_either_flag: bool, optional
    :param port_either_flag: Enable directionality for port parameters.
        ``True`` will treat port1 as source port and port2 as
        destination port, defaults to True.
    :type port_either_flag: bool, optional
    :param vrf1: VRF ID for ip1, ``0`` is the default VRF ID,
        defaults to None
    :type vrf1: str, optional
    :param vrf2: VRF ID for ip2, ``0`` is the default VRF ID,
        defaults to None
    :type vrf2: str, optional
    :param vrf_either: VRF ID for flows sourced from or destinted to.
        Accepted values are ``any``, ``0`` for default VRF, or a
        specific VRF ID, defaults to None
    :type vrf_either: str, optional
    :param application: Filter for application-specific flows. Allows
        both built-in and user-defined applications as values,
        defaults to None
    :type application: str, optional
    :param application_group: Filter for application-group flows,
        defaults to None
    :type application_group: str, optional
    :param protocl: Filter by protocol, e.g. ``ip``, ``icmp``, ``bgp``,
        etc., defaults to None
    :type protocol: str, optional
    :param vlan: Filter for VLAN ID, defaults to None
    :type vlan: int, optional
    :param dscp: Filter for DSCP marking, defaults to None
    :type dscp: str, optional
    :param overlays: Filter for Overlay ID, multiple values can be
        passed separated by | e.g. ``1|2``, defaults to None
    :type overlays: str, optional
    :param transport: Transport type, accepted values include
        ``fabric``, ``underlay``, ``breakout``. Multiple values can be
        used together separated by | e.g. ``fabric|underlay``,
        defaults to None
    :type transport: str, optional
    :param services: Service name, third-party services should be
        formatted with an asterisk at the end to filter by prefix
        instead of complete match, multiple services separated by |
        e.g. ``Zscaler_*|PaloAlto``, defaults to None
    :type services: str, optional
    :param zone1: Flows to zone1, accepted values include ``any``, ``0``
        for default zone, or specific zone id, defaults to None
    :type zone1: str, optional
    :param zone2: Flows from zone2, accepted values include ``any``,
        ``0`` for default zone, or specific zone id, defaults to None
    :type zone2: str, optional
    :param zone_either: Flows to or from specified zone, accepted values
        include ``any``, ``0`` for default zone, or specific zone id,
        defaults to None
    :type zone_either: str, optional
    :param flow_category: Filter flow category, accepted values are
        ``all``, ``asymmetric``, ``stale``, ``passThrough``,
        ``boosted``, ``routeDropped``, ``firewallDropped``,
        ``directlyAttached``, defaults to None
    :type flow_category: str, optional
    :param edge_ha: ``True`` to include EdgeHA flows, False to exclude,
        defaults to False
    :type edge_ha: bool, optional
    :param built_in: ``True`` to include built-in policy flows, False to
        exclude, defaults to False
    :type built_in: bool, optional
    :param uptime: Filter for uptime of flow. Term for ended within.
        Accepted values include ``anytime``, ``last5m``, ``term5m``,
        ``term``, ``last1hr``, ``term1hr``, ``last4hr``, ``term4h``,
        ``last24hr``, ``term24hr``, defaults to None
    :type uptime: str, optional
    :param bytes_transferred: Bytes transfered, accepted values are
        ``total`` and ``last5m``, defaults to "total"
    :type bytes_transferred: str, optional
    :param duration: Flows that have lasted less than ("<") or greater
        than (">") the specified duration (in minutes). Value should be
        ``any`` or a number formatted with a "<" or ">" in front of a
        value between ``0`` and ``18446744073709551615``.
        e.g. ``>5000``, defaults to None
    :type duration: str, optional
    :param anytime_slow_flows: Slow Flows flag. If this flag is present,
        it will show slow flows only, defaults to None
    :type anytime_slow_flows: str, optional
    :return: Returns dictionary of flows based on supplied query
        details \n
        * keyword **total_flows** (`int`): Total number of flows
        * keyword **matched_flows** (`int`): Total number of matched
          flows
        * keyword **now** (`int`): current epoch time in seconds
        * keyword **returned_flows** (`int`): Number of returned flows
        * keyword **stale_flows** (`int`): Number of stale flows
        * keyword **inconsistent_flows** (`int`): Number of inconsistent
          flows
        * keyword **flows_with_issues** (`int`): Number of flows with
          issues
        * keyword **flows_optimized** (`int`): Number of optimized flows
        * keyword **flows_with_ignores** (`int`): No description in
          Swagger
        * keyword **flows_passthrough** (`int`): Number of passthrough
          flows
        * keyword **flows_management** (`int`): Number of management
          flows
        * keyword **active** (`dict`): Active flows object \n
            * keyword **total_flows** (`int`): Number of active flows
            * keyword **stale_flows** (`int`): Number of active stale
              flows
            * keyword **inconsistent_flows** (`int`): Number of active
              inconsistent flows
            * keyword **flows_with_issues** (`int`): Number of active
              flows with issues
            * keyword **flows_optimized** (`int`): Number of active
              optimized flows
            * keyword **flows_with_ignores** (`int`): No description in
              Swagger
            * keyword **flows_passthrough** (`int`): Number of active
              passthrough flows
            * keyword **flows_management** (`int`): Number of active
              management flows
            * keyword **flows_asymmetric** (`int`): Number of active
              asymmetric flows
            * keyword **flows_route_dropped** (`int`): Number of active
              flows dropped due to route
            * keyword **flows_firewall_dropped** (`int`): Number of
              active flows dropped due to firewall
        * keyword **inactive** (`dict`): Inactive flows object \n
            * keyword **total_flows** (`int`): Number of inactive flows
            * keyword **stale_flows** (`int`): Number of inactive stale
              flows
            * keyword **inconsistent_flows** (`int`): Number of inactive
              inconsistent flows
            * keyword **flows_with_issues** (`int`): Number of inactive
              flows with issues
            * keyword **flows_optimized** (`int`): Number of inactive
              optimized flows
            * keyword **flows_with_ignores** (`int`): No description in
              Swagger
            * keyword **flows_passthrough** (`int`): Number of inactive
              passthrough flows
            * keyword **flows_management** (`int`): Number of inactive
              management flows
            * keyword **flows_asymmetric** (`int`): Number of inactive
              asymmetric flows
            * keyword **flows_route_dropped** (`int`): Number of
              inactive flows dropped due to route
            * keyword **flows_firewall_dropped** (`int`): Number of
              inactive flows dropped due to firewall
        * keyword **ret_code** (`int`): No description in Swagger
        * keyword **err_msg** (`str`): Error message
        * keyword **flows** (`list[list]`): List of flow details \n
            * [0] (`int`): Flow Id
            * [1] (`int`): Flow Sequence Id
            * [2] (`int`): SilverPeak Flow Id
            * [3] (`str`): Application Name, e.g. ``https``
            * [4] (`int`): IP1_1, IPv6 128-bit source IP address spread
              over four fields (IP1_1-4). If IPv4, 32-bit integer format
              and other fields are ``0``.
            * [5] (`int`): IP1_2, in 32-bit integer format
            * [6] (`int`): IP1_3, in 32-bit integer format
            * [7] (`int`): IP1_4, in 32-bit integer format
            * [8] (`int`): Ip1 Version e.g. ``4`` or ``6``
            * [9] (`str`): IP1 String
            * [10] (`int`): Port1, port number of source address
            * [11] (`int`): IP2_1, IPv6 128-bit destination IP address
              spread over four fields (IP2_1-4). If IPv4, 32-bit integer
              format and other fields are ``0``.
            * [12] (`int`): IP2_2, in 32-bit integer format
            * [13] (`int`): IP2_3, in 32-bit integer format
            * [14] (`int`): IP2_4, in 32-bit integer format
            * [15] (`int`): Ip2 Version e.g. ``4`` or ``6``
            * [16] (`str`): IP2 String
            * [17] (`int`): Port2, port number of destination address
            * [18] (`int`): Flow Optimization Status
            * [19] (`int`): Percentage Reduction Inbound
            * [20] (`int`): Inbound TX Bytes
            * [21] (`int`): Inbound RX Bytes
            * [22] (`int`): Outbound RX Bytes
            * [23] (`int`): Outbound TX Bytes
            * [24] (`int`): Percentage Reduction OutBound
            * [25] (`int`): Uptime in ms
            * [26] (`str`): Protocol, e.g. ``tcp``
            * [27] (`str`): Outbound Tunnel Id
            * [28] (`str`): Inbound Tunnel Id
            * [29] (`str`): Configured Outbound Tunnel Id
            * [30] (`int`): LAN Side VLAN associated with flow
            * [31] (`int`): QoS Traffic Class (1-10)
            * [32] (`str`): LAN DSCP treatment behavior,
              e.g. ``trust-lan``
            * [33] (`str`): WAN DSCP treatment behavior,
              e.g. ``trust-lan``
            * [34] (`int`): IP address of Peer flow redirected from
            * [35] (`str`): ISCI vendor Flow Info
            * [36] (`int`): NAT address of IP1 (source)
            * [37] (`int`): NAT address of IP1 (destination)
            * [38] (`int`): Flow Start Time, unix epoch seconds
            * [39] (`int`): Flow End Time, unix epoch seconds
            * [40] (`int`): Service Id, identifying owner and location
            * [41] (`int`): SaaS Id
            * [42] (`int`): TCP UTC Slow Start Time, unix epoch seconds
            * [43] (`int`): TCP Slow Duration
            * [44] (`str`): IP1 Domain Name
            * [45] (`str`): IP2 Domain Name
            * [46] (`int`): From Zone, integer zone id
            * [47] (`int`): To Zone, integer zone id
            * [48] (`int`): If flow was dropped by security policy (ZBF)
              e.g. ``0`` if not dropped.
            * [49] (`str`): EdgeHA, ``"true"`` or ``"false"`` if belongs
              to HA interface subnet
            * [50] (`str`): LAN TX DSCP
            * [51] (`str`): LAN RX DSCP
            * [52] (`str`): WAN TX DSCP
            * [53] (`str`): WAN RX DSCP
            * [54] (`str`): NAT IP (if NAT applied)
            * [55] (`str`): NAT Port
            * [56] (`str`): Original Port
            * [57] (`str`): NAT Type, e.g. ``LAN_SNAT``, ``LAN_DNAT``,
              ``WAN_SNAT`` or ``WAN_DNAT``
            * [58] (`str`): Application Type, e.g. ``Idle``, ``Voice``,
              ``Video_Conferencing``, ``Video_Streaming``,
              ``Bulk_Data_transfer``, or ``Interactive``
            * [59] (`int`): Drop reason, ``0`` for not dropped, ``1``
              indicates dropped by ZBF, ``2`` dropped due to routing
              decision
            * [60] (`str`): Business Intent Overlay,
              e.g. ``DefaultOverlay``
            * [61] (`int`): Source VRF ID
            * [62] (`int`): Destination VRF ID
    :rtype: dict
    """
    path = "/flow/{}/q?".format(ne_id)

    if ip1 is not None:
        path = path + "&ip1={}".format(ip1)
    if mask1 is not None:
        path = path + "&mask1={}".format(mask1)
    if port1 is not None:
        path = path + "&port1={}".format(port1)
    if ip2 is not None:
        path = path + "&ip2={}".format(ip2)
    if mask2 is not None:
        path = path + "&mask2={}".format(mask2)
    if port2 is not None:
        path = path + "&port2={}".format(port2)

    path = path + "&ipEitherFlag={}".format(ip_either_flag)
    path = path + "&portEitherFlag={}".format(port_either_flag)

    if vrf1 is not None:
        path = path + "&vrf1={}".format(vrf1)
    if vrf2 is not None:
        path = path + "&vrf2={}".format(vrf2)
    if vrf_either is not None:
        path = path + "&vrfEither={}".format(vrf_either)
    if application is not None:
        path = path + "&application={}".format(application)
    if application_group is not None:
        path = path + "&applicationGroup={}".format(application_group)
    if protocol is not None:
        path = path + "&protocol={}".format(protocol)
    if vlan is not None:
        path = path + "&vlan={}".format(vlan)
    if dscp is not None:
        path = path + "&dscp={}".format(dscp)
    if overlays is not None:
        path = path + "&overlays={}".format(overlays)
    if transport is not None:
        path = path + "&transport={}".format(transport)
    if services is not None:
        path = path + "&services={}".format(services)
    if zone1 is not None:
        path = path + "&zone1={}".format(zone1)
    if zone2 is not None:
        path = path + "&zone2={}".format(zone2)
    if zone_either is not None:
        path = path + "&zoneEither={}".format(zone_either)

    path = path + "&filter={}".format(flow_category)
    path = path + "&edgeHa={}".format(edge_ha)
    path = path + "&builtIn={}".format(built_in)

    if uptime is not None:
        path = path + "&uptime={}".format(uptime)

    path = path + "&bytes={}".format(bytes_transferred)
    path = path + "&duration={}".format(duration)

    if duration is not None:
        path = path + "&duration={}".format(duration)
    if anytime_slow_flows is not None:
        path = path + "&anytimeSlowFlows={}".format(anytime_slow_flows)

    return self._get(path)


def reset_flows(
    self,
    ne_id: str,
    flow_id_list: list,
) -> dict:
    """Reset specified flows on an appliance.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - flow
          - POST
          - /flow/flowReset/{neId}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param flow_id_list: List of flow id's to be reset on appliance,
        e.g. ``[0,1,2]``
    :type flow_id_list: list
    :return: If specified flows were present, returns results, otherwise
        will respond with a 204, empty content
    :rtype: dict
    """
    data = {"spIds": flow_id_list}

    return self._post(
        "/flow/flowReset/{}".format(ne_id),
        data=data,
        expected_status=[200, 204],
    )


def reclassify_flows(
    self,
    ne_id: str,
    flow_id_list: list = [],
) -> dict:
    """Reclassify specified flows on an appliance.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - flow
          - POST
          - /flow/flowReClassification/{neId}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param flow_id_list: List of flow id's to be reset on appliance,
        e.g. ``[0,1,2]``, defaults to empty list to reclassify all flows
    :type flow_id_list: list
    :return: Responds with dictionary with action success message \n
        * keyword **results** (`list`): No description in Swagger
        * keyword **rc** (`int`): ``0`` indicates success, ``-1``
          indicates failure
        * keyword **value** (`str`): Action message,
          e.g. ``Action set successful.``
    :rtype: dict
    """
    data = {"spIds": flow_id_list}

    return self._post("/flow/flowReClassification/{}".format(ne_id), data=data)


def get_appliance_flow_bandwidth_stats(
    self,
    ne_id: str,
    flow_id: int,
    flow_seq_num: int,
) -> list:
    """Get the so far accumulated bandwidth stats about the flow

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - flow
          - GET
          - /flow/flowBandwidthStats/{neId}/q

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param flow_id: Flow ID
    :type flow_id: int
    :param flow_seq_num: Flow sequence number
    :type flow_seq_num: int
    :return: Returns list of dictionaries for so far accumulated
        bandwidth stats about the flow
    :rtype: list[dict]
    """
    return self._get(
        "/flow/flowBandwidthStats/{}/q?id={}&seq={}".format(
            ne_id, flow_id, flow_seq_num
        )
    )


def get_appliance_flow_details(
    self,
    ne_id: str,
    flow_id: int,
    flow_seq_num: int,
) -> list:
    """Get specific flow details from appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - flow
          - GET
          - /flow/flowDetails/{neId}/q

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param flow_id: Flow ID
    :type flow_id: int
    :param flow_seq_num: Flow sequence number
    :type flow_seq_num: int
    :return: Returns nested dictionary/lists of flow details \n
        [`dict`]: Response object \n
            * keyword **Route** (`list[dict]`): No description in
              Swagger
            * keyword **Optimization** (`list[dict]`): No description in
              Swagger
            * keyword **Stats** (`list[dict]`): No description in
              Swagger
            * keyword **QoS** (`list[dict]`): No description in Swagger
            * keyword **Application Performance** (`list[dict]`): No
              description in Swagger
    :rtype: list
    """
    return self._get(
        "/flow/flowDetails/{}/q?id={}&seq={}".format(
            ne_id, flow_id, flow_seq_num
        )
    )


def get_appliance_flow_details_verbose(
    self,
    ne_id: str,
    flow_id: int,
    flow_seq_num: int,
) -> list:
    """Get verbose specific flow details from appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - flow
          - GET
          - /flow/flowDetails2/{neId}/q

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param flow_id: Flow ID
    :type flow_id: int
    :param flow_seq_num: Flow sequence number
    :type flow_seq_num: int
    :return: Returns list of dictionaries flow details \n
        [`dict`]: Response object \n
            * keyword **General** (`dict`): General stats object \n
                * keyword **Stats** (`list[dict]`): No description in
                  Swagger
                * keyword **Route** (`list[dict]`): No description in
                  Swagger
                * keyword **Optimization** (`list[dict]`): No
                  description in Swagger
                * keyword **QoS** (`list[dict]`): No description in
                  Swagger
            * keyword **TCP Info** (`dict`): TCP info object \n
                * keyword **TCP-Sats** (`list[dict]`):  No description
                  in Swagger
            * keyword **Nat Info** (`dict`): NAT info object \n
                * keyword **NAT** (`list[dict]`): No description in
                  Swagger

    :rtype: list
    """
    return self._get(
        "/flow/flowDetails2/{}/q?id={}&seq={}".format(
            ne_id, flow_id, flow_seq_num
        )
    )
