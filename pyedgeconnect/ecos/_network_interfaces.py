# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# networkInterfaces : Interfaces


def get_appliance_network_interfaces(self) -> dict:
    """Get interface information from appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - networkInterfaces
          - GET
          - /networkInterfaces

    :return: Returns dictionary of detailed interface information from
        appliance
    :rtype: dict
    """
    return self._get("/networkInterfaces")


def modify_network_interfaces(
    self,
    if_info: list,
) -> bool:
    """Modify interface information on appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - networkInterfaces
          - POST
          - /networkInterfaces

    :param if_info: List of dictionaries of interfaces to modify
    :type if_info: list
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/networkInterfaces", data={"ifInfo": if_info}, return_type="bool"
    )
