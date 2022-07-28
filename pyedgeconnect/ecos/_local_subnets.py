# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# localSubnets : Local subnets
from __future__ import annotations


def get_appliance_subnets(self) -> dict:
    """Gets all configured, learned subnets from remote Silverpeak
    appliances and automatically learned local subnets.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - localSubnets
          - GET
          - /subnets3/all

    :return: Dictionary of appliance configured and learned subnets \n
        * keyword **subnets** (`dict`): Subnet object \n
            * keyword **count** (`int`): Count of all subnets
            * keyword **max** (`int`): Max subnets IPv4 & IPv6, 60000
            * keyword **entries** (`list[dict]`): List of subnet detail
              objects \n
                * keyword **state** (`dict`): Subnet detail object \n
                    * keyword **version** (`int`): IP Version, e.g.
                      ``4`` or ``6``
                    * keyword **prefix** (`str`): Route prefix, e.g.
                      ``10.98.98.3/32``
                    * keyword **nextHop** (`str`): Next hop for prefix
                    * keyword **metric** (`int`): Metric of route, e.g.
                      ``50``
                    * keyword **ifName** (`str`): Interface name, e.g.
                      ``lo20000``
                    * keyword **peerid** (`int`): Peer id, e.g.
                      ``1894366``
                    * keyword **saas** (`int`): SaaS value, e.g. ``0``
                    * keyword **community** (`str`): Community string
                    * keyword **aspath** (`str`): AS Path, e.g.
                      ``64512,64710``
                    * keyword **learned** (`bool`): Learned from peer
                    * keyword **configured** (`bool`): Locally
                      configured
                    * keyword **advert** (`bool`): Advertise to peers
                    * keyword **automatic** (`bool`): Automatically
                      added by system
                    * keyword **local** (`bool`): Local route
                    * keyword **learnedFromIp** (`str`): IP peer route
                      learned from
                    * keyword **cloudApp** (`bool`): Cloud app
                    * keyword **advert_bgp** (`bool`): Advertise to BGP
                    * keyword **advert_ospf** (`bool`): Advertise to
                      OSPF
                    * keyword **learned_bgp** (`bool`): Learned from BGP
                    * keyword **learned_ospf** (`bool`): Learned from
                      OSPF
                    * keyword **state** (`str`): State of route, e.g.
                      ``UP`` or ``DOWN``
                    * keyword **routeTag** (`str`): Tag on route, e.g.
                      ``0``
                    * keyword **learnFrom** (`str`): How route was
                      learned, e.g. ``LRN_SPS_HUB`` for learned by an
                      EdgeConnect Hub or ``LRN_SPS_SPOKE`` for learned
                      by an EdgeConnect Spoke
                    * keyword **resolvedNexthop** (`str`): Resolved next
                      hop
                    * keyword **resolvedInterface** (`str`): Resolved
                      interface for route
                    * keyword **peerType** (`str`): Routing peer type,
                      e.g. ``PE`` for PE Router BGP peering
                    * keyword **nexthopTunnel** (`str`): Next hop tunnel
                    * keyword **networkRegionId** (`str`): Region ID and
                      name of route, e.g. ``1,East``
                    * keyword **subnetMessage** (`str`): Subnet message
                    * keyword **zone_id** (`str`): Firewall zone id for
                      route, e.g. ``0`` for Default
                    * keyword **advOSPFTag** (`str`): Advertise OSPF tag
                    * keyword **routeType** (`str`): Type of route e.g.
                      ``EBGP``
                    * keyword **saasAppName** (`str`): SaaS Application
                      Name
                    * keyword **adminDistance** (`int`): Admin distance
                      of route, e.g. ``1`` for local static
            * keyword **disabledByIPSLA** (`bool`): If routes are
              disabled by an IPSLA in a down state
            * keyword **metricAddedByIPSLA** (`int`): Metric added to
              routes due to an IPSLA being in a down state
            * keyword **peers** (`list[dict]`): List of SDWAN peer
              objects \n
                * keyword **index** (`str`): Peer index, e.g. ``0``
                * keyword **peerid** (`int`): Peer id value
                * keyword **peerName** (`str`): Hostname of peer
                * keyword **role** (`str`): Peer role, e.g. ``0`` for
                  ``Spoke``
                * keyword **roleName** (`str`): Friendly name of peer
                  role tyle, e.g. ``Spoke``
                * keyword **metric** (`int`): Route metric
                * keyword **peerPriority** (`int`): Peer priority value
                * keyword **txtrans** (`int`): Last transmitted
                  transaction count
                * keyword **txsecs** (`int`): Time elapsed since last
                  transmitted update
                * keyword **rxtrans** (`int`): Last received transaction
                  count
                * keyword **rxsecs** (`int`): Time elapsed since last
                  received update
                * keyword **rxrecs** (`int`): NEEDS DESCRIPTION
                * keyword **rxtabs** (`int`): NEEDS DESCRIPTION
                * keyword **outOfOrderCount** (`int`): Out of order
                  packets count, e.g. ``0``
                * keyword **majorVersion** (`str`): Major software
                  version, e.g. ``9`` in ``9.1.0.3``
                * keyword **minorVersion** (`str`): Minor software
                  version, e.g. ``1`` in ``9.1.0.3``
                * keyword **pointVersion** (`str`): Point software
                  version, e.g. ``0`` in ``9.1.0.3``
                * keyword **subVersion** (`str`): Sub software version
                  e.g. ``3`` in ``9.1.0.3``
                * keyword **region** (`str`): Appliance region id,
                  e.g. ``1``
                * keyword **regionName** (`str`): Appliance region name,
                  e.g. ``East``
                * keyword **messageVersion** (`str`): Subnet message
                  version, e.g. ``6``
                * keyword **message** (`str`): Specifies Information
                  about the supported subnet message version, e.g.
                  ``Submsg Ver6 (>= Rel9.0 or main)``
                * keyword **priorTxSec** (`str`): Prior Transmit second,
                  e.g. ``1418``
                * keyword **mainVerAndRegion** (`str`): Full software
                  version and region ID, e.g. ``9.1.0.3 (1)``
                * keyword **peername** (`str`): Hostname of peer
                * keyword **prio** (`int`): Peer priority value, e.g.
                  ``1024``
            * keyword **moduleInfo** (`dict`): local node details
              object \n
                * keyword **my system id** (`str`): String system ID,
                  e.g. ``1894366``
                * keyword **network region** (`str`): Local appliance
                  region name and ID, e.g. ``East (1)``
                * keyword **network role** (`str`): Local appliance role
                  , e.g. ``NRHub``
                * keyword **allow management to leak** (`str`): Allow
                  management routes to leak, boolean string e.g.
                  ``true``
                * keyword **last peer index** (`str`): Last peer index
                  number, e.g. ``0``
                * keyword **local change** (`str`): Local change id,
                  e.g. ``0x0000``
                * keyword **last time** (`str`): MS time since boot,
                  e.g. ``1961072580 ms after boot``
                * keyword **last change** (`str`): MS time since last
                  change, e.g. ``1960554071 ms after boot``
                * keyword **time since change** (`str`): Time since last
                  change, e.g.  ``518 seconds``
                * keyword **last tx trans** (`str`): Last Transmit
                  message, e.g. ``2212``
                * keyword **last tx rec count** (`str`): Last Transmit
                  message received count, e.g. ``0``
                * keyword **last tx msg count** (`str`): Last Transmit
                  message count, e.g. ``0``
                * keyword **rx invalid msg** (`str`): Receive invalid
                  message count, e.g. ``0``
                * keyword **rx unknown msg** (`str`): Receive unknown
                  message count, e.g. ``0``
                * keyword **IP tracking** (`str`): If IP Tracking is
                  enabled, e.g. ``ENABLED``
                * keyword **IP track delta** (`str`): IP Tracking delta,
                  e.g. ``0``
                * keyword **Active READER index** (`str`): Active reader
                  index, e.g.  ``0``
    :rtype: dict
    """
    return self._get("/subnets3/all")


def get_appliance_subnets_all_vrfs(self) -> dict:
    """Gets all segments configured, learned subnets from remote
    Silverpeak appliances and automatically learned local subnets

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - localSubnets
          - GET
          - /subnets3/all/vrfs

    :return: Dictionary of appliance configured and learned subnets \n
        * keyword **subnets** (`dict`): Subnet object \n
            * keyword **<vrf_id>** (`dict`): Subnets in Segment/VRF \n
                * keyword **count** (`int`): Count of all subnets
                * keyword **max** (`int`): Max subnets IPv4 & IPv6,
                  60000
                * keyword **entries** (`list[dict]`): List of subnet
                  detail objects \n
                    * keyword **state** (`dict`): Subnet detail object\n
                        * keyword **version** (`int`): IP Version, e.g.
                          ``4`` or ``6``
                        * keyword **prefix** (`str`): Route prefix, e.g.
                          ``10.98.98.3/32``
                        * keyword **nextHop** (`str`): Next hop for
                          prefix
                        * keyword **metric** (`int`): Metric of route,
                          e.g. ``50``
                        * keyword **ifName** (`str`): Interface name,
                          e.g. ``lo20000``
                        * keyword **peerid** (`int`): Peer id, e.g.
                          ``1894366``
                        * keyword **saas** (`int`): SaaS value, e.g.
                          ``0``
                        * keyword **community** (`str`): Community
                          string
                        * keyword **aspath** (`str`): AS Path, e.g.
                          ``64512,64710``
                        * keyword **learned** (`bool`): Learned from
                          peer
                        * keyword **configured** (`bool`): Locally
                          configured
                        * keyword **advert** (`bool`): Advertise to
                          peers
                        * keyword **automatic** (`bool`): Automatically
                          added by system
                        * keyword **local** (`bool`): Local route
                        * keyword **learnedFromIp** (`str`): IP peer
                          route learned from
                        * keyword **cloudApp** (`bool`): Cloud app
                        * keyword **advert_bgp** (`bool`): Advertise to
                          BGP
                        * keyword **advert_ospf** (`bool`): Advertise to
                          OSPF
                        * keyword **learned_bgp** (`bool`): Learned from
                          BGP
                        * keyword **learned_ospf** (`bool`): Learned
                          from OSPF
                        * keyword **state** (`str`): State of route,
                          e.g. ``UP`` or ``DOWN``
                        * keyword **routeTag** (`str`): Tag on route,
                          e.g. ``0``
                        * keyword **learnFrom** (`str`): How route was
                          learned, e.g. ``LRN_SPS_HUB`` for learned by
                          an EdgeConnect Hub or ``LRN_SPS_SPOKE`` for
                          learned by an EdgeConnect Spoke
                        * keyword **resolvedNexthop** (`str`): Resolved
                          next hop
                        * keyword **resolvedInterface** (`str`):
                          Resolved interface for route
                        * keyword **peerType** (`str`): Routing peer
                          type, e.g. ``PE`` for PE Router BGP peering
                        * keyword **nexthopTunnel** (`str`): Next hop
                          tunnel
                        * keyword **networkRegionId** (`str`): Region ID
                          and name of route, e.g. ``1,East``
                        * keyword **subnetMessage** (`str`): Subnet
                          message
                        * keyword **zone_id** (`str`): Firewall zone id
                          for route, e.g. ``0`` for Default
                        * keyword **advOSPFTag** (`str`): Advertise OSPF
                          tag
                        * keyword **routeType** (`str`): Type of route
                          e.g. ``EBGP``
                        * keyword **saasAppName** (`str`): SaaS
                          Application Name
                        * keyword **adminDistance** (`int`): Admin
                          distance of route, e.g. ``1`` for local static
                * keyword **disabledByIPSLA** (`bool`): If routes are
                  disabled by an IPSLA in a down state
                * keyword **metricAddedByIPSLA** (`int`): Metric added
                  to routes due to an IPSLA being in a down state
            * keyword **peers** (`list[dict]`): List of SDWAN peer
              objects \n
                * keyword **index** (`str`): Peer index, e.g. ``0``
                * keyword **peerid** (`int`): Peer id value
                * keyword **peerName** (`str`): Hostname of peer
                * keyword **role** (`str`): Peer role, e.g. ``0`` for
                  ``Spoke``
                * keyword **roleName** (`str`): Friendly name of peer
                  role tyle, e.g. ``Spoke``
                * keyword **metric** (`int`): Route metric
                * keyword **peerPriority** (`int`): Peer priority value
                * keyword **txtrans** (`int`): Last transmitted
                  transaction count
                * keyword **txsecs** (`int`): Time elapsed since last
                  transmitted update
                * keyword **rxtrans** (`int`): Last received transaction
                  count
                * keyword **rxsecs** (`int`): Time elapsed since last
                  received update
                * keyword **rxrecs** (`int`): NEEDS DESCRIPTION
                * keyword **rxtabs** (`int`): NEEDS DESCRIPTION
                * keyword **outOfOrderCount** (`int`): Out of order
                  packets count, e.g. ``0``
                * keyword **majorVersion** (`str`): Major software
                  version, e.g. ``9`` in ``9.1.0.3``
                * keyword **minorVersion** (`str`): Minor software
                  version, e.g. ``1`` in ``9.1.0.3``
                * keyword **pointVersion** (`str`): Point software
                  version, e.g. ``0`` in ``9.1.0.3``
                * keyword **subVersion** (`str`): Sub software version
                  e.g. ``3`` in ``9.1.0.3``
                * keyword **region** (`str`): Appliance region id,
                  e.g. ``1``
                * keyword **regionName** (`str`): Appliance region name,
                  e.g. ``East``
                * keyword **messageVersion** (`str`): Subnet message
                  version, e.g. ``6``
                * keyword **message** (`str`): Specifies Information
                  about the supported subnet message version, e.g.
                  ``Submsg Ver6 (>= Rel9.0 or main)``
                * keyword **priorTxSec** (`str`): Prior Transmit second,
                  e.g. ``1418``
                * keyword **mainVerAndRegion** (`str`): Full software
                  version and region ID, e.g. ``9.1.0.3 (1)``
                * keyword **peername** (`str`): Hostname of peer
                * keyword **prio** (`int`): Peer priority value, e.g.
                  ``1024``
            * keyword **moduleInfo** (`dict`): local node details
              object \n
                * keyword **my system id** (`str`): String system ID,
                  e.g. ``1894366``
                * keyword **network region** (`str`): Local appliance
                  region name and ID, e.g. ``East (1)``
                * keyword **network role** (`str`): Local appliance role
                  , e.g. ``NRHub``
                * keyword **allow management to leak** (`str`): Allow
                  management routes to leak, boolean string e.g.
                  ``true``
                * keyword **last peer index** (`str`): Last peer index
                  number, e.g. ``0``
                * keyword **local change** (`str`): Local change id,
                  e.g. ``0x0000``
                * keyword **last time** (`str`): MS time since boot,
                  e.g. ``1961072580 ms after boot``
                * keyword **last change** (`str`): MS time since last
                  change, e.g. ``1960554071 ms after boot``
                * keyword **time since change** (`str`): Time since last
                  change, e.g.  ``518 seconds``
                * keyword **last tx trans** (`str`): Last Transmit
                  message, e.g. ``2212``
                * keyword **last tx rec count** (`str`): Last Transmit
                  message received count, e.g. ``0``
                * keyword **last tx msg count** (`str`): Last Transmit
                  message count, e.g. ``0``
                * keyword **rx invalid msg** (`str`): Receive invalid
                  message count, e.g. ``0``
                * keyword **rx unknown msg** (`str`): Receive unknown
                  message count, e.g. ``0``
                * keyword **IP tracking** (`str`): If IP Tracking is
                  enabled, e.g. ``ENABLED``
                * keyword **IP track delta** (`str`): IP Tracking delta,
                  e.g. ``0``
                * keyword **Active READER index** (`str`): Active reader
                  index, e.g.  ``0``
    :rtype: dict
    """
    return self._get("/subnets3/all/vrfs")


def get_appliance_subnets_single_vrf(
    self,
    vrf_id: int,
) -> dict:
    """Gets specified segment configured, learned subnets from remote
    Silverpeak appliances and automatically learned local subnets.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - localSubnets
          - GET
          - /subnets3/all/vrfs/{vrfId}

    :param vrf_id: ID Number of Segment/VRF to query for routes
    :type vrf_id: int
    :return: Dictionary of appliance configured and learned subnets for
        a specified Segment/VRF \n
        * keyword **subnets** (`dict`): Subnet object \n
            * keyword **count** (`int`): Count of all subnets
            * keyword **max** (`int`): Max subnets IPv4 & IPv6, 60000
            * keyword **entries** (`list[dict]`): List of subnet detail
              objects \n
                * keyword **state** (`dict`): Subnet detail object \n
                    * keyword **version** (`int`): IP Version, e.g.
                      ``4`` or ``6``
                    * keyword **prefix** (`str`): Route prefix, e.g.
                      ``10.98.98.3/32``
                    * keyword **nextHop** (`str`): Next hop for prefix
                    * keyword **metric** (`int`): Metric of route, e.g.
                      ``50``
                    * keyword **ifName** (`str`): Interface name, e.g.
                      ``lo20000``
                    * keyword **peerid** (`int`): Peer id, e.g.
                      ``1894366``
                    * keyword **saas** (`int`): SaaS value, e.g. ``0``
                    * keyword **community** (`str`): Community string
                    * keyword **aspath** (`str`): AS Path, e.g.
                      ``64512,64710``
                    * keyword **learned** (`bool`): Learned from peer
                    * keyword **configured** (`bool`): Locally
                      configured
                    * keyword **advert** (`bool`): Advertise to peers
                    * keyword **automatic** (`bool`): Automatically
                      added by system
                    * keyword **local** (`bool`): Local route
                    * keyword **learnedFromIp** (`str`): IP peer route
                      learned from
                    * keyword **cloudApp** (`bool`): Cloud app
                    * keyword **advert_bgp** (`bool`): Advertise to BGP
                    * keyword **advert_ospf** (`bool`): Advertise to
                      OSPF
                    * keyword **learned_bgp** (`bool`): Learned from BGP
                    * keyword **learned_ospf** (`bool`): Learned from
                      OSPF
                    * keyword **state** (`str`): State of route, e.g.
                      ``UP`` or ``DOWN``
                    * keyword **routeTag** (`str`): Tag on route, e.g.
                      ``0``
                    * keyword **learnFrom** (`str`): How route was
                      learned, e.g. ``LRN_SPS_HUB`` for learned by an
                      EdgeConnect Hub or ``LRN_SPS_SPOKE`` for learned
                      by an EdgeConnect Spoke
                    * keyword **resolvedNexthop** (`str`): Resolved next
                      hop
                    * keyword **resolvedInterface** (`str`): Resolved
                      interface for route
                    * keyword **peerType** (`str`): Routing peer type,
                      e.g. ``PE`` for PE Router BGP peering
                    * keyword **nexthopTunnel** (`str`): Next hop tunnel
                    * keyword **networkRegionId** (`str`): Region ID and
                      name of route, e.g. ``1,East``
                    * keyword **subnetMessage** (`str`): Subnet message
                    * keyword **zone_id** (`str`): Firewall zone id for
                      route, e.g. ``0`` for Default
                    * keyword **advOSPFTag** (`str`): Advertise OSPF tag
                    * keyword **routeType** (`str`): Type of route e.g.
                      ``EBGP``
                    * keyword **saasAppName** (`str`): SaaS Application
                      Name
                    * keyword **adminDistance** (`int`): Admin distance
                      of route, e.g. ``1`` for local static
            * keyword **disabledByIPSLA** (`bool`): If routes are
              disabled by an IPSLA in a down state
            * keyword **metricAddedByIPSLA** (`int`): Metric added to
              routes due to an IPSLA being in a down state
            * keyword **peers** (`list[dict]`): List of SDWAN peer
              objects \n
                * keyword **index** (`str`): Peer index, e.g. ``0``
                * keyword **peerid** (`int`): Peer id value
                * keyword **peerName** (`str`): Hostname of peer
                * keyword **role** (`str`): Peer role, e.g. ``0`` for
                  ``Spoke``
                * keyword **roleName** (`str`): Friendly name of peer
                  role tyle, e.g. ``Spoke``
                * keyword **metric** (`int`): Route metric
                * keyword **peerPriority** (`int`): Peer priority value
                * keyword **txtrans** (`int`): Last transmitted
                  transaction count
                * keyword **txsecs** (`int`): Time elapsed since last
                  transmitted update
                * keyword **rxtrans** (`int`): Last received transaction
                  count
                * keyword **rxsecs** (`int`): Time elapsed since last
                  received update
                * keyword **rxrecs** (`int`): NEEDS DESCRIPTION
                * keyword **rxtabs** (`int`): NEEDS DESCRIPTION
                * keyword **outOfOrderCount** (`int`): Out of order
                  packets count, e.g. ``0``
                * keyword **majorVersion** (`str`): Major software
                  version, e.g. ``9`` in ``9.1.0.3``
                * keyword **minorVersion** (`str`): Minor software
                  version, e.g. ``1`` in ``9.1.0.3``
                * keyword **pointVersion** (`str`): Point software
                  version, e.g. ``0`` in ``9.1.0.3``
                * keyword **subVersion** (`str`): Sub software version
                  e.g. ``3`` in ``9.1.0.3``
                * keyword **region** (`str`): Appliance region id,
                  e.g. ``1``
                * keyword **regionName** (`str`): Appliance region name,
                  e.g. ``East``
                * keyword **messageVersion** (`str`): Subnet message
                  version, e.g. ``6``
                * keyword **message** (`str`): Specifies Information
                  about the supported subnet message version, e.g.
                  ``Submsg Ver6 (>= Rel9.0 or main)``
                * keyword **priorTxSec** (`str`): Prior Transmit second,
                  e.g. ``1418``
                * keyword **mainVerAndRegion** (`str`): Full software
                  version and region ID, e.g. ``9.1.0.3 (1)``
                * keyword **peername** (`str`): Hostname of peer
                * keyword **prio** (`int`): Peer priority value, e.g.
                  ``1024``
            * keyword **moduleInfo** (`dict`): local node details
              object \n
                * keyword **my system id** (`str`): String system ID,
                  e.g. ``1894366``
                * keyword **network region** (`str`): Local appliance
                  region name and ID, e.g. ``East (1)``
                * keyword **network role** (`str`): Local appliance role
                  , e.g. ``NRHub``
                * keyword **allow management to leak** (`str`): Allow
                  management routes to leak, boolean string e.g.
                  ``true``
                * keyword **last peer index** (`str`): Last peer index
                  number, e.g. ``0``
                * keyword **local change** (`str`): Local change id,
                  e.g. ``0x0000``
                * keyword **last time** (`str`): MS time since boot,
                  e.g. ``1961072580 ms after boot``
                * keyword **last change** (`str`): MS time since last
                  change, e.g. ``1960554071 ms after boot``
                * keyword **time since change** (`str`): Time since last
                  change, e.g.  ``518 seconds``
                * keyword **last tx trans** (`str`): Last Transmit
                  message, e.g. ``2212``
                * keyword **last tx rec count** (`str`): Last Transmit
                  message received count, e.g. ``0``
                * keyword **last tx msg count** (`str`): Last Transmit
                  message count, e.g. ``0``
                * keyword **rx invalid msg** (`str`): Receive invalid
                  message count, e.g. ``0``
                * keyword **rx unknown msg** (`str`): Receive unknown
                  message count, e.g. ``0``
                * keyword **IP tracking** (`str`): If IP Tracking is
                  enabled, e.g. ``ENABLED``
                * keyword **IP track delta** (`str`): IP Tracking delta,
                  e.g. ``0``
                * keyword **Active READER index** (`str`): Active reader
                  index, e.g.  ``0``
    :rtype: dict
    """
    return self._get(f"/subnets3/all/vrfs/{vrf_id}")


def get_appliance_locally_configured_subnets(self) -> dict:
    """Get configured local subnets only.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - localSubnets
          - GET
          - /subnets3/configured

    :return: Dictionary of locally configured subnets \n
        * keyword **prefix** (`dict`): Subnets object \n
            * keyword **<ip_and_mask>** (`dict`): Object for this
              prefix, e.g. key value ``10.1.1.0/24`` \n
                * keyword **self** (`int`): Max subnets IPv4 & IPv6,
                  60000
                * keyword **advert** (`bool`): If route is advertised
                * keyword **advert_bgp** (`bool`): If route is
                  advertised to BGP
                * keyword **advert_ospf** (`bool`): If route is
                  advertised to OSPF
                * keyword **local** (`bool`): If route is locally
                  configured
                * keyword **nhop** (`dict`): Next hop detail object \n
                    * keyword **<next_hop_ip>** (`dict`): Next hop \n
                        * keyword **self** (`str`): Next hop ip address
                        * keyword **interface** (`dict`): Next hop
                          interface detail object \n
                            * keyword **<interface_name>** (`dict`):
                              interface name for next hop, e.g.
                              ``lan0`` \n
                            "lan0.40": {
                                * keyword **self** (`str`): Interface
                                  name
                                * keyword **comment** (`str`): Comment
                                  on route
                                * keyword **dir** (`str`): Direction
                                  applied, e.g. ``FROM_LAN``,
                                  ``FROM_WAN``, ``ANY``
                                * keyword **gms_marked** (`bool`):
                                  If route is Orchestrator configured
                                * keyword **metric** (`int`): Metric
                                  of configured route
                                * keyword **zone_id** (`int`): Firewall
                                  zone id for route, ``65534`` for
                                  None/Default
    :rtype: dict
    """
    return self._get("/subnets3/configured")


def update_appliance_all_locally_configured_subnets(
    self,
    locally_configured_subnets: dict,
) -> bool:
    """Set configured local subnets. Any subnets which posted but not
    on appliance currently are added, missing subnets are removed,
    matching subnets are updated.

    .. warning::

        Use :func:`~pyedgeconnect.EdgeConnect.get_appliance_locally_configured_subnets`
        to obtain current subnets on appliance to avoid accidentally
        deleting static routes, or use
        :func:`~pyedgeconnect.EdgeConnect.add_appliance_locally_configured_routes`
        to only add net-new routes to appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - localSubnets
          - POST
          - /subnets3/configured

    :param locally_configured_subnets: Dictionary of locally configured
        subnets \n
        * keyword **prefix** (`dict`): Subnets object \n
            * keyword **<ip_and_mask>** (`dict`): Object for this
              prefix, e.g. key value ``10.1.1.0/24`` \n
                * keyword **self** (`int`): Max subnets IPv4 & IPv6, 60000
                * keyword **advert** (`bool`): If route is advertised
                * keyword **advert_bgp** (`bool`): If route is
                  advertised to BGP
                * keyword **advert_ospf** (`bool`): If route is
                  advertised to OSPF
                * keyword **local** (`bool`): If route is locally
                  configured
                * keyword **nhop** (`dict`): Next hop detail object \n
                    * keyword **<next_hop_ip>** (`dict`): Next hop \n
                        * keyword **self** (`str`): Next hop ip address
                        * keyword **interface** (`dict`): Next hop
                          interface detail object \n
                            * keyword **<interface_name>** (`dict`):
                              interface name for next hop, e.g.
                              ``lan0`` \n
                            "lan0.40": {
                                * keyword **self** (`str`): Interface
                                  name
                                * keyword **comment** (`str`): Comment
                                  on route
                                * keyword **dir** (`str`): Direction
                                  applied, e.g. ``FROM_LAN``,
                                  ``FROM_WAN``, ``ANY``
                                * keyword **gms_marked** (`bool`):
                                  If route is Orchestrator configured
                                * keyword **metric** (`int`): Metric
                                  of configured route
                                * keyword **zone_id** (`int`): Firewall
                                  zone id for route, ``65534`` for
                                  None/Default
    :type locally_configured_subnets: dict
    :return: Returns True/False based on successful call
    :rtype: bool
    """  # noqa: W505, E501
    return self._post(
        "/subnets3/configured",
        data=locally_configured_subnets,
        return_type="bool",
    )


def get_appliance_locally_configured_subnets_single_vrf(
    self,
    vrf_id: int,
) -> dict:
    """Get configured local subnets only of specified Segment/VRF

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - localSubnets
          - GET
          - /subnets3/configured/vrfs/{vrfId}

    :param vrf_id: ID Number of Segment/VRF to query for routes
    :type vrf_id: int
    :return: Dictionary of locally configured subnets of specified
        Segment/VRF \n
        * keyword **prefix** (`dict`): Subnets object \n
            * keyword **<ip_and_mask>** (`dict`): Object for this
              prefix, e.g. key value ``10.1.1.0/24`` \n
                * keyword **self** (`int`): Max subnets IPv4 & IPv6,
                  60000
                * keyword **advert** (`bool`): If route is advertised
                * keyword **advert_bgp** (`bool`): If route is
                  advertised to BGP
                * keyword **advert_ospf** (`bool`): If route is
                  advertised to OSPF
                * keyword **local** (`bool`): If route is locally
                  configured
                * keyword **nhop** (`dict`): Next hop detail object \n
                    * keyword **<next_hop_ip>** (`dict`): Next hop \n
                        * keyword **self** (`str`): Next hop ip address
                        * keyword **interface** (`dict`): Next hop
                          interface detail object \n
                            * keyword **<interface_name>** (`dict`):
                              interface name for next hop, e.g.
                              ``lan0`` \n
                            "lan0.40": {
                                * keyword **self** (`str`): Interface
                                  name
                                * keyword **comment** (`str`): Comment
                                  on route
                                * keyword **dir** (`str`): Direction
                                  applied, e.g. ``FROM_LAN``,
                                  ``FROM_WAN``, ``ANY``
                                * keyword **gms_marked** (`bool`):
                                  If route is Orchestrator configured
                                * keyword **metric** (`int`): Metric
                                  of configured route
                                * keyword **zone_id** (`int`): Firewall
                                  zone id for route, ``65534`` for
                                  None/Default
    :rtype: dict
    """
    return self._get(f"/subnets3/configured/vrfs/{vrf_id}")


def update_appliance_all_locally_configured_subnets_single_vrf(
    self,
    vrf_id: int,
    locally_configured_subnets: dict,
) -> bool:
    """Set configured local subnets for specified Segment/VRF. Any
    subnets which posted but not on appliance currently are added,
    missing subnets are removed, matching subnets are updated.

    .. warning::

        Use :func:`~pyedgeconnect.EdgeConnect.get_appliance_locally_configured_subnets_single_vrf`
        to obtain current subnets on appliance to avoid accidentally
        deleting static routes

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - localSubnets
          - POST
          - /subnets3/configured/vrfs/{vrfId}

    :param vrf_id: ID Number of Segment/VRF to query for routes
    :type vrf_id: int
    :param locally_configured_subnets: Dictionary of locally configured
        subnets \n
        * keyword **prefix** (`dict`): Subnets object \n
            * keyword **<ip_and_mask>** (`dict`): Object for this
              prefix, e.g. key value ``10.1.1.0/24`` \n
                * keyword **self** (`int`): Max subnets IPv4 & IPv6, 60000
                * keyword **advert** (`bool`): If route is advertised
                * keyword **advert_bgp** (`bool`): If route is
                  advertised to BGP
                * keyword **advert_ospf** (`bool`): If route is
                  advertised to OSPF
                * keyword **local** (`bool`): If route is locally
                  configured
                * keyword **nhop** (`dict`): Next hop detail object \n
                    * keyword **<next_hop_ip>** (`dict`): Next hop \n
                        * keyword **self** (`str`): Next hop ip address
                        * keyword **interface** (`dict`): Next hop
                          interface detail object \n
                            * keyword **<interface_name>** (`dict`):
                              interface name for next hop, e.g.
                              ``lan0`` \n
                            "lan0.40": {
                                * keyword **self** (`str`): Interface
                                  name
                                * keyword **comment** (`str`): Comment
                                  on route
                                * keyword **dir** (`str`): Direction
                                  applied, e.g. ``FROM_LAN``,
                                  ``FROM_WAN``, ``ANY``
                                * keyword **gms_marked** (`bool`):
                                  If route is Orchestrator configured
                                * keyword **metric** (`int`): Metric
                                  of configured route
                                * keyword **zone_id** (`int`): Firewall
                                  zone id for route, ``65534`` for
                                  None/Default
    :type locally_configured_subnets: dict
    :return: Returns True/False based on successful call
    :rtype: bool
    """  # noqa: W505, E501
    return self._post(
        f"/subnets3/configured/vrfs/{vrf_id}",
        data=locally_configured_subnets,
        return_type="bool",
    )


def add_appliance_locally_configured_routes(
    self,
    locally_configured_subnets: dict,
) -> bool:
    """Add configured local subnets to existing routes.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - localSubnets
          - POST
          - /subnets3/configured/addMultiple

    :param locally_configured_subnets: Dictionary of locally configured
        subnets \n
        * keyword **prefix** (`dict`): Subnets object \n
            * keyword **<ip_and_mask>** (`dict`): Object for this
              prefix, e.g. key value ``10.1.1.0/24`` \n
                * keyword **self** (`int`): Max subnets IPv4 & IPv6,
                  60000
                * keyword **advert** (`bool`): If route is advertised
                * keyword **advert_bgp** (`bool`): If route is
                  advertised to BGP
                * keyword **advert_ospf** (`bool`): If route is
                  advertised to OSPF
                * keyword **local** (`bool`): If route is locally
                  configured
                * keyword **nhop** (`dict`): Next hop detail object \n
                    * keyword **<next_hop_ip>** (`dict`): Next hop \n
                        * keyword **self** (`str`): Next hop ip address
                        * keyword **interface** (`dict`): Next hop
                          interface detail object \n
                            * keyword **<interface_name>** (`dict`):
                              interface name for next hop, e.g.
                              ``lan0`` \n
                            "lan0.40": {
                                * keyword **self** (`str`): Interface
                                  name
                                * keyword **comment** (`str`): Comment
                                  on route
                                * keyword **dir** (`str`): Direction
                                  applied, e.g. ``FROM_LAN``,
                                  ``FROM_WAN``, ``ANY``
                                * keyword **gms_marked** (`bool`):
                                  If route is Orchestrator configured
                                * keyword **metric** (`int`): Metric
                                  of configured route
                                * keyword **zone_id** (`int`): Firewall
                                  zone id for route, ``65534`` for
                                  None/Default
    :type locally_configured_subnets: dict
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/subnets3/configured/addMultiple",
        data=locally_configured_subnets,
        return_type="bool",
    )


def delete_appliance_locally_configured_routes(
    self,
    local_subnets_to_delete: list[dict],
) -> bool:
    """Delete configured local subnets specified in
    ``local_subnets_to_delete`` parameter

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - localSubnets
          - POST
          - /subnets3/configured/deleteMultiple

    :param local_subnets_to_delete: List of locally configured subnets
        to remove from appliance \n
        * [`dict`]: Array of routes to remove
            * keyword **prefix** (`str`): Prefix of route to remove
            * keyword **nhop** (`str`): Nexthop of route to remove
            * keyword **interface** (`str`): Interface of route to
              remove
    :type local_subnets_to_delete: list
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/subnets3/configured/deleteMultiple",
        data=local_subnets_to_delete,
        return_type="bool",
    )


def appliance_find_preferred_route(
    self,
    ip_address: str,
    in_port: str,
    overlay_id: int,
    segment_name: str,
) -> dict:
    """Find the preferred routes from appliance based on query

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - localSubnets
          - POST
          - /routes/preferredRoute

    :param ip_address: IP address to query for preferred route
    :type ip_address: str
    :param in_port: Incoming traffic direction. possible values are
        ``l2w`` (from lan) or ``w2l`` (from wan) or ``self`` (for self
        generated)
    :type in_port: str
    :param overlay_id: Overlay ID, use ``0`` for any overlay
    :type overlay_id: str
    :param segment_name: Should specify only if VRF is enabled. If left
        as blank string the default value is ``Default``. If a Segment
        name that does not exist is specified response will be a blank
        dictionary.
    :type segment_name: str
    :return: Returns dictionary of preferred route from appliance \n
        * keyword **passthrough** (`dict`): Contains matched passthrough
          route details, if not passthrough will have value of
          ``null`` \n
            * keyword **srcMAC** (`str`): Source MAC Address
            * keyword **destMAC** (`str`): Destination MAC Address
            * keyword **interfaceName** (`str`): Interface name, e.g.
              ``wan0``
            * keyword **nexthop** (`str`): Next hop IP address
            * keyword **vlan** (`str`): VLAN
            * keyword **isApplianceIP** (`bool`): If IP belongs to
              appliances
        * keyword **swdwan** (`dict`): Contains matched sdwan route
          details, if not sdwan will have value of ``null`` \n
            * keyword **peerID** (`str`): Peer ID number
            * keyword **peerName** (`str`): Hostname of SDWAN peer
    :rtype: dict
    """
    data = {
        "ipAddress": ip_address,
        "inPort": in_port,
        "overlayId": overlay_id,
        "segmentName": segment_name,
    }

    return self._post(
        "/routes/preferredRoute",
        data=data,
    )


def get_appliance_routing_peers_info(self) -> list:
    """Get appliance routing peers information

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - localSubnets
          - GET
          - /subnets/state/peersInfo

    :return: List of appliance routing peers info \n
        * [`dict`]: List of appliance routing peers information \n
            * keyword **index** (`str`): Peer index, e.g. ``0``
            * keyword **peerid** (`int`): Peer id value
            * keyword **peerName** (`str`): Hostname of peer
            * keyword **role** (`str`): Peer role, e.g. ``0`` for
              ``Spoke``
            * keyword **roleName** (`str`): Friendly name of peer
              role tyle, e.g. ``Spoke``
            * keyword **metric** (`int`): Route metric
            * keyword **peerPriority** (`int`): Peer priority value
            * keyword **txtrans** (`int`): Last transmitted
                transaction count
            * keyword **txsecs** (`int`): Time elapsed since last
                transmitted update
            * keyword **rxtrans** (`int`): Last received transaction
                count
            * keyword **rxsecs** (`int`): Time elapsed since last
                received update
            * keyword **rxrecs** (`int`): NEEDS DESCRIPTION
            * keyword **rxtabs** (`int`): NEEDS DESCRIPTION
            * keyword **outOfOrderCount** (`int`): Out of order
              packets count, e.g. ``0``
            * keyword **majorVersion** (`str`): Major software
              version, e.g. ``9`` in ``9.1.0.3``
            * keyword **minorVersion** (`str`): Minor software
              version, e.g. ``1`` in ``9.1.0.3``
            * keyword **pointVersion** (`str`): Point software
              version, e.g. ``0`` in ``9.1.0.3``
            * keyword **subVersion** (`str`): Sub software version
              e.g. ``3`` in ``9.1.0.3``
            * keyword **region** (`str`): Appliance region id,
              e.g. ``1``
            * keyword **regionName** (`str`): Appliance region name,
              e.g. ``East``
            * keyword **messageVersion** (`str`): Subnet message
              version, e.g. ``6``
            * keyword **message** (`str`): Specifies Information
              about the supported subnet message version, e.g.
              ``Submsg Ver6 (>= Rel9.0 or main)``
            * keyword **priorTxSec** (`str`): Prior Transmit second,
              e.g. ``1418``
            * keyword **mainVerAndRegion** (`str`): Full software
              version and region ID, e.g. ``9.1.0.3 (1)``
    :rtype: dict
    """
    return self._get("/subnets/state/peersInfo")
