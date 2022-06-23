# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# rbacApplianceAccessGroup : RBAC: Get, Add, Update, Delete appliance
# access groups / assets
from __future__ import annotations


def get_all_appliance_access_groups(
    self,
) -> dict:
    """Get all appliance access groups / assets

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - rbacApplianceAccessGroup
          - GET
          - /rbac/asset

    :return: Returns dictionary of all appliance access groups \n
        * keyword **<appliance_access_group_name>** (`dict`): appliance
          access group object \n
            * keyword **applianceGroups** (`list[str]`): List of
              appliance group id's to allow access to,
              e.g. ``["160.Network", "148.Network"]``
            * keyword **applianceRegions** (`str`): List of appliance
              regions to allow access to, e.g. ``["16", "3", "7"]``
    :rtype: dict
    """
    return self._get("/rbac/asset")


def update_appliance_access_group(
    self,
    appliance_access_group_name: str,
    appliance_groups: list[str],
    appliance_regions: list[str],
) -> bool:
    """Create or update appliance access group / asset.
    Both list of ``appliance_groups`` and ``appliance_regions``
    must be specified, if no group or region is desired, provide
    a blank list as input.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - rbacApplianceAccessGroup
          - POST
          - /rbac/asset

    :param appliance_access_group_name: Name of new or existing
        appliance access group to create or update
    :type appliance_access_group_name: str
    :param appliance_groups: List of appliance group id's the access
        group will allow access to
    :type appliance_groups: list[str]
    :param appliance_regions: List of region id's the access group will
        allow access to
    :type appliance_regions: list[str]
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        appliance_access_group_name: {
            "applianceGroups": appliance_groups,
            "applianceRegions": appliance_regions,
        }
    }

    return self._post(
        "/rbac/asset",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def get_appliance_access_group(
    self,
    appliance_access_group_name: str,
) -> dict:
    """Get appliance access group / asset by name

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - rbacApplianceAccessGroup
          - GET
          - /rbac/asset/{applianceAccessGroupName}

    :param appliance_access_group_name: Name of appliance access group
        to retrieve
    :type appliance_access_group_name: str
    :return: Returns dictionary of appliance access group details \n
        * keyword **applianceGroups** (`list[str]`): List of
            appliance group id's allowed access to,
            e.g. ``["160.Network", "148.Network"]``
        * keyword **applianceRegions** (`str`): List of appliance
            regions allowed access to, e.g. ``["16", "3", "7"]``
    :rtype: dict
    """
    return self._get("/rbac/asset/{}".format(appliance_access_group_name))


def delete_appliance_access_group(
    self,
    appliance_access_group_name: str,
) -> dict:
    """Delete appliance access group / asset by name

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - rbacApplianceAccessGroup
          - DELETE
          - /rbac/asset/{applianceAccessGroupName}

    :param appliance_access_group_name: Name of appliance access group
        to delete
    :type appliance_access_group_name: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        "/rbac/asset/{}".format(appliance_access_group_name),
        return_type="bool",
    )
