# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# bondedTunnelsConfiguration : ECOS bonded tunnel configuration
from __future__ import annotations


def get_bonded_tunnel_details(
    self,
    limit: int,
    matching_alias: str = None,
    overlay_id: int = None,
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
    children: bool = None,
) -> dict:
    """Get bonded tunnel details across all appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - bondedTunnelsConfiguration
          - GET
          - /tunnels2/bonded

    :param limit: Max number of tunnels to return in response
    :type limit: int
    :param matching_alias: Match tunnel alias on text string provided,
        defaults to None
    :type matching_alias: str, optional
    :param overlay_id: The overlay ID to match tunnels on,
        defaults to None
    :type overlay_id: int, optional
    :param state: Regular expression to match tunnel state,
        e.g. "Up" "Down", defaults to None
    :type state: str, optional
    :param tunnel_id: Include bonded tunnel id in response,
        defaults to None
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
    :param children: Include physical tunnels within bonded tunnel in
        response, defaults to None
    :type children: bool, optional
    :return: Returns dictionary of tunnel details based on supplied
        query details
    :rtype: dict
    """
    path = "/tunnels2/bonded?limit={}".format(limit)

    if matching_alias is not None:
        path = path + "&matchingAlias={}".format(matching_alias)
    if overlay_id is not None:
        path = path + "&overlayId={}".format(overlay_id)
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
    if children is not None:
        path = path + "&children={}".format(children)

    return self._get(path)


def get_bonded_tunnel_details_for_appliance(
    self,
    ne_pk: str,
    limit: int,
    matching_alias: str = None,
    overlay_id: int = None,
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
    children: bool = None,
) -> dict:
    """Get bonded tunnel details for specific appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - bondedTunnelsConfiguration
          - GET
          - /tunnels2/bonded/{nePk}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param limit: Max number of tunnels to return in response
    :type limit: int
    :param matching_alias: Match tunnel alias on text string provided,
        defaults to None
    :type matching_alias: str, optional
    :param overlay_id: The overlay ID to match tunnels on,
        defaults to None
    :type overlay_id: int, optional
    :param state: Regular expression to match tunnel state,
        e.g. "Up" "Down", defaults to None
    :type state: str, optional
    :param tunnel_id: Include bonded tunnel id in response,
        defaults to None
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
    :param children: Include physical tunnels within bonded tunnel in
        response, defaults to None
    :type children: bool, optional
    :return: Returns dictionary of tunnel details based on supplied
        query details
    :rtype: dict
    """
    path = "/tunnels2/bonded/{}?limit={}".format(ne_pk, limit)

    if matching_alias is not None:
        path = path + "&matchingAlias={}".format(matching_alias)
    if overlay_id is not None:
        path = path + "&overlayId={}".format(overlay_id)
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
    if children is not None:
        path = path + "&children={}".format(children)

    return self._get(path)


def get_bonded_tunnel_details_for_appliance_tunnel(
    self,
    ne_pk: str,
    bonded_tunnel_id: str,
) -> dict:
    """Get bonded tunnel details for specific tunnel on appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - bondedTunnelsConfiguration
          - GET
          - /tunnels2/bonded/{nePk}/{bondedTunnelId}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param bonded_tunnel_id: Bonded tunnel id, e.g. "bondedTunnel_12"
    :type bonded_tunnel_id: str
    :return: Returns dictionary of tunnel details based on supplied
        query details
    :rtype: dict
    """
    return self._get("/tunnels2/bonded/{}/{}".format(ne_pk, bonded_tunnel_id))


def get_bonded_tunnels_for_physical_tunnel(
    self,
    ne_pk: str,
    physical_tunnel_id: str,
    state: str = None,
) -> dict:
    """Get bonded tunnels associated with a particular physical tunnel

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - bondedTunnelsConfiguration
          - GET
          - /tunnels2/bondedTunnelsWithPhysicalTunnel/{nePk}/{physicalTunnelId}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param physical_tunnel_id: Physical tunnel id, e.g. "Tunnel_12"
    :type physical_tunnel_id: str
    :param state: Regular expression to match tunnel state,
        e.g. "Up" "Down", defaults to None
    :type state: str, optional
    :return: Returns dictionary of tunnel details based on supplied
        query details
    :rtype: dict
    """  # noqa: W505
    if state is not None:
        return self._get(
            "/tunnels2/bondedTunnelsWithPhysicalTunnel/{}/{}?state={}".format(
                ne_pk, physical_tunnel_id, state
            )
        )
    else:
        return self._get(
            "/tunnels2/bondedTunnelsWithPhysicalTunnel/{}/{}".format(
                ne_pk, physical_tunnel_id
            )
        )


def get_bonded_tunnels_state(
    self,
    ne_pk_list: list[str],
) -> dict:
    """Get bonded tunnel details for list of appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - bondedTunnelsConfiguration
          - POST
          - /tunnels/bonded/state

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :return: Returns dictionary of bonded tunnel details for provided
        appliances
    :rtype: dict
    """
    data = {"ids": ne_pk_list}

    return self._post("/tunnels2/bonded/state", data=data)
