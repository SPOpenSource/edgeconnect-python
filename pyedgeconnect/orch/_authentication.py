# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# authentication : ECOS RADIUS and TACACS+


def get_appliance_auth_information(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get configured authentication and authorization on appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - authentication
          - GET
          - /authRadiusTacacs/{neId}

    The returned data contains ``aaa``, ``radius`` and ``tacacs``
    objects. ``aaa`` object includes ``auth_method`` and ``author``
    objects. ``auth_method`` represents Authentication Order for the
    appliance, You can have up to 3 levels of Authentication Order
    (local, radius and tacacs). ``author`` represents Authorization
    Information for the appliance and it consists of default user and
    map order. ``radius`` and ``tacacs`` contains server object, The
    return value is a hash map of RADIUS/TACACS settings keyed by their
    order.

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary of AAA configuration information
    :rtype: dict
    """
    return self._get("/vrrp/{}?cached={}".format(ne_id, cached))
