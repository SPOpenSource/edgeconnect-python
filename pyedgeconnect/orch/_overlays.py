# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# overlays : Add, update, delete overlay configurations
import requests


def get_all_overlays_config(self) -> list:
    """Get all configured overlays in Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - overlays
          - GET
          - /gms/overlays/config

    :return: Returns list of dictionaries of each overlay configuration
    :rtype: list
    """
    return self._get("/gms/overlays/config")


def configure_new_overlay(
    self,
    overlay_config: dict,
) -> requests.Response:
    """Configure a new overlay on Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - overlays
          - POST
          - /gms/overlays/config

    .. note::

        See Swagger for more details on constructing valid
        ``overlay_config`` parameter to pass.

    :param overlay_config: Full overlay configuration object
    :type overlay_config: dict
    :return: Returns full response details. On successful call will
        return newly created Overlay ID
    :rtype: Requests.response object
    """
    return self._post(
        "/gms/overlays/config",
        data=overlay_config,
        return_type="full_response",
    )


def get_all_overlays_config_keyed(self) -> dict:
    """Get all configured overlays in Orchestrator keyed by overlay ID
    and region ID

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - overlays
          - GET
          - /gms/overlays/config/regions

    :return: Returns dictionary of overlay configuration \n
        * keyword **<overlay_id** (`dict`): overlay object \n
            * keyword **<region_id** (`dict`): regional overlay config
    :rtype: dict
    """
    return self._get("/gms/overlays/config/regions")


def configure_regionalized_overlay(
    self,
    regional_overlay_config: list,
) -> requests.Response:
    """Use this API to create an exhaustive representation of
    regionalized overlays. The body of this request should be an array
    of map which keyed by region id whose value is regional overlay
    configuration.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - overlays
          - POST
          - /gms/overlays/config/regions

    .. note::

        See Swagger for more details on constructing valid
        ``regional_overlay_config`` parameter to pass.

    :param overlay_config: Full overlay configuration object
    :type overlay_config: dict
    :return: Returns full response details. On successful call will
        return newly created Overlay ID
    :rtype: Requests.response object
    """
    return self._post(
        "/gms/overlays/config/regions",
        data=regional_overlay_config,
        return_type="full_response",
    )


def modify_regionalized_overlay(
    self,
    regional_overlay_config: list,
) -> requests.Response:
    """Use this API to update an exhaustive representation of
    regionalized overlays. The body of this request should be a map
    keyed by overlayId whose value is a map of regionId to regional
    overlay configuration, use region_id ``0`` to update global overlay
    configuration.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - overlays
          - PUT
          - /gms/overlays/config/regions

    .. note::

        See Swagger for more details on constructing valid
        ``regional_overlay_config`` parameter to pass.

    :return: Returns full response details. On successful call will
        return newly created Overlay ID
    :rtype: Requests.response object
    """
    return self._put(
        "/gms/overlays/config/regions",
        data=regional_overlay_config,
        return_type="full_response",
    )


def get_overlay_config(
    self,
    overlay_id: int,
) -> dict:
    """Get overlay config by overlay ID from Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - overlays
          - GET
          - /gms/overlays/config/{overlayId}

    :param overlay_id: Numeric ID of overlay to retrieve
    :type overlay_id: int
    :return: Returns dictionary of overlay configuration
    :rtype: dict
    """
    return self._get("/gms/overlays/config/{}".format(overlay_id))


def modify_overlay_config(
    self,
    overlay_id: int,
    overlay_config: dict,
) -> requests.Response:
    """Use this API to update an existing overlay configuration. If you
    are using regions and have customized regional BIO per region, it
    will be overridden. To avoid this use the other PUT api which takes
    regionID as an input. Any changes made to the overlay configuration
    will be pushed to the appliances automatically.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - overlays
          - PUT
          - /gms/overlays/config/{overlayId}

    :param overlay_id: Numeric ID of overlay to retrieve
    :type overlay_id: int
    :param overlay_config: Full overlay configuration object
    :type overlay_config: dict
    :return: Returns full response details. On successful call will
        return newly created Overlay ID
    :rtype: Requests.response object
    """
    return self._put(
        "/gms/overlays/config/{}".format(overlay_id),
        data=overlay_config,
        return_type="full_response",
    )


def delete_overlay(
    self,
    overlay_id: int,
) -> dict:
    """Deletes the overlay from the Orchestrator. Removes any appliances
    from the overlay and deletes any reports specifically for this
    overlay.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - overlays
          - DELETE
          - /gms/overlays/config/{overlayId}

    :param overlay_id: Numeric ID of overlay to retrieve
    :type overlay_id: int
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        "/gms/overlays/config/{}".format(overlay_id),
        expected_status=[204],
        return_type="bool",
    )


def get_overlay_config_for_region(
    self,
    overlay_id: int,
    region_id: int,
) -> dict:
    """Get a particular regional overlay configuration, if using
    regionId ``0``, global overlay configuration is returned.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - overlays
          - GET
          - /gms/overlays/config/regions/{overlayId}/{regionId}

    :param overlay_id: Numeric ID of overlay to retrieve
    :type overlay_id: int
    :param region_id: Numeric ID of region to retrieve
    :type region_id: int
    :return: Returns dictionary of overlay configuration
    :rtype: dict
    """
    return self._get(
        "/gms/overlays/config/{}/{}".format(overlay_id, region_id)
    )


def modify_overlay_config_for_region(
    self,
    overlay_id: int,
    region_id: int,
    overlay_config: dict,
) -> requests.Response:
    """Use this API to update an existing overlay configuration, use
    region_id ``0`` to update global overlay configuration.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - overlays
          - PUT
          - /gms/overlays/config/regions/{overlayId}/{regionId}

    :param overlay_id: Numeric ID of overlay to retrieve
    :type overlay_id: int
    :param region_id: Numeric ID of region to retrieve
    :type region_id: int
    :param overlay_config: Full overlay configuration object
    :type overlay_config: dict
    :return: Returns dictionary of overlay configuration
    :rtype: dict
    """
    return self._put(
        "/gms/overlays/config/{}/{}".format(overlay_id, region_id),
        data=overlay_config,
        return_type="full_response",
    )


def get_max_overlays(
    self,
) -> dict:
    """Get max number of overlays

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - overlays
          - GET
          - /gms/overlays/config/maxNumOfOverlays

    :return: Returns dictionary of max overlays \n
        * keyword **max** (`int`): Maximum number of overlays that can
          be configured
    :rtype: dict
    """
    return self._get("/gms/overlays/maxNumOfOverlays")


def get_overlays_priorities(
    self,
) -> dict:
    """Get overlay priorities. Keys are overlay priority, values are the
    overlay id numbers.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - overlays
          - GET
          - /gms/overlays/priority

    .. code::

        >>> p = Orchestrator.get_overlays_priorities()
        >>> print(p)
        {"1": 5,"2": 6,"3": 7}

    In the example above, Overlay 5 has 1st priority, Overlay 6 is 2nd,
    and Overlay 7 is 3rd.

    :return: Returns dictionary of overlay priority \n
        * keyword **1** (`int`): Overlay ID with 1st priority
        * keyword **2** (`int, optional`): Overlay ID with 2nd priority
        * keyword **3** (`int, optional`): Overlay ID with 3rd priority
        * keyword **4** (`int, optional`): Overlay ID with 4th priority
        * keyword **5** (`int, optional`): Overlay ID with 5th priority
        * keyword **6** (`int, optional`): Overlay ID with 6th priority
        * keyword **7** (`int, optional`): Overlay ID with 7th priority
    :rtype: dict
    """
    return self._get("/gms/overlays/priority")


def set_overlays_priorities(
    self,
    overlay_prioirty: dict,
) -> dict:
    """Set overlay priorities. This affects the order of the different
    overlays' route maps. Keys are overlay priority, values are the
    overlay id numbers.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - overlays
          - POST
          - /gms/overlays/priority

    .. code::

        overlay_prioirty = {
            "1": 5,
            "2": 6,
            "3": 7,
        }

    In the example above, Overlay 5 has 1st priority, Overlay 6 is 2nd,
    and Overlay 7 is 3rd.

    .. note::

        Each overlay ID must have a unique priority. This function will
        overwrite existing priorities so it is best to first run
        :func:`~get_overlays_priorities` to account for all current
        overlay priorities.

    :return: Returns dictionary of overlay priority \n
    :rtype: dict
    """
    return self._post(
        "/gms/overlays/priority",
        data=overlay_prioirty,
        expected_status=[204],
        return_type="bool",
    )


def get_appliance_overlays_association(self) -> dict:
    """Get all appliance associations to Overlays

    .. note::

      This API Call is not in current Swagger as of Orch 9.0.3

    :return: Returns dictionary of overlay appliance associations \n
        * keyword **<overlay_id** (`list[str]`): List of associated
          appliance NePK's to overlay \n
    :rtype: dict
    """
    return self._get("/gms/overlays/association")
