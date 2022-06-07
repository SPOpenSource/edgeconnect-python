# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# appliance : Add, delete and modify appliances
from __future__ import annotations


def get_appliances(self) -> list:
    """Get all appliances from Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliance
          - GET
          - /appliance

    :return: Returns list of dictionaries of each appliance
    :rtype: list
    """
    return self._get("/appliance")


def delete_appliance(
    self,
    ne_pk: str,
) -> bool:
    """Delete an appliance from Orchestrator. **IMPORTANT** - In
    addition to removing from Orchestrator, this will remove account/key
    and Orchestrator information on appliance.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliance
          - DELETE
          - /appliance/{nePk}

    :param ne_pk: Network Primary Key (nePk) of existing appliance,
        e.g. ``3.NE``
    :type ne_pk: str
    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    valid = ".NE"
    if valid not in ne_pk:
        raise ValueError(
            "nePk must be in format '0.NE', but %r was provided" % ne_pk
        )

    return self._delete(
        "/appliance/{}".format(ne_pk),
        expected_status=[204],
        return_type="bool",
    )


def get_appliances_queued_for_deletion(self) -> dict:
    """Get all appliances queued for deletion from Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliance
          - GET
          - /appliance/queuedForDeletion

    :return: Returns list of dictionaries of each appliance queued for
        deletion
    :rtype: list
    """
    return self._get("/appliance/queuedForDeletion")


def delete_appliance_for_rediscovery(
    self,
    ne_pk: str,
) -> bool:
    """Delete an appliance from Orchestrator for rediscovery

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliance
          - DELETE
          - /appliance/deleteForDiscovery/{nePk}

    :param ne_pk: Network Primary Key (nePk) of existing appliance,
        e.g. ``3.NE``
    :type ne_pk: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    valid = ".NE"
    if valid not in ne_pk:
        raise ValueError(
            "nePk must be in format '0.NE', but %r was provided" % ne_pk
        )

    return self._delete(
        "/appliance/deleteForDiscovery/{}".format(ne_pk),
        expected_status=[204],
        return_type="bool",
    )


def modify_appliance(
    self,
    ne_pk: str,
    username: str,
    password: str,
    ip: str,
    web_protocol_type: int,
    network_role: str,
) -> bool:
    """Modify an appliance's IP address, username, password,
    network Role, and webProtocol

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliance
          - POST
          - /appliance/{nePk}

    :param ne_pk: Network Primary Key (nePk) of existing appliance,
        e.g. ``3.NE``
    :type ne_pk: str
    :param username: The username for logging on to this appliance.
    :type username: str
    :param password: The password for logging on to this appliance.
    :type password: str
    :param ip: The ip address of the appliance.
    :type ip: str
    :param web_protocol_type: Protocol used by Orchestrator to talk to
        appliance. Http = ``1``, Https = ``2``, Both = ``3``,
    :type web_protocol_type: int
    :param network_role: The network role the appliance is configured in
        Orchestrator. spoke = ``0``, hub = ``1``, mesh = ``2``
    :type network_role: str
    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    data = {
        "userName": username,
        "password": password,
        "IP": ip,
        "webProtocolType": web_protocol_type,
        "networkRole": network_role,
    }

    return self._post(
        "/appliance/{}".format(ne_pk),
        data=data,
        return_type="bool",
    )


def change_appliance_group(
    self,
    group_pk: str,
    ne_pk_list: list[str],
) -> bool:
    """Modify an appliance's group membership. To get primary key of
    Orchestrator group, use
    :func:`~pyedgeconnect.Orchestrator.get_gms_groups`

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliance
          - POST
          - /appliance/changeGroup/{groupPk}

    :param group_pk: The appliance group identifier, e.g. "4.Network"
    :type group_pk: str
    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    return self._post(
        "/appliance/changeGroup/{}".format(group_pk),
        data={
            "ids": ne_pk_list,
        },
        return_type="bool",
    )


def get_appliance_info(
    self,
    ne_pk: str,
) -> dict:
    """Get appliance information

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliance
          - GET
          - /appliance/{nePk}

    :param ne_pk: Network Primary Key (nePk) of existing appliance,
        e.g. ``3.NE``
    :type ne_pk: str
    :return: Returns dictionary of appliance information \n
        * keyword **id** (`str`): This is the primary key of the
          appliance. Every appliance managed by Orchestrator is given a
          primary key and it uniquely identifies an appliance among all
          appliances managed by Orchestrator
        * keyword **uuid** (`str`): This is also an unique identifier.
          It is generated and self assigned by the appliance itself.
        * keyword **networkRole** (`str`): The network role the
          appliance is configured in Orchestrator. spoke = ``0``,
          hub = ``1``, mesh = ``2``
        * keyword **site** (`str`): An identifier used to tag an
          appliance with a site name
        * keyword **sitePriority** (`int`): Priority given to the
          appliance with the site it belongs to
        * keyword **userName** (`str`): User name used to login to
          appliance
        * keyword **password** (`str`): Password used to login to
          appliance. They are not returned for security reasons
        * keyword **groupId** (`str`): Primary key identifier of the
          Orchestrator group the appliance belongs to
        * keyword **IP** (`str`): IP Address of the appliance
        * keyword **webProtocolType** (`int`): Protocol used by
          Orchestrator to talk to appliance. Http = ``1``,
          Https = ``2``, Both = 3
        * keyword **serial** (`str`): Serial number of the appliance
        * keyword **hasUnsavedChanges** (`bool`): If ``True``, there are
          unsaved changes on the appliance
        * keyword **rebootRequired** (`bool`): If ``True``, the
          applianceappliance requires areboot
        * keyword **model** (`str`): Appliance model. Eg: EC-XS
        * keyword **hardwareRevision** (`str`): Hardware revision of the
          appliance. e.g. ``200193-004 Rev A``
        * keyword **hostName** (`str`): Appliance hostname
        * keyword **applianceId** (`str`): This is yet another
          identifier of the appliance. But it is mainly used by the
          appliance to identify its peer
        * keyword **mode** (`str`): Deployment mode the appliance is
          configured in
        * keyword **bypass** (`bool`): If ``True``, appliance is
          currently in bypass
        * keyword **softwareVersion** (`str`): Software version running
          on the appliance
        * keyword **startupTime** (`int`): No description in Swagger
        * keyword **webProtocol** (`str`): String version of the
          protocol field. Possible values are ``BOTH``, ``HTTP``, and
          ``HTTPS``
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
        * keyword **ip** (`str`): Same as IP field
        * keyword **nePk** (`str`): same as ID field
        * keyword **zoneList** (`dict`): dictionary of list of zones
          being used by appliance \n
            * keyword **zones** (`list[str]`): list of zones
        * keyword **interfaceList** (`dict`): dictionary of list of
          interface labels being used by appliance \n
            * keyword **interfaceLabels** (`list[str]`): list of
              interface numbers
        * keyword **tagsList** (`list`): No description in Swagger
    :rtype: dict
    :raises ValueError: Checks format of provided NePK value containing
        ".NE"
    """
    valid = ".NE"
    if valid not in ne_pk:
        raise ValueError(
            "nePk must be in format '0.NE', but %r was provided" % ne_pk
        )

    return self._get("/appliance/{}".format(ne_pk))


def get_all_discovered(self) -> list:
    """Get all appliances currently discovered

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliance
          - GET
          - /appliance/discovered

    :return: Returns discovered appliances
    :rtype: list
    """
    return self._get("/appliance/discovered")


def get_all_approved(self) -> list:
    """Get all appliances currently approved

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliance
          - GET
          - /appliance/approved

    :return: Returns approved appliances
    :rtype: list
    """
    return self._get("/appliance/discovered")


def get_all_denied_appliances(self) -> list:
    """Get all appliances currently denied

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliance
          - GET
          - /appliance/denied

    :return: Returns denied appliances
    :rtype: list
    """
    return self._get("/appliance/denied")


def delete_denied_appliances(
    self,
    appliances: list[str],
) -> bool:
    """This API is to permanently delete denied appliances. The portal
    object ID can be found from
    :func:`~pyedgeconnect.Orchestrator.get_all_denied_appliances`

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliance
          - POST
          - /appliance/denied/delete

    :param appliances: List of strings of appliance portal object id's
      to permanently delete, e.g. ``["6193c766026ea2b776b038ac",...]``
    :type appliances: list[str]
    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    data = {"portalObjectIds": appliances}

    return self._post(
        "/appliance/denied/delete",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def add_and_approve_discovered_appliances(
    self,
    id_key: int,
    group_pk: str,
    longitude: float = 0,
    latitude: float = 0,
) -> bool:
    """Add and approve discovered appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliance
          - POST
          - /appliance/discovered/approve/{key}

    :param id_key: ID of appliance to be approved, e.g. ``10``
    :type id_key: int
    :param group_pk: The appliance group identifier, e.g. ``4.Network``
    :type group_pk: str
    :param latitude: the latitude of the appliance's address,
        defaults to 0
    :type latitude: float, optional
    :param longitude: the longitude of the appliance's address,
        defaults to 0
    :type longitude: float, optional
    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    data = {"id": group_pk, "latitude": longitude, "longitude": latitude}

    return self._post(
        "/appliance/discovered/approve/{}".format(id_key),
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def add_discovered_appliances(
    self,
    id_key: int,
    group_pk: str,
    longitude: float = 0,
    latitude: float = 0,
) -> bool:
    """Add discovered appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliance
          - POST
          - /appliance/discovered/add/{key}

    :param id_key: ID of appliance to be approved, e.g. ``10``
    :type id_key: int
    :param group_pk: The appliance group identifier, e.g. ``4.Network``
    :type group_pk: str
    :param latitude: the latitude of the appliance's address,
        defaults to 0
    :type latitude: float, optional
    :param longitude: the longitude of the appliance's address,
        defaults to 0
    :type longitude: float, optional
    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    data = {"id": group_pk, "latitude": longitude, "longitude": latitude}

    return self._post(
        "/appliance/discovered/add/{}".format(id_key),
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def deny_appliance(
    self,
    id_key: int,
) -> bool:
    """Deny discovered appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliance
          - POST
          - /appliance/discovered/deny/{id}

    :param id_key: ID of appliance to be approved, e.g. ``10``
    :type id_key: int
    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    return self._post(
        "/appliance/discovered/deny/{}".format(id_key),
        expected_status=[204],
        return_type="bool",
    )


def update_discovered_appliances(self) -> bool:
    """Trigger discovered appliances update

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliance
          - PUT
          - /appliance/discovered/update

    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    return self._put(
        "/appliance/discovered/update",
        expected_status=[204],
        return_type="bool",
    )


def rediscover_denied_appliance(
    self,
    id_key: int,
) -> bool:
    """Discover denied appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliance
          - POST
          - /appliance/rediscoverAppliance/{id}

    :param ne_pk: Network Primary Key (nePk) of existing appliance,
        e.g. ``3.NE``
    :type ne_pk: str
    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    return self._post(
        "/appliance/rediscoverAppliance/{}".format(id_key),
        return_type="bool",
    )


def change_appliance_credentials(
    self,
    ne_pk: str,
    username: str,
    password: str,
) -> bool:
    """Update appliance access credentials

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliance
          - POST
          - /appliance/changePassword/{nePk}/{username}

    :param ne_pk: Network Primary Key (nePk) of existing appliance,
        e.g. ``3.NE``
    :type ne_pk: str
    :param username: The username for logging on to this appliance.
    :type username: str
    :param password: The password for logging on to this appliance.
    :type password: str
    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    return self._post(
        "/appliance/changePassword/{}/{}".format(ne_pk, username),
        data={"password": password},
        expected_status=[204],
        return_type="bool",
    )


def appliance_get_api(
    self,
    ne_pk: str,
    url: str,
) -> dict:
    """Pass along a GET API call to an appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliance
          - GET
          - /appliance/rest/{nePk}/{url : (.*)}

    :param ne_pk: Network Primary Key (nePk) of existing appliance,
        e.g. ``3.NE``
    :type ne_pk: str
    :param url: The API url call to pass to the appliance. This should
        be the path after 'rest/json/' of the appliance API call.
    :type url: str
    :return: Returns response of appliance GET API call
    :rtype: dict
    """
    return self._get("/appliance/rest/{}/{}".format(ne_pk, url))


def appliance_post_api(
    self,
    ne_pk: str,
    url: str,
    data,
) -> dict:
    """Pass along a POST API call to an appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliance
          - POST
          - /appliance/rest/{nePk}/{url : (.*)}

    :param ne_pk: Network Primary Key (nePk) of existing appliance,
        e.g. ``3.NE``
    :type ne_pk: str
    :param url: The API url call to pass to the appliance. This should
        be the path after 'rest/json/' of the appliance API call.
    :type url: str
    :param data: The data to pass in body of call. Can be a ``list`` or
      ``dict``
    :type data: list or dict
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/appliance/rest/{}/{}".format(ne_pk, url),
        data=data,
        expected_status=[200, 204],
        return_type="bool",
    )


def appliance_delete_api(
    self,
    ne_pk: str,
    url: str,
) -> dict:
    """Pass along a POST API call to an appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliance
          - DELETE
          - /appliance/rest/{nePk}/{url : (.*)}

    :param ne_pk: Network Primary Key (nePk) of existing appliance,
        e.g. ``3.NE``
    :type ne_pk: str
    :param url: The API url call to pass to the appliance. This should
        be the path after 'rest/json/' of the appliance API call.
    :type url: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        "/appliance/rest/{}/{}".format(ne_pk, url),
        expected_status=[200, 204],
        return_type="bool",
    )


def get_appliance_stats_config(self) -> dict:
    """Get appliance statistics configuration

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliance
          - GET
          - /appliance/statsConfig

    :return: Returns dictionary of appliance stats configuration
    :rtype: dict
    """
    return self._get("/appliance/statsConfig")


def modify_appliance_stats_config(
    self,
    vertical_retention: int,
    minute_retention: int,
    app: dict,
    port: dict,
    dns: dict,
    ip: dict,
    flows_csv_enable: bool,
) -> bool:
    """Update appliance stats configuration to be synchronized to
    appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliance
          - POST
          - /appliance/statsConfig

    :param vertical_retention: The setting of how many days of vertical
        stats this appliance will keep,
    :type vertical_retention: int
    :param minute_retention: The setting of how many minutes of minute
        stats this appliance will keep,
    :type minute_retention: int
    :param app: Dictionary with two k/v pairs \n
        * keyword **max_items** (`int`): ``-1`` indicates that appliance
          controls the number of entries.
        * keyword **evict_enable** (`bool`): No description in Swagger
    :type app: dict
    :param port: Dictionary with two k/v pairs \n
        * keyword **max_items** (`int`): ``-1`` indicates that appliance
          controls the number of entries.
        * keyword **evict_enable** (`bool`): No description in Swagger
    :type port: dict
    :param dns: Dictionary with two k/v pairs \n
        * keyword **max_items** (`int`): ``-1`` indicates that appliance
          controls the number of entries.
        * keyword **evict_enable** (`bool`): No description in Swagger
    :type dns: dict
    :param ip: Dictionary with two k/v pairs \n
        * keyword **max_items** (`int`): ``-1`` indicates that appliance
          controls the number of entries.
        * keyword **evict_enable** (`bool`): No description in Swagger
    :type ip: dict
    :param flows_csv_enable: No description in Swagger
    :type flows_csv_enable: bool
    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    data = {
        "verticalRetention": vertical_retention,
        "minuteRetention": minute_retention,
        "app": {
            "max_items": app["max_items"],
            "evict_enable": app["evict_enable"],
        },
        "port": {
            "max_items": port["max_items"],
            "evict_enable": port["evict_enable"],
        },
        "dns": {
            "max_items": dns["max_items"],
            "evict_enable": dns["evict_enable"],
        },
        "ip": {
            "max_items": ip["max_items"],
            "evict_enable": ip["evict_enable"],
        },
        "flows_csv_enable": flows_csv_enable,
    }

    return self._post(
        "/appliance/statsConfig",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def default_appliance_stats_config(self) -> dict:
    """Get default values for appliance statistics configuration

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliance
          - GET
          - /appliance/statsConfig/default

    :return: Returns dictionary of appliance stats configuration
    :rtype: dict
    """
    return self._get("/appliance/statsConfig/default")


def get_appliance_dns_cache_config(
    self,
    ne_pk: str,
    cached: bool,
) -> dict:
    """Get appliance DNS Cache configuration

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliance
          - GET
          - /appliance/dnsCache/config/{neId}?cached={cached}

    :return: Returns dictionary of DNS cache configuration
    :rtype: dict
    """
    valid = ".NE"
    if valid not in ne_pk:
        raise ValueError(
            "nePk must be in format '0.NE', but %r was provided" % ne_pk
        )

    return self._get(
        "/appliance/dnsCache/config/{}?cached={}".format(ne_pk, cached)
    )
