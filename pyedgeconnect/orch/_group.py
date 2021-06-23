# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# group : Manage appliance groups


def get_gms_groups(self) -> dict:
    """Get all appliance groups in Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - group
          - GET
          - /gms/group

    :return: Returns dictionary of all appliance groups in Orchestrator
    :rtype: dict
    """
    return self._get("/gms/group")


def get_gms_group(
    self,
    group_pk: str,
) -> dict:
    """Get appliance group in Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - group
          - GET
          - /gms/group/{id}

    :param group_pk: The appliance group identifier, e.g. ``0.Network``
        is root group, ``1.Network`` is internal use, ``2.Network`` is
        auto-discovered groups. ``3.Network`` and beyond is user-defined
        groups.
    :type group_pk: str
    :return: Returns dictionary of group details in Orchestrator \n
        * keyword **id** (`str`): Group Primary Key, e.g. ``3.Network``
        * keyword **name** (`str`): Unique name given to group
        * keyword **subType** (`int`): Network sub type: Root Group is
          ``0``, Auto discovered group is ``2``, and User defined group
          is ``3``
        * keyword **parentId** (`str`): Parent group Primary Key
        * keyword **backgroundImage** (`str`): Name of background
          image filename, e.g. ``data_net.png``
    :rtype: dict
    """
    return self._get("/gms/group/{}".format(group_pk))


def update_gms_group(
    self,
    group_pk: str,
    group_name: str,
    background_image_file: str = "",
) -> bool:
    """Update appliance group in Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - group
          - POST
          - /gms/group/{id}

    :param group_pk: The appliance group identifier, e.g. ``3.Network``
        this cannot be changed from the original
    :type group_pk: str
    :param group_name: Name of the group. Must be unique.
    :type group_name: str
    :param background_image_file: Image filename for group,
        defaults to ""
    :type background_image_file: str, optional
    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    data = {
        "id": group_pk,
        "name": group_name,
        "backgroundImage": background_image_file,
    }

    return self._post(
        "/gms/group/{}".format(group_pk),
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def delete_gms_group(
    self,
    group_pk: str,
) -> bool:
    """Delete an appliance group

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - group
          - DELETE
          - /gms/group/{id}

    :param group_pk: The appliance group identifier, e.g. ``3.Network``
    :type group_pk: str
    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    return self._delete(
        "/gms/group/{}".format(group_pk),
        expected_status=[204],
        return_type="bool",
    )


def add_gms_group(
    self,
    group_name: str,
    parent_pk: str = "",
    background_image_file: str = "",
) -> bool:
    """Update appliance group in Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - group
          - POST
          - /gms/group/new

    :param group_name: Name of the group. Must be unique.
    :type group_name: str
    :param parent_pk: The appliance group identifier,
        e.g. ``3.Network``, "" will act as to root group, defaults to ""
    :type parent_pk: str, optional
    :param background_image_file: Image filename for group,
        defaults to ""
    :type background_image_file: str, optional
    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    data = {
        "name": group_name,
        "parentId": parent_pk,
        "backgroundImage": background_image_file,
    }

    return self._post(
        "/gms/group/new",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def get_root_gms_group(self) -> dict:
    """Get root appliance group

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - group
          - GET
          - /gms/group/root

    :return: Returns dictionary of root appliance group, ``0.Network``
    :rtype: dict
    """
    return self._get("/gms/group/root")


def get_all_appliance_locations(self) -> list:
    """Get all appliance graphical node location details (map position)

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - group
          - GET
          - /gms/grNode

    :return: Returns list of dictionaries with appliance details. \n
        [`dict`]: appliance detail object \n
            * keyword **id** (`str, optional`): ID, assigned by
              Orchestrator like ``1.GrNode``
            * keyword **groupId** (`str`): ID of the group belonged to
            * keyword **sourceId** (`str`): The source ID. For an
              appliance expect nePk values like ``3.NE``. For groups,
              expect group ID like ``10.Network``
            * keyword **appliance** (`bool`): ``True`` for an Appliance
              and ``False`` for Group
            * keyword **wx** (`int`): Coordinates X in map window
            * keyword **wy** (`int`): Coordinates Y in map window
            * keyword **latitude** (`float`): Latitude
            * keyword **longitude** (`float`): Longitude
    :rtype: list
    """
    return self._get("/gms/grNode")


def get_appliance_location(
    self,
    gr_node_pk: str,
) -> dict:
    """Get appliance graphical node location details (map position)

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - group
          - GET
          - /gms/grNode/{grNodePk}

    :param gr_node_pk: The appliance graphical node identifier,
        e.g. ``0.GrNode``
    :type gr_node_pk: str
    :return: Returns dictionary with appliance details \n
        * keyword **id** (`str, optional`): ID, assigned by
          Orchestrator, e.g. ``1.GrNode``
        * keyword **groupId** (`str`): ID of the group belonged to
        * keyword **sourceId** (`str`): The source ID. For an
          appliance expect nePk values like ``3.NE``. For groups, expect
          group ID like ``10.Network``
        * keyword **appliance** (`bool`): ``True`` for an Appliance and
          ``False`` for Group
        * keyword **wx** (`int`): Coordinates X in map window
        * keyword **wy** (`int`): Coordinates Y in map window
        * keyword **latitude** (`float`): Latitude
        * keyword **longitude** (`float`): Longitude
    :rtype: dict
    """
    return self._get("/gms/grNode/{}".format(gr_node_pk))


def update_appliance_location_grnodepk(
    self,
    gr_node_pk: str,
    wx: int,
    wy: int,
    latitude: float,
    longitude: float,
) -> bool:
    """Update appliance location graphical information by graphical
    node id

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - group
          - POST
          - /gms/grNode/{grNodePk}

    :param gr_node_pk: The appliance graphical node identifier,
        e.g. ``0.GrNode``
    :type gr_node_pk: str
    :param wx: X Coordinates in map window
    :type wx: int
    :param wy: Y Coordinates in map window
    :type wy: int
    :param latitude: Latitude coordinates
    :type latitude: float
    :param longitude: Latitude coordinates
    :type longitude: float
    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    data = {"wx": wx, "wy": wy, "latitude": latitude, "longitude": longitude}

    return self._post(
        "/gms/grNode/{}".format(gr_node_pk),
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def update_appliance_location_nepk(
    self,
    ne_pk: str,
    wx: int,
    wy: int,
    latitude: float,
    longitude: float,
) -> bool:
    """Update appliance location graphical information by Network
    Primary Key (nePk)

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - group
          - POST
          - /gms/grNode/forNePk/{nePk}

    :param ne_pk: Network Primary Key (nePk) of existing appliance,
        e.g. ``3.NE``
    :type ne_pk: str
    :param wx: X Coordinates in map window
    :type wx: int
    :param wy: Y Coordinates in map window
    :type wy: int
    :param latitude: Latitude coordinates
    :type latitude: float
    :param longitude: Latitude coordinates
    :type longitude: float
    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    data = {"wx": wx, "wy": wy, "latitude": latitude, "longitude": longitude}

    return self._post(
        "/gms/grNode/forNePk/{}".format(ne_pk),
        data=data,
        expected_status=[204],
        return_type="bool",
    )
