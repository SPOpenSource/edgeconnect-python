# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# dns : DNS server and domain


def get_appliance_dns_config(
    self,
) -> dict:
    """Get the current DNS IP address and domain names configured for
    your appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - dns
          - GET
          - /resolver

    :return: Returns dictionary of current appliance dns configuration\n
        * keyword **domain_search** (`dict`): Domain search settings \n
            * keyword **<Order of search 1-6>** (`dict`): \n
                * keyword **self** (`int`): Order of Domain Name, which
                  should be the same as this entry's key
                * keyword **domainname** (`str`): Search Domain
        * keyword **nameserver** (`dict`): Name server settings \n
            * keyword **1** (`dict`): Primary name server\n
                * keyword **self** (`int`): Order of Name Server, which
                  should be the same as this entry's key
                * keyword **address** (`str`): IP of DNS Server
                * keyword **vrf_id** (`int`): Segment ID, which default
                  value is 0
                * keyword **srcinf** (`str`): Source Interface, which
                  default value is any
            * keyword **2** (`dict`): Secondary name server\n
                * keyword **self** (`int`): Order of Name Server, which
                  should be the same as this entry's key
                * keyword **address** (`str`): IP of DNS Server
                * keyword **vrf_id** (`int`): Segment ID, which default
                  value is 0
                * keyword **srcinf** (`str`): Source Interface, which
                    default value is any
            * keyword **3** (`dict`): Tertiary name server\n
                * keyword **self** (`int`): Order of Name Server, which
                  should be the same as this entry's key
                * keyword **address** (`str`): IP of DNS Server
                * keyword **vrf_id** (`int`): Segment ID, which default
                  value is 0
                * keyword **srcinf** (`str`): Source Interface, which
                  default value is any
    :rtype: dict
    """
    return self._get("/resolver")


def set_appliance_dns_config(
    self,
    domain_search_settings: dict,
    primary_ns_address: str,
    primary_ns_vrf_id: int,
    primary_ns_source_interface: str,
    secondary_ns_address: str,
    secondary_ns_vrf_id: int,
    secondary_ns_source_interface: str,
    tertiary_ns_address: str,
    tertiary_ns_vrf_id: int,
    tertiary_ns_source_interface: str,
) -> dict:
    """Get the current DNS IP address and domain names configured for
    your appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - dns
          - POST
          - /resolver

    Example:

    .. code-block:: python

        domain_search_settings = {
            "1": {
                "self": 1,
                "domainname": "my.search.domain",
            },
        }

        ec.set_appliance_dns_config(
            domain_search_settings = domain_search_settings,
            primary_ns_address = "192.0.2.100",
            primary_ns_vrf_id = 0,
            primary_ns_source_interface = "mgmt0",
            secondary_ns_address = "192.0.2.200",
            secondary_ns_vrf_id = 0,
            secondary_ns_source_interface = "",
            tertiary_ns_address = "",
            tertiary_ns_vrf_id = 0,
            tertiary_ns_source_interface = "",
        )

    :param domain_search_settings: Domain search settings dictionary
        object. Up to 6 can be specified, each with a key of the
        order they should be applied (1-6). Example below \n
        * keyword **1** (`dict`): Search domain object \n
            * keyword **self** (`int`): Numeric ID, same as key
            * keyword **domainname** (`str`): Search domain,
              e.g. ``my.search.domain``
    :type domain_search_settings: dict
    :param primary_ns_address: Primary DNS server IP address
    :type primary_ns_address: str
    :param primary_ns_vrf_id: Segment/VRF ID to reach Primary DNS
        server, e.g. ``0`` for Default VRF
    :type primary_ns_vrf_id: int
    :param primary_ns_source_interface: Interface to reach Primary
        DNS server, e.g. ``mgmt0`` or ``lan0``
    :type primary_ns_source_interface: str
    :param secondary_ns_address: Secondary DNS server IP address
    :type secondary_ns_address: str
    :param secondary_ns_vrf_id: Segment/VRF ID to reach Secondary
        DNS server, e.g. ``0`` for Default VRF
    :type secondary_ns_vrf_id: int
    :param secondary_ns_source_interface: Interface to reach
        Secondary DNS server, e.g. ``mgmt0`` or ``lan0``
    :type secondary_ns_source_interface: str
    :param tertiary_ns_address: Tertiary DNS server IP address
    :type tertiary_ns_address: str
    :param tertiary_ns_vrf_id: Segment/VRF ID to reach Tertiary DNS
        server, e.g. ``0`` for Default VRF
    :type tertiary_ns_vrf_id: int
    :param tertiary_ns_source_interface: Interface to reach Tertiary
        DNS server, e.g. ``mgmt0`` or ``lan0``
    :type tertiary_ns_source_interface: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "domain_search": domain_search_settings,
        "nameserver": {
            "1": {
                "self": 1,
                "address": primary_ns_address,
                "vrf_id": primary_ns_vrf_id,
                "srcinf": primary_ns_source_interface,
            },
            "2": {
                "self": 2,
                "address": secondary_ns_address,
                "vrf_id": secondary_ns_vrf_id,
                "srcinf": secondary_ns_source_interface,
            },
            "3": {
                "self": 3,
                "address": tertiary_ns_address,
                "vrf_id": tertiary_ns_vrf_id,
                "srcinf": tertiary_ns_source_interface,
            },
        },
    }

    return self._post(
        "/resolver",
        data=data,
        return_type="bool",
    )
