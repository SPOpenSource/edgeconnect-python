# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# IdleTime : User idle time


def clear_idle_time(self) -> dict:
    """Clear the user idle timeout

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - IdleTime
          - GET
          - /idle/clear

    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._get("/idle/clear")


def increment_idle_time(self) -> dict:
    """Increment the user idle time

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - IdleTime
          - GET
          - /idle/increment

    :return: Returns a dictionary of key ``isTimeout`` with value of
        ``True`` or ``False``
    :rtype: dict
    """
    return self._get("/idle/increment")
