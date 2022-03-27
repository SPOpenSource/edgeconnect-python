# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# zones : Manage Zones


def get_zones(
    self,
    all_vrf_zones: bool = False,
) -> dict:
    """Get all zones configured on Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - zones
          - GET
          - /zones

    :param all_vrf_zones: ``True`` will return all zones names assigned
      to different Segments. ``False`` will return list of unique zone
      names. There can be multiple zones with the same name with
      different ID's that are applied to different segments.
    :type all_vrf_zones: bool
    :return: Returns dictionary of configured zones \n
      * keyword **<zone_id>** (`dict`): Zone object \n
        * keyword **name** (`str`): Zone name
    :rtype: dict
    """
    return self._get("/zones?allVRFZones={}".format(all_vrf_zones))


def update_zones(
    self,
    zones: dict,
    delete_dependencies: bool,
) -> bool:
    """Configure zones on Orchestrator.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - zones
          - POST
          - /zones

    .. warning::
        This will overwrite the zones so use the :func:`~get_zones`
        function to get existing zones and append if you don't want to
        remove existing zones

    :param zones: Dictionary of zones to configure in the format \n
        ``{"ZONE_ID" : {"name" : "ZONE_NAME"}, ... }`` \n
        e.g. {"1" : {"name" : "MPLS"}, ...}
    :type zones: dict
    :param delete_dependencies: If True, Zones deleted here will be
        removed from overlays, policies, interfaces and deployment
        profiles currently using those zones.
    :type delete_dependencies: bool
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/zones?deleteDependencies={}".format(delete_dependencies),
        data=zones,
        expected_status=[204],
        return_type="bool",
    )


def get_zone_next_id(self) -> dict:
    """Get zone ID that will be assigned to next configured zone

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - zones
          - GET
          - /zones/nextId

    :return: Returns dictionary with {"nextId" : int}, where int is the
        next ID to be assigned
    :rtype: dict
    """
    return self._get("/zones/nextId")


def set_zone_next_id(
    self,
    zone_id: int,
) -> bool:
    """Sets zone ID that will be assigned to next configured zone

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - zones
          - POST
          - /zones/nextId

    :param zone_id: Integer of next assigned zone ID
    :type zone_id: int
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {"nextId": zone_id}

    return self._post(
        "/zones/nextId",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def get_zones_end_to_end_state(self) -> dict:
    """Gets end-to-end ZBFW config state

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - zones
          - GET
          - /zones/eeEnable

    :return: Returns dictionary of end-to-end ZBFW config state
    :rtype: dict
    """
    return self._get("/zones/eeEnable")


def update_zones_end_to_end_state(
    self,
    enable: bool,
) -> bool:
    """Sets end-to-end ZBFW config state

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - zones
          - POST
          - /zones/eeEnable

    :param enable: Enable end-to-end ZBFW (True) or Disable (False)
    :type enable: bool
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {"enable": enable}

    return self._post(
        "/zones/eeEnable",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def get_zones_vrf_mapping(self) -> dict:
    """Gets VRF Firewall Zones mapping

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - zones
          - GET
          - /zones/vrfZonesMap

    :return: Returns dictionary of VRF Firewall Zones mapping, primary
        key values are VRF ID's
    :rtype: dict
    """
    return self._get("/zones/vrfZonesMap")
