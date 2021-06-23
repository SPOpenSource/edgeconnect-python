# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# inboundShaper : ECOS inbound bandwidth shaping


def get_appliance_inbound_shaper(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get inbound shaper settings from Edge Connect appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - inboundShaper
          - GET
          - /inboundShaper/{neId}?cached={cached}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary where each key is a segment id that
        contains its associated DNS proxy configuration (profiles,
        domain groups and maps).
    :rtype: dict
    """
    return self._get("/inboundShaper/{}?cached={}".format(ne_id, cached))
