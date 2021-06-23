# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# vti : Gets Appliance VTI interfaces config


def get_vti_interfaes(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get configured vti interfaces on appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - vti
          - GET
          - /virtualif/vti/{neId}?cached={cached}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary of VTI configurations
    :rtype: dict
    """
    return self._get("/virtualif/vti/{}?cached={}".format(ne_id, cached))
