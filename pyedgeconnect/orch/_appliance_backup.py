# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# applianceBackup : ECOS backup and restore
from __future__ import annotations


def backup_appliance_config(
    self,
    ne_pk_list: list[str],
    comment: str,
) -> dict:
    """Backup appliance configuration to Orchestrator database

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applianceBackup
          - POST
          - /appliance/backup

    The response of this operation is a client key which can be polled
    to get progress of the requested operation. To poll for status,
    perform
    :func:`pyedgeconnect.Orchestrator.get_audit_log_task_status`

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :param comment: Comment to include with action
    :type comment: str
    :return: Returns dictionary with identifying key of this task. \n
        * keyword **clientKey** (`str`): Client key which can be polled
          to get progress of the requested action.
    :rtype: dict
    """
    data = {
        "neList": ne_pk_list,
        "comment": comment,
    }

    return self._post("/appliance/backup", data=data)


def get_appliance_backup_history(
    self,
    ne_id: str,
    running_config: bool,
    appliance_backup_id: int = None,
) -> list:
    """Get backup history of appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applianceBackup
          - GET
          - /appliance/backup/{neId}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param running_config: ``True`` to include appliance running
        configuration in the response data. ``False`` will set the
        ``runningConfig`` value to ``null``
    :type running_config: bool
    :param appliance_backup_id: The integer id of a specific backup to
        filter for, defaults to None
    :type appliance_backup_id: int, optional
    :return: Returns list of dictionaries of appliance backup history \n
        [`dict`]: Appliance backup object \n
            * keyword **id** (`int`): The id number of this backup in
              Orchestrator database
            * keyword **comment** (`str`): Comment message on backup
            * keyword **backupTime** (`int`): Time backup was executed
              in unix epoch seconds
            * keyword **swVersion** (`str`): Appliance software version
              at time of backup
            * keyword **fileName** (`str`): The filename on which the
              appliance configuration is now based
            * keyword **runningConfig** (`str`): The appliance currently
              active configuration files' data
            * keyword **uploadStream**: No description in Swagger, often
              value of ``null``
    :rtype: dict
    """
    path = "/appliance/backup/{}?runningConfig={}".format(
        ne_id, running_config
    )

    if appliance_backup_id is not None:
        path = path + "&id={}".format(appliance_backup_id)

    return self._get(path)


def delete_appliance_backup(
    self,
    appliance_backup_id: int,
) -> bool:
    """Delete specific backup of appliance from Orchestrator database

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applianceBackup
          - DELETE
          - /appliance/backup/{backupFilePk}

    :param appliance_backup_id: The integer id of a specific backup to
        filter for, defaults to None
    :type appliance_backup_id: int
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        "/appliance/backup/{}".format(appliance_backup_id),
        return_type="bool",
    )


def restore_appliance_from_backup(
    self,
    ne_pk: str,
    appliance_backup_id: int,
) -> dict:
    """Restore appliance from the specified backup

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applianceBackup
          - POST
          - /appliance/restore/{nePk}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param appliance_backup_id: The integer id of a specific backup to
        filter for, defaults to None
    :type appliance_backup_id: int
    :return: Returns dictionary with identifying key of this task. \n
        * keyword **clientKey** (`str`): Client key which can be polled
          to get progress of the requested action.
    :rtype: dict
    """
    data = {"backupFilePk": appliance_backup_id}

    return self._post("/appliance/restore/{}".format(ne_pk), data=data)
