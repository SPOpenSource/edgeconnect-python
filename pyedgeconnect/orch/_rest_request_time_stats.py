# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# restRequestTimeStats : Get time used info of rest requests sent to
# appliances through web socket


def get_appliance_rest_stats(
    self,
    ne_pk: str,
    resource: str,
    portal_ws: bool,
    timedout: bool,
    time_from: int,
    time_to: int = 0,
) -> list:
    """Get summary of time used info of rest requests sent to appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - restRequestTimeStats
          - GET
          - /restRequestTimeStats/summary

    :param ne_pk: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_pk: str
    :param resource: Base resource of the appliance to send to, 'all'
        means all resources
    :type resource: str
    :param portal_ws: Through what web socket the requests were sent,
        ``True`` for portal web socket, ``False`` for direct web socket
    :type portal_ws: bool
    :param timedout: Whether the requests timedout
    :type timedout: bool
    :param time_from: The minimum epoch time when the requests were sent
    :type time_from: int
    :param time_to: The maximum epoch time when the requests were sent,
        0 represents current time, defaults to 0
    :type time_to: int, optional
    :return: Returns list of associated stats
    :rtype: list
    """

    path = "/restRequestTimeStats/summary?nePk={}".format(ne_pk)
    path = path + "&resource={}&portalWS={}&timedout={}&from={}&to={}".format(
        resource, portal_ws, timedout, time_from, time_to
    )
    return self._get(path)


def get_appliance_rest_stats_by_method(
    self,
    ne_pk: str,
    resource: str,
    portal_ws: bool,
    time_from: int,
    method: str = "GET",
    time_to: int = 0,
) -> list:
    """Get summary of time used info of rest requests sent to specific
    resource on appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - restRequestTimeStats
          - GET
          - /restRequestTimeStats/{nePk}/%2F{resource}/{portalWS}/{method}

    :param ne_pk: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_pk: str
    :param resource: Base resource of the appliance to send to, ``all``
        means all resources
    :type resource: str
    :param portal_ws: Through what web socket the requests were sent,
        ``True`` for portal web socket, ``False`` for direct web socket
    :type portal_ws: bool
    :param timedout: Whether the requests timedout
    :type timedout: bool
    :param time_from: The minimum epoch time when the requests were sent
    :type time_from: int
    :param time_to: The maximum epoch time when the requests were sent,
        ``0`` represents current time, defaults to 0
    :type time_to: int, optional
    :param method: The HTTP request method, e.g. ``GET``, ``POST``,
        ``PUT``, and ``DELETE``, defaults to "GET"
    :type method: str, optional
    :return: Returns list of associated stats
    :rtype: list
    """  # noqa: W505

    path = (
        "/restRequestTimeStats/{}/".format(ne_pk)
        + r"%2F"
        + "{}/{}/{}?from={}&to={}".format(
            resource, portal_ws, method, time_from, time_to
        )
    )

    return self._get(path)
