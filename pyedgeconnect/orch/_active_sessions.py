# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# activeSessions : Orchestrator active sessions


def get_active_sessions_orchestrator(
    self,
) -> list:
    """Get all current active sessions on Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - activeSessions
          - GET
          - /session/activeSessions

    :return: Returns list of dictionaries of active sessions \n
        [`dict`]: Active session object \n
            * keyword **username** (`str`): Username
            * keyword **type** (`str`): Protocol/method used for
              establishing the session e.g. ``web`` or ``ssh``
            * keyword **idle_time** (`int`): Measure of current interval
              during which user is idle (seconds)
            * keyword **login_time** (`int`): Time of user login (EPOCH
              time in seconds)
            * keyword **remote_host** (`str`): The IP address of the
              user originating the session
    :rtype: dict
    """
    return self._get("/session/activeSessions")
