# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# multicast : Gets Appliance multicast config and state


def get_appliance_multicast_enabled(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get multicast enabled info from appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - multicast
          - GET
          - /multicast/enable/{neId}?cached={cached}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary of multicast enabled info
    :rtype: dict
    """
    return self._get("/multicast/enable/{}?cached={}".format(ne_id, cached))


def get_appliance_multicast_config(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get multicast configuration from appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - multicast
          - GET
          - /multicast/config/{neId}?cached={cached}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary of multicast configuration
    :rtype: dict
    """
    return self._get("/multicast/config/{}?cached={}".format(ne_id, cached))


def get_appliance_multicast_interfaces(
    self,
    ne_id: str,
) -> list:
    """Get multicast interface state from appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - multicast
          - GET
          - /multicast/state/interfaces/{neId}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :return: Returns list of multicast interface states
    :rtype: list
    """
    return self._get("/multicast/state/interfaces/{}".format(ne_id))


def get_appliance_multicast_neighbors(
    self,
    ne_id: str,
) -> list:
    """Get multicast neighbors state from appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - multicast
          - GET
          - /multicast/state/neighbors/{neId}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :return: Returns list of multicast neighbor states
    :rtype: list
    """
    return self._get("/multicast/state/neighbors/{}".format(ne_id))


def get_appliance_multicast_routes(
    self,
    ne_id: str,
) -> list:
    """Get multicast routes state from appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - multicast
          - GET
          - /multicast/state/routes/{neId}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :return: Returns list of multicast route states
    :rtype: list
    """
    return self._get("/multicast/state/routes/{}".format(ne_id))
