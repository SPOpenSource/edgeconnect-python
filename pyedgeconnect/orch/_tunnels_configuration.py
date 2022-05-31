# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# tunnelsConfiguration : ECOS tunnel configuration
from __future__ import annotations


def get_total_tunnel_count(
    self,
    metadata: bool = True,
) -> dict:
    """Get total tunnel count across all appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnelsConfiguration
          - GET
          - /tunnels2

    :param metadata: Includes the tunnel count, false returns an empty
        body, defaults to True
    :type metadata: bool
    :return: Returns dictionary of tunnel count with single key
        "totalTunnelCount"
    :rtype: dict
    """
    return self._get("/tunnels2?metaData={}".format(metadata))


def get_tunnel_count_for_appliances(
    self,
    ne_pk_list: list[str],
) -> dict:
    """Get total tunnel count organized by appliance and overaly for
    specified appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnelsConfiguration
          - POST
          - /tunnels2/tunnelCounts

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :return: Returns nexted dictionary of tunnel count, each top-level
        key is an appliance NePK, then sub-dictionary is tunnel counts
        per-overlay name and total.
    :rtype: dict
    """
    data = {"ids": ne_pk_list}

    return self._post(
        "/tunnels2/tunnelCounts",
        data=data,
    )


def get_physical_tunnel_details(
    self,
    limit: int,
    matching_alias: str = None,
    state: str = None,
    tunnel_id: bool = None,
    alias: bool = None,
    tag: bool = None,
    source_ne_pk: bool = None,
    dest_ne_pk: bool = None,
    dest_tunnel_id: bool = None,
    dest_tunnel_alias: bool = None,
    operational_status: bool = None,
    admin_status: bool = None,
    remote_id_state: bool = None,
    fec_status: bool = None,
    fec_ratio: bool = None,
) -> dict:
    """Get physical tunnel details across all appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnelsConfiguration
          - GET
          - /tunnels2/physical

    :param limit: Max number of tunnels to return in response
    :type limit: int
    :param matching_alias: Match tunnel alias on text string provided,
        defaults to None
    :type matching_alias: str, optional
    :param state: Regular expression to match tunnel state,
        e.g. ``Up`` ``Down``, defaults to None
    :type state: str, optional
    :param tunnel_id: Include tunnel id in response, defaults to None
    :type tunnel_id: bool, optional
    :param alias: Include alias name of tunnel in UI in response,
        defaults to None
    :type alias: bool, optional
    :param tag: Include overlay name for bonded tunnel in response,
        defaults to None
    :type tag: bool, optional
    :param source_ne_pk: Include nePk of appliance that the tunnel
        belongs to in response, defaults to None
    :type source_ne_pk: bool, optional
    :param dest_ne_pk: Include nePk of destination appliance for the
        tunnel in response, defaults to None
    :type dest_ne_pk: bool, optional
    :param dest_tunnel_id: Include tunnel id of opposite tunnel on the
        destination appliance in response, defaults to None
    :type dest_tunnel_id: bool, optional
    :param dest_tunnel_alias: Include tunnel alias of opposite tunnel on
        the destination appliance in response, defaults to None
    :type dest_tunnel_alias: bool, optional
    :param operation_status: Include current status of tunnel in
        response, defaults to None
    :type operational_status: bool, optional
    :param admin_status: Include admin status of tunnel in response,
        defaults to None
    :type admin_status: bool, optional
    :param remote_id_state: Include remote tunnel id state in response,
        defaults to None
    :type remote_id_state: bool, optional
    :param fec_status: Include FEC status of the tunnel in response,
        defaults to None
    :type fec_status: bool, optional
    :param fec_ratio: Include current FEC ratio of the tunnel in
        response, defaults to None
    :type fec_ratio: bool, optional
    :return: Returns dictionary of tunnel details based on supplied
        query details
    :rtype: dict
    """
    path = "/tunnels2/physical?limit={}".format(limit)

    if matching_alias is not None:
        path = path + "&matchingAlias={}".format(matching_alias)
    if state is not None:
        path = path + "&state={}".format(state)
    if tunnel_id is not None:
        path = path + "&id={}".format(tunnel_id)
    if alias is not None:
        path = path + "&alias={}".format(alias)
    if tag is not None:
        path = path + "&tag={}".format(tag)
    if source_ne_pk is not None:
        path = path + "&srcNePk={}".format(source_ne_pk)
    if dest_ne_pk is not None:
        path = path + "&destNePk={}".format(dest_ne_pk)
    if dest_tunnel_id is not None:
        path = path + "&destTunnelId={}".format(dest_tunnel_id)
    if dest_tunnel_alias is not None:
        path = path + "&destTunnelAlias={}".format(dest_tunnel_alias)
    if operational_status is not None:
        path = path + "&operStatus={}".format(operational_status)
    if admin_status is not None:
        path = path + "&adminStatus={}".format(admin_status)
    if remote_id_state is not None:
        path = path + "&remoteIdState={}".format(remote_id_state)
    if fec_status is not None:
        path = path + "&fecStatus={}".format(fec_status)
    if fec_ratio is not None:
        path = path + "&fecRatio={}".format(fec_ratio)

    return self._get(path)


def get_physical_tunnel_details_for_appliance(
    self,
    ne_pk: str,
    limit: int,
    matching_alias: str = None,
    state: str = None,
    tunnel_id: bool = None,
    alias: bool = None,
    tag: bool = None,
    source_ne_pk: bool = None,
    dest_ne_pk: bool = None,
    dest_tunnel_id: bool = None,
    dest_tunnel_alias: bool = None,
    operational_status: bool = None,
    admin_status: bool = None,
    remote_id_state: bool = None,
    fec_status: bool = None,
    fec_ratio: bool = None,
) -> dict:
    """Get physical tunnel details for specific appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnelsConfiguration
          - GET
          - /tunnels2/physical/{nePk}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param limit: Max number of tunnels to return in response
    :type limit: int
    :param matching_alias: Match tunnel alias on text string provided,
        defaults to None
    :type matching_alias: str, optional
    :param state: Regular expression to match tunnel state,
        e.g. ``Up`` ``Down``, defaults to None
    :type state: str, optional
    :param tunnel_id: Include tunnel id in response, defaults to None
    :type tunnel_id: bool, optional
    :param alias: Include alias name of tunnel in UI in response,
        defaults to None
    :type alias: bool, optional
    :param tag: Include overlay name for bonded tunnel in response,
        defaults to None
    :type tag: bool, optional
    :param source_ne_pk: Include nePk of appliance that the tunnel
        belongs to in response, defaults to None
    :type source_ne_pk: bool, optional
    :param dest_ne_pk: Include nePk of destination appliance for the
        tunnel in response, defaults to None
    :type dest_ne_pk: bool, optional
    :param dest_tunnel_id: Include tunnel id of opposite tunnel on the
        destination appliance in response, defaults to None
    :type dest_tunnel_id: bool, optional
    :param dest_tunnel_alias: Include tunnel alias of opposite tunnel on
        the destination appliance in response, defaults to None
    :type dest_tunnel_alias: bool, optional
    :param operation_status: Include current status of tunnel in
        response, defaults to None
    :type operational_status: bool, optional
    :param admin_status: Include admin status of tunnel in response,
        defaults to None
    :type admin_status: bool, optional
    :param remote_id_state: Include remote tunnel id state in response,
        defaults to None
    :type remote_id_state: bool, optional
    :param fec_status: Include FEC status of the tunnel in response,
        defaults to None
    :type fec_status: bool, optional
    :param fec_ratio: Include current FEC ratio of the tunnel in
        response, defaults to None
    :type fec_ratio: bool, optional
    :return: Returns dictionary of tunnel details based on supplied
        query details
    :rtype: dict
    """
    path = "/tunnels2/physical/{}?limit={}".format(ne_pk, limit)

    if matching_alias is not None:
        path = path + "&matchingAlias={}".format(matching_alias)
    if state is not None:
        path = path + "&state={}".format(state)
    if tunnel_id is not None:
        path = path + "&id={}".format(tunnel_id)
    if alias is not None:
        path = path + "&alias={}".format(alias)
    if tag is not None:
        path = path + "&tag={}".format(tag)
    if source_ne_pk is not None:
        path = path + "&srcNePk={}".format(source_ne_pk)
    if dest_ne_pk is not None:
        path = path + "&destNePk={}".format(dest_ne_pk)
    if dest_tunnel_id is not None:
        path = path + "&destTunnelId={}".format(dest_tunnel_id)
    if dest_tunnel_alias is not None:
        path = path + "&destTunnelAlias={}".format(dest_tunnel_alias)
    if operational_status is not None:
        path = path + "&operStatus={}".format(operational_status)
    if admin_status is not None:
        path = path + "&adminStatus={}".format(admin_status)
    if remote_id_state is not None:
        path = path + "&remoteIdState={}".format(remote_id_state)
    if fec_status is not None:
        path = path + "&fecStatus={}".format(fec_status)
    if fec_ratio is not None:
        path = path + "&fecRatio={}".format(fec_ratio)

    return self._get(path)


def get_physical_tunnel_details_for_appliance_tunnel(
    self,
    ne_pk: str,
    tunnel_id: str,
) -> dict:
    """Get physical tunnel details for specific tunnel on appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnelsConfiguration
          - GET
          - /tunnels2/physical/{nePk}/{tunnelId}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param tunnel_id: Tunnel id, e.g. ``tunnel_12``
    :type tunnel_id: str
    :return: Returns dictionary of tunnel details based on supplied
        query details
    :rtype: dict
    """
    return self._get("/tunnels2/physical/{}/{}".format(ne_pk, tunnel_id))


def get_tunnels_between_appliances(
    self,
    ne_pk_list: list[str],
    limit: int,
    matching_alias: str = None,
    overlay_id: str = None,
    state: str = None,
) -> dict:
    """Get physical tunnel details for specific tunnel on appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnelsConfiguration
          - POST
          - /tunnels2/getTunnelsBetweenAppliances

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :param limit: Max number of tunnels to return in response
    :type limit: int
    :param matching_alias: Match tunnel alias on text string provided,
        defaults to None
    :type matching_alias: str, optional
    :param overlay_id: The overlay ID to match tunnels on. Value of
        ``0`` for all physical tunnels, "all" for all bonded tunnels,
        defaults to None
    :type overlay_id: str, optional
    :param state: Regular expression to match tunnel state,
        e.g. ``Up`` ``Down``, defaults to None
    :type state: str, optional
    :return: Returns list of dictionaries of tunnel details between
        provided appliances
    :rtype: list
    """
    path = "/tunnels2/getTunnelsBetweenAppliances?limit={}".format(limit)

    if matching_alias is not None:
        path = path + "&matchingAlias={}".format(matching_alias)
    if overlay_id is not None:
        path = path + "&overlayId={}".format(overlay_id)
    if state is not None:
        path = path + "&state={}".format(state)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_tunnels_between_appliances_config_data(
    self,
    ne_pk_list: list[str],
    state: str = None,
) -> dict:
    """Get physical tunnel details for specific tunnel on appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnelsConfiguration
          - POST
          - /tunnels2/physical/state

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :param state: Regular expression to match tunnel state,
        e.g. ``Up`` ``Down``, defaults to None
    :type state: str, optional
    :return: Returns dictionary of tunnel configuration details between
        provided appliances
    :rtype: dict
    """
    path = "/tunnels2/physical/state"

    if state is not None:
        path = path + "&state={}".format(state)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def initiate_tunnel_traceroute(
    self,
    ne_pk: str,
    tunnel_id: str,
) -> bool:
    """Initiate a traceroute over a specified tunnel on an appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnelsConfiguration
          - POST
          - /tunnels2/physical/traceroute/{id}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param tunnel_id: Tunnel id, e.g. ``tunnel_12``
    :type tunnel_id: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {"nePk": ne_pk}

    return self._post(
        "/tunnels/physical/traceroute/{}".format(tunnel_id),
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def get_appliance_tunnel_ids(
    self,
    ne_pk: str,
    state: str = None,
) -> dict:
    """Get tunnel id's on an appliance, can filter by state

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnelsConfiguration
          - GET
          - /tunnels2/physical/tunnelIds/{nePk}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param state: Regular expression to match tunnel state,
        e.g. ``Up`` ``Down``, defaults to None
    :type state: str, optional
    :return: Returns dictionary of tunnel count with single key
        "totalTunnelCount"
    :rtype: dict
    """
    if state is not None:
        return self._get(
            "/tunnels/physical/tunnelIds/{}?state={}".format(ne_pk, state)
        )
    else:
        return self._get("/tunnels/physical/tunnelIds/{}".format(ne_pk))


def get_tunnel_traceroute(
    self,
    ne_pk: str,
    tunnel_id: str,
) -> bool:
    """Get status of a traceroute over a specified tunnel on an
    appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tunnelsConfiguration
          - POST
          - /tunnels2/physical/tracerouteState/{id}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param tunnel_id: Tunnel id, e.g. ``tunnel_12``
    :type tunnel_id: str
    :return: Returns dictionary of traceroute hops and related details
        (index, ip, min/max/avg rtt, etc.)
    :rtype: dict
    """
    data = {"nePk": ne_pk}

    return self._post(
        "/tunnels/physical/tracerouteState/{}".format(tunnel_id),
        data=data,
    )


def get_batch_appliance_tunnels_config(
    self,
    ne_pk: str,
    tunnel_id_list: list,
) -> bool:
    """Get appliance tunnel configuration for specified tunnels

    .. note::
      This API Call is not in current Swagger as of Orch 9.0.3

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - n/a
          - POST
          - /tunnels/physical/config/getBatch/{nePk}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param tunnel_id_list: List of tunnel ids to retrieive config
        details for, e.g. ``["tunnel_12", "tunnel_13"]``
    :type tunnel_id: list
    :return: Returns dictionary of tunnel configuration details from
        specified tunnels
    :rtype: dict
    """
    data = tunnel_id_list

    return self._post(
        "/tunnels/physical/config/getBatch/{}".format(ne_pk),
        data=data,
    )


def get_batch_appliance_tunnels_state(
    self,
    ne_pk: str,
    tunnel_id_list: list,
) -> bool:
    """Get appliance tunnel state for specified tunnels

    .. note::
      This API Call is not in current Swagger as of Orch 9.0.3

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - n/a
          - POST
          - /tunnels/physical/state/getBatch/{nePk}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param tunnel_id_list: List of tunnel ids to retrieive config
        details for, e.g. ``["tunnel_12", "tunnel_13"]``
    :type tunnel_id: list
    :return: Returns dictionary of tunnel state details from specified
        tunnels
    :rtype: dict
    """
    data = tunnel_id_list

    return self._post(
        "/tunnels/physical/state/getBatch/{}".format(ne_pk),
        data=data,
    )
