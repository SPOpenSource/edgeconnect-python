# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# thirdPartyServices : Third Party Services Orchestration

# ZScaler - todo
# Check Point - todo
# Azure - todo
# AWS - todo
# Service Orchestration - todo
# Aruba Clearpass
def clearpass_get_configured_accounts(
    self,
) -> dict:
    """Get all ClearPass accounts with ID

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyServices
          - GET
          - /thirdPartyServices/clearpass/accounts

    :return: Returns dictionary of configured ClearPass Policy Manager
      accounts \n
        * keyword **<account_id>** (`dict`): CPPM account object id \n
            * keyword **name** (`str`): Configured name of CPPM in
              Orchestrator
            * keyword **domain** (`str`): IP or FQDN of CPPM
            * keyword **clientId** (`str`): Account ID to access CPPM
            * keyword **verifyCert** (`bool`): If Orchestrator is set to
              validate certificate of CPPM server
    :rtype: dict
    """
    return self._get("/thirdPartyServices/clearpass/accounts")


def clearpass_add_account(
    self,
    name: str,
    domain: str,
    client_id: str,
    access_key: str,
    verify_cert: bool,
) -> str:
    """Add new ClearPass Policy Manager account to Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyServices
          - POST
          - /thirdPartyServices/clearpass/accounts

    :param name: Name to identify CPPM in UI, must be a unique value
    :type name: str
    :param domain: IP address or FQDN of CPPM server to connect, must be
        a unique value
    :type domain: str
    :param client_id: Client ID to connect to CPPM with
    :type client_id: str
    :param access_key: Access key to authenticate connection to CPPM
    :type access_key: str
    :param verify_cert: ``True`` to have Orchestrator verify CPPM
        certificate, ``False`` to not verify
    :type verify_cert: bool
    :return: Returns empty response on success or error details of a
        failed attempt to add CPPM account
    :rtype: str
    """
    data = {
        "name": name,
        "domain": domain,
        "clientId": client_id,
        "accessKey": access_key,
        "verifyCert": verify_cert,
    }

    return self._post(
        "/thirdPartyServices/clearpass/accounts",
        data=data,
        expected_status=[204],
        return_type="text",
    )


def clearpass_get_configured_account(
    self,
    account_id: int,
) -> dict:
    """Get ClearPass Policy Manager account details using ID

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyServices
          - GET
          - /thirdPartyServices/clearpass/accounts/{id}

    :param account_id: Integer ID of configured CPPM account
    :type account_id: int
    :return: Returns dictionary of configured ClearPass Policy Manager
      account \n
        * keyword **name** (`str`): Configured name of CPPM in
          Orchestrator
        * keyword **domain** (`str`): IP or FQDN of CPPM
        * keyword **clientId** (`str`): Account ID to access CPPM
        * keyword **verifyCert** (`bool`): If Orchestrator is set to
          validate certificate of CPPM server
    :rtype: dict
    """
    return self._get(
        "/thirdPartyServices/clearpass/accounts/{}".format(account_id)
    )


def clearpass_update_account(
    self,
    name: str,
    domain: str,
    client_id: str,
    access_key: str,
    verify_cert: bool,
    account_id: int,
) -> str:
    """Update ClearPass Policy Manager account configuration.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyServices
          - PUT
          - /thirdPartyServices/clearpass/accounts{id}

    :param name: Name to identify CPPM in UI, must be a unique value
    :type name: str
    :param domain: IP address or FQDN of CPPM server to connect, must be
        a unique value
    :type domain: str
    :param client_id: Client ID to connect to CPPM with
    :type client_id: str
    :param access_key: Access key to authenticate connection to CPPM
    :type access_key: str
    :param verify_cert: ``True`` to have Orchestrator verify CPPM
        certificate, ``False`` to not verify
    :type verify_cert: bool
    :param account_id: Integer ID of configured CPPM account
    :type account_id: int
    :return: Returns empty response on success or error details of a
        failed attempt to add CPPM account
    :rtype: str
    """
    data = {
        "name": name,
        "domain": domain,
        "clientId": client_id,
        "accessKey": access_key,
        "verifyCert": verify_cert,
    }

    return self._put(
        "/thirdPartyServices/clearpass/accounts/{}".format(account_id),
        data=data,
        expected_status=[204],
        return_type="text",
    )


def clearpass_delete_account(
    self,
    account_id: int,
) -> str:
    """Delete ClearPass Policy Manager account configuration.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyServices
          - DELETE
          - /thirdPartyServices/clearpass/accounts{id}

    :param account_id: Integer ID of configured CPPM account
    :type account_id: int
    :return: Returns empty 204 response on success or error details of a
        failed attempt to add CPPM account
    :rtype: str
    """

    return self._delete(
        "/thirdPartyServices/clearpass/accounts/{}".format(account_id),
        expected_status=[204],
        return_type="text",
    )


def clearpass_get_configured_account_details(
    self,
    account_id: int,
) -> dict:
    """Get all ClearPass Policy Manager configuration

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyServices
          - GET
          - /thirdPartyServices/clearpass/configurations/{id}

    :param account_id: Integer ID of configured CPPM account
    :type account_id: int
    :return: Returns dictionary of configured ClearPass Policy Manager
      account configuration\n
        * keyword **id** (`int`): Account ID,
        * keyword **name** (`str`): Unique user defined name for the
          clearpass configuration
        * keyword **domain** (`str`): Azure VPN Site ID to which VPN
          Connection is established.
        * keyword **configData** (`str`): ClearPass Account details in a
          string-formatted dictionary
        * keyword **serviceInfo** (`str`): ClearPass service endpoint
          information in a string-formatted dictionary
        * keyword **status** (`int`): ClearPass account connection
          status, ``0`` disconnected, ``1`` connected
        * keyword **serviceStatus** (`int`): Not documented in Swagger
          , ``0`` disconnected, ``1`` connected
        * keyword **paused** (`bool`): Account pause status, ``True`` if
          paused, ``False`` if active
        * keyword **needService** (`bool`): boolean value to decide
          whether the account needs service, ``True`` if needs service,
          ``False`` if no service required
    :rtype: dict
    """
    return self._get(
        "/thirdPartyServices/clearpass/configurations/{}".format(account_id)
    )


def clearpass_pause_individual_orchestration(
    self,
    pause: bool,
    account_id: int,
) -> str:
    """Pause individual ClearPass Policy Manager orchestration.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyServices
          - PUT
          - /thirdPartyServices/clearpass/accounts/pause/{id}

    :param pause: Set pause status of Orchestration with CPPM, ``True``
        to pause, ``False`` to make active
    :type pause: bool
    :param account_id: Integer ID of configured CPPM account
    :type account_id: int
    :return: Returns ``1`` on successful call, otherwise provides error
        message if invalid ID
    :rtype: str
    """

    return self._put(
        "/thirdPartyServices/clearpass/accounts/pause/{}?isPaused={}".format(
            account_id, pause
        ),
        return_type="text",
    )


def clearpass_get_pause_orchestration_status(
    self,
) -> dict:
    """Get ClearPass Policy Manager pause orchestration status.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyServices
          - GET
          - /thirdPartyServices/clearpass/pauseOrchestration

    :return: Returns dictionary of ClearPass Policy Manager
      Orchestration pause status \n
        * keyword **paused** (`bool`): ``True`` if paused, ``False`` if
          active
    :rtype: dict
    """
    return self._get("/thirdPartyServices/clearpass/pauseOrchestration")


def clearpass_set_pause_orchestration_status(
    self,
    pause: bool,
) -> bool:
    """Set ClearPass Policy Manager pause orchestration status.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyServices
          - POST
          - /thirdPartyServices/clearpass/pauseOrchestration

    :param pause: ``True`` to pause orchestration, ``False`` to resume
    :type pause: bool
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {"paused": pause}
    return self._post(
        "/thirdPartyServices/clearpass/pauseOrchestration",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def clearpass_get_service_endpoint_status(
    self,
    account_id: int,
) -> dict:
    """Get ClearPass Policy Manager service endpoint status.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyServices
          - GET
          - /thirdPartyServices/clearpass/service/status/{id}

    :param account_id: Integer ID of configured CPPM account
    :type account_id: int
    :return: Returns dictionary of ClearPass Policy Manager service
      status \n
        * keyword **context_server** (`int`): ``1`` if active, ``0`` if
          failed
        * keyword **login_context_server_action** (`int`): ``1`` if
          active, ``0`` if failed
        * keyword **logout_context_server_action** (`int`): ``1`` if
          active, ``0`` if failed
    :rtype: dict
    """
    return self._get(
        "/thirdPartyServices/clearpass/service/status/{}".format(account_id)
    )


def clearpass_reset_service_endpoint(
    self,
    account_id: int,
    service: str,
) -> dict:
    """Reset ClearPass Policy Manager service endpoint.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyServices
          - PUT
          - /thirdPartyServices/clearpass/service/status/{id}

    :param account_id: Integer ID of configured CPPM account
    :type account_id: int
    :param service: Service to reset, accepted values are
      ``context_server``, ``login_context_server_action``, and
      ``logout_context_server_action``
    :type service: str
    :return: Returns dictionary of ClearPass Policy Manager service
      status \n
        * keyword **context_server** (`int`): ``1`` if active, ``0`` if
          failed
        * keyword **login_context_server_action** (`int`): ``1`` if
          active, ``0`` if failed
        * keyword **logout_context_server_action** (`int`): ``1`` if
          active, ``0`` if failed
    :rtype: dict
    """
    return self._put(
        "/thirdPartyServices/clearpass/service/status/{}?service={}".format(
            account_id, service
        )
    )


def clearpass_get_connectivity(
    self,
    account_id: int,
) -> dict:
    """Get ClearPass Policy Manager account connectivity status

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyServices
          - GET
          - /thirdPartyServices/clearpass/connectivity/{id}

    :param account_id: Integer ID of configured CPPM account
    :type account_id: int
    :return: Returns dictionary of ClearPass Policy Manager connectivity
      status \n
        * keyword **connectivity** (`str`): The connectivity status to
          ClearPass Policy Manager: ``0`` - Not Connected, ``1`` -
          Connected, ``2`` - Auth Failed, ``3``- Unreachable
    :rtype: dict
    """
    return self._get(
        "/thirdPartyServices/clearpass/connectivity/{}".format(account_id)
    )


def clearpass_post_login_event(
    self,
    timestamp: str = "",
    event_type: str = "",
    ip_address: str = "",
    cppm_domain: str = "",
    username: str = "",
    device_os: str = "",
    roles: str = "",
    ssid: str = "",
    auth_protocol: str = "",
    posture: str = "",
    mac: str = "",
    location_id: str = "",
    other_info: str = "",
) -> bool:
    """Posts ClearPass Policy Manager login event

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyServices
          - POST
          - /thirdPartyServices/clearpass/event/login

    :param timestamp: ClearPass policy manager event timestamp.
      Timestamp format : yyyy-MM-dd HH:mm:ss
    :type timestamp: str
    :param event_type: Event type (login/logout)
    :type event_type: str
    :param ip_address: Client's IP address
    :type ip_address: str
    :param cppm_domain: ClearPass Policy Manager's domain IP
    :type cppm_domain: str
    :param username: client's username
    :type username: str
    :param device_os: Identified device OS
    :type device_os: str
    :param roles: User roles
    :type roles: str
    :param ssid: Device's SSID
    :type ssid: str
    :param auth_protocol: Authentication protocol type
    :type auth_protocol: str
    :param posture: device health info
    :type posture: str
    :param mac: Client's mac address
    :type mac: str
    :param location_id: Access point's location ID
    :type location_id: str
    :param other_info: Unmatched extra info in JSON format
    :type other_info: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "timestamp": timestamp,
        "eventType": event_type,
        "ipAddress": ip_address,
        "cppmDomain": cppm_domain,
        "username": username,
        "deviceOS": device_os,
        "roles": roles,
        "ssid": ssid,
        "authProtocol": auth_protocol,
        "posture": posture,
        "mac": mac,
        "locationId": location_id,
        "otherInfo": other_info,
    }

    return self._post(
        "/thirdPartyServices/clearpass/event/login",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def clearpass_post_logout_event(
    self,
    timestamp: str = "",
    event_type: str = "",
    ip_address: str = "",
    cppm_domain: str = "",
    username: str = "",
    device_os: str = "",
    roles: str = "",
    ssid: str = "",
    auth_protocol: str = "",
    posture: str = "",
    mac: str = "",
    location_id: str = "",
    other_info: str = "",
) -> bool:
    """Posts ClearPass Policy Manager logout event

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyServices
          - POST
          - /thirdPartyServices/clearpass/event/logout

    :param timestamp: ClearPass policy manager event timestamp
    :type timestamp: str
    :param event_type: Event type (login/logout)
    :type event_type: str
    :param ip_address: Client's IP address
    :type ip_address: str
    :param cppm_domain: ClearPass Policy Manager's domain IP
    :type cppm_domain: str
    :param username: client's username
    :type username: str
    :param device_os: Identified device OS
    :type device_os: str
    :param roles: User roles
    :type roles: str
    :param ssid: Device's SSID
    :type ssid: str
    :param auth_protocol: Authentication protocol type
    :type auth_protocol: str
    :param posture: device health info
    :type posture: str
    :param mac: Client's mac address
    :type mac: str
    :param location_id: Access point's location ID
    :type location_id: str
    :param other_info: Unmatched extra info in JSON format
    :type other_info: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "timestamp": timestamp,
        "eventType": event_type,
        "ipAddress": ip_address,
        "cppmDomain": cppm_domain,
        "username": username,
        "deviceOS": device_os,
        "roles": roles,
        "ssid": ssid,
        "authProtocol": auth_protocol,
        "posture": posture,
        "mac": mac,
        "locationId": location_id,
        "otherInfo": other_info,
    }

    return self._post(
        "/thirdPartyServices/clearpass/event/logout",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def clearpass_filter_events(
    self,
    start_time: int,
    end_time: int,
    ip_address: str = None,
    username: str = None,
    limit: int = 10000,
    event_type: str = None,
) -> list:
    """Filter ClearPass Policy Manager events

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyServices
          - GET
          - /thirdPartyServices/clearpass/events/filter

    :param start_time: Long(Signed 64 bits) value of milliseconds since
      EPOCH time indicating the starting time boundary of data time
      range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of milliseconds since
      EPOCH time indicating the ending time boundary of data time range
    :type end_time: int
    :param ip_address: IP address to filter for, e.g. ``10.1.1.100``,
      defaults to None
    :type ip_address: str, optional
    :param username: Username to filter for, defaults to None
    :type username: str, optional
    :param limit: Limit number of returned results, defaults to
      ``10000``
    :type limit: int, optional
    :param event_type: Event filter type. Please specify one of these
      values ``All``, ``Active``, ``Historical``, defaults to None
    :type event_type: str, optional
    :return: Returns list of ClearPass Policy Manager events \n
        [`dict`]: ClearPass event object \n
            * keyword **timestamp** (`str`): ClearPass policy manager
              event timestamp
            * keyword **eventType** (`str`): Event type (login/logout)
            * keyword **ipAddress** (`str`): Client's IP address
            * keyword **cppmDomain** (`str`): ClearPass Policy Manager's
              domain IP
            * keyword **username** (`str`): client's username
            * keyword **deviceOS** (`str`): Identified device OS
            * keyword **roles** (`str`): User roles
            * keyword **ssid** (`str`): Device's SSID
            * keyword **authProtocol** (`str`): Authentication protocol
              type
            * keyword **posture** (`str`): device health info
            * keyword **mac** (`str`): Client's mac address
            * keyword **locationId** (`str`): Access point's location ID
            * keyword **otherInfo** (`str`): Unmatched extra info in
              JSON format
    :rtype: list
    """
    path = (
        "/thirdPartyServices/clearpass/events/filter?startTime="
        + "{}&endTime={}".format(start_time, end_time)
    )

    if ip_address is not None:
        path = path + "&ip={}".format(ip_address)
    if username is not None:
        path = path + "&username={}".format(username)

    path = path + "&limit={}".format(limit)

    if event_type is not None:
        path = path + "&type={}".format(event_type)

    return self._get(path)


def clearpass_get_user_roles_for_ip(
    self,
    ip_address: str,
    start_time: int = None,
    end_time: int = None,
) -> dict:
    """Get username and role list for given IP and time range

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyServices
          - GET
          - /thirdPartyServices/clearpass/events/filter/userinfo/{ip}

    :param ip_address: IP address to filter for, e.g. ``10.1.1.100``
    :type ip_address: str
    :param start_time: Long(Signed 64 bits) value of milliseconds since
      EPOCH time indicating the starting time boundary of data time
      range, defaults to None
    :type start_time: int, optional
    :param end_time: Long(Signed 64 bits) value of milliseconds since
      EPOCH time indicating the ending time boundary of data time range,
      defaults to None
    :type end_time: int, optional
    :return: Returns dictionary of usernames and roles matching a given
      IP address within the specified time range \n
        * keyword **roles** (`list[str]`): list of roles
        * keyword **usernames** (`list[str]`): list of usernames
    :rtype: dict
    """
    path = "/thirdPartyServices/clearpass/events/filter/userinfo/{}".format(
        ip_address
    )

    if start_time is not None:
        path = path + "&startTime={}".format(start_time)
    if end_time is not None:
        path = path + "&endTime={}".format(end_time)

    return self._get(path)


# Aruba Central
def central_get_subscription(
    self,
) -> dict:
    """Returns Aruba Central subscription

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyServices
          - GET
          - /thirdPartyServices/arubaCentral/subscription

    :return: Returns dictionary of aruba central subscription
      information \n
        * keyword **customerId** (`str`): The Customer ID of Aruba
          Central
        * keyword **username** (`str`): The username of Aruba Central
        * keyword **password** (`str`, optional): The password of Aruba
          Central
        * keyword **clientId** (`str`): clientId to use for Orchestrator
          mapping
        * keyword **clientSecret** (`str`): clientSecret to use for
          Orchestrator mapping
        * keyword **domain** (`str`): Domain to use for Orchestrator
          mapping
    :rtype: dict
    """
    return self._get("/thirdPartyServices/arubaCentral/subscription")


def central_add_subscription(
    self,
    customer_id: str,
    username: str,
    password: str,
    client_id: str,
    client_secret: str,
    domain: str,
) -> bool:
    """Add/Update Aruba Central subscription

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyServices
          - POST
          - /thirdPartyServices/arubaCentral/subscription

    :param customer_id: The Customer ID of Aruba Central
    :type customer_id: str
    :param username: The username of Aruba Central
    :type username: str
    :param password: The password of Aruba Central
    :type password: str
    :param client_id: clientId to use for Orchestrator mapping
    :type client_id: str
    :param client_secret: clientSecret to use for Orchestrator mapping
    :type client_secret: str
    :param domain: Domain to use for Orchestrator
    :type domain: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "customerId": customer_id,
        "username": username,
        "password": password,
        "clientId": client_id,
        "clientSecret": client_secret,
        "domain": domain,
    }

    return self._post(
        "/thirdPartyServices/arubaCentral/subscription",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def central_delete_subscription(
    self,
) -> bool:
    """Delete Aruba Central subscription

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyServices
          - DELETE
          - /thirdPartyServices/arubaCentral/subscription

    :return: Returns True/False based on successful call
    :rtype: bool
    """

    return self._delete(
        "/thirdPartyServices/arubaCentral/subscription",
        expected_status=[204],
        return_type="bool",
    )


def central_get_site_mapping(
    self,
) -> list:
    """Get Aruba Central site and appliances mapping

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyServices
          - GET
          - /thirdPartyServices/arubaCentral/sitesMapping

    :return: Returns list of dictionaries with site mapping
      to Edge Connect appliance relationships \n
        * [`dict`]: List of site to appliance relationship objects \n
          * keyword <site_id_#> (`list[dict]`): Key is Site ID string
            integer, list of appliance object dictionaries related to
            site \n
            * keyword **nePk** (`str`): Appliance ID
            * keyword **applianceName** (`str`): Appliance hostname
            * keyword **recommendSite** (`str`): Recommended site ID
            * keyword **gmsMarked** (`bool`): ``True`` if set by
              Orchestrator
    :rtype: List
    """

    return self._get("/thirdPartyServices/arubaCentral/sitesMapping")


def central_assign_appliance_to_site(
    self,
    ne_pk: str,
    origin_site: str = None,
    new_site: str = None,
) -> bool:
    """Manually assign appliance to the aruba central site

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyServices
          - POST
          - /thirdPartyServices/arubaCentral/sitesMapping/{nePk}


    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param origin_site: Aruba Central site ID appliance originally
      associated to, defaults to None
    :type origin_site: str, optional
    :param new_site: New Aruba Central site ID to associate appliance
      to, defaults to None
    :type new_site: str, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "origin": origin_site,
        "siteId": new_site,
    }

    return self._post(
        "/thirdPartyServices/arubaCentral/sitesMapping/{}".format(ne_pk),
        data=data,
        expected_status=[204],
        return_type="bool",
    )
