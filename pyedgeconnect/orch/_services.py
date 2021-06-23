# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# services : Services list


def get_gms_internet_policy_services(self) -> dict:
    """Get configured services used in Overlay editor's Internet Policy
    section.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - services
          - GET
          - /gms/services

    For every service, a 'Send to ' option will be shown in the
    available options list. The service name will correspond to the peer
    name of the pass through tunnel the internet traffic will go on. It
    is the user's responsibility to create these pass through tunnels on
    appliances.

    :return: Returns configured services
    :rtype: dict
    """
    return self._get("/gms/services")


def update_gms_internet_policy_services(
    self,
    services: dict,
) -> bool:
    """Set a new service list used in Overlay editor's Internet Policy
    section.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - services
          - POST
          - /gms/services

    Saving a new service list will completely replace the current
    implementation. Any service IDs that were saved previously, but not
    included in the POST body will be removed. These services will also
    be removed from the overlay's policy list.

    :param services: Dictionary of services to be set in the form
        ``{"SERVICE_1" : {"name":"SERVICE_NAME_1"}, ...}``
    :type services: dict
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/gms/services",
        data=services,
        return_type="bool",
    )


def get_gms_third_party_services(self) -> dict:
    """Get configured services used in Overlay editor's Internet Policy
    section.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - services
          - GET
          - /gms/thirdPartyServices

    The list of services is used to provide options in the Overlay
    editor's Internet Policy section. For every service, a dynamically
    generated options list will be shown in the available options list.
    The service name will correspond to the peer name of the pass
    through tunnel the internet traffic will go on. Pass through tunnels
    will be generated automatically.

    :return: Returns configured 3rd party services
    :rtype: dict
    """
    return self._get("/gms/thirdPartyServices")
