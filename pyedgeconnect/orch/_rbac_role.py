# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# rbacRole : RBAC: Get, Add, Update, Delete roles


def get_all_rbac_roles(self) -> dict:
    """Get all rbac roles

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - rbacRole
          - GET
          - /rbac/role

    :return: Returns dictionary of rbac roles
    :rtype: dict
    """
    return self._get("/rbac/role")


def update_rbac_role(
    self,
    role: str,
    menu_items: list,
    net_read: bool,
) -> bool:
    """Create or update rbac role

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - rbacRole
          - POST
          - /rbac/role

    .. note::
        Swagger documentation (in 9.0.2.0) shows net_read value of
        ``True`` to be read/write but it is flipped.

    :param role: Name of the role
    :type role: str
    :param menu_items: List of menu items assigned for access from the
        role
    :type menu_items: list
    :param net_read: Permissions for the attributes,
        Read/Write (``False``), Read-Only (``True``)
    :type net_read: bool
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {}
    data[role] = {
        "menuTypeItems": menu_items,
        "net_read": net_read,
    }

    return self._post(
        "/rbac/role",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def get_rbac_role(
    self,
    role: str,
) -> dict:
    """Get rbac role by name

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - rbacRole
          - GET
          - /rbac/role/{roleName}

    :param role: Name of the role
    :type role: str
    :return: Returns dictionary of rbac role
    :rtype: dict
    """
    return self._get("/rbac/role/{}".format(role))


def delete_rbac_role(
    self,
    role: str,
) -> bool:
    """Delete rbac role by name

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - rbacRole
          - DELETE
          - /rbac/role/{roleName}

    .. note::
        If role is assigned to one or more users, API will return
        HTTP 423

    :param role: Name of the role
    :type role: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete("/rbac/role/{}".format(role), return_type="bool")


def get_rbac_role_assigned(self) -> dict:
    """Get list of accessible menus based on the current session
    permissions

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - rbacRole
          - GET
          - /rbac/role/menuAssigned

    .. note::
        Returns HTTP 204 Empty Response if nothing is assigned

    :return: Returns dictionary of current session accessible menus
    :rtype: dict
    """
    return self._get("/rbac/role/menuAssigned")
