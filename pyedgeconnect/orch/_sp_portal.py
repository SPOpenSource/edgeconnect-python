# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# spPortal : Silver Peak Portal related apis


def get_orchestrator_to_cloud_portal_status(
    self,
) -> dict:
    """Get current connectivity status between Orchestrator and Cloud
    Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/connectivity

    :return: Dictionary of status \n
        * keyword **portal** (`int`): integer representing status,
          ``0``: Unable to connect ``1``: Connected ``2``: Connecting
    :rtype: dict
    """
    return self._get("/spPortal/connectivity")


def get_cloud_portal_broadcast_message(self) -> dict:
    """Get broadcast message from Cloud Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/broadcastMessage

    :return: Dictionary of broadcast message details \n
        * keyword **resourceBase** (`str`): Path to base,
          e.g. ``/spPortal``
        * keyword **resourceKey** (`str`): Path to broadcast,
            e.g. ``/broadcastMessages``
        * keyword **configData** (`list[dict]`): list of dictonaries \n
            [`dict`]: config data object \n
                * keyword **_id**: No description in Swagger
                * keyword **message**: No description in Swagger
                * keyword **expireAfter**: No description in Swagger
                * keyword **createdOn**: No description in Swagger
                * keyword **modifiedOn**: No description in Swagger
        * keyword **version** (`int`): integer version number
        * keyword **timestamp** (`int`): integer timestamp in unix epoch
          in milliseconds
    :rtype: dict
    """
    return self._get("/spPortal/broadcastMessage")


def get_service_id_to_service_mapping(
    self,
    match_any: str = None,
    org: str = None,
    service_ids: str = None,
    top: int = None,
) -> dict:
    """Returns collection of service id to service details [serviceId,
    saasId, country, countryCode, org, saasAppName, displayName,
    priority] mapping.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/internetDb/serviceIdToSaasId

    If no filters are specified this returns top 100 results only
    because the data may be too large.

    :param match_any: Wildcard match on country, organization, or SaaS
        application name, defaults to None
    :type match_any: str, optional
    :param org: Wildcard match on organization, defaults to None
    :type org: str, optional
    :param service_ids: Filter on service identifiers, can include
        multiple service id's comma separated, defaults to None
    :type service_ids: str, optional
    :param top: Top number of results to return, defaults to None
    :type top: int, optional
    :return: Dictionary of service id to service details mapping \n
        * keyword **<service_id_number** (`list`): List of mappings \n
            * [0] (`str`): Service ID number
            * [1] (`str`): SaaS ID number
            * [2] (`str`): Country
            * [3] (`str`): Country code
            * [4] (`str`): Organization
            * [5] (`str`): SaaS application name
            * [6] (`str`): Display name
            * [7] (`str`): Priority number
    :rtype: dict
    """
    path = "/spPortal/internetDb/serviceIdToSaasId"

    if any(v is not None for v in [match_any, org, service_ids, top]):
        path = path + "?"

    if match_any is not None:
        path = path + "matchAny={}".format(match_any)
        if org is not None:
            path = path + "&org={}".format(org)
        if service_ids is not None:
            path = path + "&serviceIds={}".format(service_ids)
        if top is not None:
            path = path + "&top={}".format(top)
    elif org is not None:
        path = path + "org={}".format(org)
        if service_ids is not None:
            path = path + "&serviceIds={}".format(service_ids)
        if top is not None:
            path = path + "&top={}".format(top)
    elif service_ids is not None:
        path = path + "serviceIds={}".format(service_ids)
        if top is not None:
            path = path + "&top={}".format(top)
    elif top is not None:
        path = path + "top={}".format(top)
    else:
        pass

    return self._get(path)


def get_service_id_to_country_mapping(self) -> dict:
    """Get collection of service id to country details [serviceId,
    saasId, country, countryCode, org, saasAppName, displayName,
    priority] mapping.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/internetDb/serviceIdToSaasId/countries

    :return: Dictionary of countries, with nested list of attributes \n
        * keyword **<country_name>** (`list[str]`): Country name,
          underlying list of attributes \n
            * [0] (`str`): Service ID number
            * [1] (`str`): SaaS ID number
            * [2] (`str`): Country
            * [3] (`str`): Country code
            * [4] (`str`): Organization
            * [5] (`str`): SaaS application name
            * [6] (`str`): Display name
            * [7] (`str`): Priority number
    :rtype: dict
    """
    return self._get("/spPortal/internetDb/serviceIdToSaasId/countries")


def get_all_saas_apps(self) -> list:
    """Get list of unique SaaS applications in the internet services
    database

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/internetDb/serviceIdToSaasId/saasApps

    :return: List of Saas applications
    :rtype: list
    """
    return self._get("/spPortal/internetDb/serviceIdToSaasId/saasApps")


def get_count_of_saas_apps(self) -> dict:
    """Get count of internet services defined on Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/internetDb/serviceIdToSaasId/count

    :return: Dictionary containing count of SaaS applications \n
        * keyword **count** (`int`): Integer count
    :rtype: dict
    """
    return self._get("/spPortal/internetDb/serviceIdToSaasId/count")


def geo_locate_single_ip(
    self,
    ip_address: int,
) -> dict:
    """Get geo-location information on single ip address from Cloud
    Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/internetDb/geoLocateIp/{ip}

    :param ip_address: 32-bit integer ip address, e.g. ``167837953``
        rather than ``10.1.1.1``
    :type ip_address: str
    :return: Dictionary of ip address geo-location information \n
        * keyword **<ip_address>** (`int`): Nested dictionary of
          attributes \n
            * keyword **ip** (`int`): ip address of location calculated
            * keyword **rangeIpStart** (`int`): Start of subnet that
              geo-located IP falls under
            * keyword **rangeIpEnd** (`int`): End of subnet that
              geo-located IP falls under
            * keyword **isp** (`str`): ISP provider registered to
              address
            * keyword **org** (`str`): Organization registered to
              address
            * keyword **country** (`str`): Country
            * keyword **countryCode** (`str`): Country code
            * keyword **city** (`str`): City
            * keyword **postalCode** (`int`): Postal/Zip code
            * keyword **latitude** (`int`): Latitude coordinates of ip
              address
            * keyword **longitude** (`int`): Longitude coordinates of ip
              address
    :rtype: dict
    """
    return self._get("/spPortal/internetDb/geoLocateIp/{}".format(ip_address))


def geo_locate_multiple_ips(
    self,
    ip_address_list: list,
) -> dict:
    """Get geo-location information on multiple ip addresses from Cloud
    Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - POST
          - /spPortal/internetDb/geoLocateIp

    :param ip_address_list: List of 32-bit integer ip addresses,
        e.g. ``[167837953, 167837954, ...]``
    :type ip_address_list: list
    :return: Dictionary of ip address geo-location information for all
        ip's \n
        * keyword **<ip_address>** (`int`): Nested dictionary of
          attributes \n
            * keyword **ip** (`int`): ip address of location calculated
            * keyword **rangeIpStart** (`int`): Start of subnet that
              geo-located IP falls under
            * keyword **rangeIpEnd** (`int`): End of subnet that
              geo-located IP falls under
            * keyword **isp** (`str`): ISP provider registered to
              address
            * keyword **org** (`str`): Organization registered to
              address
            * keyword **country** (`str`): Country
            * keyword **countryCode** (`str`): Country code
            * keyword **city** (`str`): City
            * keyword **postalCode** (`int`): Postal/Zip code
            * keyword **latitude** (`int`): Latitude coordinates of ip
              address
            * keyword **longitude** (`int`): Longitude coordinates of ip
              address
    :rtype: dict
    """
    data = ip_address_list

    return self._post("/spPortal/internetDb/geoLocateIp", data=data)


def get_update_time_for_app_definitions(self) -> dict:
    """Get last update time for application definition data for Address
    Map from Cloud Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/internetDb/ipIntelligence/info

    :return: Dictionary containing update time \n
        * keyword **lastUpdateTime** (`str`): Last update time in unix
          epoch milliseconds
    :rtype: dict
    """
    return self._get("/spPortal/internetDb/ipIntelligence/info")


def get_app_definition_data(
    self,
    start: int,
    limit: int,
) -> list:
    """Get application definition data for Address Map from Cloud Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/internetDb/ipIntelligence

    :param start: Starting SaaS id to query from
    :type start: int
    :param limit: Limit number of returned values, maximum is 10,000
    :type limit: int, optional
    :return: List of dictionaries for IP intelligence data
    :rtype: list
    """
    return self._get(
        "/spPortal/internetDb/ipIntelligence?start={}&limit={}".format(
            start, limit
        )
    )


def get_app_definition_total(self) -> str:
    """Get count for application definition data for Address Map from
    Cloud Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/internetDb/ipIntelligence/total

    :return: Count of application definitions
    :rtype: str
    """
    return self._get(
        "/spPortal/internetDb/ipIntelligence/total", return_type="text"
    )


def search_app_definition_data(
    self,
    ip_address: int = None,
    data_filter: str = None,
) -> list:
    """Search application definition data for Address Map from Cloud
    Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/internetDb/ipIntelligence/search

    If provides a valid IPv4 address in 32-bit integer format, it will
    search through ip. Otherwise it will search by match filter
    [app name, description, country, organization].

    :param ip_address: 32-bit integer ip address,
        e.g. ``167837953`` rather than ``10.1.1.1``, defaults to None
    :type ip_address: int, optional
    :param data_filter: Filter on app name, description, country or
        organzation, defaults to None
    :type data_filter: str, optional
    :return: List of IP intelligence data with top 5000 results,
        otherwise data may be too large
    :rtype: list
    """
    path = "/spPortal/internetDb/ipIntelligence/search"

    if ip_address is not None or data_filter is not None:
        path = path + "?"
    if ip_address is not None:
        path = path + "ip={}".format(ip_address)
        if data_filter is not None:
            path = path + "&filter={}".format(data_filter)
    elif data_filter is not None:
        path = path + "filter={}".format(data_filter)
    else:
        pass

    return self._get(path)


def get_port_protocol_classification(self) -> dict:
    """Get application definition for IP Protocol, TCP Port, UDP Port
    from Cloud Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/portProtocolClassification

    :return: Returns nested dictionary with port/protocol details
    :rtype: dict
    """
    return self._get("/spPortal/portProtocolClassification")


def get_port_protocol_classification_hash(self) -> dict:
    """Get hash code for application data for IP Protocol, TCP Port,
    UDP port from Cloud Portal (used as version number)

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/portProtocolClassification/info

    :return: Returns dictionary with hash code \n
        * keyword **hashVal** (`str`): Hash code of classification
          information
    :rtype: dict
    """
    return self._get("/spPortal/portProtocolClassification/info")


def get_dns_classification(self) -> list:
    """Get application definition for DNS from Cloud Portal. This
    generates a lot of data and require longer response time.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/dnsClassification

    :return: Returns list of dictionaries with DNS details
    :rtype: dict
    """
    return self._get("/spPortal/dnsClassification")


def get_dns_classification_hash(self) -> dict:
    """Get hash code for application data for DNS from Cloud Portal
    (used as version number)

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/dnsClassification/info

    :return: Returns dictionary with hash code \n
        * keyword **hashVal** (`str`): Hash code of classification
          information
    :rtype: dict
    """
    return self._get("/spPortal/dnsClassification/info")


def get_flow_classification(self) -> dict:
    """Get application definition for meter flow from Cloud Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/meterFlowClassification

    :return: Returns dictionary per flow type with meter flow details
    :rtype: dict
    """
    return self._get("/spPortal/meterFlowClassification")


def get_flow_classification_hash(self) -> dict:
    """Get hash code for application data for meter flow from Cloud
    Portal (used as version number)

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/meterFlowClassification/info

    :return: Returns dictionary with hash code \n
        * keyword **hashVal** (`str`): Hash code of classification
          information
    :rtype: dict
    """
    return self._get("/spPortal/meterFlowClassification/info")


def get_compound_classification(self) -> dict:
    """Get application definition for compound applications from Cloud
    Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/compoundClassification

    :return: Returns dictionary per compound application details
    :rtype: dict
    """
    return self._get("/spPortal/compoundClassification")


def get_compound_classification_hash(self) -> dict:
    """Get hash code for application data for compound applications from
    Cloud Portal (used as version number)

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/compoundClassification/info

    :return: Returns dictionary with hash code \n
        * keyword **hashVal** (`str`): Hash code of classification
          information
    :rtype: dict
    """
    return self._get("/spPortal/compoundClassification/info")


def get_saas_classification(self) -> dict:
    """Get application definition for SaaS applications from Cloud
    Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/saasClassification

    :return: Returns dictionary per SaaS application details
    :rtype: dict
    """
    return self._get("/spPortal/saasClassification")


def get_saas_classification_hash(self) -> dict:
    """Get hash code for application data for SaaS applications from
    Cloud Portal (used as version number)

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/saasClassification/info

    :return: Returns dictionary with hash code \n
        * keyword **hashVal** (`str`): Hash code of classification
          information
    :rtype: dict
    """
    return self._get("/spPortal/saasClassification/info")


def get_app_groups(self) -> dict:
    """Get application definition for application groups from Cloud
    Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/applicationTags

    :return: Returns dictionary per application group details
    :rtype: dict
    """
    return self._get("/spPortal/applicationTags")


def get_app_groups_hash(self) -> dict:
    """Get hash code for application data for application groups from
    Cloud Portal (used as version number)

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/applicationTags/info

    :return: Returns dictionary with hash code \n
        * keyword **hashVal** (`str`): Hash code of classification
          information
    :rtype: dict
    """
    return self._get("/spPortal/applicationTags/info")


def get_traffic_behavior(self) -> dict:
    """Get traffic behavior configuration and names from Cloud Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/trafficBehavior

    :return: Returns dictionary for traffic behavior \n
        * keyword **TB_CONFIG** (`dict`): Dictionary of traffic behavior
          configuration
        * keyword **TB_NAME** (`list`): List of traffic behavior names
          e.g. ``["Voice", "Video conferencing", "Bulk data",...]``
    :rtype: dict
    """
    return self._get("/spPortal/trafficBehavior")


def get_traffic_behavior_hash(self) -> dict:
    """
    Get hash code for traffic behavior data from Cloud Portal (used as
    version number)

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/trafficBehavior/info

    :return: Returns dictionary with hash code \n
        * keyword **hashVal** (`str`): Hash code of classification
          information
    :rtype: dict
    """
    return self._get("/spPortal/trafficBehavior/info")


def get_portal_registration_status(self) -> dict:
    """Get current Orchestrator Cloud Portal registration status

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/registration

    :return: Returns dictionary for registration status details \n
        * keyword **emails** (`list[str]`): list of configured emails
        * keyword **site** (`str`): Site name, if assigned,
          ``unassigned`` if empty
        * keyword **accountName** (`str`): Account name
        * keyword **registered** (`bool`): ``True`` if currently
          registered
        * keyword **enabled** (`bool`): ``True`` if Orchestrator has
          registered with Cloud Portal and has been approved
        * keyword **accountKey** (`str`): Account Key
        * keyword **pendingPoll** (`bool`): ``True`` if pending on
          polling data
        * keyword **group** (`str`): Group name if assigned,
          ``unassigned`` if empty
    :rtype: dict
    """
    return self._get("/spPortal/registration")


def update_portal_registration_status(self) -> dict:
    """Use this API to reset the GMS-Portal registration state and
    initiate new Registration cycle with Cloud Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - POST
          - /spPortal/registration

    :return: Returns dictionary for registration status details \n
        * keyword **emails** (`list[str]`): list of configured emails
        * keyword **site** (`str`): Site name, if assigned,
          ``unassigned`` if empty
        * keyword **accountName** (`str`): Account name
        * keyword **registered** (`bool`): ``True`` if currently
          registered
        * keyword **enabled** (`bool`): ``True`` if Orchestrator has
          registered with Cloud Portal and has been approved
        * keyword **accountKey** (`str`): Account Key
        * keyword **pendingPoll** (`bool`): ``True`` if pending on
          polling data
        * keyword **group** (`str`): Group name if assigned,
          ``unassigned`` if empty
    :rtype: dict
    """
    return self._post("/spPortal/registration")


def get_portal_services_status(self) -> dict:
    """Debug API to view current status of all Cloud Portal related
    services

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/status

    :return: Returns nested dictionary for each service
    :rtype: dict
    """
    return self._get("/spPortal/status")


def get_portal_registration_config(self) -> dict:
    """Get Cloud Portal registration information

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/config

    :return: Returns dictionary of registration information
    :rtype: dict
    """
    return self._get("/spPortal/config")


def update_portal_registration_config(
    self,
    host: str = "",
    port: int = 0,
    account_id: str = "",
    account_name: str = "",
    account_key: str = "",
    old_account_key: str = "",
    group: str = "",
    site: str = "",
) -> dict:
    """Update Cloud Portal registration information

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - POST
          - /spPortal/config

    :param host: Hostname for cloud portal,
        e.g. ``portal.silverpeak.cloud``, defaults to ""
    :type host: str, optional
    :param port: Port to connect to cloud portal on, e.g. ``443``,
        defaults to 0
    :type port: int, optional
    :param account_id: Account ID string,
        e.g. ``5f347e4637f3de001a2a6e77``, defaults to ""
    :type account_id: str, optional
    :param account_name: Account name, defaults to ""
    :type account_name: str, optional
    :param account_key: Account key, defaults to ""
    :type account_key: str, optional
    :param old_account_key: Old account key, defaults to ""
    :type old_account_key: str, optional
    :param group: Group, can be ``unassigned``, defaults to ""
    :type group: str, optional
    :param site: Site, can be ``unassigned``, defaults to ""
    :type site: str, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "host": host,
        "port": port,
        "registration": {
            "accountId": account_id,
            "account": account_name,
            "key": account_key,
            "oldKey": old_account_key,
            "group": group,
            "site": site,
        },
    }

    return self._post(
        "/spPortal/config",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def get_portal_top_sites(self) -> list:
    """Get list of top internet sites

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/topSites

    :return: Returns list of top internet sites fetched from Cloud
        Portal
    :rtype: list
    """
    return self._get("/spPortal/topSites")


def get_tcp_udp_port_data(self) -> dict:
    """Get list of TCP, UDP ports and their applications

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/tcpUdpPorts

    :return: Returns dictionary of ports and their corresponding TCP and
        UDP applications, parent keys are port number \n
        * keyword **<port_number>** (`dict`): protocol info object \n
            * keyword **tcp** (`list[dict]`): tcp information \n
                [`dict`]: protocol information \n
                    * keyword **description** (`str`): port
                      description
                    * keyword **name** (`str`): port name
            * keyword **udp** (`list[dict]`): udp information \n
                [`dict`]: protocol information \n
                    * keyword **description** (`str`): port
                      description
                    * keyword **name** (`str`): port name
    :rtype: dict
    """
    return self._get("/spPortal/tcpUdpPorts")


def get_ip_protocol_numbers(self) -> list:
    """Get list of IP protocol numbers

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/ipProtocolNumbers

    :return: Returns list of dictionaries for each protocol number with
        name and description (keys are "number" "name" and
        "description") \n
        [`dict`]: IP protocol info object \n
            * keyword **description** (`str`): IP protocol description
            * keyword **name** (`str`): protocol name
            * keyword **number** (`int`): protocol number

    :rtype: list
    """
    return self._get("/spPortal/ipProtocolNumbers")


def get_appliance_orch_portal_status(
    self,
    ne_id: str,
) -> dict:
    """Return status of orchestrator > portal > appliance websocket and
    orchestrator > appliance websocket connections

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/applianceWSStatus/{neId}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :return: Returns dictionary of reachability status \n
        * keyword **portalWS** (`dict`): Portal websocket status \n
            * keyword **reachable** (`bool`): ``True`` if reachable
            * keyword **err** (`str`): String of error, if any
        * keyword **directWS** (`dict`): Orchestrator websocket status\n
            * keyword **reachable** (`bool`): ``True`` if reachable
            * keyword **err** (`str`): String of error, if any
    :rtype: dict
    """
    return self._get("/spPortal/applianceWSStatus/{}".format(ne_id))


def get_account_license_type(self) -> dict:
    """Get account license type from Cloud Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/account/license/type

    :return: Returns dictionary of license type information \n
        * keyword **name** (`str`): No description from Swagger
        * keyword **displayName** (`str`): No description from Swagger
    :rtype: dict
    """
    return self._get("/spPortal/account/license/type")


def get_account_license_feature(self) -> list:
    """Get account license feature from Cloud Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/account/license/feature

    :return: Returns list of a dictionary with name, displayName, and
        expire \n
        * keyword **name** (`str`): No description from Swagger
        * keyword **displayName** (`str`): No description from Swagger
        * keyword **expire** (`int`): Expiration date of license in unix
          epoch timestamp, milliseconds
    :rtype: list
    """
    return self._get("/spPortal/account/license/feature")


def get_account_license_ecsp_status(self) -> list:
    """Get Edge Connect license status from Cloud Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/account/license/appliance/ecsp/status

    :return: Returns list of dictionaries for licences, dates, accounts,
        boost, etc.
    :rtype: list
    """
    return self._get("/spPortal/account/license/appliance/ecsp/status")


def assign_account_license_ecsp(
    self,
    license_map: list,
) -> list:
    """Assign EC-SP licenses on Cloud Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - POST
          - /spPortal/account/license/appliance/ecsp/assign

    :param license_map: List of mapping dictionaries for license ID and
        appliance ID
        e.g. ``[{licenseId": "xxx", "applianceId": "77.NE"},...]`` \n
        [`dict`]: license/appliance mapping object \n
            * keyword **licenseId** (`str`): Portal mongo object id for
              the ecsp license
            * keyword **applianceId** (`str`): Portal mongo object id
              for the appliance
    :type license_map: list
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {"licenses": license_map}

    return self._post(
        "/spPortal/account/license/appliance/ecsp/assign",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def unassign_account_license_ecsp(
    self,
    licence_ids: list,
) -> list:
    """Uassign EC-SP licenses on Cloud Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - POST
          - /spPortal/account/license/appliance/ecsp/unassign

    :param licence_ids: List of license IDs to unnasign in dictionaries,
        e.g. ``[{licenseId": "xxx"},...]`` \n
        [`dict`]: license/appliance mapping object \n
            * keyword **licenseId** (`str`): Portal mongo object id for
              the ecsp license
    :type licence_ids: list
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {"licenses": licence_ids}

    return self._post(
        "/spPortal/account/license/appliance/ecsp/unassign",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def get_account_key_change_count(self) -> dict:
    """Get number of times account key has been changed.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/account/key/changeCount

    .. note::
        If never been changed, will return an HTTP 500 with no content.

    :return: Returns dictionary of account key changes \n
        * keyword **count** (`int`): Integer number of times account key
          has been changed
    :rtype: dict
    """
    return self._get("/spPortal/account/key/changeCount")


def get_account_key_change_status(
    self,
) -> dict:
    """Get current account key change status

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/account/key/changeStatus

    :return: Returns dictionary of account key change status \n
        * keyword **generateTimestamp** (`int`): Latest epoch time in
          milliseconds when new account key was generated. ``Null`` if
          account key has never been changed.
        * keyword **committedToPortalTimestamp** (`int`): Latest epoch
          time in milliseconds when old account key was delete from
          Portal. ``Null`` if current account key change has not been
          committed to Portal.
    :rtype: dict
    """
    return self._get("/spPortal/account/key/changeStatus")


def request_new_account_key(self) -> dict:
    """Request Cloud Portal to generate a new account key (requires
    connectivity to Cloud Portal)

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - PUT
          - /spPortal/account/key/generate")

    :return: Returns dictionary of new and old account key \n
        * keyword **accountKey** (`str`): New account key
        * keyword **oldAccountKey** (`str`): Previous account key
    :rtype: dict
    """
    return self._put("/spPortal/account/key/generate")


def delete_old_account_key(self) -> bool:
    """Delete old account key from Cloud Portal.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - DELETE
          - /spPortal/account/oldKey

    Acts as "commit" for a previous account key change. Make sure all
    managed appliances have the new account key before calling this.
    Requires Portal connectivity.

    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        "/spPortal/account/oldKey",
        expected_status=[204],
        return_type="bool",
    )


def create_case_with_portal(
    self,
    contact_name: str,
    contact_email: str,
    contact_phone: str,
    ne_pk: str,
    case_priority: str,
    case_subject: str,
    case_description: str,
) -> bool:
    """Create a case for the Orchestrator or an appliance.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - POST
          - /spPortal/createCaseWithPortal

    :param contact_name: Contact name for case
    :type contact_name: str
    :param contact_email: Contact email for case, if Orchestrator is not
        registered to Portal, a valid Silver Peak support account email
        address is required in order to create a case.
    :type contact_email: str
    :param contact_phone: Contact phone number for case,
        e.g. ``123-555-1234``
    :type contact_phone: str
    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param case_priority: Priority of case, accepted values:
        ``P1 - Urgent``, ``P2 - High``, ``P3 - Normal``, ``P4 - Low``
    :type case_priority: str
    :param case_subject: Title of case to be opened
    :type case_subject: str
    :param case_description: Longer description of case to be opened
    :type case_description: str
    :return: Returns True/False based on successful call
    :rtype: bool
    :raises ValueError: case_priority parameter must match one of the
        accepted values.
    """
    valid_priorities = [
        "P1 - Urgent",
        "P2 - High",
        "P3 - Normal",
        "P4 - Low",
    ]
    if case_priority not in valid_priorities:
        raise ValueError(
            """The case priority of {} is not valid.
            Must be one of the following...\n {}""".format(
                case_priority, valid_priorities
            )
        )

    data = {
        "caseName": contact_name,
        "caseEmail": contact_email,
        "casePhone": contact_phone,
        "orchSerialNum": ne_pk,
        "casePrio": case_priority,
        "caseSubject": case_subject,
        "caseDesc": case_description,
    }

    return self._post(
        "/spPortal/createCaseWithPortal",
        data=data,
    )
