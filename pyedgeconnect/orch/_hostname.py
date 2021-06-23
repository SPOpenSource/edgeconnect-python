# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# hostName : Orchestrator server hostname


def get_orchestrator_hostname(
    self,
) -> dict:
    """Get configured hostname of Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - hostName
          - GET
          - /gmsHostname

    :return: Returns dictionary with Orchestrator hostname \n
        * keyword **gms_hostname** (`str`): Orchestrator hostname
    :rtype: dict
    """
    return self._get("/gmsHostname")
