# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# diskUsage : Available disk space


def get_appliance_disk_usage(
    self,
) -> dict:
    """Get the disk usage of the appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - diskUsage
          - GET
          - /diskUsage

    :return: Returns dictionary of current appliance disk usage \n
        * keyword **<directory name>** (`dict`): Directory disk
          utilization, e.g. ``/`` or ``/dev`` etc. \n
            * keyword **1k-blocks** (`int`): The number of 1k-blocks
            * keyword **used** (`int`): Size of used space, KB
            * keyword **available** (`int`): Size of available space, KB
            * keyword **usedpercent** (`int`): Percent of used space
            * keyword **filesystem** (`str`): Name of the filesystem
    :rtype: dict
    """
    return self._get("/diskUsage")
