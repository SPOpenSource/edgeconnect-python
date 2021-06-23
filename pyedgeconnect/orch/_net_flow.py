# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# netFlow : ECOS Netflow configuration


def get_net_flow_configuration(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get netflow configurations from Edge Connect appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - netFlow
          - GET
          - /netFlow/{neId}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary of netflow configuration information \n
        * keyword **active_timeout** (`int`): Specify NetFlow timeout
          (1..30) mins
        * keyword **ipfix_tmplt_rfrsh_t** (`int`): Specify IPFIX
          template refresh timeout (1..1440) mins
        * keyword **port1** (`int`): No description from Swagger
        * keyword **if_wan_tx** (`bool`): No description from Swagger
        * keyword **enable** (`bool`): No description from Swagger
        * keyword **ipaddr1** (`str`): valid ip address
        * keyword **if_lan_rx** (`bool`): No description from Swagger
        * keyword **if_lan_tx** (`bool`): No description from Swagger
        * keyword **ipaddr2** (`str`): valid ip address
        * keyword **if_wan_rx** (`bool`): No description from Swagger
        * keyword **port2** (`int`): No description from Swagger
        * keyword **optional_ies** (`dict, optional`): dictionary of
          optional IES \n
            * keyword **app_perf_ies** (`bool, optional`): app
              performance optional IES
            * keyword **zbf_ies** (`bool, optional`): zbf optional IES\n
        * keyword **collector_type1** (`str`): NetFlow or IPFIX
          collector type
        * keyword **collector_type2** (`str`): NetFlow or IPFIX
          collector type
    :rtype: dict
    """
    return self._get("/netFlow/{}?cached={}".format(ne_id, cached))
