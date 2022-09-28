# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# cpu : CPU Stat APIs


def get_appliance_cpu(
    self,
    time: int,
) -> dict:
    """Get the appliance cpu utilization for a particular minute.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - cpu
          - GET
          - /cpustat

    .. note::

        Requires ECOS 9.1+

    :param time: Epoch time in milliseconds to query for cpu data
    :type time: int
    :return: Returns dictionary of appliance deployment information \n
        * keyword **data** (`list`): CPU utilization array \n
          * [`dict`]: CPU utilization object \n
            * keyword **<timestamp>** (`list`): Array of utilization
              data for this timestamp for each cpu \n
              * [`dict`]: CPU utilization detail \n
                * keyword **cpu_number** (`str`): CPU number identifier
                * keyword **pIRQ** (`float`): CPU percentage Interrupt
                  Requests
                * keyword **pIdle** (`float`): CPU percentage Idle
                * keyword **pNice** (`float`): CPU percentage of NICE
                * keyword **pSys** (`float`): CPU percentage System
                * keyword **pUser** (`float`): CPU percentage User
        * keyword **latestTimestamp** (`int`): Epoch ms from latest
          timestamp in returned data
    :rtype: dict
    """
    return self._get(f"/cpustat?time={time}")
