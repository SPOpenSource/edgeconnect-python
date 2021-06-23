# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# reachability : Orchestrator to/from ECOS connectivity


def get_reachability_status_appliance(
    self,
    ne_id: str,
) -> dict:
    """Get the reachability status from an appliance. Includes status
    for rest, ssh, https, and web socket.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - reachability
          - GET
          - /reachability/appliance/{neId}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :return: Returns dictionary of reachability status
    :rtype: dict
    """
    return self._get("/reachability/appliance/{}".format(ne_id))


def get_reachability_status_orchestrator(
    self,
    ne_id: str,
) -> list:
    """Get the reachability status from Orchestrator. Includes status
    for id, username, state, hostname, web protocol type, and if there
    are unsaved changes.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - reachability
          - GET
          - /reachability/gms/{neId}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :return: Returns dictionary of reachability status
    :rtype: dict
    """
    return self._get("/reachability/gms/{}".format(ne_id))
