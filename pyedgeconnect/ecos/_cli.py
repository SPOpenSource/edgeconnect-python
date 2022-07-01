# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# cli : API to execute commands on appliance CLI
from __future__ import annotations


def perform_appliance_cli_command(
    self,
    cli_command: str,
) -> str:
    """Run single cli command on appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - cli
          - POST
          - /cli

    :param cli_command: CLI command to perform on appliance, e.g.
        ``show subnet learned``
    :type cli_command: str
    :return: Returns text response of cli command
    :rtype: str
    """
    data = {"command": cli_command}
    return self._post(
        "/cli",
        data=data,
        return_type="text",
    )


def perform_appliance_multiple_cli_command(
    self,
    cli_commands: list[str],
) -> list:
    """Run multiple cli commands on appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - cli
          - POST
          - /cliMultiple

    :param cli_commands: List of CLI command to perform on appliance,
        e.g. ``["show version", "show transceiver"]``
    :type cli_command: list[str]
    :return: Returns list of dictionaries of reuslts for each command \n
        * [`list[dict]`]: List of command results \n
            * keyword **command** (`str`): Cli command run
            * keyword **result** (`str`): Text result from cli command
    :rtype: list
    """
    data = {"commands": cli_commands}
    return self._post(
        "/cliMultiple",
        data=data,
    )
