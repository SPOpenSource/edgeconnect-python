# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# networkRoleAndSite : ECOS network role and site


def get_appliance_network_role_and_site(
    self,
    ne_id: str,
) -> dict:
    """Get an appliance Network Role and Site information

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - networkRoleAndSite
          - GET
          - /appliance/networkRoleAndSite/{neid}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :return: Returns appliance network role and site information \n
        * keyword **id** (`str`): Appliance ID or NePK, e.g. ``3.NE``
        * keyword **uuid** (`str`): Appliance uuid
        * keyword **networkRole** (`str`): Appliance role, ``1`` for
          Hub, ``0`` for spoke, ``2`` for mesh
        * keyword **site** (`str`): Appliance site
        * keyword **sitePriority** (`int`): Appliance site priority
        * keyword **userName** (`str`): Username for appliance
        * keyword **password** (`str`): Password for appliance, ``null``
        * keyword **groupId** (`str`): Appliance Group ID,
          e.g. ``15.Network``
        * keyword **IP** (`str`): Appliance management IP
        * keyword **webProtocolType** (`int`): Web protocol type,
          ``1`` for HTTP, ``2`` for HTTPS, ``3`` for Both
        * keyword **serial** (`str`): Appliance serial number
        * keyword **hasUnsavedChanges** (`bool`): ``True`` if appliance
          has unsaved changes
        * keyword **rebootRequired** (`bool`): ``True`` if appliance
          requires a reboot
        * keyword **model** (`str`): Appliance model
        * keyword **hardwareRevision** (`str`): Specific revision of
          appliance hardware
        * keyword **hostName** (`str`): Configured hostname of appliance
        * keyword **applianceId** (`int`): Integer appliance id
        * keyword **platform** (`str`): Running platform,
          e.g. ``VMware`` for a VM EC running on ESXi
        * keyword **mode** (`str`): Deployment mode the appliance is
          configured in
        * keyword **bypass** (`bool`): If ``True``, appliance is
          currently in bypass
        * keyword **softwareVersion** (`str`): Software version running
          on the appliance
        * keyword **startupTime** (`int`): No description in Swagger
        * keyword **webProtocol** (`str`): ``HTTP``, ``HTTPS``, or
          ``BOTH``
        * keyword **systemBandwidth** (`int`): Appliance system
          bandwidth, in Kbps
        * keyword **state** (`int`): State of the appliance. ``0`` -
          Unknown ( When an appliance is added to Orchestrator, it is in
          this state ),
          ``1`` - Normal (Appliance is reachable from Orchestrator),
          ``2`` - Unreachable (Appliance is unreachable from
          Orchestrator),
          ``3`` - Unsupported Version (Orchestrator does not support
          this version of the appliance ),
          ``4`` - Out of Synchronization (Orchestrator's cache of
          appliance configuration/state is out of sync with the
          configuration/state on the appliance),
          ``5`` - Synchronization in Progress (Orchestrator is currently
          synchronizing appliances's configuration and state)
        * keyword **dynamicUuid** (`str`): NEEDS DESCRIPTION
        * keyword **portalObjectId** (`str`): Appliance hash ID in
          Cloud Portal
        * keyword **discoveredFrom** (`int`): How the appliance was
          added to Orchestrator. ``1`` = MANUAL, ``2`` = PORTAL, ``3`` =
          APPLIANCE
        * keyword **reachabilityChannel** (`int`): Reachability channel
          of the appliance. ``0`` - Unknown, ``1`` - Orchestrator talks
          to appliance using HTTP/HTTPS using user id and password. This
          is not used for EdgeConnects and SD-WAN, ``2`` - Appliance
          connects to Orchestrator using HTTPS Websocket. Orchestrator
          uses this permanent connection to configure/monitor appliance.
          This is done because Appliance may be behind a firewall making
          it hard for Orchestrator to contact appliance using IP
          address, ``4`` - Orchestrator sends configuration/monitoring
          request to Cloud Portal which relays those requests to
          Appliance. Appliance sends its response to Cloud Portal which
          relays it back to Orchestrator.
        * keyword **haPeer** (`str`): Name of appliance EdgeHA peer,
          if applicable
        * keyword **zoneList** (`dict`): dictionary of list of zones
          being used by appliance \n
            * keyword **zones** (`list[str]`): list of zones
        * keyword **interfaceList** (`dict`): dictionary of list of
          interface labels being used by appliance \n
            * keyword **interfaceLabels** (`list[str]`): list of
              interface numbers
        * keyword **tagsList** (`str`): NEEDS DESCRIPTION
        * keyword **preconfigStatus** (`str`): NEEDS DESCRIPTION
        * keyword **ip** (`str`): Appliance management IP
        * keyword **nePk** (`str`): Appliance ID or NePK, e.g. ``3.NE``
    :rtype: dict
    """
    return self._get("/appliance/networkRoleAndSite/{}".format(ne_id))


def update_appliance_network_role_and_site(
    self,
    ne_id: str,
    network_role: int,
    site: str,
    site_priority: int = 0,
) -> dict:
    """Update an appliance Network Role and Site information

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - networkRoleAndSite
          - POST
          - /appliance/networkRoleAndSite/{neid}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param network_role: Appliance role, ``1`` for Hub, ``0`` for spoke,
        ``2`` for mesh
    :type network_role: int
    :param site: Appliance site
    :type site: str
    :param site_priority: Site priority, needs further description
    :type site_priority: int
    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    data = {
        "id": ne_id,
        "networkRole": network_role,
        "site": site,
        "sitePriority": site_priority,
    }

    return self._post(
        "/appliance/networkRoleAndSite/{}".format(ne_id),
        data=data,
        return_type="bool",
    )
