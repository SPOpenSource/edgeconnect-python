# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# interfaceLabels : Save and delete labels for interfaces


def get_all_interface_labels(
    self,
    active: bool = None,
) -> dict:
    """Get all configured interface labels. Can filter response for
    active labels or inactive labels with ``active`` parameter.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - interfaceLabels
          - GET
          - /gms/interfaceLabels

    :param active: ``True`` to filter for active labels, ``False`` to
        filter for inactive labels.
    :type active: bool, optional
    :return: Returns dictionary of configured interface labels \n
        * keyword **wan** (`dict`): Dictionary of wan interface labels\n
            * keyword **<label_id>** (`dict`): Interface label id \n
                * keyword **name** (`str`): Name of interface label
                * keyword **topology** (`int`): Allowed topology for
                  building tunnels. ``0`` allows full mesh, ``2`` limits
                  to hub & spoke topology.
                * keyword **active** (`bool`): ``True`` if active,
                  ``False`` if inactive
        * keyword **lan** (`dict`): Dictionary of lan interface labels\n
            * keyword **<label_id>** (`dict`): Interface label id \n
                * keyword **name** (`str`): Name of interface label
                * keyword **topology** (`int`): Allowed topology for
                  building tunnels. ``0`` allows full mesh, ``2`` limits
                  to hub & spoke topology.
                * keyword **active** (`bool`): ``True`` if active,
                  ``False`` if inactive
    :rtype: dict
    """
    path = "/gms/interfaceLabels"

    if active is not None:
        path = path + "?active={}".format(active)

    return self._get(path)


def update_interface_labels(
    self,
    interface_label_config: dict,
    delete_dependencies: bool = None,
) -> bool:
    """Save interface labels, **NOTE** this will completely replace the
    current implementation. You cannot remove labels that are in use in
    an overlay. Label ids have to be unique across both wan and lan.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - interfaceLabels
          - POST
          - /gms/interfaceLabels

    **Example:**

    .. code-block::

        interface_label_config = {
            "wan": {
                "1": {
                "name": "MPLS1",
                "active": true,
                "topology": 0
                },
                "2": {
                "name": "INET1",
                "active": true,
                "topology": 0
                },
                "3": {
                "name": "LTE",
                "active": true,
                "topology": 2
                },
                "6": {
                "name": "INET2",
                "active": true,
                "topology": 0
                },
                "7": {
                "name": "MPLS2",
                "active": true,
                "topology": 0
                }
            },
            "lan": {
                "4": {
                "name": "Voice",
                "active": true,
                "topology": 0
                },
                "5": {
                "name": "Data",
                "active": true,
                "topology": 0
                }
            }
        }

    :param interface_label_config: Interface label configuration \n
        * keyword **wan** (`dict`): Dictionary of wan interface labels\n
            * keyword **<label_id>** (`dict`): Unique interface label id
              as a string integer, e.g. ``1`` \n
                * keyword **name** (`str`): Name of interface label
                * keyword **topology** (`int`): Allowed topology for
                  building tunnels. ``0`` allows full mesh, ``2`` limits
                  to hub & spoke topology.
                * keyword **active** (`bool`): ``True`` if active,
                  ``False`` if inactive
        * keyword **lan** (`dict`): Dictionary of lan interface labels\n
            * keyword **<label_id>** (`dict`): Unique interface label id
              as a string integer, e.g. ``1`` \n
                * keyword **name** (`str`): Name of interface label
                * keyword **topology** (`int`): Allowed topology for
                  building tunnels. ``0`` allows full mesh, ``2`` limits
                  to hub & spoke topology.
                * keyword **active** (`bool`): ``True`` if active,
                  ``False`` if inactive
    :type interface_label_config: dict
    :param delete_dependencies: ``True`` to delete labels from port
        profiles and templates using it, ``False`` to not remove them.
    :type delete_dependencies: bool, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    path = "/gms/interfaceLabels"

    if delete_dependencies is not None:
        path = path + "?deleteDependencies={}".format(delete_dependencies)

    return self._post(
        "/gms/interfaceLabels",
        data=interface_label_config,
        expected_status=[204],
        return_type="bool",
    )


def get_interface_labels_by_type(
    self,
    label_type: str,
    active: bool = None,
) -> dict:
    """Get all configured interface labels of either wan or lan. Can
    filter response for active labels or inactive labels with ``active``
    parameter.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - interfaceLabels
          - GET
          - /gms/interfaceLabels/{type}

    :param label_type: ``wan`` to return wan-related labels, ``lan`` to
        return lan-related labels
    :type label_type: str
    :param active: ``True`` to filter for active labels, ``False`` to
        filter for inactive labels.
    :type active: bool, optional
    :return: Returns dictionary of wan or lan interface labels \n
        * keyword **<label_id>** (`dict`): Interface label id \n
            * keyword **name** (`str`): Name of interface label
            * keyword **topology** (`int`): Allowed topology for
                building tunnels. ``0`` allows full mesh, ``2`` limits
                to hub & spoke topology.
            * keyword **active** (`bool`): ``True`` if active,
                ``False`` if inactive
    :rtype: dict
    """
    path = "/gms/interfaceLabels/{}".format(label_type)

    if active is not None:
        path = path + "?active={}".format(active)

    return self._get(path)


def push_interface_labels_to_appliance(
    self,
    ne_pk: str,
) -> dict:
    """Pushes the active interface labels on Orchestrator to an
    appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - interfaceLabels
          - POST
          - /interfaceLabels/{nePk}

    :param ne_pk: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_pk: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post("interfaceLabels/{}".format(ne_pk), return_type="bool")
