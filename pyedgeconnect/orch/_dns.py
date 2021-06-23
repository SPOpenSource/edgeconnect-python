# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# dns : ECOS DNS information


def get_appliance_dns(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get DNS server IP addresses and domain configurations from Edge
    Connect appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - dns
          - GET
          - /resolver/{neId}?cached={cached}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary of appliance DNS configuration \n
        * keyword **domain_search** (`dict`): DNS search domains \n
            * keyword **1** (`dict, optional`): Primary Domain \n
                * keyword **self** (`int`): 1
                * keyword **domainname** (`str`): Search domain
            * keyword **2** (`dict, optional`): Secondary Domain \n
                * keyword **self** (`int`): 2
                * keyword **domainname** (`str`): Search domain
            * keyword **3** (`dict, optional`): Tertiary Domain \n
                * keyword **self** (`int`): 3
                * keyword **domainname** (`str`): Search domain
        * keyword **nameserver** (`dict`): DNS server \n
            * keyword **1** (`dict, optional`): Primary DNS server \n
                * keyword **self** (`int`): 1
                * keyword **address** (`str`): IP address of DNS server
                * keyword **srcinf** (`str`): Source interface
                * keyword **vrf_id** (`int`): VRF ID number, e.g. ``0``
            * keyword **2** (`dict, optional`): Secondary DNS server \n
                * keyword **self** (`int`): 2
                * keyword **address** (`str`): IP address of DNS server
                * keyword **srcinf** (`str`): Source interface
                * keyword **vrf_id** (`int`): VRF ID number, e.g. ``0``
            * keyword **3** (`dict, optional`): Tertiary DNS server \n
                * keyword **self** (`int`): 3
                * keyword **address** (`str`): IP address of DNS server
                * keyword **srcinf** (`str`): Source interface
                * keyword **vrf_id** (`int`): VRF ID number, e.g. ``0``
    :rtype: dict
    """
    return self._get("/resolver/{}?cached={}".format(ne_id, cached))
