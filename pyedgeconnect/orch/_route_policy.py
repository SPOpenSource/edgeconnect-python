# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# routePolicy : ECOS route policies


def get_route_policy(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get route policy configurations from Edge Connect appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - routePolicy
          - GET
          - GET /routeMaps/{neId}?cached={cached}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary with options object and data object.
        Data objects includes Route map(s), each map includes Route
        rule(s), each rule has a match part and a set part. The schema
        of returned is ``{ 'options' : {'activeMap': 'map1'}, 'data':
        {'map1' : {'prio': {...}, 'self':'map1'}}}``
        The ``prio`` object contains rules key value pairs, each key is
        the priority of a rule, each value is the rule object.
    :rtype: dict
    """
    return self._get("/routeMaps/{}?cached={}".format(ne_id, cached))
