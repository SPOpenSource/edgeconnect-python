# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# internalSubnets : Internal Subnets


def get_internal_subnets(self) -> dict:
    """Gets the current internal subnets configured in Orchestrator to
    classify internet traffic

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - internalSubnets
          - GET
          - /gms/internalSubnets2

    :return: Returns dictionary of internal subnets
    :rtype: dict
    """
    return self._get("/gms/internalSubnets2")


def update_internal_subnets(
    self,
    ipv4_list: list = [
        "10.0.0.0/8",
        "172.16.0.0/12",
        "192.168.0.0/16",
        "169.254.0.0/16",
        "224.0.0.0/4",
    ],
    ipv6_list: list = [],
    segment_ipv4_list: list = [],
    non_default_routes: bool = False,
) -> bool:
    """Update the list of internal subnets to use to classify internet
    traffic.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - internalSubnets
          - POST
          - /gms/internalSubnets2

    Any traffic not matching the internal subnets will be classified as
    internet traffic. This list will be pushed to all appliances. User
    can configure up to 512 subnets in each ipv4 and ipv6 entry.

    .. warning::
        This will overwrite current subnets!

    :param ipv4_list: List of ipv4 networks in CIDR format for all VRFs,
        defaults to ["10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16",
        "169.254.0.0/16", "224.0.0.0/4"]
    :type ipv4_list: list, optional
    :param ipv6_list: List of ipv6 networks in CIDR format,
        defaults to []
    :type ipv6_list: list, optional
    :param segment_ipv4_list: List of ipv4 networks each prefaced with
        related VRF id #, e.g. For VRF 1 only ["1:192.168.0.0/16"],
        defaults to []
    :type segment_ipv4_list: list, optional
    :param non_default_routes: Treat non-default routes as internal
        subnets, defaults to False
    :param non_default_routes: bool, optional
    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    data = {
        "ipv4": ipv4_list,
        "ipv6": ipv6_list,
        "segmentIpv4": segment_ipv4_list,
        "nonDefaultRoutes": non_default_routes,
    }

    return self._post(
        "/gms/internalSubnets2",
        data=data,
        expected_status=[204],
        return_type="bool",
    )
