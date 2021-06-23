# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# gmsBackup : Orchestrator Backup


def get_orchestrator_backup_config(self) -> dict:
    """Get configured backup settings for Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsBackup
          - GET
          - /gms/backup

    :return: Returns dictionary of Orchestrator backup settings \n
        * keyword **protocol** (`int`): The protocol of the remote
          server, ``3`` - SCP, ``4`` - HTTP, ``5`` - HTTPS, ``6`` -
          SFTP, any other number corresponds to FTP
        * keyword **hostname** (`str`): The hostname of the remote
          server
        * keyword **port** (`int`): The port of the remote server
        * keyword **maxBackups** (`int`): The number of the backup files
          in the directory,
        * keyword **directory** (`str`): The directory for the backup on
          the remote server
        * keyword **username** (`str`): The username to connect to the
          remote server
        * keyword **password** (`str`): Will be ``null`` for security
          reasons
    :rtype: dict
    """
    return self._get("/gms/backup")


def test_orchestrator_backup_config(
    self,
    protocol: int,
    hostname: str,
    port: int,
    directory: str,
    username: str,
    password: str,
) -> dict:
    """Test specified settings for an Orchestrator backup

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsBackup
          - POST
          - /gms/backup/testConnection

    :param protocol: The protocol of the remote server, ``3`` - SCP,
        ``4`` - HTTP, ``5`` - HTTPS, ``6`` - SFTP, any other number
        corresponds to FTP
    :type protocol: int
    :param hostname: The hostname or ip of the remote server
    :type hostname:
    :param port: Port to connect to remove server on
    :type port: int
    :param directory: The directory for the backup on the remote server
    :type directory: str
    :param username: The username to connect to the remote server
    :type username: str
    :param password: The password to connect to the remote server
    :type password: str
    :return: Returns dictionary of backup test results \n
        * keyword **message** (`str`): Orchestrator backup test results
    :rtype: dict
    """
    data = {
        "protocol": protocol,
        "hostname": hostname,
        "port": port,
        "directory": directory,
        "username": username,
        "password": password,
        "maxBackups": 0,
    }

    return self._post("/gms/backup/testConnection", data=data)


def add_or_update_orchestrator_backup_config(
    self,
    protocol: int,
    hostname: str,
    port: int,
    directory: str,
    username: str,
    password: str,
    max_backups: int,
) -> dict:
    """Add or update Orchestrator backup configuration. Separate
    configurations are unique by value of hostname.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsBackup
          - POST
          - /gms/backup/config

    The schedule of the backup has to be added or adjusted via the job
    scheduling functions (rest API calls beginning with `/gms/job...`)

    :param protocol: The protocol of the remote server, ``3`` - SCP,
        ``4`` - HTTP, ``5`` - HTTPS, ``6`` - SFTP, any other number
        corresponds to FTP
    :type protocol: int
    :param hostname: The hostname or ip of the remote server
    :type hostname:
    :param port: Port to connect to remove server on
    :type port: int
    :param directory: The directory for the backup on the remote server
    :type directory: str
    :param username: The username to connect to the remote server
    :type username: str
    :param password: The password to connect to the remote server
    :type password: str
    :param max_backups: Number of maximum backups to store
    :type max_backups: int
    :return: Returns dictionary with backup configuration id \n
        * keyword **gmsConfigId** (`int`): Backup configuration id
          number
    :rtype: dict
    """
    data = {
        "protocol": protocol,
        "hostname": hostname,
        "port": port,
        "directory": directory,
        "username": username,
        "password": password,
        "maxBackups": max_backups,
    }

    return self._post("/gms/backup/config", data=data)


def create_orchestrator_blueprint_template(
    self,
    mode: str,
    download: str = "",
) -> dict:
    """Create an Orchestrator blueprint template and download. This
    operation takes a significant amount of time to run.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsBackup
          - GET
          - /gms/backup/exportTemplate?mode={mode}&download={download}

    For the ``mode`` parameter: \n
    * Value of ``template`` includes all Orchestrator configuration
      except for the following: \n
        * All stats and large historical data (including audit logs,
          report histories, etc.)
        * Not allowed if appliances are in orchestrator.
    * Value of ``migration`` Includes all Orchestrator configuration
      except for the following: \n
        * All stats and large historical data (including audit logs,
          report histories, etc.)
        * Should be used to migrate from cloud to on premise or vice
          versa.

    :param mode: Accepted values are ``template`` or ``migration``
    :type mode: str
    :param download: Any supplied value will be considered as true,
        defaults to ""
    :type download: str, optional
    :return: Returns string of all Orchestrator blueprint config
    :rtype: str
    """
    return self._get(
        "/gms/backup/exportTemplate?mode={}&download={}".format(
            mode, download
        ),
        return_type="text",
    )
