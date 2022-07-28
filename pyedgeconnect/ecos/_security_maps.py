# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# securityMaps : Manage Security Policies


def get_appliance_security_policies(
    self,
) -> dict:
    """Get appliance security policies

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - securityMaps
          - GET
          - /securityMaps

    :return: Returns dictionary of current appliance security policy \n
        * keyword **map1** (`dict`): Security policy object \n
            * keyword **<zone_pair>** (`dict`): Security policy between
              two zones, the zone pair is represented by a string of the
              source and destination zone ids e.g. If a zone
              ``CorpUsers`` in Default segment has an id of ``5`` and a
              zone ``IOT`` in Default segment has an id of ``6`` the
              zone pair would be ``5_6`` \n
                * keyword **prio** (`dict`): Security policy rules \n
                    * keyword **<priority_number>** (`dict`): A security
                      rule \n
                        * keyword **comment** (`str`):
                        * keyword **gms_marked** (`bool`): ``True`` if
                          rule is created by Orchestrator
                        * keyword **match** (`dict`): Rule match
                          criteria. Keywords are optional for desired
                          match criteria \n
                            * keyword **acl** (`str`): ACL name
                            * keyword **src_ip** (`str`): Source IP
                            * keyword **dst_ip** (`str`): Dest IP
                            * keyword **either_ip** (`str`): Either
                              Source or Dest IP
                            * keyword **src_addrgrp_groups** (`str`):
                              Source address group
                            * keyword **dst_addrgrp_groups** (`str`):
                              Dest address group
                            * keyword **either_addrgrp_groups** (`str`):
                              Either address group
                            * keyword **protocol** (`str`): Protocol
                            * keyword **src_port** (`str`): Source port
                            * keyword **dst_port** (`str`): Dest port
                            * keyword **vlan** (`str`): Vlan
                            * keyword **application** (`str`):
                              Application name
                            * keyword **app_group** (`str`):
                              Application group name
                            * keyword **dscp** (`str`):
                              DSCP marking
                            * keyword **src_dns** (`str`):
                              Source domain name
                            * keyword **dst_dns** (`str`):
                              Dest domain name
                            * keyword **either_dns** (`str`):
                              Either domain name
                            * keyword **src_geo** (`str`):
                              Source geo-location
                            * keyword **dst_geo** (`str`):
                              Dest geo-location
                            * keyword **either_geo** (`str`):
                              Either geo-location
                            * keyword **src_service** (`str`):
                              Source service
                            * keyword **dst_service** (`str`):
                              Destination service
                            * keyword **either_service** (`str`):
                              Either service
                            * keyword **tbehavior** (`str`):
                              Traffic behavior
                            * keyword **overlay** (`str`):
                              Overlay name
                            * keyword **internet** (`str`):
                              Internet or Fabric
                        * keyword **misc** (`dict`): Rule enablement and
                          logging settings \n
                            * keyword **rule** (`str`): ``enable`` if
                              rule is enabled,  ``disable`` if disabled
                            * keyword **logging_priority** (`str`):
                              Logging facility for rule
                              ``0`` translates to ``None``,
                              ``1`` translates to ``Emergency``,
                              ``2`` translates to ``Alert``,
                              ``3`` translates to ``Critical``,
                              ``4`` translates to ``Error``,
                              ``5`` translates to ``Warning``,
                              ``6`` translates to ``Notice``,
                              ``7`` translates to ``Info``,
                              ``8`` translates to ``Debug``,
                            * keyword **logging** (`str`): ``enable`` to
                              enable logging, ``disable`` to disable
                              logging
                        * keyword **set** (`dict`): Action object \n
                            * keyword **action** (`str`): Rule action,
                              e.g. ``allow``, ``deny``, and ``inspect``
                              for ids allow and inspect action
    :rtype: dict
    """
    return self._get("/securityMaps")


def configure_appliance_security_policies(
    self,
    security_policy: dict,
) -> dict:
    """Configure appliance security policies. Use
    :func:`~pyedgeconnect.EdgeConnect.get_appliance_security_policies`
    to retrieve policy from an existing EdgeConnect appliance to
    reference data structure and example values.

    .. note::
        The easiest way to identify zones along with relationship to
        Segments if Segmentation is enabled is through Orchestrator.
        Use :func:`~pyedgeconnect.Orchestrator.get_zones_vrf_mapping`
        which will return per-Segment/VRF the IDs and names of related
        security zones.

        :func:`~pyedgeconnect.Orchestrator.get_zones` with parameter
        ``all_vrf_zones`` will return all Zone IDs but not the mapping
        of which ID belongs to which Segment/VRF.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - securityMaps
          - POST
          - /securityMaps

    :param security_policy: Full security policy to upload to
        EdgeConnect appliance. Use
        :func:`~pyedgeconnect.EdgeConnect.get_appliance_security_policies`
        to retrieve policy from an existing EdgeConnect appliance to
        reference data structure and example values
    :type security_policy: dict
    :return: Returns True/False based on successful call
    :rtype: bool
    """  # noqa:W505
    return self._post(
        "/securityMaps",
        data=security_policy,
        return_type="bool",
    )


def get_appliance_security_policy_map(
    self,
    map_name: str = "map1",
) -> dict:
    """Get appliance security policy map

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - securityMaps
          - GET
          - /securityMaps/{mapName}

    :param map_name: Name of security map to retrieve, Defaults to
        ``map1`` as the primary map on appliances if security policy
        is configured, Defaults to ``map1``
    :type map_name: str, optional
    :return: Returns dictionary of current appliance security policy \n
        * keyword **<zone_pair>** (`dict`): Security policy between two
          zones, the zone pair is represented by a string of the source
          and destination zone ids e.g. If a zone ``CorpUsers`` in
          Default segment has an id of ``5`` and a zone ``IOT`` in
          Default segment has an id of ``6`` the zone pair would be
          ``5_6`` \n
            * keyword **prio** (`dict`): Security policy rules \n
                * keyword **<priority_number>** (`dict`): A security
                  rule \n
                    * keyword **comment** (`str`):
                    * keyword **gms_marked** (`bool`): ``True`` if rule
                      is created by Orchestrator
                    * keyword **match** (`dict`): Rule match criteria.
                      Keywords are optional for desired match criteria\n
                        * keyword **acl** (`str`): ACL name
                        * keyword **src_ip** (`str`): Source IP
                        * keyword **dst_ip** (`str`): Dest IP
                        * keyword **either_ip** (`str`): Either Source
                          or Dest IP
                        * keyword **src_addrgrp_groups** (`str`): Source
                          address group
                        * keyword **dst_addrgrp_groups** (`str`): Dest
                          address group
                        * keyword **either_addrgrp_groups** (`str`):
                          Either address group
                        * keyword **protocol** (`str`): Protocol
                        * keyword **src_port** (`str`): Source port
                        * keyword **dst_port** (`str`): Dest port
                        * keyword **vlan** (`str`): Vlan
                        * keyword **application** (`str`): Application
                          name
                        * keyword **app_group** (`str`): Application
                          group name
                        * keyword **dscp** (`str`): DSCP marking
                        * keyword **src_dns** (`str`): Source domain
                          name
                        * keyword **dst_dns** (`str`): Dest domain name
                        * keyword **either_dns** (`str`): Either domain
                          name
                        * keyword **src_geo** (`str`): Source
                          geo-location
                        * keyword **dst_geo** (`str`): Dest geo-location
                        * keyword **either_geo** (`str`): Either
                          geo-location
                        * keyword **src_service** (`str`): Source
                          service
                        * keyword **dst_service** (`str`): Destination
                          service
                        * keyword **either_service** (`str`): Either
                          service
                        * keyword **tbehavior** (`str`): Traffic
                          behavior
                        * keyword **overlay** (`str`): Overlay name
                        * keyword **internet** (`str`): Internet or
                          Fabric
                    * keyword **misc** (`dict`): Rule enablement and
                      logging settings \n
                        * keyword **rule** (`str`): ``enable`` if rule
                          is enabled,  ``disable`` if disabled
                        * keyword **logging_priority** (`str`):
                          Logging facility for rule
                          ``0`` translates to ``None``,
                          ``1`` translates to ``Emergency``,
                          ``2`` translates to ``Alert``,
                          ``3`` translates to ``Critical``,
                          ``4`` translates to ``Error``,
                          ``5`` translates to ``Warning``,
                          ``6`` translates to ``Notice``,
                          ``7`` translates to ``Info``,
                          ``8`` translates to ``Debug``,
                        * keyword **logging** (`str`): ``enable`` to
                          enable logging, ``disable`` to disable logging
                    * keyword **set** (`dict`): Action object \n
                        * keyword **action** (`str`): Rule action,
                          e.g. ``allow``, ``deny``, and ``inspect``
                          for ids allow and inspect action
    :rtype: dict
    """
    return self._get(f"/securityMaps/{map_name}")


def get_appliance_security_policy_zone_pair(
    self,
    zone_pair: str,
    map_name: str = "map1",
) -> dict:
    """Get appliance security policy map for particular zone pair.
    Security policy between two zones, the zone pair is represented by a
    string of the source and destination zone ids e.g. If a zone
    ``CorpUsers`` in Default segment has an id of ``5`` and a zone
    ``IOT`` in Default segment has an id of ``6`` the zone pair would be
    ``5_6``.

    .. note::
        The easiest way to identify zones along with relationship to
        Segments if Segmentation is enabled is through Orchestrator.
        Use :func:`~pyedgeconnect.Orchestrator.get_zones_vrf_mapping`
        which will return per-Segment/VRF the IDs and names of related
        security zones.

        :func:`~pyedgeconnect.Orchestrator.get_zones` with parameter
        ``all_vrf_zones`` will return all Zone IDs but not the mapping
        of which ID belongs to which Segment/VRF.


    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - securityMaps
          - GET
          - /securityMaps/{mapName}/{zoneMap}

    :param zone_pair: String representation of zone pairing, e.g.
        ``5_6``
    :type zone_pair: str
    :param map_name: Name of security map to retrieve, Defaults to
        ``map1`` as the primary map on appliances if security policy
        is configured, Defaults to ``map1``
    :type map_name: str, optional
    :return: Returns dictionary of current appliance security policy of
        particular zone pair \n
        * keyword **prio** (`dict`): Security policy rules \n
            * keyword **<priority_number>** (`dict`): A security rule \n
                * keyword **comment** (`str`):
                * keyword **gms_marked** (`bool`): ``True`` if rule is
                  created by Orchestrator
                * keyword **match** (`dict`): Rule match criteria.
                  Keywords are optional for desired match criteria \n
                    * keyword **acl** (`str`): ACL name
                    * keyword **src_ip** (`str`): Source IP
                    * keyword **dst_ip** (`str`): Dest IP
                    * keyword **either_ip** (`str`): Either Source or
                      Dest IP
                    * keyword **src_addrgrp_groups** (`str`): Source
                      address group
                    * keyword **dst_addrgrp_groups** (`str`): Dest
                      address group
                    * keyword **either_addrgrp_groups** (`str`): Either
                      address group
                    * keyword **protocol** (`str`): Protocol
                    * keyword **src_port** (`str`): Source port
                    * keyword **dst_port** (`str`): Dest port
                    * keyword **vlan** (`str`): Vlan
                    * keyword **application** (`str`): Application name
                    * keyword **app_group** (`str`): Application group
                      name
                    * keyword **dscp** (`str`): DSCP marking
                    * keyword **src_dns** (`str`): Source domain name
                    * keyword **dst_dns** (`str`): Dest domain name
                    * keyword **either_dns** (`str`): Either domain name
                    * keyword **src_geo** (`str`): Source geo-location
                    * keyword **dst_geo** (`str`): Dest geo-location
                    * keyword **either_geo** (`str`): Either
                      geo-location
                    * keyword **src_service** (`str`): Source service
                    * keyword **dst_service** (`str`): Destination
                      service
                    * keyword **either_service** (`str`): Either service
                    * keyword **tbehavior** (`str`): Traffic behavior
                    * keyword **overlay** (`str`): Overlay name
                    * keyword **internet** (`str`): Internet or Fabric
                * keyword **misc** (`dict`): Rule enablement and
                  logging settings \n
                    * keyword **rule** (`str`): ``enable`` if rule is
                      enabled,  ``disable`` if disabled
                    * keyword **logging_priority** (`str`): Logging
                      facility for rule
                      ``0`` translates to ``None``,
                      ``1`` translates to ``Emergency``,
                      ``2`` translates to ``Alert``,
                      ``3`` translates to ``Critical``,
                      ``4`` translates to ``Error``,
                      ``5`` translates to ``Warning``,
                      ``6`` translates to ``Notice``,
                      ``7`` translates to ``Info``,
                      ``8`` translates to ``Debug``,
                    * keyword **logging** (`str`): ``enable`` to enable
                      logging, ``disable`` to disable logging
                * keyword **set** (`dict`): Action object \n
                    * keyword **action** (`str`): Rule action, e.g.
                      ``allow``, ``deny``, and ``inspect`` for ids allow
                      and inspect action
    :rtype: dict
    """
    return self._get(f"/securityMaps/{map_name}/{zone_pair}")


def delete_appliance_security_policy_zone_pair(
    self,
    zone_pair: str,
    map_name: str = "map1",
) -> bool:
    """Delete zone pair from appliance security policy

    .. note::
        The easiest way to identify zones along with relationship to
        Segments if Segmentation is enabled is through Orchestrator.
        Use :func:`~pyedgeconnect.Orchestrator.get_zones_vrf_mapping`
        which will return per-Segment/VRF the IDs and names of related
        security zones.

        :func:`~pyedgeconnect.Orchestrator.get_zones` with parameter
        ``all_vrf_zones`` will return all Zone IDs but not the mapping
        of which ID belongs to which Segment/VRF.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - securityMaps
          - DELETE
          - /securityMaps/{mapName}/{zoneMap}

    :param zone_pair: String representation of zone pairing, e.g.
        ``5_6``
    :type zone_pair: str
    :param map_name: Name of security map to retrieve, Defaults to
        ``map1`` as the primary map on appliances if security policy
        is configured, Defaults to ``map1``
    :type map_name: str, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        f"/securityMaps/{map_name}/{zone_pair}",
        return_type="bool",
    )


def delete_appliance_security_policy_rule(
    self,
    rule_priority: int,
    zone_pair: str,
    map_name: str = "map1",
) -> bool:
    """Delete security policy rule from appliance by priority number

    .. note::
        The easiest way to identify zones along with relationship to
        Segments if Segmentation is enabled is through Orchestrator.
        Use :func:`~pyedgeconnect.Orchestrator.get_zones_vrf_mapping`
        which will return per-Segment/VRF the IDs and names of related
        security zones.

        :func:`~pyedgeconnect.Orchestrator.get_zones` with parameter
        ``all_vrf_zones`` will return all Zone IDs but not the mapping
        of which ID belongs to which Segment/VRF.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - securityMaps
          - DELETE
          - /securityMaps/{mapName}/{zoneMap}/{priority}

    :param rule_priority: Rule priority number to delete
    :type rule_priority: int
    :param zone_pair: String representation of zone pairing, e.g.
        ``5_6``
    :type zone_pair: str
    :param map_name: Name of security map to retrieve, Defaults to
        ``map1`` as the primary map on appliances if security policy
        is configured, Defaults to ``map1``
    :type map_name: str, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        f"/securityMaps/{map_name}/{zone_pair}/{rule_priority}",
        return_type="bool",
    )


def get_appliance_security_policy_settings(
    self,
) -> dict:
    """Get appliance security policy settings for implicit drop logging

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - securityMaps
          - GET
          - /securityMapsSettings

    :return: Returns dictionary of current appliance security policy of
        particular zone pair \n
        * keyword **map1** (`dict`): Security policy map \n
            * keyword **logging** (`dict`): Logging settings object \n
                * keyword **imp_fw_drop** (`int`): Logging level for
                  implicit deny drops inter-zone.
                  ``0`` translates to ``None``,
                  ``1`` translates to ``Emergency``,
                  ``2`` translates to ``Alert``,
                  ``3`` translates to ``Critical``,
                  ``4`` translates to ``Error``,
                  ``5`` translates to ``Warning``,
                  ``6`` translates to ``Notice``,
                  ``7`` translates to ``Info``,
                  ``8`` translates to ``Debug``,
    :rtype: dict
    """
    return self._get("/securityMapsSettings/")


def set_appliance_security_policy_settings(
    self,
    logging_level: int,
) -> bool:
    """Set appliance security policy settings for implicit drop logging

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - securityMaps
          - POST
          - /securityMapsSettings

    :param logging_level: Logging level for implicit firewall drops
        inter-zone.
        ``0`` translates to ``None``,
        ``1`` translates to ``Emergency``,
        ``2`` translates to ``Alert``,
        ``3`` translates to ``Critical``,
        ``4`` translates to ``Error``,
        ``5`` translates to ``Warning``,
        ``6`` translates to ``Notice``,
        ``7`` translates to ``Info``,
        ``8`` translates to ``Debug``,
    :type logging_level: int
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "map1": {
            "logging": {
                "imp_fw_drop": logging_level,
            }
        }
    }
    return self._post(
        "/securityMapsSettings/",
        data=data,
        return_type="bool",
    )


def get_appliance_security_policy_settings_by_map_name(
    self,
    map_name: str = "map1",
) -> dict:
    """Get appliance security policy settings for implicit drop logging
    by specified map name

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - securityMaps
          - GET
          - /securityMapsSettings/{mapName}

    :param map_name: Name of security map to retrieve, Defaults to
        ``map1`` as the primary map on appliances if security policy
        is configured, Defaults to ``map1``
    :type map_name: str, optional
    :return: Returns dictionary of current appliance security policy of
        particular zone pair \n
        * keyword **map1** (`dict`): Security policy map \n
            * keyword **logging** (`dict`): Logging settings object \n
                * keyword **imp_fw_drop** (`int`): Logging level for
                  implicit deny drops inter-zone.
                  ``0`` translates to ``None``,
                  ``1`` translates to ``Emergency``,
                  ``2`` translates to ``Alert``,
                  ``3`` translates to ``Critical``,
                  ``4`` translates to ``Error``,
                  ``5`` translates to ``Warning``,
                  ``6`` translates to ``Notice``,
                  ``7`` translates to ``Info``,
                  ``8`` translates to ``Debug``,
    :rtype: dict
    """
    return self._get(f"/securityMapsSettings/{map_name}")
