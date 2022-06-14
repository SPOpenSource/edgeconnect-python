# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# exception : Exception configuration
from __future__ import annotations


def get_tunnel_exceptions(
    self,
) -> list:
    """Get all configured tunnel exceptions

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - exception
          - GET
          - /exception/tunnel

    :return: Returns list of all tunnel exceptions \n
        [`dict`]: Tunnel exception object \n
            * keyword **id** (`int`): ID of tunnel exception entry
            * keyword **appliance_id_1** (`str`): NePk of appliance 1
            * keyword **interface_label_1** (`str`): Appliance 1
              interface label id
            * keyword **appliance_id_2** (`str`): NePk of appliance 2
            * keyword **interface_label_2** (`str`): Appliance 2
              interface label id
            * keyword **description** (`str`): Description of this
              tunnel exception
    :rtype: list
    """
    return self._get("/exception/tunnel")


def create_tunnel_exceptions(
    self,
    tunnel_exceptions: list[dict],
) -> list:
    """Configure a tunnel exception between appliances from all or
    specific interface labels.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - exception
          - POST
          - /exception/tunnel

    The interface label is the numeric id (as a string) of the interface
    label. These can be retrieved with
    :func:`pyedgeconnect.Orchestrator.get_all_interface_labels`
    The interface labels can also use the value of ``any`` to include
    all interface labels for that appliance. The description can be left
    as a blank string, but must be included in the body.

    **Example:**

    .. code-block::

        tunnel_exceptions = [
            {
                "appliance_id_1": "3.NE",
                "interface_label_1": "1",
                "appliance_id_2": "4.NE",
                "interface_label_2": "1",
                "description": "Exclude 3-4 on 1"
            },
            {
                "appliance_id_1": "5.NE",
                "interface_label_1": "any",
                "appliance_id_2": "6.NE",
                "interface_label_2": "any",
                "description": ""
            },
        ]

    :param tunnel_exceptions: List of tunnel exception pairings \n
        [`dict`]: Tunnel exception pair \n
            * keyword **appliance_id_1** (`str`): "77.NE",
            * keyword **interface_label_1** (`str`): "1",
            * keyword **appliance_id_2** (`str`): "80.NE",
            * keyword **interface_label_2** (`str`): "1",
            * keyword **description** (`str`): ""
    :type tunnel_exceptions: list[dict]
    :return: Returns list of the configured exception if success. If
        there is an existing exception with the same parameters the
        return list will be empty, ``[]`` \n
        [`dict`]: Tunnel exception object \n
            * keyword **id** (`int`): ID of tunnel exception entry
            * keyword **appliance_id_1** (`str`): NePk of appliance 1
            * keyword **interface_label_1** (`str`): Appliance 1
              interface label id
            * keyword **appliance_id_2** (`str`): NePk of appliance 2
            * keyword **interface_label_2** (`str`): Appliance 2
              interface label id
            * keyword **description** (`str`): Description of this
              tunnel exception
    :rtype: list
    """
    return self._post("/exception/tunnel", data=tunnel_exceptions)


def update_tunnel_exceptions(
    self,
    tunnel_exceptions: list[dict],
) -> bool:
    """Update one or multiple tunnel exceptions between appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - exception
          - PUT
          - /exception/tunnel

    The interface label is the numeric id (as a string) of the interface
    label. These can be retrieved with
    :func:`pyedgeconnect.Orchestrator.get_all_interface_labels`
    The interface labels can also use the value of ``any`` to include
    all interface labels for that appliance. The description can be left
    as a blank string, but must be included in the body.
    The existing tunnel exception ids can be retrieved with
    :func:`pyedgeconnect.Orchestrator.get_tunnel_exceptions`

    **Example:**

    .. code-block::

        tunnel_exceptions = [
            {
                "id": 5,
                "appliance_id_1": "3.NE",
                "interface_label_1": "1",
                "appliance_id_2": "4.NE",
                "interface_label_2": "1",
                "description": "Exclude 3-4 on 1"
            },
            {
                "id": 6,
                "appliance_id_1": "5.NE",
                "interface_label_1": "any",
                "appliance_id_2": "6.NE",
                "interface_label_2": "any",
                "description": ""
            },
        ]

    :param tunnel_exceptions: List of tunnel exception pairings \n
        [`dict`]: Tunnel exception pair \n
            * keyword **id** (`int`): ID of existing tunnel exception
            * keyword **appliance_id_1** (`str`): "77.NE",
            * keyword **interface_label_1** (`str`): "1",
            * keyword **appliance_id_2** (`str`): "80.NE",
            * keyword **interface_label_2** (`str`): "1",
            * keyword **description** (`str`): ""
    :type tunnel_exceptions: list[dict]
    :return: Returns True/False based on successful call
    :rtype: bool
    """

    return self._put(
        "/exception/tunnel",
        data=tunnel_exceptions,
        expected_status=[204],
        return_type="bool",
    )


def delete_all_tunnel_exceptions(
    self,
) -> bool:
    """Delete all configured tunnel exceptions

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - exception
          - DELETE
          - /exception/tunnel

    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        "/exception/tunnel",
        expected_status=[204],
        return_type="bool",
    )


def delete_tunnel_exceptions_list(self, exception_id_list: list[int]) -> bool:
    """Delete list of tunnel exceptions

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - exception
          - POST
          - /exception/tunnel/deleteByIds

    :param exception_id_list: List of tunnel exception ids to delete
    :type exception_id_list: list[int]
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/exception/tunnel/deleteByIds",
        return_type="bool",
    )


def update_single_tunnel_exception(
    self,
    exception_id: int,
    appliance_1_ne_pk: str,
    appliance_1_label: str,
    appliance_2_ne_pk: str,
    appliance_2_label: str,
    description: str = "",
) -> bool:
    """Update a tunnel exception between two appliances.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - exception
          - PUT
          - /exception/tunnel/{id}

    :param exception_id: ID of the existing tunnel exception to update
    :type exception_id: int
    :param appliance_1_ne_pk: Network Primary Key (nePk) of first
        appliance, e.g. ``3.NE``
    :type appliance_1_ne_pk: str
    :param appliance_1_label: Interface label id of first appliance for
        tunnel exception. Can use the value of ``any`` for all interface
        labels, e.g. ``2`` or ``any``
    :type appliance_1_label: str
    :param appliance_1_ne_pk: Network Primary Key (nePk) of second
        appliance, e.g. ``5.NE``
    :type appliance_2_ne_pk: str
    :param appliance_2_label: Interface label id of second appliance for
        tunnel exception. Can use the value of ``any`` for all interface
        labels, e.g. ``2`` or ``any``
    :type appliance_2_label: str
    :param description: Description/comment to include with exception
    :type description: str, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "appliance_id_1": appliance_1_ne_pk,
        "interface_label_1": appliance_1_label,
        "appliance_id_2": appliance_2_ne_pk,
        "interface_label_2": appliance_2_label,
        "description": description,
    }

    return self._put(
        "/exception/tunnel/{}".format(exception_id),
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def delete_single_tunnel_exception(self, exception_id: int) -> bool:
    """Delete specified tunnel exception by id

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - exception
          - DELETE
          - /exception/tunnel/{id}

    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        "/exception/tunnel/{}".format(exception_id),
        return_type="bool",
    )
