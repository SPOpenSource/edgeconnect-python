# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# shaper : ECOS bandwidth shaping


def get_appliance_shaper(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get shaper settings from Edge Connect appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - shaper
          - GET
          - /shaper/{neId}?cached={cached}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary where each key is name of an interface,
        each value is an object defining shaper properties of that
        interface which includes ``traffic-class``, ``accuracy``, and
        ``max_bw`` fields.
    :rtype: dict
    """
    return self._get("/shaper/{}?cached={}".format(ne_id, cached))
