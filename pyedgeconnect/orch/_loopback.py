# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# loopback : Gets Appliance Loopback interfaces config


def get_loopback_interfaes(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get configured loopback interfaces on Edge Connect appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - loopback
          - GET
          - /virtualif/loopback/{neId}?cached={cached}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary of configured loopback interfaces
    :rtype: dict
    """
    return self._get("/virtualif/loopback/{}?cached={}".format(ne_id, cached))
