# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# interfaces : Get interface related information


def get_appliance_interfaces(self) -> dict:
    """Retrieve interface information from appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - interfaces
          - GET
          - /interfaces

    :return: Dictionary of interface details from appliance
    :rtype: dict
    """
    return self._get("/interfaces")
