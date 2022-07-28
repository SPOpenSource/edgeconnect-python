# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# peers : Neighboring EdgeConnect Appliances


def get_appliance_peers(
    self,
) -> dict:
    """Get appliance SDWAN peers and related tunnels, including local
    breakout passthrough tunnels

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - peers
          - GET
          - /peers

    :return: Returns dictionary of peers and local breakout peers with
        list of related tunnels for each \n
        * keyword **<peer_name>** (`list[str]`): Peer object, the peer
          name will be EdgeConnect hostname for EdgeConnect peer, or
          Overlay name in format of ``Overlay_<OVERLAY_NAME>_Primary``
          for local breakout \n
            * [`str`]: List of tunnel ids connecting to this peer, e.g.
              ``tunnel_385`` for SDWAN tunnel peer or
              ``passThrough_320`` for local breakout
    :rtype: dict
    """
    return self._get("/peers")


def get_appliance_peers_ec_only(
    self,
) -> dict:
    """Get appliance SDWAN peers and related tunnels

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - peers
          - GET
          - /peers/spPeers

    :return: Returns dictionary of peers and local breakout peers with
        list of related tunnels for each \n
        * keyword **<peer_name>** (`list[str]`): Peer object, the peer
          name will be EdgeConnect hostname for EdgeConnect peer\n
            * [`str`]: List of tunnel ids connecting to this peer, e.g.
              ``tunnel_385`` for SDWAN tunnel peer
    :rtype: dict
    """
    return self._get("/peers/spPeers")
