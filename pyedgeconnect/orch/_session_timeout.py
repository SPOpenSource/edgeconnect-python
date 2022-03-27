# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# sessionTimeout : Auto logout and Max sessions


def get_orch_session_timeout(
    self,
) -> dict:
    """Get information of auto logout and max login session

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - sessionTimeout
          - GET
          - /gms/sessionTimeout

    :return: Returns dictionary of auto logout and max login session
        information \n
        * keyword **resourceBase** (`str`): The API endpoint,
          ``/sessionTimeout``
        * keyword **resourceKey** (`str`): NEEDS DESCRIPTION
        * keyword **configData** (`dict`): Config info object \n
            * keyword **autoLogout** (`int`): Auto logout time for
              an idle user session in minutes, e.g. ``30``
            * keyword **maxSession** (`int`): Maximum number of active
              sessions logged into Orchestrator
        * keyword **version** (`int`): Incremental version number when
          the values are edited
        * keyword **timestamp** (`int`): Timestamp when the values were
          last changed in Unix Epoch milliseconds
    :rtype: dict
    """
    return self._get("/gms/sessionTimeout")


def set_orch_session_timeout(
    self,
    auto_logout: int,
    max_session: int,
) -> dict:
    """Update auto logout and max login session

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - sessionTimeout
          - PUT
          - /gms/sessionTimeout

    :param auto_logout:
    :type auto_logout: int
    :param max_session:
    :type max_session: int
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "autoLogout": auto_logout,
        "maxSession": max_session,
    }

    return self._put(
        "/gms/sessionTimeout",
        data=data,
        expected_status=[204],
        return_type="bool",
    )
