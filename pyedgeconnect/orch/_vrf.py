# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# vrf : Routing Segments
from __future__ import annotations


def get_routing_segmentation_enable_status(
    self,
) -> dict:
    """Get routing segmentation enable status in Orchestrator (VRFs)

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - vrf
          - GET
          - /vrf/config/enable

    :return: Returns dictionary with VRF enabled status \n
        * keyword **enable** (`bool`): ``True`` for enabled, ``False``
          for disabled
    :rtype: dict
    """
    return self._get("/vrf/config/enable")


def update_routing_segmentation_enable_status(
    self,
    enable: bool,
) -> bool:
    """Get routing segmentation enable status in Orchestrator (VRFs)

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - vrf
          - POST
          - /vrf/config/enable

    :param enable: ``True`` to enable routing segmentation. ``False`` to
        disable
    :type enable: bool
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {"enable": enable}

    return self._post(
        "/vrf/config/enable",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def get_routing_segmentation_segments(
    self,
) -> dict:
    """Get configured routing segmentation segments in Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - vrf
          - GET
          - /vrf/config/segments

    :return: Returns dictionary with configured segments \n
        * keyword **<segment_id>** (`dict`): Routing segment id, e.g.
          ``"0"`` \n
            * keyword **id** (`int`): Routing segment id
            * keyword **name** (`str`): Routing segment name
            * keyword **status** (`int`): No description in Swagger,
              often value of ``0``
            * keyword **comment** (`str`): Comment on routing segment
    :rtype: dict
    """
    return self._get("/vrf/config/segments")


def add_routing_segmentation_segment(
    self,
    segment_name: str,
) -> dict:
    """Add new routing segment to Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - vrf
          - POST
          - /vrf/config/segments

    :param segment_name: Name of new routing segment. Routing Segment
        name can only contain alphanumeric characters and underscores
    :type segment_name: str
    :return: Returns dictionary with id of new routing segment \n
        * keyword **id** (`int`): Numeric id of new routing segment
    :rtype: dict
    """
    data = {"name": segment_name}

    return self._post("/vrf/config/segments", data=data)


def get_routing_segmentation_segment_by_id(
    self,
    segment_id: int,
) -> dict:
    """Get routing segment in Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - vrf
          - GET
          - /vrf/config/segments/{id}

    :param segment_id: Numeric id of routing segment
    :type segment_id: int
    :return: Returns dictionary with segment details \n
        * keyword **id** (`int`): Routing segment id
        * keyword **name** (`str`): Routing segment name
        * keyword **status** (`int`): No description in Swagger,
            often value of ``0``
        * keyword **comment** (`str`): Comment on routing segment
    :rtype: dict
    """
    return self._get("/vrf/config/segments/{}".format(segment_id))


def update_routing_segmentation_segment_by_id(
    self,
    segment_id: int,
    new_segment_name: str,
) -> bool:
    """Update routing segment name in Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - vrf
          - PUT
          - /vrf/config/segments/{id}

    :param segment_id: Numeric id of routing segment
    :type segment_id: int
    :param new_segment_name: New name to assign to routing segment
    :type new_segment_name: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {"name": new_segment_name}

    return self._put(
        "/vrf/config/segments/{}".format(segment_id),
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def delete_routing_segmentation_segment_by_id(
    self,
    segment_id: int,
) -> bool:
    """Delete routing segment in Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - vrf
          - DELETE
          - /vrf/config/segments/{id}

    :param segment_id: Numeric id of routing segment
    :type segment_id: int
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        "/vrf/config/segments/{}".format(segment_id),
        expected_status=[204],
        return_type="bool",
    )


def get_routing_segmentation_maps(
    self,
) -> dict:
    """Get all D-NAT policies configured in Orchestrator by segment

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - vrf
          - GET
          - /vrf/config/maps

    :return: Returns dictionary keyed by segment id of D-NAT maps \n
        * keyword **<segment_id>** (`dict`): Routing segment D-NAT
          maps \n
            * keyword **<priority_number>** (`dict`): D-NAT rule
              object \n
                * keyword **match** (`dict`): Match object \n
                    * keyword **acl** (`str`): ACL to match against
                    * keyword **matchstr** (`dict`): Matching ip
                      object \n
                        * keyword **dst_ip** (`str`): Destination IP
                * keyword **set** (`dict`): Set action object \n
                    * keyword **dst_vrf** (`str`): Destination VRF id
                    * keyword **trans_dst_ip** (`str`): Translated IP
                * keyword **comment** (`str`): Rule comment
                * keyword **enable** (`bool`): Rule enable status
                * keyword **gms_marked** (`bool`): Flag to determine if
                  this rule was created by Orchestrator
                * keyword **misc** (`str`): No description in Swagger
    :rtype: dict
    """
    return self._get("/vrf/config/maps")


def get_routing_segmentation_maps_from_source_segment(
    self,
    segment_id: int,
) -> dict:
    """Get all D-NAT policies configured in Orchestrator for specific
    source segment

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - vrf
          - GET
          - /vrf/config/maps/{srcSegmentId}

    :param segment_id: Numeric id of routing segment
    :type segment_id: int
    :return: Returns dictionary keyed by priority number of each rule
        for D-NAT map \n
        * keyword **<priority_number>** (`dict`): D-NAT rule
          object \n
            * keyword **match** (`dict`): Match object \n
                * keyword **acl** (`str`): ACL to match against
                * keyword **matchstr** (`dict`): Matching ip
                  object \n
                    * keyword **dst_ip** (`str`): Destination IP
            * keyword **set** (`dict`): Set action object \n
                * keyword **dst_vrf** (`str`): Destination VRF id
                * keyword **trans_dst_ip** (`str`): Translated IP
            * keyword **comment** (`str`): Rule comment
            * keyword **enable** (`bool`): Rule enable status
            * keyword **gms_marked** (`bool`): Flag to determine if this
              rule was created by Orchestrator
            * keyword **misc** (`str`): No description in Swagger
    :rtype: dict
    """
    return self._get("/vrf/config/maps/{}".format(segment_id))


def update_routing_segmentation_maps_from_source_segment(
    self,
    segment_id: int,
    segment_map: dict,
) -> bool:
    """Update D-NAT policies for specific source segment

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - vrf
          - POST
          - /vrf/config/maps/{srcSegmentId}

    .. warning::

        This will replace all D-NAT map rules for this source segment!

    :param segment_id: Numeric id of routing segment
    :type segment_id: int
    :param segment_map: Dictionary of segment map to configure \n
        * keyword **<priority_number>** (`dict`): D-NAT rule
            object \n
            * keyword **match** (`dict`): Match object \n
                * keyword **acl** (`str`): ACL to match against
                * keyword **matchstr** (`dict`): Matching ip
                    object \n
                    * keyword **dst_ip** (`str`): Destination IP
            * keyword **set** (`dict`): Set action object \n
                * keyword **dst_vrf** (`str`): Destination VRF id
                * keyword **trans_dst_ip** (`str`): Translated IP
            * keyword **comment** (`str`): Rule comment
            * keyword **enable** (`bool`): Rule enable status
            * keyword **gms_marked** (`bool`): Flag to determine if this
              rule was created by Orchestrator
            * keyword **misc** (`str`): No description in Swagger
    :type segment_map: dict
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/vrf/config/maps/{}".format(segment_id),
        data=segment_map,
        expected_status=[204],
        return_type="bool",
    )


def delete_routing_segmentation_maps_from_source_segment(
    self,
    segment_id: int,
) -> bool:
    """Delete D-NAT policies for specific source segment

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - vrf
          - DELETE
          - /vrf/config/maps/{srcSegmentId}

    :param segment_id: Numeric id of routing segment
    :type segment_id: int
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        "/vrf/config/maps/{}".format(segment_id),
        expected_status=[204],
        return_type="bool",
    )


def get_routing_segmentation_security_policy(
    self,
    source_zone: str,
    destination_zone: str,
) -> dict:
    """Get all security policies configured on Orchestrator for a
    particular pair source and destination segments

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - vrf
          - GET
          - /vrf/config/securityPolicies/{map}

    :param source_zone: Numeric string id of source segment, e.g. ``0``
    :type source_zone: int
    :param destination_zone: Numeric string id of destination segment,
        e.g. ``0``
    :type destination_zone: int
    :return: Returns dictionary of applicable maps and details
    :rtype: dict
    """
    return self._get(
        "/vrf/config/securityPolicies/{}_{}".format(
            source_zone, destination_zone
        )
    )


def update_routing_segmentation_security_policy(
    self,
    source_zone: str,
    destination_zone: str,
    segment_map: dict,
) -> bool:
    """Update security policies configured on Orchestrator for a
    particular pair source and destination segments

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - vrf
          - POST
          - /vrf/config/securityPolicies/{map}

    Refer to Swagger for more details of security map. Example structure
    of security map:

    .. code-block::

        segment_map = {
            "data": {
                "map1": {
                    "<zoneFromId_zoneToId>": {
                        "prio": {
                            "<priorityNumber>": {
                                "match": "object",
                                "misc": "object",
                                "comment": "",
                                "gms_marked": false,
                                "set": "object"
                            }
                        }
                    }
                }
            },
            "settings": {
                "map1": {
                    "logging": {
                        "imp_fw_drop": ""
                    }
                }
            },
            "options": {
                "merge": false,
                "templateApply": false
            }
        }

    :param source_zone: Numeric string id of source segment, e.g. ``0``
    :type source_zone: int
    :param destination_zone: Numeric string id of destination segment,
        e.g. ``0``
    :type destination_zone: int
    :param segment_map: Security map details, see above example. Note
        that the `<zoneFromId_zoneToId>` under the map are the firewall
        zones and not related to the segment ids.
    :type segment_map: dict
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/vrf/config/securityPolicies/{}_{}".format(
            source_zone, destination_zone
        ),
        data=segment_map,
        expected_status=[204],
        return_type="bool",
    )


def get_routing_segmentation_list_of_security_maps(
    self,
) -> list[str]:
    """Get all security map pairings where there are rules for
    source/destination routing segments

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - vrf
          - GET
          - /vrf/config/securityPoliciesSegments

    :return: Returns list of strings of map pairings, e.g. ``0_0`` for
        if there is a security map for default to default segment
    :rtype: list[str]
    """
    return self._get("/vrf/config/securityPoliciesSegments")


def get_routing_segmentation_snat_maps(
    self,
) -> dict:
    """Get all disabled inter-segment S-NAT rules defined in
    Orchestrator. By default S-NAT is enabled between routing segments.
    If there are no rules will return an empty dictionary ``{}``.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - vrf
          - GET
          - /vrf/config/snatMaps

    :return: Returns dictionary of disabled S-NAT rules between
        segments \n
        * keyword **<SourceVrfId_DstVrfId>** (`dict`): Segment pair
          object of source and destination VRF ids, e.g. ``0_1`` \n
            * keyword **enable** (`bool`): ``False`` if S-NAT is
              disabled
            * keyword **gms_marked** (`bool`): Flag to determine if this
              rule was created by Orchestrator
            * keyword **comment** (`str`): Comment on rule
    :rtype: dict
    """
    return self._get("/vrf/config/snatMaps")


def update_routing_segmentation_snat_maps(
    self,
    snat_maps: dict,
) -> dict:
    """Update all disabled inter-segment S-NAT rules defined in
    Orchestrator. By default S-NAT is enabled between routing segments.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - vrf
          - POST
          - /vrf/config/snatMaps

    .. warning::

        This will replace all disabled S-NAT map rules so include
        existing rules to avoid making unintended changes!

    :param snat_maps: Dictionary of S-NAT maps to disable between
        specified VRF ids \n
        * keyword **<SourceVrfId_DstVrfId>** (`dict`): VRF pair \n
            * keyword **enable** (`bool`): ``True`` to enable S-NAT for
              the source/destination pair, ``False`` to disable.
    :type snat_maps: dict
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/vrf/config/snatMaps",
        data=snat_maps,
        expected_status=[204],
        return_type="bool",
    )
