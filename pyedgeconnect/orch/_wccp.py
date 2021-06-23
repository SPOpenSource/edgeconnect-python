# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# wccp : ECOS WCCP configuration


def get_wccp_system_settings(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get WCCP system settings from appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - wccp
          - GET
          - /wccp/config/system/{neId}?cached={cached}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary of wccp settings \n
        * keyword **mcast_ttl** (`int`): TTL value for wccp
        * keyword **enable** (`bool`): ``True`` if WCCP is enabled
    :rtype: dict
    """
    return self._get("/wccp/config/system/{}?cached={}".format(ne_id, cached))


def get_wccp_service_group_settings(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get per-group WCCP configuration settings from appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - wccp
          - GET
          - /wccp/config/group/{neId}?cached={cached}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns nested dictionary of wccp settings per group-id \n
        * keyword **<wccp_group_id>** (`dict`): WCCP group detail
          object \n
            * keyword **password** (`str, optional`): WCCP service group
              password
            * keyword **mask_src_port** (`int, optional`): WCCP service
              group mask source port
            * keyword **force_l2_return** (`bool, optional`): WCCP
              service group force l2 return
            * keyword **hash_dst_ip** (`bool, optional`): WCCP service
              group hash destination ip
            * keyword **self** (`int, optional`): Integer value of
              service group Id
            * keyword **weight** (`int, optional`): WCCP service group
              weight
            * keyword **hash_src_port** (`bool, optional`): WCCP service
              group hash source port
            * keyword **assign_method** (`str, optional`): Assignment
              Method
            * keyword **hash_dst_port** (`bool, optional`): WCCP service
              group hash destination port
            * keyword **hash_src_ip** (`bool, optional`): WCCP service
              group hash source ip
            * keyword **encap** (str ing, optional): WCCP service group
              forwarding method
            * keyword **protocol** (`str, optional`): WCCP service group
              protocol
            * keyword **assign_detail** (`str, optional`): WCCP service
              group assignment detail
            * keyword **compatibility** (`str, optional`): WCCP service
              group compatibility mode. Valid values: ``ios``, ``nexus``
            * keyword **interface** (`str, optional`): WCCP service
              group interface
            * keyword **mask_dst_ip** (`int, optional`): WCCP service
              group mask destination ip
            * keyword **mask_dst_port** (`int, optional`): WCCP service
              group mask destination port
            * keyword **mask_src_ip** (`int, optional`): WCCP service
              group mask source ip
            * keyword **priority** (`int, optional`): WCCP service group
              priority. Valid range: ``[0, 255]``
            * keyword **router** (`dict, optional`): WCCP service group
              router information
    :rtype: dict
    """
    return self._get("/wccp/config/group/{}?cached={}".format(ne_id, cached))


def get_wccp_state(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get per-group WCCP status from appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - wccp
          - GET
          - /wccp/state/{neId}?cached={cached}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns nested dictionary of wccp settings per group-id \n
        * keyword **system** (`dict`): System information object \n
            * keyword **debug_global** (`str`): global debug information
              for WCCP
            * keyword **debug_all** (`str`): all debug information for
              WCCP
            * keyword **is_alive** (`str`): is alive information for
              WCCP
            * keyword **proto_ver** (`str`): prototype version
              information for WCCP
        * keyword **group** (`dict`): WCCP group state objects \n
            * keyword **<wccp_group_id>** (`dict`): WCCP group detail \n
                * keyword **debug** (`str, optional`): debug information
                  for the WCCP service group
                * keyword **app_id** (`str, optional`): No description
                  in Swagger
                * keyword **self** (`int, optional`): integer value of
                  the group Id
                * keyword **assignment** (`str, optional`): assignment
                  information for the WCCP service group
                * keyword **num_appliances** (`int, optional`): number
                  of appliances for the WCCP service group
                * keyword **num_routers** (`int, optional`): number of
                  routers for the WCCP service group
                * keyword **oper** (`str, optional`): operational status
                  for the WCCP service group
                * keyword **uptime** (`int, optional`): uptime for the
                  WCCP service group
    :rtype: dict
    """
    return self._get("/wccp/state/{}?cached={}".format(ne_id, cached))
