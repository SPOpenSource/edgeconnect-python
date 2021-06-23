# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# adminDistance : Admin Distance


def get_appliance_admin_distance(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get Admin Distance configurations from Edge Connect appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - adminDistance
          - GET
          - /appliance/adminDistance/{neId}?cached={cached}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary of admin distance values
    :rtype: dict
    """

    return self._get(
        "/appliance/adminDistance/{}?cached={}".format(ne_id, cached)
    )
