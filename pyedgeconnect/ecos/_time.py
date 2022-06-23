# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# time : Current time


def get_appliance_time(
    self,
) -> dict:
    """Get the current time on the appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - time
          - GET
          - /time

    :return: Returns dictionary of current appliance time \n
        * keyword **current** (`int`): Current unix epoch time in
          milliseconds
        * keyword **gmtOffset** (`int`): Hours offset from GMT
    :rtype: dict
    """
    return self._get("/time")
