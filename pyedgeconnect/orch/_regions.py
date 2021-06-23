# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# regions : Set or get regions and region appliance associations


def get_all_regions(self) -> dict:
    """Get all regions

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - regions
          - GET
          - /regions

    :return: Returns dictionary of configured regions
    :rtype: dict
    """
    return self._get("/regions")


def create_region(
    self,
    region: str,
) -> bool:
    """Create a new region

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - regions
          - POST
          - /regions

    :param region: Name of the new region to be created
    :type region: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {"regionName": region}

    return self._post(
        "/regions",
        data=data,
        return_type="bool",
    )


def get_region(
    self,
    region_id: int,
) -> dict:
    """Get region by ID

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - regions
          - GET
          - /regions/{regionId}

    :param region_id: Numeric ID of region
    :type region_id: int
    :return: Returns dictionary of region
    :rtype: dict
    """
    return self._get("/regions/{}".format(region_id))


def update_region_name(
    self,
    region_id: int,
    region_name: str,
) -> bool:
    """Update the name of an existing region

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - regions
          - PUT
          - /regions/{regionId}

    :param region_id: Numeric ID of region
    :type region_id: int
    :param region_name: New name of the region
    :type region_name: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._put(
        "/regions/{}".format(region_id),
        expected_status=[204],
        return_type="bool",
    )


def delete_region(
    self,
    region_id: int,
) -> bool:
    """Delete a region by region ID

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - regions
          - DELETE
          - /regions/{regionId}

    :param region_id: Numeric ID of region
    :type region_id: int
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        "/regions/{}".format(region_id),
        expected_status=[204],
        return_type="bool",
    )


def get_region_appliance_association(self) -> dict:
    """Get all appliance/region associations

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - regions
          - GET
          - /regions/appliances

    :return: Returns dictionary of appliance associations to regions
    :rtype: dict
    """
    return self._get("/regions/appliances")


def set_region_appliance_association(
    self,
    appliance_region_map: dict,
) -> bool:
    """Set association between appliances and regions. Can set one or
    many associations.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - regions
          - POST
          - /regions/appliances

    :param appliance_region_map: Dictionary where each key/value pair is
        an appliance nePk (e.g. ``3.NE``) and region_id.
        e.g. {"3.NE":"1", "10.NE","2",...}
    :type appliance_region_map: dict
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/regions",
        data=appliance_region_map,
        expected_status=[204],
        return_type="bool",
    )


def update_region_appliance_association(
    self,
    ne_pk: str,
    region_id: int,
) -> bool:
    """Update association between appliance and regions.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - regions
          - PUT
          - /regions/appliances/{nePk}

    :param ne_pk: Network Primary Key (nePk) of existing appliance,
        e.g. ``3.NE``
    :type ne_pk: str
    :param region_id: Numeric ID of region
    :type region_id: int
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {"regionId": region_id}

    return self._put(
        "/regions/appliances/{}".format(ne_pk),
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def get_region_appliance_association_by_nepk(
    self,
    ne_pk: str,
) -> dict:
    """Get appliance/region association by nePk of appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - regions
          - GET
          - /regions/appliances/nePk/{nePk}

    :param ne_pk: Network Primary Key (nePk) of existing appliance,
        e.g. ``3.NE``
    :type ne_pk: str
    :return: Returns dictionary of appliance association to region \n
        * keyword **nePk** (`str`): Appliance NePK, e.g. ``3.NE``
        * keyword **regionId** (`int`): Region ID, ``0`` is default
        * keyword **regionName** (`str`): Region name
    :rtype: dict
    """
    return self._get("/regions/appliances/nePk/{}".format(ne_pk))


def get_region_appliance_association_by_region_id(
    self,
    region_id: int,
) -> dict:
    """Get all appliances associated with region

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - regions
          - GET
          - /regions/appliances/regionId/{regionId}

    :param region_id: Numeric ID of region
    :type region_id: int
    :return: Returns dictionary of appliances associated to region
    :rtype: dict
    """
    return self._get("/regions/appliances/regionId/{}".format(region_id))
