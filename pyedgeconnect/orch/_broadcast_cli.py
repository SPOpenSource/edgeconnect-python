# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# broadcastCli : Broadcast CLI commands to ECOS appliances


def broadcast_cli(
    self,
    appliance_list: list,
    cli_commands: list,
) -> bool:
    """Send broadcast CLI commands to list of appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - broadcastCli
          - POST
          - /broadcastCli

    :param appliance_list: List of appliances by Network Primary Key
        (nePk), e.g. ``3.NE``
    :type appliance_list: list
    :param cli_commands: List of commands to be executed on appliance,
        e.g. "ping 8.8.8.8"
    :type cli_commands: list
    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    return self._post(
        "/broadcastCli",
        data={"neList": appliance_list, "cmdList": cli_commands},
        return_type="bool",
    )
