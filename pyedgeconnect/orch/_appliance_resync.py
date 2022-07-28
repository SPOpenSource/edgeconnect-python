# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# applianceResync : Orchestrator appliance configuration synchronization
from __future__ import annotations


def appliance_resync(
    self,
    ne_pk_list: list[str],
) -> str:
    """Trigger synchronization for list of appliances provided.
    Synchronize operation will return a string key.
    Use :func:`pyedgeconnect.Orchestrator.get_audit_log_task_status`
    with the key value to get the status of the operation.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applianceResync
          - POST
          - /applianceResync

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :return: Returns key value for requested operation.
        Use :func:`pyedgeconnect.Orchestrator.get_audit_log_task_status`
        with the key value to get the status of the operation.
    :rtype: str
    """
    data = {"ids": ne_pk_list}

    return self._post("/applianceResync", data=data, return_type="text")
