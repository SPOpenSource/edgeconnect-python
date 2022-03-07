# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# gmsServer : Orchestrator server info


def get_orchestrator_hello(self) -> str:
    """Returns hello message from Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsServer
          - GET
          - /gmsserver/hello

    :return: Returns str hash message
    :rtype: str
    """
    return self._get(
        "/gmsserver/hello",
        return_type="text",
    )


def get_orchestrator_server_info(self) -> dict:
    """Returns orchestrator server information such as used disk space,
    hostname, release, etc.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsServer
          - GET
          - /gmsserver/info

    :return: Returns dictionary of orchestrator server information \n
        * keyword **usedDiskSpace** (`str`): Total disk Memory used so
          far
        * keyword **hostName** (`str`): Host name of the orchestrator
          server
        * keyword **role** (`int`): Role
        * keyword **serialNumber** (`str`): Orchestrator server serial
          number
        * keyword **hwRev** (`str`): hwRev
        * keyword **numCpus** (`int`): Number of CPUs
        * keyword **release** (`str`): Orchestrator release version
        * keyword **freeDiskSpace** (`str`): Remaining disk Memory
        * keyword **osRev** (`str`): Operating system version
        * keyword **uptime** (`str`): Duration since the server came
          online
        * keyword **domain** (`str`): Orchestrator domain name
        * keyword **host** (`str`): Orchestrator host IP address
        * keyword **numActiveUsers** (`int`): Number of active users
          accessing the Orchestrator
        * keyword **model** (`str`): Orchestrator server model number
        * keyword **platform** (`str`): The platform Orchestrator
          deployed
        * keyword **loadAverage** (`int`): loadAverage
        * keyword **time** (`int`): Current time as integer
        * keyword **memSize** (`int`): Total memory of the server
        * keyword **inContainerMode** (`bool`): Container mode
    :rtype: dict
    """
    return self._get("/gmsserver/info")


def get_orchestrator_server_ping(self) -> dict:
    """Returns orchestrator server information such as hostname, uptime,
    version, dbHealth

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsServer
          - GET
          - /gmsserver/ping

    :return: Returns dictionary of orchestrator server information \n
        * keyword **hostName** (`str`): Host name of the orchestrator
          server
        * keyword **dbHealth** (`bool`): Orchestrator db health status
        * keyword **timeStr** (`str`): Current time as a string
        * keyword **time** (`int`): Current time as integer
        * keyword **message** (`str`): "I am alive!"
        * keyword **version** (`str`): Orchestrator release version
        * keyword **uptime** (`str`): Duration since the server came
          online
    :rtype: dict
    """
    return self._get("/gmsserver/info")


def get_orchestrator_server_brief(self) -> dict:
    """Returns orchestrator server information such as uptime, release,
    timeZone, container mode etc.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsServer
          - GET
          - /gmsserver/briefInfo

    :return: Returns dictionary of orchestrator server information \n
        * keyword **uptime** (`str`): Duration since the server came
          online
        * keyword **release** (`str`): Orchestrator release version
        * keyword **time** (`str`): Current time as a string
        * keyword **timeZone** (`str`): Time zone of orchestrator
        * keyword **inContainerMode** (`bool`): Container mode
    :rtype: dict
    """
    return self._get("/gmsserver/briefInfo")


def get_orchestrator_server_versions(self) -> dict:
    """Returns available orchestrator versions

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsServer
          - GET
          - /gms/versions

    :return: Returns dictionary of orchestrator server versions \n
        * keyword **current** (`str`): Current Orchestrator release
          version, e.g. ``9.0.3.40345``
        * keyword **installed** (`list[str]`): List of all installed
          orchestrator versions
    :rtype: dict
    """
    return self._get("/gms/versions")


def get_orchestrator_server_os(self) -> str:
    """Returns orchestrator operating system

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsServer
          - GET
          - /gmsOperatingSystem

    :return: Returns string of orchestrator server operating system,
        e.g. ``linux``
    :rtype: str
    """
    return self._get("/gmsOperatingSystem")
