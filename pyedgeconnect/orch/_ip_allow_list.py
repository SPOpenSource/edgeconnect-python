# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# ipAllowList : Access IP Allow List


def get_ip_allow_list(self) -> dict:
    """Returns the external IP/mask allow list to access Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - ipAllowList
          - GET
          - /gms/ipAllowList/external

    :return: Returns dictionary of allowed IP addresses allowed to
        access Orchestrator
    :rtype: dict
    """

    return self._get("/gms/ipAllowList/external")


def update_ip_allow_list(
    self,
    ip_allow_list: list,
) -> bool:
    """Set the external IP/mask allow list to access Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - ipAllowList
          - POST
          - /gms/ipAllowList/external

    This will overwrite the existing values in the list. Can supply a
    blank list [] as input to allow any IP.

    :param ip_allow_list: List of IP addresses in CIDR format as
        strings. e.g. ["10.0.0.0/8", "192.0.2.0/24"]
    :type ip_allow_list: list
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = ip_allow_list

    return self._post(
        "/gms/ipAllowList/external",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def get_ip_allow_list_drops(self) -> dict:
    """Returns the IP addresses of the dropped requests to this server

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - ipAllowList
          - GET
          - /gms/ipAllowList/drops

    :return: Returns dictionary of dropped IP addresses blocked based on
        the allow list
    :rtype: dict
    """
    return self._get("/gms/ipAllowList/drops")
