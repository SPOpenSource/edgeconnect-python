# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# deployment : Deployment configuration


def get_appliance_deployment(
    self,
) -> dict:
    """Get the deployment configuration of the appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - deployment
          - GET
          - /deployment

    :param ne_pk: Network Primary Key (nePk) of existing appliance,
        e.g. ``3.NE``
    :type ne_pk: str
    :return: Returns dictionary of appliance deployment information \n
        * keyword **scalars** (`dict`): Scalars object, example values
          included below \n
            * keyword **maxWanBandwidth** (`int`): 200000
            * keyword **defaultMaxWanBandwidth** (`int`): 200000
            * keyword **maxRxTargetBandwidth** (`int`): 2000000
            * keyword **maxTunnels** (`int`): 2000
            * keyword **maxIKETunnels** (`int`): 4000
            * keyword **minMtu** (`int`): 700
            * keyword **maxMtu** (`int`): 9000
            * keyword **maxRouteMaps** (`int`): 10
            * keyword **maxOptMaps** (`int`): 10
            * keyword **maxQoSMaps** (`int`): 10
            * keyword **maxNatMaps** (`int`): 10
            * keyword **maxRouteMapEntries** (`int`): 2000
            * keyword **maxOptMapEntries** (`int`): 200
            * keyword **maxQoSMapEntries** (`int`): 200
            * keyword **maxNatMapEntries** (`int`): 300
            * keyword **isPortalLicensed** (`bool`): true
            * keyword **portalLicenseType** (`int`): 2
            * keyword **supportServerMode** (`bool`): true
            * keyword **isLicenseRequired** (`bool`): false
            * keyword **isDynamicLimits** (`bool`): true
            * keyword **isDynamicInterface** (`bool`): true
            * keyword **isModel4Port** (`bool`): true
            * keyword **isModel10G** (`bool`): false
            * keyword **isModelSingleDisk** (`bool`): true
            * keyword **isModelPowerCycle** (`bool`): false
            * keyword **num1GigPorts** (`int`): 32
            * keyword **num1GigFiberPorts** (`int`): 0
            * keyword **numMgmtPorts** (`int`): 2
            * keyword **num10GigPorts** (`int`): 0
            * keyword **isGMSCompatible** (`bool`): true
            * keyword **maxAcls** (`int`): 100
            * keyword **maxAclEntries** (`int`): 100
            * keyword **maxUDAs** (`int`): 200
            * keyword **maxUDAEntries** (`int`): 400
            * keyword **maxVLANs** (`int`): 127
            * keyword **maxSubInterfaces** (`int`): 127
            * keyword **diskLayout** (`str`): ""
            * keyword **vrrpCompatible** (`bool`): false
            * keyword **supportsBridgeLoopTest** (`bool`): true
            * keyword **supportsDiskSelfTest** (`bool`): true
            * keyword **supportsBypass** (`bool`): false
            * keyword **isNMInDisklessMode** (`bool`): false
            * keyword **nmDiskSize** (`int`): 70
            * keyword **processorCount** (`int`): 2
            * keyword **memorySize** (`int`): 6
            * keyword **cacheDiskCount** (`int`): 0
            * keyword **spindleDiskCount** (`int`): 1
            * keyword **maxFlows** (`int`): 128000
            * keyword **maxRedFlows** (`int`): 1024000
            * keyword **maxBypassFlows** (`int`): 1024000
            * keyword **actualProcessorCount** (`int`): 2
            * keyword **actualMemorySize** (`int`): 6
            * keyword **actualNMDiskSize** (`int`): 70
            * keyword **isModelForReplication** (`bool`): false
            * keyword **maxIpServiceEntries** (`int`): 1000000
            * keyword **maxSaasEntries** (`int`): 256000
            * keyword **maxOverlays** (`int`): 7
            * keyword **maxSegMapEntries** (`int`): 2000
            * keyword **maxDnsProxySegments** (`int`): 4
            * keyword **maxRoutemaps** (`int`): 10
            * keyword **maxOptmaps** (`int`): 10
            * keyword **maxQosmaps** (`int`): 10
            * keyword **maxNatmaps** (`int`): 10
            * keyword **maxAcmaps** (`int`): 10
            * keyword **maxPolicymaps** (`int`): 70
            * keyword **maxMapnamelen** (`int`): 32
            * keyword **maxRulesperacl** (`int`): 100
            * keyword **maxAclrulelen** (`int`): 1024
            * keyword **isIdsSupported** (`bool`): false
        * keyword **sysConfig** (`dict`): Appliance's system
          configuration \n
            * keyword **mode** (`str`):  System deployment mode,
              ``bridge`` or ``router``
            * keyword **useMgmt0** (`bool`): Use mgmt0 interface as a
              datapath interface as well. (only valid under router mode)
            * keyword **tenG** (`bool`): Use 10Gbps interfaces (only
              valid for models with 10Gbps interfaces)
            * keyword **bonding** (`bool`): Use interface bonding (only
              valid for models with 2 LAN interfaces and 2 WAN
              interfaces)
            * keyword **maxBW** (`int`): System maximum bandwidth in
              Kbps
            * keyword **propagateLinkDown** (`bool`): Propagate link
              down state: this is valid in bridge mode only. If it is
              true, if either LAN or WAN side interface of the bridge is
              down, the system brings down the other interface
              automatically
            * keyword **singleBridge** (`bool`): Single 4-port flat
              bridge configuration (only valid for 4-port models)
            * keyword **inline** (`bool`): Inline router mode (only
              valid for router mode). This is the recommended mode.
            * keyword **ifLabels** (`dict`): interface labels \n
                * keyword **lan** (`list[dict]`): Available LAN
                  interface labels \n
                    * [`dict`]: interface detail \n
                        * keyword **id** (`str`): Unique label ID
                        * keyword **name** (`str`): Label name eg:
                          ``Voice``, ``Data``, ``MPLS``...
                * keyword **wan** (`list[dict]`): Available WAN
                  interface labels \n
                    * [`dict`]: interface detail \n
                        * keyword **id** (`str`): Unique label ID
                        * keyword **name** (`str`): Label name eg:
                          ``Voice``, ``Data``, ``MPLS``...
            * keyword **haIf** (`str`): Name of the interface used to
              build 'internal' High Availability (HA) VLAN interfaces
              using which two appliances in a HA configuration can
              communicate with each other
            * keyword **maxInBW** (`int`): System maximum inbound
              bandwidth in Kbps (to enable inbound shaping make sure
              maxInBWEnabled is set to true)
            * keyword **maxInBWEnabled** (`bool`): Enable inbound
              bandwidth shaping (if this is true, you must specify
              maxInBW)
            * keyword **licence** (`dict`): Appliance EC license
              information (only valid for EC models) \n
                * keyword **ecMini** (`bool`): Is EC Mini license
                  enabled
                * keyword **ecPlus** (`bool`): Is EC Plus license
                  enabled
                * keyword **ecTier** (`str`): EC Tier license name
                * keyword **ecTierBW** (`int`): EC Tier bandwidth in
                  Kbps
                * keyword **ecBoost** (`bool`): Is EC Boost license
                  enabled
                * keyword **ecBoostBW** (`int`): Boost bandwidth in
                  Kbps
                * keyword **<license_type>** (`dict`, optional): This
                  key is dynamic based on the EC license type (``fx``,
                  ``ecsp`` etc). Contains additional details based on
                  license type.
            * keyword **zones** (`list[dict]`): Firewall zones \n
                * [`dict`]: FW Zones object \n
                    * keyword **id** (`int`): Zone ID, e.g. ``1``
                    * keyword **name** (`str`): Zone name,
                      e.g. ``Public``
            * keyword **vrfs** (`list[dict]`): VRF segments \n
                * [`dict`]: VRF segments object \n
                    * keyword **id** (`int`): VRF ID, e.g. ``0``
                    * keyword **name** (`str`): VRF name,
                      e.g. ``Default``
            * keyword **vrfZonesMap** (`dict`): Mapping of zone ids
              and corresponding VRFs \n
                * keyword **<vrf_id>** (`dict`): VRF mapping \n
                    * keyword **<zone_id>** (`dict`): Zone mapping \n
                        * keyword **id** (`int`): Zone ID, e.g. ``1``
                        * keyword **name** (`str`): Zone name,
                          e.g. ``Public``
        * keyword **mgmtIfData** (`dict`): Appliance's management
          network interfaces information \n
            * keyword **<mgmt_interface>** (`dict`): mgmt object \n
                * keyword **dhcp** (`bool`): Is DHCP on or off on this
                  management interface
                * keyword **nexthop** (`str`): Management interface
                  gateway IP address
                * keyword **ip** (`str`): Management interface IP
                  address
                * keyword **mask** (`int`): Management interface network
                  mask
        * keyword **modeIfs** (`list[dict]`): Interface details \n \n
            * keyword **devNum** (`str`): Deployment interface type,
              rtr1/rtr2, bdg1/bdg2, only for UI use, not needed in POST
            * keyword **ifName** (`str`): Deployment interface name,
              wan0/lan0 for router mode, bvi0/bvi1 for bridge mode
            * keyword **applianceIPs** (`list[dict]`): Deployment
              interface IP addresses assignment \n
                * [`dict`]: Interface object \n
                    * keyword **ip** (`str`): Appliance interface IP
                      address
                    * keyword **mask** (`int`): IP address network mask
                    * keyword **subif** (`str`): Sub-interface ID
                    * keyword **vlan** (`str`): VLAN ID
                    * keyword **wanNexthop** (`str`): Next hop IP
                      address
                    * keyword **label** (`str`): Interface label
                      assigned to this interface
                    * keyword **lanSide** (`bool`): Determines if this
                      interface is on LAN side
                    * keyword **wanSide** (`bool`): Determines if this
                      interface is on WAN side
                    * keyword **dhcp** (`bool`): Determines if DHCP is
                      enabled for this interface (only applicable for
                      WAN side main interface IPs in inline router mode)
                    * keyword **harden** (`int`): Determines if this
                      interface has firewall configured (only applicable
                      for WAN side main/VLAN interfaces in router mode).
                      Valid values are 0:Allow All, 1:Hardened,
                      2:Stateful, 3:Stateful+SNAT
                    * keyword **behindNAT** (`str`): Determines if this
                      interface is connected to a Network Address
                      Translation device (only applicable to WAN
                      interfaces). Valid values are 'auto', 'none', ''.
                      'auto' means interface is behind a NAT device.
                      'none' or '' mean interface is NOT behind a NAT
                      device
                    * keyword **maxBW** (`dict`): Maximum
                      inbound/outbound bandwidth for this interface in
                      Kbps (only applicable to WAN interfaces) \n
                        * keyword **inbound** (`int`): Maximum inbound
                          (WAN to LAN) bandwidth for this interface in
                          Kbps
                        * keyword **outbound** (`int`): Maximum outbound
                          (LAN to WAN) bandwidth for this interface in
                          Kbps
                    * keyword **dhcpd** (`dict`): Interface DHCP
                      (server/relay) configuration (only applicable
                      to LAN interfaces in inline router mode) \n
                        * keyword **type** (`str`): Enum to determine if
                          this LAN interface is acting like a DHCP
                          server, relay or none. Valid values are
                          ``server``, ``relay``, ``none``
                        * keyword **server** (`dict`): DHCP server
                          related configuration \n
                            * keyword **prefix** (`str`): DHCP server
                              subnet and mask value
                              e.g. ``10.3.171.0/24``
                            * keyword **ipStart** (`str`): IP within the
                              DHCP server subnet from where to start
                              allocating IPs
                            * keyword **ipEnd** (`str`): IP within the
                              DHCP server subnet till where IPs can be
                              allocated
                            * keyword **gw** (`list[str]`): Gateway IP
                              Address
                            * keyword **dns** (`list[str]`): DNS
                              server(s) IP Address
                            * keyword **ntpd** (`list[str]`): NTP
                              server(s) IP Address
                            * keyword **netbios** (`list[str]`): NetBIOS
                              name server(s) IP Address
                            * keyword **netbiosNodeType** (`str`): Enum
                              denoting the type of NetBIOS server. Valid
                              values are ``B``, ``P``, ``M``, ``H``
                            * keyword **maxLease** (`int`): Maximum
                              lease time in seconds
                            * keyword **defaultLease** (`int`): Default
                              lease time in seconds
                            * keyword **options** (`dict`): Object
                              containing dynamic DHCP options \n
                                * keyword **<option_id>** (`str`):
                                  option value
                            * keyword **host** (`dict`): Object
                              containing list of hosts with static IP
                              reservations \n
                                * keyword **<hostname>** (`dict`): \n
                                    * keyword **mac** (`str`): MAC
                                      address
                                    * keyword **ip** (`str`): IP address
                            * keyword **failover** (`bool`): Determine
                              if appliance enable DHCP failover
                        * keyword **relay** (`dict`): DHCP relay related
                          configuration \n
                            * keyword **dhcpserver** (`list[str]`):
                              Array of destination DHCP server IP
                              addresses
                            * keyword **option82** (`bool`): Determine
                              whether option 82 is enabled
                            * keyword **option82_policy** (`str`): Enum
                              to determine option 82 policy used if
                              option 82 is enabled. Valid values are
                              ``append``, ``replace``, ``forward``,
                              ``discard``
                    * keyword **brifs** (`dict`): Bridge
                      interface configurations \n
                        * keyword **<interface>** (`dict`): brif
                          object \n
                            * keyword **label** (`str`): Bridge lan/wan
                              side interface label
                            * keyword **harden** (`str`): Firewall
                              configuration for bridge interface. Valid
                              values are 0:Allow All, 1:Hardened,
                              2:Stateful, 3:Stateful+SNAT
                            * keyword **wanSide** (`bool`): This bridge
                              interface is on WAN side
                            * keyword **lanSide** (`bool`): This bridge
                              interface is on LAN side
                            * keyword **comment** (`str`): User comments
                    * keyword **zone** (`int`): Zone id assigned to
                      this interface. 0 if no zone assigned
                    * keyword **vrf** (`int`): VRF segment id assigned
                      to this interface. 0 if default VRF segment is
                      assigned
                    * keyword **comment** (`str`): User comments
                    * keyword **failover** (`bool`): Determine if
                      appliance enable DHCP failover
        * keyword **dpRoutes** (`list[dict]`): \n
            * [`dict`]: dpRoutes object \n
                * keyword **prefix** (`str`): Subnetwork prefix, for
                  example, ``2.2.2.0/24``
                * keyword **nexthop** (`str`): Next hop IP address for
                  this route entry
                * keyword **intf** (`str`): Interface name for this
                  route entry, auto or bvi0/bvi1/VLAN for bridge mode
                * keyword **metric** (`int`): Routing metric value,
                  lower values have higher priority
                * keyword **type** (`str`): Route entry type, gw is the
                  only option for now
        * keyword **vifs** (`dict`): vifs object \n
            * keyword **pppoe** (`list[str]`): List of PPPoE interface
              names configured on this appliance
            * keyword **bondedIfs** (`list[str]`): List of bonded
              interfaces configured on this appliance
        * keyword **dhcpFailover** (`dict`): DHCP failover config \n
            * keyword **<interface>** (`dict`): interface dhcp failover
              config \n
                * keyword **max_unack_updates** (`int`): Tells the
                  remote DHCP server how many BNDUPD messages it can
                  send before it receives a BNDACK from the local system
                * keyword **peer_port** (`int`): Define which TCP port
                  to connect to its failover peer for failover messages
                * keyword **my_port** (`int`): Defines which TCP port
                  the server should listen for connections from its
                  failover peer
                * keyword **max_resp_delay** (`int`): Tells the DHCP
                  server how many seconds may pass without receiving a
                  message from its failover peer before it assumes that
                  connection has failed
                * keyword **load_bal_max** (`int`): Defines a threshold
                  to compare with the secs field of the client's DHCP
                  packet in order to override load balancing
                * keyword **role** (`str`) = Specify if the server is
                  the primary or secondary, ``primary`` or ``secondary``
                * keyword **mclt** (`int`): Define the Maximum Client
                  Lead Time
                * keyword **split** (`int`): Specify the split between
                  the primary and secondary
                * keyword **peer_ip** (`str`): Define which server it
                  should connect to reach its failover peer
                * keyword **my_ip** (`str`): Define the address that the
                  server should listen for connections from its failover
                  peer
    :rtype: dict
    """
    return self._get("/deployment")


# TODO - POST /deployment
#      - Modify the deployment settings
# TODO - POST /deployment/validate
#      - Validate deployment configuration
