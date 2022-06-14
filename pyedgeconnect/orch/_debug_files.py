# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# debugFiles : ECOS debug files like tcpdump, snapshots, sysdumps
from __future__ import annotations


def get_debug_files_from_appliance(
    self,
    ne_pk: str,
) -> dict:
    """Get debug files from appliance. Each debug file info contains
    'name' and 'stats'. The value of the stats is a dictionary of the
    stats.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - debugFiles
          - GET
          - /debugFiles/{nePk}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :return: Returns dictionary of appliance debug file information. \n
        * keyword **debugDump** (`list[dict]`): Info of Sys Dump file \n
            [`dict`]: debug file object \n
                * keyword **name** (`str`): name of file
                * keyword **stats** (`dict`): file statistics \n
                    * keyword **dev** (`int, optional`): No description
                      in Swagger
                    * keyword **mode** (`int, optional`): The mode of
                      the file
                    * keyword **nlink** (`int, optional`): No
                      description in Swagger
                    * keyword **uid** (`int, optional`): No description
                      in Swagger
                    * keyword **gid** (`int, optional`): No description
                      in Swagger
                    * keyword **rdev** (`int, optional`): No description
                      in Swagger
                    * keyword **blksize** (`int, optional`): The size of
                      the block
                    * keyword **ino** (`int, optional`): No description
                      in Swagger
                    * keyword **size** (`int, optional`): The size of
                      the file
                    * keyword **blocks** (`int, optional`): The blocks
                      of the file
                    * keyword **atime** (`str, optional`): The access
                      time of the file
                    * keyword **mtime** (`str, optional`): The modified
                      time of the file
                    * keyword **ctime** (`str, optional`): The change
                      time of the file
                    * keyword **birthtime** (`str, optional`): No
                      description in Swagger
        * keyword **techDump** (`list[dict]`): Info of Show Tech file \n
            [`dict`]: debug file object \n
                * keyword **name** (`str`): name of file
                * keyword **stats** (`dict`): file statistics \n
                    * keyword **dev** (`int, optional`): No description
                      in Swagger
                    * keyword **mode** (`int, optional`): The mode of
                      the file
                    * keyword **nlink** (`int, optional`): No
                      description in Swagger
                    * keyword **uid** (`int, optional`): No description
                      in Swagger
                    * keyword **gid** (`int, optional`): No description
                      in Swagger
                    * keyword **rdev** (`int, optional`): No description
                      in Swagger
                    * keyword **blksize** (`int, optional`): The size of
                      the block
                    * keyword **ino** (`int, optional`): No description
                      in Swagger
                    * keyword **size** (`int, optional`): The size of
                      the file
                    * keyword **blocks** (`int, optional`): The blocks
                      of the file
                    * keyword **atime** (`str, optional`): The access
                      time of the file
                    * keyword **mtime** (`str, optional`): The modified
                      time of the file
                    * keyword **ctime** (`str, optional`): The change
                      time of the file
                    * keyword **birthtime** (`str, optional`): No
                      description in Swagger
        * keyword **snapshots** (`list[dict]`): Info of Snapshot file \n
            [`dict`]: debug file object \n
                * keyword **name** (`str`): name of file
                * keyword **stats** (`dict`): file statistics \n
                    * keyword **dev** (`int, optional`): No description
                      in Swagger
                    * keyword **mode** (`int, optional`): The mode of
                      the file
                    * keyword **nlink** (`int, optional`): No
                      description in Swagger
                    * keyword **uid** (`int, optional`): No description
                      in Swagger
                    * keyword **gid** (`int, optional`): No description
                      in Swagger
                    * keyword **rdev** (`int, optional`): No description
                      in Swagger
                    * keyword **blksize** (`int, optional`): The size of
                      the block
                    * keyword **ino** (`int, optional`): No description
                      in Swagger
                    * keyword **size** (`int, optional`): The size of
                      the file
                    * keyword **blocks** (`int, optional`): The blocks
                      of the file
                    * keyword **atime** (`str, optional`): The access
                      time of the file
                    * keyword **mtime** (`str, optional`): The modified
                      time of the file
                    * keyword **ctime** (`str, optional`): The change
                      time of the file
                    * keyword **birthtime** (`str, optional`): No
                      description in Swagger
        * keyword **tcpDump** (`list[dict]`): Info of TCP Dump file \n
            [`dict`]: debug file object \n
                * keyword **name** (`str`): name of file
                * keyword **stats** (`dict`): file statistics \n
                    * keyword **dev** (`int, optional`): No description
                      in Swagger
                    * keyword **mode** (`int, optional`): The mode of
                      the file
                    * keyword **nlink** (`int, optional`): No
                      description in Swagger
                    * keyword **uid** (`int, optional`): No description
                      in Swagger
                    * keyword **gid** (`int, optional`): No description
                      in Swagger
                    * keyword **rdev** (`int, optional`): No description
                      in Swagger
                    * keyword **blksize** (`int, optional`): The size of
                      the block
                    * keyword **ino** (`int, optional`): No description
                      in Swagger
                    * keyword **size** (`int, optional`): The size of
                      the file
                    * keyword **blocks** (`int, optional`): The blocks
                      of the file
                    * keyword **atime** (`str, optional`): The access
                      time of the file
                    * keyword **mtime** (`str, optional`): The modified
                      time of the file
                    * keyword **ctime** (`str, optional`): The change
                      time of the file
                    * keyword **birthtime** (`str, optional`): No
                      description in Swagger
        * keyword **debugFile** (`list[dict]`): Info of debug file \n
            [`dict`]: debug file object \n
                * keyword **name** (`str`): name of file
                * keyword **stats** (`dict`): file statistics \n
                    * keyword **dev** (`int, optional`): No description
                      in Swagger
                    * keyword **mode** (`int, optional`): The mode of
                      the file
                    * keyword **nlink** (`int, optional`): No
                      description in Swagger
                    * keyword **uid** (`int, optional`): No description
                      in Swagger
                    * keyword **gid** (`int, optional`): No description
                      in Swagger
                    * keyword **rdev** (`int, optional`): No description
                      in Swagger
                    * keyword **blksize** (`int, optional`): The size of
                      the block
                    * keyword **ino** (`int, optional`): No description
                      in Swagger
                    * keyword **size** (`int, optional`): The size of
                      the file
                    * keyword **blocks** (`int, optional`): The blocks
                      of the file
                    * keyword **atime** (`str, optional`): The access
                      time of the file
                    * keyword **mtime** (`str, optional`): The modified
                      time of the file
                    * keyword **ctime** (`str, optional`): The change
                      time of the file
                    * keyword **birthtime** (`str, optional`): No
                      description in Swagger
        * keyword **log** (`list[dict]`): Info of the log file \n
            [`dict`]: debug file object \n
                * keyword **name** (`str`): name of file
                * keyword **stats** (`dict`): file statistics \n
                    * keyword **dev** (`int, optional`): No description
                      in Swagger
                    * keyword **mode** (`int, optional`): The mode of
                      the file
                    * keyword **nlink** (`int, optional`): No
                      description in Swagger
                    * keyword **uid** (`int, optional`): No description
                      in Swagger
                    * keyword **gid** (`int, optional`): No description
                      in Swagger
                    * keyword **rdev** (`int, optional`): No description
                      in Swagger
                    * keyword **blksize** (`int, optional`): The size of
                      the block
                    * keyword **ino** (`int, optional`): No description
                      in Swagger
                    * keyword **size** (`int, optional`): The size of
                      the file
                    * keyword **blocks** (`int, optional`): The blocks
                      of the file
                    * keyword **atime** (`str, optional`): The access
                      time of the file
                    * keyword **mtime** (`str, optional`): The modified
                      time of the file
                    * keyword **ctime** (`str, optional`): The change
                      time of the file
                    * keyword **birthtime** (`str, optional`): No
                      description in Swagger
    :rtype: dict
    """
    return self._get("/debugFiles/{}".format(ne_pk))


def delete_debug_file_from_orchestrator(
    self,
    filename: str,
) -> bool:
    """Delete debug file from Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - debugFiles
          - POST
          - /debugFiles/delete

    :param filename: Name of debug file to delete from Orchestrator
    :type filename: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {"fileName": filename}

    return self._post(
        "/debugFiles/delete",
        data=data,
        return_type="bool",
    )


def get_debug_file_proxy_settings(self) -> dict:
    """Get debug file proxy settings on Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - debugFiles
          - GET
          - /debugFiles/proxyConfig

    :return: Returns dictionary of appliance debug file information. \n
        * keyword **useProxy** (`bool`): Use a proxy or not for file
          upload
        * keyword **proxyHost** (`str`): Hostname or IP address of proxy
        * keyword **proxyUser** (`str`): Username
        * keyword **proxyPassword** (`str`): Password
        * keyword **proxyPort** (`int`): Port to connect to proxy
    :rtype: dict
    """
    return self._get("/debugFiles/proxyConfig")


def set_debug_file_proxy_settings(
    self,
    use_proxy: bool,
    proxy_host: str,
    proxy_user: str,
    proxy_password: str,
    proxy_port: int,
) -> bool:
    """Set proxy settings for debug files on Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - debugFiles
          - POST
          - /debugFiles/proxyConfig

    :param use_proxy: ``True`` to use a proxy for file upload or
        ``False`` if not
    :type use_proxy: bool
    :param proxy_host: Hostname or IP address of proxy
    :type proxy_host: str
    :param proxy_user: Username to authenticate with proxy
    :type proxy_user: str
    :param proxy_password: Password to authenticate with proxy
    :type proxy_password: str
    :param proxy_port: Port number to connect to proxy on, e.g. ``8443``
    :type proxy_port: int
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "useProxy": use_proxy,
        "proxyHost": proxy_host,
        "proxyUser": proxy_user,
        "proxyPassword": proxy_password,
        "proxyPort": proxy_port,
    }

    return self._post(
        "/debugFiles/proxyConfig",
        data=data,
        return_type="bool",
    )


def cancel_debug_file_download(self) -> bool:
    """Cancel download of debug file

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - debugFiles
          - POST
          - /debugFiles/cancel

    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/debugFiles/cancel",
        return_type="bool",
    )


def delete_debug_file_from_appliance(
    self,
    ne_pk: str,
    group: str = None,
    filename: str = None,
) -> bool:
    """Delete debug files from an appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - debugFiles
          - POST
          - /debugFiles/delete/{nePk}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param group: The group the file to delete belongs to,
        defaults to None
    :type group: str, optional
    :param filename: Name of file to delete, defaults to None
    :type filename: str, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {}
    if group is not None:
        data["group"] = group
    if filename is not None:
        data["local_filename"] = filename

    return self._post(
        "/debugFiles/delete/{}".format(ne_pk),
        data=data,
        return_type="bool",
    )


def generate_appliance_sysdump(
    self,
    ne_pk_list: list[str],
) -> bool:
    """Generate an appliance SysDump on one or more appliances

    .. note::
      This API Call is not in current Swagger as of Orch 9.0.3

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - n/a
          - POST
          - /debugFiles/generateApplianceSysDump

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {"neList": ne_pk_list}

    return self._post(
        "/debugFiles/generateApplianceSysDump",
        data=data,
        return_type="bool",
    )


def upload_appliance_debug_files_to_support(
    self,
    ne_pk: str,
    debug_file_group: str,
    debug_filenames: list,
    case_number: str,
) -> bool:
    """Upload appliance debug files to support case

    .. note::
      This API Call is not in current Swagger as of Orch 9.0.3

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - n/a
          - POST
          - /debugFiles/uploadApplianceFilesToAWS

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param debug_file_group: Type of debug files, accepted values are
        ``debugDump`` for sysdumps, ``techDump`` for show tech,
        ``snapshots``, ``tcpDump`` for packet captures, ``debugFile``,
        and ``log`` for log file.
    :type debug_file_group: str
    :param debug_filenames: List of filenames of debug files to upload
        to the case
    :type debug_filenames: list
    :param case_number: Support case number to upload the files to
    :type case_number: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "appliances": [
            {
                "nePk": ne_pk,
                "files": [
                    {"group": "debugDump", "fileNames": debug_filenames}
                ],
            }
        ],
        "options": {"caseKey": case_number},
    }

    return self._post(
        "/debugFiles/uploadApplianceFilesToAWS",
        data=data,
        return_type="bool",
    )


def upload_appliance_debug_files_to_orchestrator(
    self,
    ne_pk: str,
    debug_file_group: str,
    debug_filenames: list,
) -> bool:
    """Upload appliance debug files to Orchestrator (user can then
    download in the UI)

    .. note::
      This API Call is not in current Swagger as of Orch 9.0.3

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - n/a
          - POST
          - /applianceFiles/uploadToOrchestrator

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param debug_file_group: Type of debug files, accepted values are
        ``debugDump`` for sysdumps, ``techDump`` for show tech,
        ``snapshots``, ``tcpDump`` for packet captures, ``debugFile``,
        and ``log`` for log file.
    :type debug_file_group: str
    :param debug_filenames: List of filenames of debug files to upload
        to the case
    :type debug_filenames: list
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "appliances": [
            {
                "nePk": ne_pk,
                "files": [
                    {"group": debug_file_group, "fileNames": debug_filenames}
                ],
            }
        ],
    }

    return self._post(
        "/applianceFiles/uploadToOrchestrator",
        data=data,
        return_type="bool",
    )
