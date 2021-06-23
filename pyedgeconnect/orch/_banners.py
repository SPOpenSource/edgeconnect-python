# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# banners : ECOS login banner


def get_appliance_login_banners(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get configured message of the day (motd) and issue banners for
    Edge Connect appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - banners
          - GET
          - /banners/{neId}?cached={cached}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary with banner configuration \n
        * keyword **motd** (`str`): Message that appears on succesful
          login
        * keyword **issue** (`str`): Message that appears on login
          prompt
    :rtype: dict
    """
    return self._get("/banners/{}?cached={}".format(ne_id, cached))
