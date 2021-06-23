# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# gmsStatsCollection : Enable/disable stats collection by orchestrator


def get_gms_stats_collection(self) -> dict:
    """Returns stats collection enable/disable details

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsStatsCollection
          - GET
          - /gms/statsCollection

    :return: Returns dictionary of Orchestrator stats collection
        settings
    :rtype: dict
    """
    return self._get("/gms/statsCollection")


def update_gms_stats_collection(
    self,
    application: bool = None,
    dns: bool = None,
    drc: bool = None,
    drops: bool = None,
    dscp: bool = None,
    flow: bool = None,
    interface: bool = None,
    jitter: bool = None,
    port: bool = None,
    shaper: bool = None,
    top_talkers: bool = None,
    tunnel: bool = None,
) -> bool:
    """Enable/disable stats collection by orchestrator.
    All parameters optional.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsStatsCollection
          - POST
          - /gms/statsCollection

    :param application: Description missing in Swagger, defaults to None
    :type application: bool, optional
    :param dns: Description missing in Swagger, defaults to None
    :type dns: bool, optional
    :param drc: Description missing in Swagger, defaults to None
    :type drc: bool, optional
    :param drops: Description missing in Swagger, defaults to None
    :type drops: bool, optional
    :param dscp: Description missing in Swagger, defaults to None
    :type dscp: bool, optional
    :param flow: Description missing in Swagger, defaults to None
    :type flow: bool, optional
    :param interface: Description missing in Swagger, defaults to None
    :type interface: bool, optional
    :param jitter: Description missing in Swagger, defaults to None
    :type jitter: bool, optional
    :param port: Description missing in Swagger, defaults to None
    :type port: bool, optional
    :param shaper: Description missing in Swagger, defaults to None
    :type shaper: bool, optional
    :param top_talkers: Description missing in Swagger, defaults to None
    :type top_talkers: bool, optional
    :param tunnel: Description missing in Swagger, defaults to None
    :type tunnel: bool, optional
    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    data = {}
    if application is not None:
        data["Application"] = application
    if dns is not None:
        data["Dns"] = dns
    if drc is not None:
        data["Drc"] = drc
    if drops is not None:
        data["Drops"] = drops
    if dscp is not None:
        data["Dscp"] = dscp
    if flow is not None:
        data["Flow"] = flow
    if interface is not None:
        data["Interface"] = interface
    if jitter is not None:
        data["Jitter"] = jitter
    if port is not None:
        data["Port"] = port
    if shaper is not None:
        data["Shaper"] = shaper
    if top_talkers is not None:
        data["TopTalkers"] = top_talkers
    if tunnel is not None:
        data["Tunnel"] = tunnel

    return self._post(
        "/gms/statsCollection",
        data=data,
        return_type="bool",
    )


def get_gms_stats_collection_defaults(self) -> dict:
    """Returns default values for stats collection

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsStatsCollection
          - GET
          - /gms/statsCollection/default

    :return: Returns dictionary of default Orchestrator stats collection
        settings
    :rtype: dict
    """
    return self._get("/gms/statsCollection/default")
