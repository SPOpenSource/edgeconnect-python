# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# actionLog : Get Action/Audit Logs


def get_audit_log(
    self,
    start_time: int,
    end_time: int,
    limit: int,
    log_level: int = 1,
    ne_pk: str = None,
    username: str = None,
) -> list:
    """Get audit log details filtered by specified query parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - actionLog
          - GET
          - /action

    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param limit: Limit the number of rows to retrieve from audit log
    :type limit: int
    :param log_level: ``0`` for Debug, ``1`` for Info, ``2`` for Error.
        Defaults to 1
    :type log_level: int, optional
    :param ne_pk: Filter for specific appliance with Network Primary Key
        (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str, optional
    :param username: Filter for specific user
    :type username: str, optional
    :return: Returns list of dictionaries \n
        [`dict`]: Audit log line \n
            * keyword **id** (`int`): Id of the log entry
            * keyword **user** (`str`): User who performed this action
            * keyword **ipAddress** (`str`): IP Address who performed
              this action
            * keyword **nepk** (`str`): Primary key of the appliance on
              which this action was performed
            * keyword **name** (`str`): Name of the action
            * keyword **description** (`str`): Description of the action
            * keyword **taskStatus** (`str`): Status of the action
            * keyword **startTime** (`int`): Start time of the action in
              milliseconds since epoch
            * keyword **endTime** (`int`): End time of the action in
              milliseconds since epoch
            * keyword **queuedTime** (`int`): Original queued time of
              the action in milliseconds since epoch
            * keyword **percentComplete** (`int`): Percentage completion
              of the action
            * keyword **completionStatus** (`bool`): Show if action
              succeeded or failed
            * keyword **result** (`str`): Opaque blob of data related to
              action. Typically, this is the result of the action.
            * keyword **intTaskStatus** (`int`): Status of the action in
              integer enum format
            * keyword **guid** (`str`): GUID of a group of related
              actions
    :rtype: list
    """
    path = "/action?startTime={}&endTime={}&limit={}&logLevel={}".format(
        start_time, end_time, limit, log_level
    )

    if ne_pk is not None:
        path = path + "&appliance={}".format(ne_pk)
    if username is not None:
        path = path + "&username={}".format(username)

    return self._get(path)


def get_audit_log_task_status(
    self,
    action_key: str,
) -> dict:
    """Certain actions like appliance upgrade, appliance restore etc.,
    return a key as in response. Check for status of such operations
    using the key

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - actionLog
          - GET
          - /action/status

    :param action_key: GUID of task to retrieve status for
    :type action_key: str
    :return: Returns dictionary of specified task details \n
        * keyword **id** (`int`): Id of the log entry
        * keyword **user** (`str`): User who performed this action
        * keyword **ipAddress** (`str`): IP Address who performed
          this action
        * keyword **nepk** (`str`): Primary key of the appliance on
          which this action was performed
        * keyword **name** (`str`): Name of the action
        * keyword **description** (`str`): Description of the action
        * keyword **taskStatus** (`str`): Status of the action
        * keyword **startTime** (`int`): Start time of the action in
          milliseconds since epoch
        * keyword **endTime** (`int`): End time of the action in
          milliseconds since epoch
        * keyword **queuedTime** (`int`): Original queued time of
          the action in milliseconds since epoch
        * keyword **percentComplete** (`int`): Percentage completion
          of the action
        * keyword **completionStatus** (boolean): Show if action
          succeeded or failed
        * keyword **result** (`str`): Opaque blob of data related to
          action. Typically, this is the result of the action.
        * keyword **intTaskStatus** (`int`): Status of the action in
          integer enum format
        * keyword **guid** (`str`): GUID of a group of related
          actions
    :rtype: list
    """
    return self._get("/action/status?key={}".format(action_key))


def cancel_audit_log_task(
    self,
    action_key: str,
) -> bool:
    """Certain actions like appliance upgrade, appliance restore etc.,
    return a key as in response. Cancel the action referenced by
    provided key.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - actionLog
          - POST
          - /action/cancel

    :param action_key: GUID of task to retrieve status for
    :type action_key: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._get("/action/status?key={}".format(action_key))
