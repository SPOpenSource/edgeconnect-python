# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# saveChanges : ECOS save configuration changes
from __future__ import annotations


def save_changes_ne_pk_list(
    self,
    ne_pk_list: list[str],
) -> dict:
    """Save configuration changes in memory to a file for a list of
    appliances in Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - saveChanges
          - POST
          - /appliance/saveChanges

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :return: Returns dictionary with identifying key of this task. \n
        * keyword **clientKey** (`str`): Client key which can be polled
          to get progress of the requested action.
    :rtype: dict
    """
    data = {"ids": ne_pk_list}

    return self._post("/appliance/saveChanges", data=data)


def save_changes_single_appliance(
    self,
    ne_pk: str,
) -> dict:
    """Save configuration changes in memory to a file for an appliance
    in Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - saveChanges
          - POST
          - /appliance/saveChanges/{nePk}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :return: Returns dictionary with identifying key of this task. \n
        * keyword **clientKey** (`str`): Client key which can be polled
          to get progress of the requested action.
    :rtype: dict
    """
    # Swagger docs indicates body should be a blank {} JSON object
    return self._post("/appliance/saveChanges/{}".format(ne_pk), data={})
