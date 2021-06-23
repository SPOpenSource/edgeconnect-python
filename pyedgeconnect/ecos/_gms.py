# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# gms : Orchestrator and Autodiscovery


def get_orchestrator(self) -> dict:
    """Retrieve current orchestrator for the appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gms
          - GET
          - /gms

    :return: Dictionary of Orchestrator and reachability status \n
        * keyword **<orchestrator_ip>** (`dict`): connection protocols\n
            * keyword **rest** (`str, optional`): rest Reachable or
              Unreachable status
            * keyword **ssh** (`str, optional`): ssh Reachable or
              Unreachable status
            * keyword **https** (`str, optional`): https Reachable or
              Unreachable status
            * keyword **webSocket** (`str, optional`): websocket
              Reachable or Unreachable status
    :rtype: dict
    """
    return self._get("/gms")


def assign_orchestrator(
    self,
    orchestrator: str,
    ssl_enabled: str = "false",
    keepalive_count: int = 0,
    port: int = 0,
) -> bool:
    """Assign an Orchestrator to the appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gms
          - POST
          - /gms

    .. note::
        As of 9.0.1.0 the self_var as "" appears to fail, and instead
        not using it returns HTTP 200

    :param orchestrator: IP address or URL of orchestrator to assign
    :type orchestrator: str
    :param ssl_enabled: Enable SSL for communicating with Orchestrator,
        defaults to "false"
    :type ssl_enabled: str, optional
    :param keepalive_count: Number of keepalive messages to use as
        threshold for connectivity, defaults to 0
    :type keepalive_count: int, optional
    :param port: IP Port to connect to Orchestrator on, defaults to 0
    :type port: int, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/gms",
        data={
            orchestrator: {
                "self": orchestrator,
                "ssl_enabled": ssl_enabled,
                "keepalive_count": keepalive_count,
                "port": port,
            }
        },
        return_type="bool",
    )
