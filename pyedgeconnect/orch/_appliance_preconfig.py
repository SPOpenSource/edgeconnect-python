# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# appliancePreconfig : Get and apply appliance preconfigurations
import base64


def get_all_preconfig(
    self,
    data_filter: str = None,
) -> list:
    """Get preconfigs from Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliancePreconfig
          - GET
          - /gms/appliance/preconfiguration

    :param filter: Filter of returned results. Value of "names" will
        return list of dictionaries of just preconfig names. Value of
        "metadata" will include all associated metatdata without
        configuration data. No filter will return all metadata and
        base64 of the preconfig configuration, defaults to None
    :type filter: str, optional
    :return: Returns list of dictionaries of preconfigs and/or
        associated metadata and configuration \n
        [`dict`]: preconfig object \n
            * keyword **id** (`int, optional`): Id of the
              preconfiguration, used to reference this preconfiguration
              in the other APIs
            * keyword **name** (`str, optional`): Name of the
              preconfiguration
            * keyword **serialNum** (`str, optional`): Serial number to
              match on
            * keyword **tag** (`str, optional`): Tag to match on,
            * keyword **comment** (`str, optional`): User provided
              comment for the preconfiguration
            * keyword **autoApply** (`bool, optional`): Automatically
              apply this preconfiguration to the matched appliance when
              Orchestrator discovers it
            * keyword **configData** (`str, optional`): Base64 encoded
              preconfiguration YAML string
            * keyword **createdtime** (`int, optional`): Time when
              preconfiguration was created in epoch milliseconds
            * keyword **modifiedtime** (`int, optional`): Time when
              preconfiguration was last modified in epoch milliseconds
            * keyword **nepk** (`str, optional`): Appliance ID that
              preconfig was last applied to
            * keyword **discoveredId** (`str, optional`): Discovered
              appliance ID that preconfig was last applied to (the id
              of appliances in the discovered tab are different than
              when the appliance is approved)
            * keyword **guid** (`str, optional`): ID of the log created
              in actionlog when the preconfiguration was applied
            * keyword **taskStatus** (`int, optional`): The current
              status of the preconfig apply. ``0``: Not Started, ``1``:
              In Progress, and ``2``: Finished
            * keyword **completionStatus** (`bool, optional`): Whether
              the apply was successful or not, only look at this if
              taskStatus == ``2``
            * keyword **starttime** (`int, optional`): Start time of
              last apply in epoch milliseconds
            * keyword **endtime** (`int, optional`): End time of last
              apply in epoch milliseconds
            * keyword **result** (`list[dict], optional`): results \n
                [`dict`]: results object \n
                    * keyword **taskStatus** (`int, optional`): The
                      current status of the preconfig apply.
                      ``0``: Not Started, ``1``: In Progress, ``2``:
                      Finished
                    * keyword **completionStatus** (`bool, optional`):
                      Whether the apply was successful or not, only
                      look at this if taskStatus == ``2``
                    * keyword **name** (`str, optional`): Name of the
                      task
                    * keyword **result** (`str, optional`):
                      Status/result string information of the task
                    * keyword **nePk** (`str, optional`): Appliance ID
                      task applies to
                    * keyword **data** (`str, optional`): String or JSON
                      for the data that was used by this task
    :rtype: list
    """
    if data_filter == "names":
        return self._get("/gms/appliance/preconfiguration?filter=names")
    elif data_filter == "metadata":
        return self._get("/gms/appliance/preconfiguration?filter=metadata")
    else:
        return self._get("/gms/appliance/preconfiguration")


def create_preconfig(
    self,
    hostname: str,
    yaml_preconfig: str,
    auto_apply: bool,
    serial_number: str = "",
    tag: str = "",
    comment: str = "",
) -> bool:
    """Upload a YAML Preconfig to Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliancePreconfig
          - POST
          - /gms/appliance/preconfiguration

    :param hostname: Name of preconfig and tag to match, often the
        hostname of the intended device
    :type hostname: str
    :param yaml_preconfig: YAML text of preconfig configuration, this
        will get base64 converted in this function before upload.
    :type yaml_preconfig: str
    :param auto_apply: When ``True``, Auto Apply will immediately
        provision an appliance when discovered with matching criteria.
        ``False`` will require manual approval of an appliance.
    :type auto_apply: bool
    :param serial_number: Serial number of the appliance to match
        against discovery criteria, defaults to ""
    :type serial_number: str, optional
    :param tag: Appliance tag for Orchestrator to match against
        discovered devices, defaults to ""
    :type tag: str, optional
    :param comment: Comment field / notes on preconfig, defaults to ""
    :type comment: str, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    yaml_byte = yaml_preconfig.encode("utf-8")
    yaml_b64 = base64.b64encode(yaml_byte)
    yaml_upload = str(yaml_b64)
    # take off the (b' ') portion
    yaml_upload = yaml_upload[2:-1]

    data = {
        "name": hostname,
        "serialNum": serial_number,
        "tag": tag,
        "comment": comment,
        "autoApply": auto_apply,
        "configData": yaml_upload,
    }

    return self._post(
        "/gms/appliance/preconfiguration", data=data, return_type="bool"
    )


def modify_preconfig(
    self,
    hostname: str,
    yaml_preconfig: str,
    auto_apply: bool,
    preconfig_id: str,
    serial_number: str = "",
    tag: str = "",
    comment: str = "",
) -> bool:
    """Modify a YAML Preconfig on Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliancePreconfig
          - POST
          - /gms/appliance/preconfiguration/{preconfigId}

    :param hostname: Name of preconfig and tag to match, often the
        hostname of the intended device
    :type hostname: str
    :param yaml_preconfig: YAML text of preconfig configuration, this
        will get base64 converted in this function before upload.
    :type yaml_preconfig: str
    :param auto_apply: When ``True``, Auto Apply will immediately
        provision an appliance when discovered with matching criteria.
        ``False`` will require manual approval of an appliance.
    :type auto_apply: bool
    :param preconfig_id: ID of the preconfig to modify, e.g. ``15``
    :type preconfig_id: str
    :param serial_number: Serial number of the appliance to match
        against discovery criteria, defaults to ""
    :type serial_number: str, optional
    :param tag: Appliance tag for Orchestrator to match against
        discovered devices, defaults to ""
    :type tag: str, optional
    :param comment: Comment field / notes on preconfig, defaults to ""
    :type comment: str, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    yaml_byte = yaml_preconfig.encode("utf-8")
    yaml_b64 = base64.b64encode(yaml_byte)
    yaml_upload = str(yaml_b64)
    # take off the (b' ') portion
    yaml_upload = yaml_upload[2:-1]

    data = {
        "name": hostname,
        "serialNum": serial_number,
        "tag": tag,
        "comment": comment,
        "autoApply": auto_apply,
        "configData": yaml_upload,
    }

    return self._post(
        "/gms/appliance/preconfiguration/{}".format(preconfig_id),
        data=data,
        return_type="bool",
    )


def get_preconfig(
    self,
    preconfig_id: str,
) -> dict:
    """Get specific preconfig from Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliancePreconfig
          - GET
          - /gms/appliance/preconfiguration/{preconfigId}

    :param preconfig_id: ID of the preconfig to retrieve, e.g. ``15``
    :type preconfig_id: str
    :return: Returns dictionary with preconfig detail \n
        * keyword **id** (`int, optional`): Id of the preconfiguration,
          used to reference this preconfiguration in the other APIs
        * keyword **name** (`str, optional`): Name of preconfiguration
        * keyword **serialNum** (`str, optional`): Serial number to
          match on
        * keyword **tag** (`str, optional`): Tag to match on
        * keyword **comment** (`str, optional`): User provided comment
          for the preconfiguration
        * keyword **autoApply** (`bool, optional`): Automatically apply
          this preconfiguration to the matched appliance when
          Orchestrator discovers it
        * keyword **configData** (`str, optional`): Base64 encoded
          preconfiguration YAML string
        * keyword **createdtime** (`int, optional`): Time when
          preconfiguration was created in epoch milliseconds
        * keyword **modifiedtime** (`int, optional`): Time when
          preconfiguration was last modified in epoch milliseconds
        * keyword **nepk** (`str, optional`): Appliance ID that
          preconfig was last applied to
        * keyword **discoveredId** (`str, optional`): Discovered
          appliance ID that preconfig was last applied to (the id of
          appliances in the discovered tab are different than when the
          appliance is approved)
        * keyword **guid** (`str, optional`): ID of the log created in
          actionlog when the preconfiguration was applied
        * keyword **taskStatus** (`int, optional`): The current status
          of the preconfig apply. ``0``: Not Started, ``1``: In
          Progress, and ``2``: Finished
        * keyword **completionStatus** (`bool, optional`): Whether the
          apply was successful or not, only look at this if
          taskStatus == ``2``
        * keyword **starttime** (`int, optional`): Start time of last
          apply in epoch milliseconds
        * keyword **endtime** (`int, optional`): End time of last apply
          in unix epoch milliseconds
        * keyword **result** (`list[dict], optional`) \n
            [`dict`]: results object \n
                * keyword **taskStatus** (`int, optional`): The current
                  status of the preconfig apply. ``0``: Not Started,
                  ``1``: In Progress, and ``2``: Finished
                * keyword **completionStatus** (`bool, optional`):
                  Whether the apply was successful or not, only look at
                  this if taskStatus == ``2``
                * keyword **name** (`str, optional`): Name of the task
                * keyword **result** (`str, optional`): Status/result
                  string information of the task
                * keyword **nePk** (`str, optional`): Appliance ID task
                  is applying to
                * keyword **data** (`str, optional`): String or JSON for
                  the data that was used by this task
    :rtype: dict
    """
    return self._get("/gms/appliance/preconfiguration/{}".format(preconfig_id))


def delete_preconfig(
    self,
    preconfig_id: str,
) -> bool:
    """Delete a preconfig from Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliancePreconfig
          - DELETE
          - /gms/appliance/preconfiguration/{preconfigId}

    :param preconfig_id: Numeric ID of preconfig to delete, e.g. ``15``
    :type preconfig_id: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        "/gms/appliance/preconfiguration/{}".format(preconfig_id),
        return_type="bool",
    )


def find_matching_preconfig(
    self,
    serial_number: str = "",
    tag: str = "",
) -> dict:
    """Find and return the first matching preconfig by serial number
    then tag. If both are blank ("") will return first preconfig.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliancePreconfig
          - POST
          - /gms/appliance/preconfiguration/findMatch

    :param serial_number: Serial number of the appliance to match
        against discovery criteria, defaults to ""
    :type serial_number: str, optional
    :param tag: Appliance tag for Orchestrator to match against
        discovered devices, defaults to ""
    :type tag: str, optional
    :return: Returns dictionary with preconfig detail \n
        * keyword **id** (`int, optional`): Id of the preconfiguration,
          used to reference this preconfiguration in the other APIs
        * keyword **name** (`str, optional`): Name of preconfiguration
        * keyword **serialNum** (`str, optional`): Serial number to
          match on
        * keyword **tag** (`str, optional`): Tag to match on
        * keyword **comment** (`str, optional`): User provided comment
          for the preconfiguration
        * keyword **autoApply** (`bool, optional`): Automatically apply
          this preconfiguration to the matched appliance when
          Orchestrator discovers it
        * keyword **configData** (`str, optional`): Base64 encoded
          preconfiguration YAML string
        * keyword **createdtime** (`int, optional`): Time when
          preconfiguration was created in epoch milliseconds
        * keyword **modifiedtime** (`int, optional`): Time when
          preconfiguration was last modified in epoch milliseconds
        * keyword **nepk** (`str, optional`): Appliance ID that
          preconfig was last applied to
        * keyword **discoveredId** (`str, optional`): Discovered
          appliance ID that preconfig was last applied to (the id of
          appliances in the discovered tab are different than when the
          appliance is approved)
        * keyword **guid** (`str, optional`): ID of the log created in
          actionlog when the preconfiguration was applied
        * keyword **taskStatus** (`int, optional`): The current status
          of the preconfig apply. ``0``: Not Started, ``1``: In
          Progress, and ``2``: Finished
        * keyword **completionStatus** (`bool, optional`): Whether the
          apply was successful or not, only look at this if
          taskStatus == ``2``
        * keyword **starttime** (`int, optional`): Start time of last
          apply in epoch milliseconds
        * keyword **endtime** (`int, optional`): End time of last apply
          in unix epoch milliseconds
        * keyword **result** (`list[dict], optional`) \n
            [`dict`]: results object \n
                * keyword **taskStatus** (`int, optional`): The current
                  status of the preconfig apply. ``0``: Not Started,
                  ``1``: In Progress, and ``2``: Finished
                * keyword **completionStatus** (`bool, optional`):
                  Whether the apply was successful or not, only look at
                  this if taskStatus == ``2``
                * keyword **name** (`str, optional`): Name of the task
                * keyword **result** (`str, optional`): Status/result
                  string information of the task
                * keyword **nePk** (`str, optional`): Appliance ID task
                  is applying to
                * keyword **data** (`str, optional`): String or JSON for
                  the data that was used by this task
    :rtype: dict
    """
    data = {
        "serial": serial_number,
        "tag": tag,
    }

    return self._post("/gms/appliance/preconfiguration/findMatch", data=data)


def get_default_preconfig(
    self,
) -> dict:
    """Get the default preconfiguration, this contains the template YAML
    which has all possible configuration items. You will have to base64
    decode configData to see the YAML in plain text.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliancePreconfig
          - GET
          - /gms/appliance/preconfiguration/default

    :return: Returns dictionary with preconfig detail \n
        * keyword **id** (`int, optional`): Id of the preconfiguration,
          used to reference this preconfiguration in the other APIs
        * keyword **name** (`str, optional`): Name of preconfiguration
        * keyword **serialNum** (`str, optional`): Serial number to
          match on
        * keyword **tag** (`str, optional`): Tag to match on
        * keyword **comment** (`str, optional`): User provided comment
          for the preconfiguration
        * keyword **autoApply** (`bool, optional`): Automatically apply
          this preconfiguration to the matched appliance when
          Orchestrator discovers it
        * keyword **configData** (`str, optional`): Base64 encoded
          preconfiguration YAML string
        * keyword **createdtime** (`int, optional`): Time when
          preconfiguration was created in epoch milliseconds
        * keyword **modifiedtime** (`int, optional`): Time when
          preconfiguration was last modified in epoch milliseconds
        * keyword **nepk** (`str, optional`): Appliance ID that
          preconfig was last applied to
        * keyword **discoveredId** (`str, optional`): Discovered
          appliance ID that preconfig was last applied to (the id of
          appliances in the discovered tab are different than when the
          appliance is approved)
        * keyword **guid** (`str, optional`): ID of the log created in
          actionlog when the preconfiguration was applied
        * keyword **taskStatus** (`int, optional`): The current status
          of the preconfig apply. ``0``: Not Started, ``1``: In
          Progress, and ``2``: Finished
        * keyword **completionStatus** (`bool, optional`): Whether the
          apply was successful or not, only look at this if
          taskStatus == ``2``
        * keyword **starttime** (`int, optional`): Start time of last
          apply in epoch milliseconds
        * keyword **endtime** (`int, optional`): End time of last apply
          in unix epoch milliseconds
        * keyword **result** (`list[dict], optional`) \n
            [`dict`]: results object \n
                * keyword **taskStatus** (`int, optional`): The current
                  status of the preconfig apply. ``0``: Not Started,
                  ``1``: In Progress, and ``2``: Finished
                * keyword **completionStatus** (`bool, optional`):
                  Whether the apply was successful or not, only look at
                  this if taskStatus == ``2``
                * keyword **name** (`str, optional`): Name of the task
                * keyword **result** (`str, optional`): Status/result
                  string information of the task
                * keyword **nePk** (`str, optional`): Appliance ID task
                  is applying to
                * keyword **data** (`str, optional`): String or JSON for
                  the data that was used by this task
    :rtype: dict
    """
    return self._get("/gms/appliance/preconfiguration/default")


def validate_preconfig(
    self,
    hostname: str,
    yaml_preconfig: str,
    auto_apply: bool,
    serial_number: str = "",
    tag: str = "",
    comment: str = "",
):
    """Runs validation on a preconfig on Orchestrator to identify errors
    within the configuration

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliancePreconfig
          - POST
          - /gms/appliance/preconfiguration/validate

    :param hostname: Name of preconfig and tag to match, often the
        hostname of the intended device
    :type hostname: str
    :param yaml_preconfig: YAML text of preconfig configuration, this
        will get base64 converted in this function before upload.
    :type yaml_preconfig: str
    :param auto_apply: When ``True``, Auto Apply will immediately
        provision an appliance when discovered with matching criteria.
        ``False`` will require manual approval of an appliance.
    :type auto_apply: bool
    :param serial_number: Serial number of the appliance to match
        against discovery criteria, defaults to ""
    :type serial_number: str, optional
    :param tag: Appliance tag for Orchestrator to match against
        discovered devices, defaults to ""
    :type tag: str, optional
    :param comment: Comment field / notes on preconfig, defaults to ""
    :type comment: str, optional
    :return: Returns full requests response from Orchestrator
    :rtype: `requests.Response` object
    """
    yaml_byte = yaml_preconfig.encode("utf-8")
    yaml_b64 = base64.b64encode(yaml_byte)
    yaml_upload = str(yaml_b64)
    # take off the (b' ') portion
    yaml_upload = yaml_upload[2:-1]

    data = {
        "name": hostname,
        "serialNum": serial_number,
        "tag": tag,
        "comment": comment,
        "autoApply": auto_apply,
        "configData": yaml_upload,
    }

    return self._post(
        "/gms/appliance/preconfiguration/validate",
        data=data,
        return_type="full_response",
    )


def approve_and_apply_preconfig(
    self,
    preconfig_id: str,
    discovered_id: str,
) -> bool:
    """Approve an appliance and apply a preconfig to it

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliancePreconfig
          - POST
          - /gms/appliance/preconfiguration/{preconfigId}/apply/discovered/{discoveredId}

    :param preconfig_id: Numeric ID of preconfig to apply, e.g. ``15``
    :type preconfig_id: str
    :param discovered_id: Numeric ID of discovered appliance,
        e.g. ``10``
    :type discovered_id: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """  # noqa E501
    return self._post(
        "/gms/appliance/preconfiguration/{}/apply/discovered/{}".format(
            preconfig_id, discovered_id
        ),
        return_type="bool",
    )


def apply_preconfig_to_existing(
    self,
    preconfig_id: str,
    ne_pk: str,
) -> bool:
    """Apply preconfig to existing approved appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliancePreconfig
          - POST
          - /gms/appliance/preconfiguration/{preconfigId}/apply/{nePk}

    :param preconfig_id: Numeric ID of preconfig to apply, e.g. ``15``
    :type preconfig_id: str
    :param ne_pk: Network Primary Key (nePk) of existing appliance,
        e.g. ``3.NE``
    :type ne_pk: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/gms/appliance/preconfiguration/{}/apply/{}".format(
            preconfig_id, ne_pk
        ),
        return_type="bool",
    )


def get_apply_preconfig_status(
    self,
    preconfig_id: str,
) -> dict:
    """Get the apply status of a preconfig

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appliancePreconfig
          - GET
          - /gms/appliance/preconfiguration/{preconfigId}/apply

    :param preconfig_id: Numeric ID of preconfig to check, e.g. ``15``
    :type preconfig_id: str
    :return: Returns dictionary with preconfig status detail \n
        * keyword **id** (`int, optional`): Id of the preconfiguration,
          used to reference this preconfiguration in the other APIs
        * keyword **guid** (`str, optional`): ID of the log created in
          actionlog when the preconfiguration was applied
        * keyword **taskStatus** (`int, optional`): The current status
          of the preconfig apply. ``0``: Not Started, ``1``: In
          Progress, and ``2``: Finished
        * keyword **completionStatus** (`bool, optional`): Whether the
          apply was successful or not, only look at this if
          taskStatus == ``2``
        * keyword **starttime** (`int, optional`): Start time of last
          apply in epoch milliseconds
        * keyword **endtime** (`int, optional`): End time of last apply
          in unix epoch milliseconds
        * keyword **result** (`list[dict], optional`) \n
            [`dict`]: results object \n
                * keyword **taskStatus** (`int, optional`): The current
                  status of the preconfig apply. ``0``: Not Started,
                  ``1``: In Progress, and ``2``: Finished
                * keyword **completionStatus** (`bool, optional`):
                  Whether the apply was successful or not, only look at
                  this if taskStatus == ``2``
                * keyword **name** (`str, optional`): Name of the task
                * keyword **result** (`str, optional`): Status/result
                  string information of the task
                * keyword **nePk** (`str, optional`): Appliance ID task
                  is applying to
                * keyword **data** (`str, optional`): String or JSON for
                  the data that was used by this task
    :rtype: dict
    """
    return self._get(
        "/gms/appliance/preconfiguration/{}/apply".format(preconfig_id)
    )
