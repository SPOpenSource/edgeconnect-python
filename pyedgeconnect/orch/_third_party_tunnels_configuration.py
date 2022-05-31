# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# thirdPartyTunnelsConfiguration : ECOS third party tunnel configuration
from __future__ import annotations


def get_passthrough_tunnel_details(
    self,
    limit: int,
    matching_alias: str = None,
    matching_service: str = None,
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
    """Get passthrough tunnel details across all appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyTunnelsConfiguration
          - GET
          - /tunnels2/passThrough

    :param limit: Max number of tunnels to return in response
    :type limit: int
    :param matching_alias: Match tunnel alias on text string provided,
        defaults to None
    :type matching_alias: str, optional
    :param matching_service: Match for string within tunnel's
        Peer/service, defaults to None
    :type matching_service: str, optional
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
    :return: Returns dictionary of tunnel details based on supplied
        query details
    :rtype: dict
    """
    path = "/tunnels2/passThrough?limit={}".format(limit)

    if matching_alias is not None:
        path = path + "&matchingAlias={}".format(matching_alias)
    if matching_service is not None:
        path = path + "&matchingService={}".format(matching_service)
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


def get_passthrough_tunnel_details_for_appliance(
    self,
    ne_pk: str,
    limit: int,
    matching_alias: str = None,
    matching_service: str = None,
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
    """Get passthrough tunnel details for specific appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyTunnelsConfiguration
          - GET
          - /tunnels2/passThrough/{nePk}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param limit: Max number of tunnels to return in response
    :type limit: int
    :param matching_alias: Match tunnel alias on text string provided,
        defaults to None
    :type matching_alias: str, optional
    :param matching_service: Match for string within tunnel's
        Peer/service, defaults to None
    :type matching_service: str, optional
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
    :return: Returns dictionary of tunnel details based on supplied
        query details
    :rtype: dict
    """

    path = "/tunnels2/passThrough/{}?limit={}".format(ne_pk, limit)

    if matching_alias is not None:
        path = path + "&matchingAlias={}".format(matching_alias)
    if matching_service is not None:
        path = path + "&matchingService={}".format(matching_service)
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


def get_passthrough_tunnel_details_for_appliance_tunnel(
    self,
    ne_pk: str,
    passthrough_tunnel_id: str,
) -> dict:
    """Get passthrough tunnel details for specific tunnel on appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyTunnelsConfiguration
          - GET
          - /tunnels2/passThrough/{nePk}/{passThroughTunnelId}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param passthrough_tunnel_id: Passthrough tunnel id,
        e.g. "passThrough_3"
    :type passthrough_tunnel_id: str
    :return: Returns dictionary of tunnel details based on supplied
        query details
    :rtype: dict
    """
    return self._get(
        "/tunnels2/passThrough/{}/{}".format(ne_pk, passthrough_tunnel_id)
    )


def get_passthrough_tunnels_state(
    self,
    ne_pk_list: list[str],
) -> dict:
    """Get passthrough tunnel details for list of appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - thirdPartyTunnelsConfiguration
          - POST
          - /tunnels/thirdParty/state

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :return: Returns dictionary of passthrough tunnel details for
        provided appliances
    :rtype: dict
    """
    data = {"ids": ne_pk_list}

    return self._post("/tunnels2/thirdParty/state", data=data)
