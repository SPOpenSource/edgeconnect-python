# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# memory : Get memory related information


def get_appliance_memory(
    self,
) -> dict:
    """Get appliance memory related information

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - memory
          - GET
          - /memory

    :return: Returns dictionary of current memory utilization on
        appliance, all units in bytes \n
        * keyword **total** (`int`): Total memory
        * keyword **free** (`int`): Free memory
        * keyword **buffers** (`int`): Buffers memory
        * keyword **cached** (`int`): Cached memory
        * keyword **used** (`int`): Used memory
        * keyword **swapTotal** (`int`): Swap total memory
        * keyword **swapFree** (`int`): Swap free memory
        * keyword **swapUsed** (`int`): Swap used memory
    :rtype: dict
    """
    return self._get("/memory")
