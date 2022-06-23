# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# alarm : Alarms
from __future__ import annotations


def get_alarms_from_appliances(
    self,
    ne_pk_list: list[str],
    view: str = "all",
    severity: str = None,
    order_by_severity: bool = None,
    max_alarms: int = None,
    start_time: int = None,
    end_time: int = None,
) -> list:
    """Get active, historical, or all alarms from appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - POST
          - /alarm/appliance

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :param view: Accepted values are ``active`` for current alarms,
        ``closed`` for historical alarms, ``all`` for both active and
        historical alarms,  defaults to "all"
    :type view: str, optional
    :param severity: Filter by severity of alarm. Accepted values are
        ``warning``, ``minor``, ``major``, and ``critical``,
        defaults to None
    :type severity: str, optional
    :param order_by_severity: If ``True`` will order the response alarms
        by ranking severity, defaults to None
    :type order_by_severity: bool, optional
    :param max_alarms: Maximum number of alarms to return in response,
        defaults to None
    :type max_alarms: int, optional
    :param start_time: Long(Signed 64 bits) value of milliseconds since
        EPOCH time indicating the starting time boundary of data time
        range, defaults to None
    :type start_time: int, optional
    :param end_time: Long(Signed 64 bits) value of milliseconds since
        EPOCH time indicating the ending time boundary of data time
        range, defaults to None
    :type end_time: int, optional
    :return: Returns list of dictionaries per alarm \n
        * [`dict`]: list of alarm dictionary objects \n
            * keyword **applianceId** (`str`): appliance ne_pk value
            * keyword **severity** (`str`): severity of alarm
            * keyword **sequenceId** (`int`): alarm sequence number
            * keyword **source** (`str`): source of alarm,
              e.g. ``system``
            * keyword **acknowledged** (`bool`): if alarm has been
              acknolwedged
            * keyword **clearable** (`bool`): if the alarm can be
              cleared
            * keyword **timeOccurredInMills** (`int`): time alarm
              occured in unix epoch milliseconds
            * keyword **description** (`str`): alarm description
            * keyword **type** (`str`): alarm type
            * keyword **recommendedAction** (`str`): recommended action
              message, if any
            * keyword **serviceAffect** (`bool`): if this condition
              could affect service
            * keyword **typeId** (`int`): uuid of alarm type
            * keyword **name** (`str`): name of alarm type
            * keyword **occurrenceCount** (`int`): number of occurences
            * keyword **hostName** (`str`): hostname of appliance
              generating alarm
            * keyword **closed** (`bool`): if alarm has been closed
            * keyword **clearedTimeInMills** (`int`): time alarm cleared
              in unix epoch milliseconds
    :rtype: list
    """

    data = {"ids": ne_pk_list}

    path = "/alarm/appliance?view={}".format(view)

    if severity is not None:
        path = path + "&severity={}".format(severity)
    if order_by_severity is not None:
        path = path + "&orderBySeverity={}".format(order_by_severity)
    if max_alarms is not None:
        path = path + "&maxAlarms={}".format(max_alarms)
    if start_time is not None:
        path = path + "&from={}".format(start_time)
    if end_time is not None:
        path = path + "&to={}".format(end_time)

    return self._post(path, data=data)


def acknolwedge_alarms_from_appliance(
    self,
    ne_id: str,
    alarm_list: list,
    acknowledge: bool,
) -> bool:
    """Acknowledge alarms on appliance for specific id's and sequence
    id's of alarms

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - POST
          - /alarm/acknowledgement/appliance/{neId}

    :param ne_id: Network Primary Key (nePk) of existing appliance, e.g.
         ``3.NE``
    :type ne_id: str
    :param alarm_list: List of dictionaries with alarms to acknowledge\n
        [`dict`]: \n
            * keyword **id** (`int`): alarm id
            * keyword **sequenceId** (`int`): alarm sequence id
            * keyword **source** (`str`): alarm source, mandatory field
              but can be left as blank string ""
    :type alarm_list: list
    :param acknowledge: ``True`` to acknowledge the alarms, ``False`` to
        leave unacknowledged
    :type acknowledge: bool
    :return: Returns True/False based on successful call
    :rtype: bool
    """

    data = {"actions": alarm_list, "acknowledge": acknowledge}

    return self._post(
        "/alarm/acknowledgement/appliance/{}".format(ne_id),
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def add_note_to_appliance_alarm(
    self,
    ne_id: str,
    alarm_list: list,
    note: str,
) -> bool:
    """Add note/comment to specified appliance alarms

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - POST
          - /alarm/note/appliance/{neId}

    :param ne_id: Network Primary Key (nePk) of existing appliance, e.g.
        ``3.NE``
    :type ne_id: str
    :param alarm_list: List of dictionaries with alarms to acknowledge\n
        [`dict`]:\n
            * keyword **id** (`int`): alarm id
            * keyword **sequenceId** (`int`): alarm sequence id
            * keyword **source** (`str`): alarm source, mandatory field
              but can be left as blank string ""
    :type alarm_list: list
    :param note: Comment to add to alarms, cannot be a blank string
    :type note: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """

    data = {"actions": alarm_list, "note": note}

    return self._post(
        "/alarm/note/appliance/{}".format(ne_id),
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def clear_alarms_from_appliance(
    self,
    ne_id: str,
    alarm_list: list,
) -> bool:
    """Clear alarms on appliance for specific id's and sequence id's of
    alarms

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - POST
          - /alarm/clearance/appliance/{neId}

    :param ne_id: Network Primary Key (nePk) of existing appliance, e.g.
        ``3.NE``
    :type ne_id: str
    :param alarm_list: List of dictionaries with alarms to acknowledge\n
        [`dict`]: \n
            * keyword **id** (`int`): alarm id
            * keyword **sequenceId** (`int`): alarm sequence id
            * keyword **source** (`str`): alarm source, mandatory field
              but can be left as blank string ""
    :type alarm_list: list
    :return: Returns True/False based on successful call
    :rtype: bool
    """

    data = {"actions": alarm_list}

    return self._post(
        "/alarm/clearance/appliance/{}".format(ne_id),
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def get_alarm_count_all_appliances(
    self,
) -> list:
    """Returns summary of active alarms for each appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - GET
          - /alarm/count/appliance

    :return: Returns list of dictionaries for each appliance alarm
        counts \n
        [`dict`]: \n
            * keyword **applianceId** (`str`): ne_pk of appliance
            * keyword **numOfCriticalAlarms** (`int`): number of active
              critical alarms
            * keyword **numOfWarningAlarms** (`int`): number of active
              warning alarms
            * keyword **numOfMinorAlarms** (`int`): number of active
              minor alarms
            * keyword **numOfMajorAlarms** (`int`): number of active
              major alarms
            * keyword **numOfAlarms** (`int`): number of total active
              alarms
    :rtype: list
    """

    return self._get("/alarm/count/appliance")


def get_alarm_notification_status(
    self,
) -> dict:
    """Check status if alarm notifications are enabled

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - GET
          - /alarm/notification

    :return: Dictionary of alarm notification status \n
        * keyword **enable** (`bool`): ``True`` if enabled, ``False`` if
          disabled
    :rtype: dict
    """

    return self._get("/alarm/notification")


def set_alarm_notification_status(self, enable: bool) -> dict:
    """Set status for alarm notifications

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - POST
          - /alarm/notification

    :param enable: ``True`` to enable alarm notifications, ``False`` to
        disable
    :type enable: bool
    :return: Returns True/False based on successful call
    :rtype: bool
    """

    data = {"enable": enable}

    return self._post(
        "/alarm/notification",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def get_alarm_count_from_appliance(
    self,
    ne_id: str,
) -> dict:
    """Returns summary of active alarms for specified appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - GET
          - /alarm/count/appliance/{neId}

    :param ne_id: Network Primary Key (nePk) of existing appliance, e.g.
        ``3.NE``
    :type ne_id: str
    :return: Returns dictionary of active alarm counts \n
        * keyword **numOfCriticalAlarms** (`int`): number of active
          critical alarms
        * keyword **numOfWarningAlarms** (`int`): number of active
          warning alarms
        * keyword **numOfMinorAlarms** (`int`): number of active minor
          alarms
        * keyword **numOfMajorAlarms** (`int`): number of active major
          alarms
    :rtype: dict
    """

    return self._get("/alarm/count/appliance/{}".format(ne_id))


def get_alarm_count_orchestrator_and_appliances(
    self,
) -> dict:
    """Returns summary of active alarms for Orchestrator *and* all
    appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - GET
          - /alarm/summary

    :return: Returns dictionary of active alarm counts \n
        * keyword **numOfCriticalAlarms** (`int`): number of active
          critical alarms
        * keyword **numOfWarningAlarms** (`int`): number of active
          warning alarms
        * keyword **numOfMinorAlarms** (`int`): number of active minor
          alarms
        * keyword **numOfMajorAlarms** (`int`): number of active major
          alarms
    :rtype: dict
    """

    return self._get("/alarm/summary")


def get_alarm_count_orchestrator_or_appliances(
    self,
    alarm_from: str,
) -> dict:
    """Returns summary of active alarms for Orchestrator *or* all
    appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - GET
          - /alarm/summary/{type}

    :param alarm_from: "gms" will provide alarm count from orchestrator,
        "appliance" will provide alarm count from all appliances
    :type alarm_from: str
    :return: Returns dictionary of active alarm counts \n
        * keyword **numOfCriticalAlarms** (`int`): number of active
          critical alarms
        * keyword **numOfWarningAlarms** (`int`): number of active
          warning alarms
        * keyword **numOfMinorAlarms** (`int`): number of active minor
          alarms
        * keyword **numOfMajorAlarms** (`int`): number of active major
          alarms
    :rtype: dict
    """

    return self._get("/alarm/summary/{}".format(alarm_from))


def get_alarms_from_orchestrator(
    self,
    view: str = "all",
    severity: str = None,
    start_time: int = None,
    end_time: int = None,
) -> list:
    """Get active, historical, or all alarms from Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - GET
          - /alarm/gms

    :param view: Accepted values are "active" for current alarms,
        "closed" for historical alarms, "all" for both active and
        historical alarms, defaults to "all"
    :type view: str, optional
    :param severity: Filter by severity of alarm. Accepted values are
        ``warning``, ``minor``, ``major``, and ``critical``,  None
    :type severity: str, optional
    :param start_time: Long(Signed 64 bits) value of milliseconds since
        EPOCH time indicating the starting time boundary of data time
        range,  None
    :type start_time: int, optional
    :param end_time: Long(Signed 64 bits) value of milliseconds since
        EPOCH time indicating the ending time boundary of data time
        range,  None
    :type end_time: int, optional
    :return: Returns list of dictionaries per alarm \n
        [`dict`]: list of alarm dictionary objects \n
            * keyword **id** (`int`): alarm id number
            * keyword **severity** (`str`): severity of alarm
            * keyword **source** (`str`): source of alarm,
              e.g. ``system``
            * keyword **acknowledged** (`bool`): if alarm has been
              acknolwedged
            * keyword **clearable** (`bool`): if the alarm can be
              cleared
            * keyword **timeOccurredInMills** (`int`): time alarm
              occured in unix epoch milliseconds
            * keyword **description** (`str`): alarm description
            * keyword **typ** (`str`): alarm type
            * keyword **recommendedAction** (`str`): recommended action
              message, if any
            * keyword **serviceAffect** (`bool`): if this condition
              could affect service
            * keyword **typeId** (`int`): uuid of alarm type
            * keyword **name** (`str`): name of alarm type
            * keyword **occurrenceCount** (`int`): number of occurences
            * keyword **closed** (`bool`): if alarm has been closed
            * keyword **clearedTimeInMills** (`int`): time alarm cleared
              in unix epoch milliseconds
    :rtype: list
    """

    path = "/alarm/gms?view={}".format(view)

    if severity is not None:
        path = path + "&severity={}".format(severity)
    if start_time is not None:
        path = path + "&from={}".format(start_time)
    if end_time is not None:
        path = path + "&to={}".format(end_time)

    return self._get(path)


def acknowledge_alarms_from_orchestrator(
    self,
    alarm_list: list,
    acknowledge: bool,
) -> dict:
    """Acknowledge alarms from Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - POST
          - /alarm/acknowledgement/gms

    :param alarm_list: List of integer alarm id's to acknowledge
    :type alarm_list: list
    :param acknowledge: ``True`` to acknowledge the alarms, ``False`` to
        leave unacknowledged
    :type acknowledge: bool
    :return: Returns True/False based on successful call
    :rtype: bool
    """

    data = {"ids": alarm_list, "acknowledge": acknowledge}

    return self._post(
        "/alarm/acknowledgement/gms",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def add_note_to_orchestrator_alarm(
    self,
    alarm_list: list,
    note: str,
) -> bool:
    """Add note/comment to specified Orchestrator alarms

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - POST
          - /alarm/note/gms

    :param alarm_list: List of integer alarm id's to acknowledge
    :type alarm_list: list
    :param note: Comment to add to alarms, cannot be a blank string
    :type note: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """

    data = {"ids": alarm_list, "note": note}

    return self._post(
        "/alarm/note/gms",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def clear_alarms_from_orchestrator(
    self,
    alarm_list: list,
) -> bool:
    """Clear specified Orchestrator alarms

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - POST
          - /alarm/clearance/gms

    :param alarm_list: List of integer alarm id's to acknowledge
    :type alarm_list: list
    :param note: Comment to add to alarms, cannot be a blank string
    :type note: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """

    data = {"ids": alarm_list}

    return self._post(
        "/alarm/clearance/gms",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def get_alarm_descriptions(
    self,
    data_format: str,
    default_values: bool,
) -> list:
    """Get alarm descriptions and type details

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - GET
          - /alarm/description2

    :param data_format: If ``csv`` ask browser to download a file of
        Orchestrator alarm descriptions in .csv format.
    :type data_format: str
    :param default_values: If ``True``, export alarm descriptions with
        default values, when ``False``, export alarm descriptions with
        customized values
    :type default_values: bool
    :return: Returns list of all alarm descriptions, corresponding type
        id's, etc. \n
        [`dict`]: alarm object \n
            * keyword **typeId** (`int, optional`): Alarm type id
            * keyword **name** (`str, optional`): Alarm name
            * keyword **severity** (`str, optional`): Alarm severity
              info
            * keyword **description** (`str, optional`): Alarm
              description
            * keyword **recommendedAction** (`str, optional`):
              recommended action
            * keyword **serviceAffecting** (`bool, optional`): Is alarm
              service affecting
            * keyword **source** (`str, optional`): Module/system that
              generates alarm
            * keyword **systemType** (`int, optional`): Identifies which
              system generated the alaram. ``0`` = Appliance,
              ``100`` = Orchestartor
            * keyword **sourceType** (`int, optional`): Identifies the
              category of alarm. ``1`` = Tunnel, ``2`` = Traffic Class,
              ``3`` = Equipment, ``4`` = Software, ``5`` = Threshold
            * keyword **alarmType** (`int, optional`): Uniquely
              identifies the type of alarm within a sourceType
    :rtype: list
    """

    path = "/alarm/description2"

    if data_format is not None:
        path = path + "?format={}".format(data_format)
        if default_values is not None:
            path = path + "&default={}".format(default_values)
    elif default_values is not None:
        path = path + "?default={}".format(default_values)
    else:
        pass

    return self._get(path)


def get_customized_alarm_severity(
    self,
) -> list:
    """Get customized alarm severities

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - GET
          - /alarm/customization/severity

    :return: Returns list of all customized alarm serverities \n
        [`dict`]: alarm object \n
            * keyword **<alarm_typeId>** (`int`): Alarm severity
    :rtype: list
    """

    return self._get("/alarm/customization/severity")


def set_customized_alarm_severity(
    self,
    alarm_severities: dict,
) -> bool:
    """Set customized alarm severities for alarm type id's

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - POST
          - /alarm/customization/severity

    :param alarm_severities: Dictionary of alarm type id's and
        corresponding severity \n
        * keyword **<alarm_type_id>** (`str`): Severity values can be
          ``warning``, ``minor``, ``major``, and ``critical``
    :type alarm_severities: dict
    :return: Returns True/False based on successful call
    :rtype: bool
    """

    data = alarm_severities

    return self._post(
        "/alarm/customization/severity", data=data, return_type="bool"
    )


def update_customized_alarm_severity(
    self,
    alarm_severities: dict,
) -> bool:
    """Update customized alarm severities for alarm type id's

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - PUT
          - /alarm/customization/severity

    :param alarm_severities: Dictionary of alarm type id's and
        corresponding severity \n
        * keyword **<alarm_type_id>** (`str`): Severity values can be
          ``warning``, ``minor``, ``major``, and ``critical``
    :type alarm_severities: dict
    :return: Returns True/False based on successful call
    :rtype: bool
    """

    data = alarm_severities

    return self._put(
        "/alarm/customization/severity", data=data, return_type="bool"
    )


def delete_all_customized_alarm_severity(
    self,
) -> bool:
    """Deletes all customized alarm severity settings

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - DELETE
          - /alarm/customization/severity

    :return: Returns True/False based on successful call
    :rtype: bool
    """

    return self._delete("/alarm/customization/severity", return_type="bool")


def get_customized_alarm_severity_for_type(
    self,
    alarm_type_id: int,
) -> dict:
    """Get customized alarm severity for specific alarm type id.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - GET
          - /alarm/customization/severity/{alarmTypeId}

    .. note::
        If the alarm type is not customized it will return HTTP 204 with
        no content.

    :param alarm_type_id: Alarm type id, e.g. 65536
    :type alarm_type_id: int
    :return: Returns dictionary of customized alarm serverity for alarm
        type id \n
        * keyword **<alarm_type_id>** (`str`): Severity values can be
          ``warning``, ``minor``, ``major``, and ``critical``
    :rtype: dict
    """

    return self._get(
        "/alarm/customization/severity/{}".format(alarm_type_id),
        expected_status=[200, 204],
    )


def delete_customized_alarm_severity_for_type(
    self,
    alarm_type_id: int,
) -> bool:
    """Deletes customized alarm severity settings for specific alarm
    type id

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - DELETE
          - /alarm/customization/severity/{alarmTypeId}

    .. note::
        If the alarm type is not customized it will return HTTP 204 with
        no content.

    :param alarm_type_id: Alarm type id, e.g. ``65536``
    :type alarm_type_id: int
    :return: Returns True/False based on successful call
    :rtype: bool
    """

    return self._delete(
        "/alarm/customization/severity/{}".format(alarm_type_id),
        expected_status=[200, 204],
        return_type="bool",
    )


def get_alarm_email_delay(
    self,
) -> dict:
    """Get alarm email delay configuration.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - GET
          - /alarm/delayEmail

    .. note::
        If no delay is configured will return HTTP 204 no content.

    :return: Returns dictionary alarm email delay duration \n
        * keyword **duration** (`int`): Alarm email delay duration in
          seconds
    :rtype: dict
    """

    return self._get("/alarm/delayEmail", expected_status=[200, 204])


def set_alarm_email_delay(
    self,
    alarm_email_delay: int,
) -> bool:
    """Set alarm email delay configuration

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - POST
          - /alarm/delayEmail

    :param alarm_email_delay: Alarm email delay duration in seconds
    :type alarm_email_delay: int
    :return: Returns True/False based on successful call
    :rtype: bool
    """

    data = {"duration": alarm_email_delay}

    return self._post("/alarm/delayEmail", data=data, return_type="bool")


def update_alarm_email_delay(
    self,
    alarm_email_delay: int,
) -> bool:
    """Update alarm email delay configuration

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - PUT
          - /alarm/delayEmail

    :param alarm_email_delay: Alarm email delay duration in seconds
    :type alarm_email_delay: int
    :return: Returns True/False based on successful call
    :rtype: bool
    """

    data = {"duration": alarm_email_delay}

    return self._put("/alarm/delayEmail", data=data, return_type="bool")


def delete_alarm_email_delay(
    self,
) -> bool:
    """Deletes alarm email delay configuration

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - DELETE
          - /alarm/delayEmail

    :return: Returns True/False based on successful call
    :rtype: bool
    """

    return self._delete("/alarm/delayEmail", return_type="bool")


def get_supressed_alarms(
    self,
) -> dict:
    """Get configured supressed alarms

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - GET
          - /alarm/suppress

    :return: Returns dictionary of appliances and alarm types that are
        currently disabled \n
        * keyword **alarmTypeIds** (`list[int]`): List of alarm type ids
        * keyword **applianceIds** (`list[str]`): List of appliance ids
    :rtype: dict
    """

    return self._get("/alarm/suppress")


def set_supressed_alarms(
    self,
    action: str,
    alarm_list: list,
    ne_pk_list: list[str],
) -> bool:
    """Set to suppress or enabled (if previously suppressed) specified
    alarm types on specified appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - POST
          - /alarm/suppress

    :param action: ``ENABLE`` to enable/re-enable or ``DISABLE`` to
        suppress/disable.
    :type action: str
    :param alarm_list: List of alarm type ids. Value can not be null.
        e.g. ``[65536, 65537]``
    :type alarm_list: list
    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :return: Returns True/False based on successful call
    :rtype: bool
    """

    data = {
        "action": action,
        "alarmTypeIds": alarm_list,
        "applianceIds": ne_pk_list,
    }

    return self._post(
        "/alarm/suppress", data=data, expected_status=[204], return_type="bool"
    )


def delete_supressed_alarms(
    self,
) -> bool:
    """Re-enable all disabled alarms

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - DELETE
          - /alarm/suppress

    :return: Returns True/False based on successful call
    :rtype: bool
    """

    return self._delete("/alarm/suppress", return_type="bool")
