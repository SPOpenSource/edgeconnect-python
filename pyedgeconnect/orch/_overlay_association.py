# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# overlayAssociation : Add and remove appliances from overlays


def get_all_appliance_overlay_association(
    self,
) -> dict:
    """Get list of appliances associated with each overlay

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - overlayAssociation
          - GET
          - /gms/overlays/association

    :return: Returns dictionary of each overlay with associated
        appliances \n
        * keyword **<overlay_id>** (`list[str]`): \n
            * [`str`]: Appliance NePK ID's that are associated with the
              overlay, e.g. ``["3.NE","5.NE"]``
    :rtype: dict
    """
    return self._get("/gms/overlays/association")


def add_appliance_overlay_association(
    self,
    appliance_overlay_map: dict,
) -> bool:
    """Add appliances to overlays

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - overlayAssociation
          - POST
          - /gms/overlays/association

    :param appliance_overlay_map: Dictionary using overlay ID's as keys
        and values as list of appliance NePK values to associate to the
        overlays \n
            * keyword **<overlay_id>** (`list[str]`): \n
                * [`str`]: Appliance NePK ID's that are associated with
                  the overlay, e.g. ``["3.NE","5.NE"]``
    :type appliance_overlay_map: dict
    :return: Returns True/False based on successful call
    :rtype: bool

    **Example Dictionary:** \n
    {"1": ["834.NE"], "2": ["834.NE"]} \n
    This would add appliance ``834.NE`` to overlays with overlay ids of
    ``1`` and ``2``. \n
    """
    return self._post(
        "/gms/overlays/association",
        data=appliance_overlay_map,
        expected_status=[204],
        return_type="bool",
    )


def remove_appliance_overlay_association(
    self,
    appliance_overlay_map: dict,
) -> bool:
    """Remove appliances from overlays

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - overlayAssociation
          - POST
          - /gms/overlays/association/remove

    :param appliance_overlay_map: Dictionary using overlay ID's as keys
        and values as list of appliance NePK values to remove from the
        overlays \n
            * keyword **<overlay_id>** (`list[str]`): \n
                * [`str`]: Appliance NePK ID's that are associated with
                  the overlay, e.g. ``["3.NE","5.NE"]``
    :type appliance_overlay_map: dict
    :return: Returns True/False based on successful call
    :rtype: bool

    **Example Dictionary:** \n
    {"1": ["834.NE"], "2": ["834.NE"]} \n
    This would add appliance ``834.NE`` to overlays with overlay ids of
    ``1`` and ``2``.
    """
    return self._post(
        "/gms/overlays/association/remove",
        data=appliance_overlay_map,
        expected_status=[204],
        return_type="bool",
    )


def get_appliance_overlay_association(
    self,
    overlay_id: str,
) -> dict:
    """Get appliances associated with a specific overlay

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - overlayAssociation
          - GET
          - /gms/overlays/association/{overlayId}

    :param overlay_id: Overlay id to retrieve associated appliances,
        e.g. ``1``
    :type overlay_id: str
    :return: Returns dictionary of specific overlay with associated
        appliances \n
        * keyword **<overlay_id>** (`list[str]`): \n
            * [`str`]: Appliance NePK ID's that are associated with the
              overlay, e.g. ``["3.NE","5.NE"]``
    :rtype: dict
    """
    return self._get("/gms/overlays/association/{}".format(overlay_id))


def remove_single_appliance_overlay_association(
    self,
    overlay_id: str,
    ne_pk: str,
) -> bool:
    """Get appliances associated with a specific overlay

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - overlayAssociation
          - DELETE
          - /gms/overlays/association/{overlayId}

    :param overlay_id: Overlay id to retrieve associated appliances,
        e.g. ``1``
    :type overlay_id: str
    :param ne_pk: Network Primary Key (nePk) of existing appliance,
        e.g. ``3.NE``
    :type ne_pk: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        "/gms/overlays/association/{}/{}".format(overlay_id, ne_pk),
        expected_status=[204],
        return_type="bool",
    )
