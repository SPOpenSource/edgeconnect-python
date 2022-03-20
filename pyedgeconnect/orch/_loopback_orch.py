# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# loopbackOrch : Get, Update loopback orchestration config


def get_loopback_orchestration(self) -> dict:
    """Get loopback orchestration setting

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - loopbackOrch
          - GET
          - /loopbackOrch

    :return: Returns dictionary for loopback Orchestration \n
        * keyword **<segment_id>** (`dict`): Loopback orch object \n
            * keyword **loopbackPool** (`str`): Loopback pool CIDR,
              e.g. ``10.41.0.0/16``
            * keyword **interfaces** (`dict`): Interface configuration
              detail \n
                * keyword **<interface_id>** (`dict`): Interface
                  object ID, arbitrary value of ``20x00`` where ``x``
                  is the segment id \n
                    * keyword **mgmtIP** (`bool`): Is used for mgmt
                    * keyword **label** (`str`): Interface Label ID,
                      e.g. ``149``
                    * keyword **zone** (`int`): Firewall Zone ID,
                      e.g. ``27``
    :rtype: dict
    """

    return self._get("/loopbackOrch")


def set_loopback_orchestration(
    self,
    segment_id: str,
    loopback_pool: str,
    mgmt_ip: bool,
    label_id: str,
    zone_id: int,
    multiple_segments: dict = None,
) -> bool:
    """Set loopback orchestration setting

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - loopbackOrch
          - POST
          - /loopbackOrch

    .. warning::
        This overwrites all loopback Orchestration, must use
        :func:`~pyedgeconnect.Orchestrator.get_loopback_orchestration`
        to get existing loopback orchestration details and then use
        optional parameter ``multiple_segments`` to load multiple
        segment loopback pools.

    :param segment_id: Segment ID, ``0`` for Default segment. Ignored
        if ``multiple_segments`` is used.
    :type segment_id: str
    :param loopback_pool: CIDR subnet to use for address pool,
        e.g. ``10.41.0.0/16`` Ignored if ``multiple_segments`` is used.
    :type loopback_pool: str
    :param mgmt_ip: ``True`` for using loopback for management of
        appliance. Ignored if ``multiple_segments`` is used.
    :type mgmt_ip: bool
    :param label_id: Interface label ID to be applied to loopback,
        e.g. set to ``27`` if that is the label ID of an example
        interface label of ``LOOPBACK``. Find label ID's from
        :func:`~pyedgeconnect.Orchestrator.get_all_interface_labels`.
        Invalid ID will result in ``UNKNOWN`` for label in UI. Ignored
        if ``multiple_segments`` is used.
    :type label_id: str
    :param zone_id: Firewall zone ID to be applied to loopback,
        e.g. set to ``27`` if that is the label ID of an example
        interface label of ``LOOPBACK``. Find label ID's from
        :func:`~pyedgeconnect.Orchestrator.get_zones`.
        Invalid ID will result in ``UNKNOWN`` for zone in UI. Ignored
        if ``multiple_segments`` is used.
    :type zone_id: int
    :param multiple_segments: Used to set multiple loopback
        orchestration pools at once or add/update existing pools.
        Defaults to None. Dictionary structure must adhere as follows:\n
        * keyword **<segment_id>** (`dict`): Loopback orch object \n
            * keyword **loopbackPool** (`str`): Loopback pool CIDR,
              e.g. ``10.41.0.0/16``
            * keyword **interfaces** (`dict`): Interface configuration
              detail \n
                * keyword **<interface_id>** (`dict`): Interface
                  object ID, arbitrary value of ``20x00`` where ``x``
                  is the segment id \n
                    * keyword **mgmtIP** (`bool`): Is used for mgmt
                    * keyword **label** (`str`): Interface Label ID,
                      e.g. ``149``
                    * keyword **zone** (`int`): Firewall Zone ID,
                      e.g. ``27``
    :type multiple_segments: dict, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    if multiple_segments is not None:
        data = multiple_segments
    else:
        data = {
            segment_id: {
                "loopbackPool": loopback_pool,
                "interfaces": {
                    # Interface ID will correlate to 20x00
                    # where x is the segment id
                    "20000": {
                        "mgmtIp": mgmt_ip,
                        "label": label_id,
                        "zone": zone_id,
                    }
                },
            }
        }

    return self._post(
        "/loopbackOrch",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def get_loopback_orchestration_pool_detail(self) -> dict:
    """Get loopback orchestration pool allocation info

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - loopbackOrch
          - GET
          - /loopbackOrch/pool

    :return: Returns dictionary for loopback Orchestration pool detail\n
        * keyword **<segment_id>** (`dict`): Loopback orch object \n
            * keyword **segment** (`int``): Segment id number
            * keyword **subnet** (`str`): Loopback pool CIDR subnet
            * keyword **totalAddr** (`int`): Total amount of addresses
              in pool
            * keyword **addrAllocated** (`int`): Current amount of
              addresses allocated
            * keyword **addrDeleted** (`int`): Current amount of
              addresses deleted
    :rtype: dict
    """
    return self._get("/loopbackOrch/pool")


def reclaim_delete_loopback_orchestration_ips(self) -> bool:
    """Reclaim all deleted loopback ip addresses

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - loopbackOrch
          - DELETE
          - /loopbackOrch/pool/reclaim

    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        "/loopbackOrch/pool/reclaim",
        expected_status=[204],
        return_type="bool",
    )


def reclaim_single_deleted_loopback_orchestration_ip(
    self,
    loopback_id: int,
) -> bool:
    """Reclaim deleted loopback ip address by id

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - loopbackOrch
          - DELETE
          - /loopbackOrch/pool/reclaim/{id}

    :param loopback_id: Loopback ID number to reclaim from deleted
        list.
    :type loopback_id: int
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        "/loopbackOrch/pool/reclaim/{}".format(loopback_id),
        expected_status=[204],
        return_type="bool",
    )


def get_deleted_loopback_orchestration_ips(
    self,
    segment_id: str,
) -> list:
    """Get deleted orchestrated loopback ip addresses from segment

    .. note::
      This API Call is not in current Swagger as of Orch 9.1.1

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - n/a
          - GET
          - /loopbackOrch/pool/history/{segment_id}

    :param segment_id: Segment ID number to get deleted ip history from
    :type segment_id: int
    :return: Returns list of dictionaries of deleted loopback ip
        addresses \n
        * [`dict`]: Deleted loopback object \n
            * keyword **id** (`int`): Loopback ID
            * keyword **nePk** (`str`): Appliance ID to which loopback
              had been assigned and deleted
            * keyword **segment** (`int`): Segment ID
            * keyword **subnet** (`str`): CIDR subnet containing
              loopback address
            * keyword **ipAddress** (`str`): The loopback that was
              deleted
            * keyword **loopbackId** (`int`): Interface ID of loopback
            * keyword **status** (`int`): ``0`` indicated deleted
            * keyword **detail** (`dict`): Loopback object \n
                * keyword **mgmtIP** (`bool`): Is used for mgmt
                * keyword **label** (`str`): Interface Label ID,
                  e.g. ``149``
                * keyword **zone** (`int`): Firewall Zone ID,
                  e.g. ``27``
    :rtype: list
    """
    return self._get(
        "/loopbackOrch/pool/history/{}".format(segment_id),
    )
