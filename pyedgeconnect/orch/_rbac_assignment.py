# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# rbacAssignment : RBAC: Get, Add, Update, Delete assignments


def get_rbac_assignments(self) -> dict:
    """Get all rbac assignments

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - rbacAssignment
          - GET
          - /rbac/assignment

    :return: Returns dictionary of rbac assignments
    :rtype: dict
    """
    return self._get("/rbac/assignment")


def update_rbac_assignment(
    self,
    username: str,
    roles: str = "null",
    asset: str = "null",
) -> bool:
    """Create or update rbac assignment

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - rbacAssignment
          - POST
          - /rbac/assignment

    :param username: Username for assignment
    :type username: str
    :param roles: Comma separated list of roles. Required if asset value
        is not provided, e.g. "role1, role2, role3", defaults to "null"
    :type roles: str, optional
    :param asset: Appliance access group or asset name. Required if
        roles value is not provided, e.g. "group1", defaults to "null"
    :type asset: str, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    :raises ValueError: Both optional parameters cannot be value of
        "null"
    """
    if roles == "null" and asset == "null":
        raise ValueError("Roles and asset variables cannot both be 'null' ")

    data = {
        "username": username,
        "roles": roles,
        "asset": asset,
    }

    return self._post(
        "/rbac/assignment",
        data=data,
        return_type="bool",
    )


def get_rbac_user_assignment(
    self,
    username: str,
) -> dict:
    """Get rbac assignment for particular user

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - rbacAssignment
          - GET
          - /rbac/assignment/{username}

    :param username: Username to query for rbac assignments
    :type username: str
    :return: Returns dictionary of rbac assignments for user
    :rtype: dict
    """
    return self._get("/rbac/assignment/{}".format(username))


def delete_rbac_user_assignment(
    self,
    username: str,
) -> bool:
    """Delete rbac assignment for particular user

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - rbacAssignment
          - DELETE
          - /rbac/assignment/{username}

    :param username: Username to query for rbac assignments
    :type username: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        "/rbac/assignment/{}".format(username), return_type="bool"
    )
