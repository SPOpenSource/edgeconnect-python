# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# session : Get session information


def get_orchestrator_sessions(
    self,
) -> list:
    """Get all current sessions to Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - session
          - GET
          - /loginSessions

    :return: Returns list of active sessions \n
        * [`dict`]: Active session object \n
            * keyword **userName** (`str`): Username
            * keyword **lastInteractionTime** (`int`): Time since
              session was last active, often ``0`` with current sessions
            * keyword **loggedInTime** (`int`): Time session was
              logged in in Unix Epoch time in milliseconds
            * keyword **webClient** (`bool`): ``True`` if user session
              is via the web client
            * keyword **role** (`str`): Role of user session, e.g.
              ``net_read_write``
            * keyword **lastAccessTime** (`int`): Time session was last
              active in Unix Epoch time in milliseconds
            * keyword **isMtoSsoSession** (`bool`): ``True`` if user
              session was authenticated via SSO
    :rtype: dict
    """
    return self._get("/loginSessions")
