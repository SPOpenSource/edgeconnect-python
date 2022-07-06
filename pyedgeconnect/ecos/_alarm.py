# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# alarm : Alarms
from __future__ import annotations


def get_appliance_alarms(
    self,
) -> dict:
    """Return active alarms

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - GET
          - /alarm

    :return: Returns summary of alarms and outstanding alarm details \n
        * keyword **summary** (`dict`): Alarm summary object \n
            * keyword **num_cleared** (`int`): Number of alarms cleared
            * keyword **num_critical** (`int`): Number of critical
              alarms
            * keyword **num_equipment_outstanding** (`int`): Number of
              hardware alarms outstanding
            * keyword **num_major** (`int`): Number of major alarms
            * keyword **num_minor** (`int`): Number of minor alarms
            * keyword **num_outstanding** (`int`): Number of
              outstanding alarms
            * keyword **num_raise_ignore** (`int`): Number of raise
              ignore
            * keyword **num_software_outstanding** (`int`): Number of
              software alarms outstanding
            * keyword **num_tca_outstanding** (`int`): Number of TCA
              alarms outstanding
            * keyword **num_traffic_class_outstanding** (`int`): Number
              of traffic class alarms outstanding
            * keyword **num_tunnel_outstanding** (`int`): Number of
              tunnel alarms outstanding
            * keyword **num_warning** (`int`): Number of warning alarms
        * keyword **outstanding** (`list[dict]`): Outstanding alarms \n
            * [`dict`]: Outstanding Alarm detail object \n
                * keyword **severity** (`int`): Alarm severity,
                  ``0`` translates to ``Info``,
                  ``1`` translates to ``Warning``,
                  ``2`` translates to ``Minor``,
                  ``3`` translates to ``Major``,
                  ``4`` translates to ``Critical``,
                * keyword **sequenceId** (`int`): Alarm sequence ID
                * keyword **source** (`str`): Source IP address
                * keyword **acknowledged** (`bool`): ``True`` if alarm
                  has been acknowledged
                * keyword **clearable** (`bool`): ``True`` if alarm
                  can be cleared by user
                * keyword **time** (`int`): Time alarm occured in unix
                  epoch ms
                * keyword **description** (`str`): Description of alarm
                  detail
                * keyword **type** (`str`): Hardware (``HW``) or
                  Software (``SW``)
                * keyword **recommendation** (`str`): Recommended action
                  for alarm
                * keyword **serviceAffect** (`bool`): ``True`` if
                  condition could be service affecting
                * keyword **typeId** (`int`): Alarm type ID number
                * keyword **name** (`str`): Alarm name
                * keyword **occurenceCount** (`int`): Count of
                  occurences of alarm
                * keyword **active** (`bool`): ``True`` if alarm is
                  currently active
                * keyword **ackedBy** (`str`): Username that
                  acknolwedged alarm
                * keyword **ackedTime** (`int`): Time of acknolwedgement
                  in Unix epoch ms
                * keyword **clearedBy** (`str`): Username that cleared
                  alarm
                * keyword **clearedTime** (`int`): Time of clear in Unix
                  epoch ms
                * keyword **note** (`str`): Additional alarm notes
    :rtype: dict
    """
    return self._get("/alarm")


def acknowledge_appliance_alarms(
    self,
    alarm_seq_ids: list[int],
    acknowledge: bool,
    ack_by: str,
) -> bool:
    """Acknowledge appliance alarms by sequence ids

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - POST
          - /alarm/acknowledgement

    :param alarm_seq_ids: List of alarm sequence ids to acknowledge
    :type alarm_seq_ids: list[int]
    :param acknowledge: ``True`` to acknowledge alarms
    :type acknowledge: bool
    :param ack_by: User to mark alarms acknowledged by
    :type ack_by: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "sequenceIds": alarm_seq_ids,
        "acknowledge": acknowledge,
        "ackedBy": ack_by,
    }

    return self._post(
        "/alarm/acknowledgement",
        data=data,
        return_type="bool",
    )


def clear_appliance_alarms(
    self,
    alarm_seq_ids: list[int],
    cleared_by: str,
) -> bool:
    """Acknowledge appliance alarms by sequence ids

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - POST
          - /alarm/clearance

    :param alarm_seq_ids: List of alarm sequence ids to clear
    :type alarm_seq_ids: list[int]
    :param cleared_by: User to mark alarms cleared by
    :type cleared_by: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "sequenceIds": alarm_seq_ids,
        "clearedBy": cleared_by,
    }

    return self._post(
        "/alarm/clearance",
        data=data,
        return_type="bool",
    )


def get_appliance_alarm_descriptions(
    self,
    response_format: str = None,
) -> list:
    """Get Orchestrator alarm descriptions

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - GET
          - /alarm/description2

    :param response_format: Specify to ``csv`` to download CSV format,
        otherwise will return information in list of dictionaries of
        JSON format, defaults to None
    :type response_format: str, optional
    :return: Returns list of alarm descriptions and details \n
        * [`dict`]: List of alarm description dictionaries \n
            * keyword **typeId** (`int`): Alarm type id
            * keyword **severity** (`str`): Alarm severity info
            * keyword **description** (`str`): Alarm description
            * keyword **recommendedAction** (`str`): recommended action
            * keyword **serviceAffecting** (`bool`): Is alarm service
              affecting
            * keyword **source** (`str`): Module/system that generates
              alarm
            * keyword **systemType** (`int`): Identifies which system
              generated the alaram.0 = Appliance,100 = Orchestartor
            * keyword **sourceType** (`int`): Identifies the category of
              alarm. ``1`` = Tunnel, ``2`` = Traffic Class, ``3`` =
              Equipment, ``4`` = Software, ``5`` = Threshold
            * keyword **alarmType** (`int`): Uniquely identifies the
              type of alarm within a sourceType
            * keyword **clearable** (`bool`): Identifies whether an
              alarm is clearable
    :rtype: dict
    """
    path = "/alarm/description2"

    if response_format is not None:
        path += f"?format={response_format}"

    return self._get(path)


def add_note_appliance_alarms(
    self,
    alarm_seq_ids: list[int],
    note: str,
) -> bool:
    """Update notes on appliance alarms

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - POST
          - /alarm/note

    :param alarm_seq_ids: List of alarm sequence ids to add note to
    :type alarm_seq_ids: list[int]
    :param note: Note to add to specified alarms
    :type note: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "sequenceIds": alarm_seq_ids,
        "note": note,
    }

    return self._post(
        "/alarm/note",
        data=data,
        return_type="bool",
    )


def delete_appliance_alarms(
    self,
    alarm_seq_ids: list[int],
) -> bool:
    """Delete alarms on appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - alarm
          - POST
          - /alarm/delete

    :param alarm_seq_ids: List of alarm sequence ids to delete
    :type alarm_seq_ids: list[int]
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "sequenceIds": alarm_seq_ids,
    }

    return self._post(
        "/alarm/delete",
        data=data,
        return_type="bool",
    )
