# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# apiKey : API keys


def get_api_keys(
    self,
) -> dict:
    """Retrieves all configured API keys as JSON

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - apiKey
          - GET
          - /apiKey

    :return: Dictionary of configured API keys from Orchestrator
    :rtype: dict
    """
    return self._get("/apiKey")


def add_api_key(
    self,
    name: str,
    permission: str,
    expiration: int,
    active: bool,
    key: str = None,
    description: str = None,
    ip_list: str = None,
) -> bool:
    """Operation to add a new API key to Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - apiKey
          - POST
          - /apiKey

    :param name: API Key Name
    :type name: str
    :param permission: API Key privileges. Allowed values are
        'net_read_write' for RW and 'net_read" for RO
    :type permission: str
    :param expiration: API Key expiration in UNIX timestamp. Key will
        automatically become inactive on expiration date.
    :type expiration: int
    :param active: API Key state is active (True) or inactive (False).
        Inactive keys cannot be used to make requests.
    :type active: bool
    :param key: API Key value, defaults to None
    :type key: str, optional
    :param description: API Key description, defaults to None
    :type description: str, optional
    :param ip_list: List of allowed IP's to make requests with this API
        Key. Leave blank to allow all IP's.
    :type ip_list: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """

    permission_valid = {"net_read_write", "net_read"}
    if permission not in permission_valid:
        raise ValueError(
            "results: permission must be one of %r." % permission_valid
        )

    api_key_entry = {
        "name": name,
        "permission": permission,
        "expiration": expiration,
        "active": active,
    }

    if key is not None:
        api_key_entry["key"] = key
    if description is not None:
        api_key_entry["description"] = description
    if ip_list is not None:
        api_key_entry["ip_list"] = ip_list

    return self._post(
        "/apiKey",
        data=api_key_entry,
        expected_status=[204],
        return_type="bool",
    )


def get_api_key(
    self,
    name: str,
) -> dict:
    """Retrieves API key by name

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - apiKey
          - GET
          - /apiKey/{name}

    :param name: API Key Name to retrieve
    :type name: str
    :return: Dictionary of API key
    :rtype: dict
    """
    return self._get("/apiKey/{}".format(name))


def update_api_key(
    self,
    name: str,
    permission: str,
    expiration: int,
    active: bool,
    key: str = None,
    description: str = None,
    ip_list: str = None,
) -> bool:
    """Update existing API key on Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - apiKey
          - PUT
          - /apiKey/{name}

    :param name: API Key Name
    :type name: str
    :param permission: API Key privileges. Allowed values are
        'net_read_write' for RW and 'net_read" for RO
    :type permission: str
    :param expiration: API Key expiration in UNIX timestamp. Key will
        automatically become inactive on expiration date.
    :type expiration: int
    :param active: API Key state is active (True) or inactive (False).
        Inactive keys cannot be used to make requests.
    :type active: bool
    :param key: API Key value, defaults to None
    :type key: str, optional
    :param description: API Key description, defaults to None
    :type description: str, optional
    :param ip_list: List of allowed IP's to make requests with this API
        Key. Leave blank to allow all IP's. OptionalAPI Key state is
        active (True) or inactive (False). Inactive keys cannot be used
        to make requests, defaults to None
    :type ip_list: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """

    api_key_entry = {
        "name": name,
        "permission": permission,
        "expiration": expiration,
        "active": active,
    }

    if key is not None:
        api_key_entry["key"] = key
    if description is not None:
        api_key_entry["description"] = description
    if ip_list is not None:
        api_key_entry["ip_list"] = ip_list

    return self._put(
        "/apiKey/{}".format(name),
        data=api_key_entry,
        expected_status=[204],
        return_type="bool",
    )


def delete_api_key(
    self,
    name: str,
) -> bool:
    """Deletes API key by name

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - apiKey
          - DELETE
          - /apiKey/{name}

    :param name: API Key Name to delete
    :type name: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        "/apiKey/{}".format(name), expected_status=[204], return_type="bool"
    )
