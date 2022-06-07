# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# pauseOrchestration : Set or get appliances nePks which are paused from
# orchestration
from __future__ import annotations


def get_pause_orchestration(self) -> dict:
    """Get appliances currently paused for orchestration

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - pauseOrchestration
          - GET
          - /pauseOrchestration

    :return: Returns dictionary of appliances in nePk format
    :rtype: dict
    """
    return self._get("/pauseOrchestration")


def set_pause_orchestration(
    self,
    ne_pk_list: list[str],
) -> bool:
    """Set appliances to pause orchestration

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - pauseOrchestration
          - POST
          - /pauseOrchestration

    :param ne_pk_list: List of appliances in the format of integer.NE
        e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/pauseOrchestration",
        data=ne_pk_list,
        expected_status=[204],
        return_type="bool",
    )
