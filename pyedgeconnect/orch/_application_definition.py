# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# applicationDefinition : Application Definition


def get_user_defined_app_port_protocol(self) -> dict:
    """Retrieve user-defined application port and protocol
    classification (IP/TCP/UDP)

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applicationDefinition
          - GET
          - /applicationDefinition/portProtocolClassification

    :return: Returns user-defined application port and protocol
        classification
    :rtype: dict
    """

    return self._get(
        "/applicationDefinition/portProtocolClassification?resourceKey"
        + "=userDefined"
    )


def update_user_defined_app_port_protocol(
    self,
    port: int,
    protocol: int,
    name: str,
    priority: int,
    disabled: bool,
    description: str = "",
) -> bool:
    """
    Create or modify a user-defined application for IP port and protocol

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applicationDefinition
          - POST
          - /applicationDefinition/portProtocolClassification/{port}/{protocol}

    :param port: IP port, e.g. ``8089``
    :type port: int
    :param protocol: IP = ``0``, TCP = ``6``, UDP = ``17``
    :type protocol: int
    :param name: Identifying name of the domain, can also re-use the
        domain. Maximum of 31 characters.
    :type name: str
    :param priority: Confidence metric for classification, e.g. ``95``
    :type priority: int
    :param disabled: ``False`` is if classification is active and
        ``True`` if disabled
    :type disabled: bool
    :param description: Description of the classification,
        defaults to ""
    :type description: str, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """  # noqa: W505
    data = {
        "port": port,
        "protocol": protocol,
        "name": name,
        "description": description,
        "priority": priority,
        "disabled": disabled,
    }

    return self._post(
        "/applicationDefinition/portProtocolClassification/{}/{}".format(
            port, protocol
        ),
        data=data,
        return_type="bool",
    )


def delete_user_defined_app_port_protocol(
    self,
    port: int,
    protocol: int,
) -> bool:
    """Delete a user-defined application for IP port and protocol

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applicationDefinition
          - DELETE
          - /applicationDefinition/portProtocolClassification/{port}/{protocol}

    :param port: IP port, e.g. ``8089``
    :type port: int
    :param protocol: IP = ``0``, TCP = ``6``, UDP = ``17``
    :type protocol: int
    :return: Returns True/False based on successful call
    :rtype: bool
    """  # noqa: W505
    return self._delete(
        "/applicationDefinition/portProtocolClassification/{}/{}".format(
            port, protocol
        ),
        return_type="bool",
    )


def get_user_defined_app_dns_classification(self) -> list:
    """Retrieve user defined application dns classification

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applicationDefinition
          - GET
          - /applicationDefinition/dnsClassification

    :return: Returns list of dictionaries for user defined application
        dns classifications \n
        [`dict`]: DNS application object \n
            * keyword **domain** (`str`): Domain to match against,
              e.g. ``test.url.com``
            * keyword **name** (`str`): Name of application entry.
              Maximum of 31 characters.
            * keyword **description** (`str`): Description of entry
            * keyword **priority** (`int`): Confidence metric for
              classification, accepted value beween 0-100.
            * keyword **disabled** (`bool`): ``False`` if classification
              is active and ``True`` if disabled
    :rtype: list
    """
    return self._get(
        "/applicationDefinition/dnsClassification?resourceKey=userDefined"
    )


def update_user_defined_app_dns_classification(
    self,
    domain: str,
    name: str,
    priority: int,
    disabled: bool,
    description: str = "",
) -> bool:
    """Create or modify a user-defined application for domain name

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applicationDefinition
          - POST
          - /applicationDefinition/dnsClassification/{domain}

    :param domain: Domain for classification, e.g. ``site.tld`` or
        ``service.site.tld``
    :type domain: str
    :param name: Identifying name of the domain, can also re-use the
        domain. Maximum of 31 characters.
    :type name: str
    :param priority: Confidence metric for classification, e.g. ``95``
    :type priority: int
    :param disabled: ``False`` if classification is active and
        ``True`` if disabled
    :type disabled: bool
    :param description: Description of the classification,
        defaults to ""
    :type description: str, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "domain": domain,
        "name": name,
        "description": description,
        "priority": priority,
        "disabled": disabled,
    }

    return self._post(
        "/applicationDefinition/dnsClassification/{}".format(domain),
        data=data,
        return_type="bool",
    )


def delete_user_defined_app_dns_classification(
    self,
    domain: str,
) -> bool:
    """Delete specific user defined application dns classification

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applicationDefinition
          - DELETE
          - /applicationDefinition/dnsClassification/{domain}

    :param domain: Domain for classification, e.g. ``site.tld`` or
        ``service.site.tld``
    :type domain: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        "/applicationDefinition/dnsClassification/{}".format(domain),
        return_type="bool",
    )


def get_user_defined_app_address_map(self) -> dict:
    """Get all user defined application group based on address map

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applicationDefinition
          - GET
          - /applicationDefinition/ipIntelligenceClassification

    :return: Returns user-defined application by address map
    :rtype: dict
    """

    return self._get(
        "/applicationDefinition/ipIntelligenceClassification?resourceKey"
        + "=userDefined"
    )


def post_user_defined_app_address_map(
    self,
    ip_start: int,
    ip_end: int,
    name: str = "",
    description: str = "",
    priority: str = "",
    country: str = "",
    country_code: str = "",
    org: str = "",
) -> bool:
    """Create or update user defined application groups based on
    address map

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applicationDefinition
          - POST
          - /applicationDefinition/ipIntelligenceClassification/{ipStart}/{ipEnd}

    :param ip_start: Starting IP address, IP addresses must be passed as
        32-bit integer values, e.g. ``167837953`` rather than
        ``10.1.1.1``
    :type ip_start: str
    :param ip_end: Ending IP address, IP addresses must be passed as
        32-bit integer values, e.g. ``167837953`` rather than
        ``10.1.1.1``
    :type ip_end: str
    :param name: Name of application group, defaults to ""
    :type name: str, optional
    :param description: Description of application group, defaults to ""
    :type description: str, optional
    :param priority: Priority of application group, defaults to ""
    :type priority: str, optional
    :param country: Country of application group, defaults to ""
    :type country: str, optional
    :param country_code: Country code of application group,
        defaults to ""
    :type country_code: str, optional
    :param org: Organization of application group, defaults to ""
    :type org: str, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """  # noqa: E501,W505
    if ip_end < ip_start:
        raise ValueError(
            "End IP %r is lower than starting IP %r." % ip_end, ip_start
        )

    ipIntelligenceConfig = {
        "ip_start": ip_start,
        "ip_end": ip_end,
        "name": name,
        "description": description,
        "priority": priority,
        "country": country,
        "country_code": country_code,
        "org": org,
    }

    return self._post(
        "/applicationDefinition/ipIntelligenceClassification/{}/{}".format(
            ip_start, ip_end
        ),
        data=ipIntelligenceConfig,
        return_type="bool",
    )


def delete_user_defined_app_address_map(
    self,
    ip_start: int,
    ip_end: int,
) -> bool:
    """Delete specific user defined application group based on
    address map

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applicationDefinition
          - DELETE
          - /applicationDefinition/ipIntelligenceClassification/{ipStart}/{ipEnd}

    :param ip_start: Starting IP address, IP addresses must be passed as
        32-bit integer values, e.g. ``167837953`` rather than
        ``10.1.1.1``
    :type ip_start: str
    :param ip_end: Ending IP address, IP addresses must be passed as
        32-bit integer values, e.g. ``167837953`` rather than
        ``10.1.1.1``
    :type ip_end: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """  # noqa: E501,W505
    return self._delete(
        "/applicationDefinition/ipIntelligenceClassification/{}/{}".format(
            ip_start, ip_end
        ),
        return_type="bool",
    )


def get_user_defined_app_meter_flow(self) -> dict:
    """Get all user-defined application group based on meter flow
    classification

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applicationDefinition
          - GET
          - /applicationDefinition/meterFlowClassification

    :return: Returns user-defined application by meter flow
        classification
    :rtype: dict
    """
    return self._get(
        "/applicationDefinition/meterFlowClassification?resourceKey"
        + "=userDefined"
    )


def post_user_defined_app_meter_flow(
    self,
    flow_type: str,
    mid: int,
    name: str,
    priority: int,
    disabled: bool,
    description: str = "",
) -> bool:
    """Create or update user defined application groups based on meter
    flow classification

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applicationDefinition
          - POST
          - /applicationDefinition/meterFlowClassification/{flowType}/{mid}

    :param flow_type: Flow type, e.g. ``MF``
    :type flow_type: str
    :param mid: integer ID
    :type mid: int
    :param name: Name of application
    :type name: str
    :param priority: Priority of application
    :type priority: str
    :param disabled: ``False`` is if classification is active and
        ``True`` if disabled
    :type disabled: bool
    :param description: Description of the classification,
        defaults to ""
    :type description: str, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """  # noqa: W505
    data = {
        "flowType": flow_type,
        "mid": mid,
        "name": name,
        "description": description,
        "priority": priority,
        "disabled": disabled,
    }

    return self._post(
        "/applicationDefinition/meterFlowClassification/{}/{}".format(
            flow_type, mid
        ),
        data=data,
        return_type="bool",
    )


def delete_user_defined_app_meter_flow(
    self,
    flow_type: str,
    mid: int,
) -> bool:
    """Delete user-defined application groups based on meter flow
    classification

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applicationDefinition
          - DELETE
          - /applicationDefinition/meterFlowClassification/{flowType}/{mid}

    :param flow_type: Flow type, e.g. ``MF``
    :type flow_type: str
    :param mid: integer ID
    :type mid: int
    :return: Returns True/False based on successful call
    :rtype: bool
    """  # noqa: W505
    return self._delete(
        "/applicationDefinition/meterFlowClassification/{}/{}".format(
            flow_type, mid
        ),
        return_type="bool",
    )


def get_user_defined_app_groups(self) -> list:
    """Retrieve user defined application groups as JSON

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applicationDefinition
          - GET
          - /applicationDefinition/applicationTags

    :return: Returns user defined application groups
    :rtype: list
    """
    return self._get(
        "/applicationDefinition/applicationTags?resourceKey=userDefined"
    )


def update_user_defined_app_groups(
    self,
    app_tags_body: dict,
) -> bool:
    """Update user defined application groups

    .. warning::
        This will overwrite all user-defined application groups, to
        preserve currently defined groups, first get existing groups
        with :func:`~get_user_defined_app_groups` and append a new
        application group as a separate key in the app_tags_body
        dictionary.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applicationDefinition
          - POST
          - /applicationDefinition/applicationTags

    :param app_tags_body: Dictionary of a user-defined group name, and
        the contained applications and/or parent group. \n
        * keyword **<user_defined_group_name>** (`dict`): application
          group \n
            * keyword **apps** (`list[str]`): application list
            * keyword **parentGroup** (`list[str]`): parent group list
    :type app_tags_body: dict
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/applicationDefinition/applicationTags",
        data=app_tags_body,
        return_type="bool",
    )


def get_application_modification_times(self) -> list:
    """Retrieve modification times and hashes of application and
    application group definitions

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applicationDefinition
          - GET
          - /applicationDefinition/updatedTime

    :return: Returns list of dictionaries for both applications and
        application group modifications
    :rtype: list
    """
    return self._get("/applicationDefinition/updatedTime")
