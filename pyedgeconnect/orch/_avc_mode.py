# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# avcMode : Orchestrator AVC mode


def get_avc_mode(self) -> dict:
    """Get Orchestrator AVC mode

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - avcMode
          - GET
          - /avcMode

    :return: Returns dictionary of AVC value, e.g. {"AVC": "all"}
    :rtype: dict
    """
    return self._get("/avcMode")
