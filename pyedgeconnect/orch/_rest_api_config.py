# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# restApiConfig : Get and set the REST API config


def get_rest_api_config(self) -> dict:
    """Get REST API configuration

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - restApiConfig
          - GET
          - /restApiConfig

    :return: Returns dictionary of REST API config
    :rtype: dict
    """

    return self._get("/restApiConfig")


def set_rest_api_config(
    self,
    enable: bool,
) -> bool:
    """Update REST API configuration

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - restApiConfig
          - POST
          - /restApiConfig

    :param enable: The control value of connecting ECOS via portal web
        socket, ``True`` allows connecting ECOS via portal web socket,
        ``False`` disallows
    :type enable: bool
    :return: Returns dictionary of REST API config
    :rtype: dict
    """
    data = {"communicateWithApplianceViaPortal": enable}

    return self._get(
        "/restApiConfig", data=data, expected_status=[204], return_type="bool"
    )
