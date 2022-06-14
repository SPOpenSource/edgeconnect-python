# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# ipObjects : IP address groups and service groups management
from __future__ import annotations


def get_all_address_groups(self) -> list:
    """Use this API to get all ACL address group objects

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - ipObjects
          - GET
          - /ipObjects/addressGroup

    :return: Returns list of dictionaries for all ACL address group
        objects \n
        * [`dict`]: Address group object \n
            * keyword **type** (`str`): Type of ACL group object, should
              be set as ``AG``
            * keyword **name** (`str`): ACL group name
            * keyword **rules** (`list[dict]`): Array of rules objects\n
                * keyword **includedIPs** (`list[str]`): List of IP
                  addresses to include in address group,
                  e.g. ``["10.1.1.0/24","10.2.1.0/24"]``
                * keyword **excludedIPs** (`list[str]`): List of IP
                  addresses to exclude in address group,
                  e.g. ``["10.3.1.0/24","10.4.1.0/24"]``
                * keyword **includedGroups** (`list[str]`): List of
                  Address groups to nest/include in this group,
                  e.g. ``["AddrGroup1","AddrGroup2"]``
                * keyword **comment** (`str`): User comment for group
    :rtype: list
    """

    return self._get("/ipObjects/addressGroup")


def create_address_group(
    self,
    ag_name: str,
    included_ips: list[str] = [],
    excluded_ips: list[str] = [],
    included_groups: list[str] = [],
    comment: str = "",
) -> bool:
    """Create/Replace an ACL address group object. Every address group
    must contain at least one include list or include group, otherwise
    will return a HTTP 400 error.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - ipObjects
          - POST
          - /ipObjects/addressGroup

    :param ag_name: ACL Group name
    :type ag_name: str
    :param included_ips: List of IP addresses/subnets to include,
        defaults to ``[]``
    :type included_ips: list[str], optional
    :param excluded_ips: List of IP addresses/subnets to exclude,
        defaults to ``[]``
    :type excluded_ips: list[str], optional
    :param included_groups: List of Address Groups to include,
        defaults to ``[]``
    :type included_groups: list[str], optional
    :param comment: Comment for address group,
        defaults to ``""``
    :type comment: str, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "type": "AG",
        "name": ag_name,
        "rules": [
            {
                "includedIPs": included_ips,
                "excludedIPs": excluded_ips,
                "includedGroups": included_groups,
                "comment": comment,
            }
        ],
    }

    return self._post(
        "/ipObjects/addressGroup",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def update_address_group(
    self,
    ag_name: str,
    included_ips: list[str] = [],
    excluded_ips: list[str] = [],
    included_groups: list[str] = [],
    comment: str = "",
) -> bool:
    """Replace an ACL address group object. Group must already exist,
    and the included_ips, excluded_ips, included_groups must include
    previous values and can be appended with additional values.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - ipObjects
          - PUT
          - /ipObjects/addressGroup

    :param ag_name: ACL Group name
    :type ag_name: str
    :param included_ips: List of IP addresses/subnets to include,
        defaults to ``[]``
    :type included_ips: list[str], optional
    :param excluded_ips: List of IP addresses/subnets to exclude,
        defaults to ``[]``
    :type excluded_ips: list[str], optional
    :param included_groups: List of Address Groups to include,
        defaults to ``[]``
    :type included_groups: list[str], optional
    :param comment: Comment for address group,
        defaults to ``""``
    :type comment: str, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "type": "AG",
        "name": ag_name,
        "rules": [
            {
                "includedIPs": included_ips,
                "excludedIPs": excluded_ips,
                "includedGroups": included_groups,
                "comment": comment,
            }
        ],
    }

    return self._put(
        "/ipObjects/addressGroup",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def get_address_group(
    self,
    ag_name: str,
) -> dict:
    """Return specific address group object

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - ipObjects
          - GET
          - /ipObjects/addressGroup/{name}

    :param ag_name: ACL Group name
    :type ag_name: str
    :return: Returns dictionary address group object \n
        * keyword **type** (`str`): Type of ACL group object, should
            be ``AG``
        * keyword **name** (`str`): ACL group name
        * keyword **rules** (`list[dict]`): Array of rules objects \n
            * keyword **includedIPs** (`list[str]`): List of IP
                addresses to include in address group,
                e.g. ``["10.1.1.0/24","10.2.1.0/24"]``
            * keyword **excludedIPs** (`list[str]`): List of IP
                addresses to exclude in address group,
                e.g. ``["10.3.1.0/24","10.4.1.0/24"]``
            * keyword **includedGroups** (`list[str]`): List of
                Address groups to nest/include in this group,
                e.g. ``["AddrGroup1","AddrGroup2"]``
            * keyword **comment** (`str`): User comment for group
    :rtype: dict
    """
    return self._get("/ipObjects/addressGroup/{}".format(ag_name))


def delete_address_group(
    self,
    ag_name: str,
) -> bool:
    """Delete specific address group object

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - ipObjects
          - DELETE
          - /ipObjects/addressGroup/{name}

    :param ag_name: ACL Group name
    :type ag_name: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """

    return self._delete(
        "/ipObjects/addressGroup/{}".format(ag_name),
        expected_status=[204],
        return_type="bool",
    )


def bulk_upload_address_group(
    self,
    csv_filename: str,
) -> dict:
    """Upload CSV file for bulk address group creation. The API returns
    the status and list of groups that got imported.

    .. warning::

        This function in pyedgeconnect is currently returning a 500
        error with the file upload, despite working in the UI.
        Will be fixed in future update.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - ipObjects
          - POST
          - /ipObjects/addressGroup/bulkUpload

    :param csv_filename: Filename of CSV file to upload
    :type csv_filename: str
    :return: Returns status and data within dictionary object\n
        * keyword **success** (`bool`): ``True`` for success, ``False``
          when error encountered
        * keyword **error** (`str`): Error message, if applicable
        * keyword **groups** (`list[str]`):
        * keyword **existingGroupNames** (`list[str]`):
    :rtype: dict
    """
    # TODO - validate function, currently testing broken in SEWAN in
    # trying to upload file even in UI, need to test further before
    # completing code
    with open(csv_filename, "rb") as upload_data:
        return self._post(
            "/ipObjects/addressGroup/bulkUpload",
            files={"data": (csv_filename, upload_data, "text/xml")},
            expected_status=[204],
            return_type="bool",
        )


def merge_address_groups(
    self,
) -> dict:
    """Trigger an immediate merge of all address groups in the DB

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - ipObjects
          - POST
          - /ipObjects/addressGroup/merge

    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/ipObjects/addressGroup/merge",
        expected_status=[204],
        return_type="bool",
    )


def get_all_service_groups(self) -> list:
    """Use this API to get all ACL service group objects

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - ipObjects
          - GET
          - /ipObjects/serviceGroup

    :return: Returns list of dictionaries for all ACL service group
        objects \n
        * [`dict`]: Service group object \n
            * keyword **type** (`str`): Type of ACL group object, should
              be set as ``SG``
            * keyword **name** (`str`): ACL group name
            * keyword **rules** (`list[dict]`): Array of rules objects\n
                * keyword **protocol** (`str`): Protocol type specified,
                  e.g. ``UDP``, ``TCP``, or ``ICMP``.
                * keyword **icmpTypes** (`list[str]`): List of included
                  icmp types, e.g. ``["0","8"]``
                * keyword **includedPorts** (`list[str]`): List of
                  included ports, ranges of ports,
                  e.g. ``["443","8000-8002"]``, will be ignored if
                  ``protocol`` is set to ``ICMP``.
                * keyword **excludedPorts** (`list[str]`): List of
                  excluded ports, ranges of ports,
                  e.g. ``["443","8000-8002"]``, will be ignored if
                  ``protocol`` is set to ``ICMP``.
                * keyword **includedGroups** (`list[str]`): List of
                  service groups to nest/include in this group,
                  e.g. ``["ServiceGroup1","ServiceGroup2"]``, will be
                  ignored if ``protocol`` is set to ``ICMP``.
                * keyword **excludedGroups** (`list[str]`): List of
                  service groups to nest/include in this group,
                  e.g. ``["ServiceGroup1","ServiceGroup2"]``, will be
                  ignored if ``protocol`` is set to ``ICMP``.
                * keyword **comment** (`str`): User comment for group
    :rtype: list
    """

    return self._get("/ipObjects/addressGroup")


def create_service_group(
    self,
    sg_name: str,
    protocol: str,
    icmp_types: list[str] = [],
    included_ports: list[str] = [],
    excluded_ports: list[str] = [],
    included_groups: list[str] = [],
    excluded_groups: list[str] = [],
    comment: str = "",
) -> bool:
    """Create/Replace an ACL service group object. Every service group
    must contain at least one include list or include group, otherwise
    will return a HTTP 400 error.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - ipObjects
          - POST
          - /ipObjects/serviceGroup

    :param sg_name: ACL Group name
    :type sg_name: str
    :param protocol:
    :type protocol: str
    :param icmp_types: List of icmp types to include if ``protocol`` set
        to ``ICMP``, defaults to ``[]``
    :type icmp_types: list[str], optional
    :param included_ports: List of ports or port ranges to include, will
        be ignored if ``protocol`` is set to ``ICMP``,
        defaults to ``[]``
    :type included_ports: list[str], optional
    :param excluded_ports: List of ports or port ranges to exclude, will
        be ignored if ``protocol`` is set to ``ICMP``,
        defaults to ``[]``
    :type excluded_ports: list[str], optional
    :param included_groups: List of Service Groups to include, will
        be ignored if ``protocol`` is set to ``ICMP``,
        defaults to ``[]``
    :type included_groups: list[str], optional
    :param excluded_groups: List of Service Groups to exclude, will
        be ignored if ``protocol`` is set to ``ICMP``,
        defaults to ``[]``
    :type excluded_groups: list[str], optional
    :param comment: Comment for address group,
        defaults to ``""``
    :type comment: str, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "type": "SG",
        "name": sg_name,
        "rules": [
            {
                "protocol": protocol,
                "icmpTypes": icmp_types,
                "includedPorts": included_ports,
                "excludedPorts": excluded_ports,
                "includedGroups": included_groups,
                "excludedGroups": excluded_groups,
                "comment": comment,
            }
        ],
    }

    return self._post(
        "/ipObjects/serviceGroup",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def update_service_group(
    self,
    sg_name: str,
    protocol: str,
    icmp_types: list[str] = [],
    included_ports: list[str] = [],
    excluded_ports: list[str] = [],
    included_groups: list[str] = [],
    excluded_groups: list[str] = [],
    comment: str = "",
) -> bool:
    """Replace an ACL service group object. Group must already exist,
    and all existing data for paramters of protocol, icmp_types,
    included_ports, excluded_ports, included_groups, excluded_groups,
    must be included and appended with new additional values.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - ipObjects
          - PUT
          - /ipObjects/addressGroup

    :param sg_name: ACL Group name
    :type sg_name: str
    :param protocol:
    :type protocol: str
    :param icmp_types: List of icmp types to include if ``protocol`` set
        to ``ICMP``, defaults to ``[]``
    :type icmp_types: list[str], optional
    :param included_ports: List of ports or port ranges to include, will
        be ignored if ``protocol`` is set to ``ICMP``,
        defaults to ``[]``
    :type included_ports: list[str], optional
    :param excluded_ports: List of ports or port ranges to exclude, will
        be ignored if ``protocol`` is set to ``ICMP``,
        defaults to ``[]``
    :type excluded_ports: list[str], optional
    :param included_groups: List of Service Groups to include, will
        be ignored if ``protocol`` is set to ``ICMP``,
        defaults to ``[]``
    :type included_groups: list[str], optional
    :param excluded_groups: List of Service Groups to exclude, will
        be ignored if ``protocol`` is set to ``ICMP``,
        defaults to ``[]``
    :type excluded_groups: list[str], optional
    :param comment: Comment for address group,
        defaults to ``""``
    :type comment: str, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "type": "SG",
        "name": sg_name,
        "rules": [
            {
                "protocol": protocol,
                "icmpTypes": icmp_types,
                "includedPorts": included_ports,
                "excludedPorts": excluded_ports,
                "includedGroups": included_groups,
                "excludedGroups": excluded_groups,
                "comment": comment,
            }
        ],
    }

    return self._put(
        "/ipObjects/serviceGroup",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def get_service_group(
    self,
    sg_name: str,
) -> dict:
    """Return specific service group object

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - ipObjects
          - GET
          - /ipObjects/serviceGroup/{name}

    :param ag_name: ACL Group name
    :type ag_name: str
        :return: Returns dictionary address group object \n
    :return: Returns dictionary service group object \n
        * keyword **type** (`str`): Type of ACL group object, should
            be set as ``SG``
        * keyword **name** (`str`): ACL group name
        * keyword **rules** (`list[dict]`): Array of rules objects \n
            * keyword **protocol** (`str`): Protocol type specified,
              e.g. ``UDP``, ``TCP``, or ``ICMP``.
            * keyword **icmpTypes** (`list[str]`): List of included
              icmp types, e.g. ``["0","8"]``
            * keyword **includedPorts** (`list[str]`): List of
              included ports, ranges of ports,
              e.g. ``["443","8000-8002"]``, will be ignored if
              ``protocol`` is set to ``ICMP``.
            * keyword **excludedPorts** (`list[str]`): List of
              excluded ports, ranges of ports,
              e.g. ``["443","8000-8002"]``, will be ignored if
              ``protocol`` is set to ``ICMP``.
            * keyword **includedGroups** (`list[str]`): List of
              service groups to nest/include in this group,
              e.g. ``["ServiceGroup1","ServiceGroup2"]``, will be
              ignored if ``protocol`` is set to ``ICMP``.
            * keyword **excludedGroups** (`list[str]`): List of
              service groups to nest/include in this group,
              e.g. ``["ServiceGroup1","ServiceGroup2"]``, will be
              ignored if ``protocol`` is set to ``ICMP``.
            * keyword **comment** (`str`): User comment for group
    :rtype: dict
    """
    return self._get("/ipObjects/serviceGroup/{}".format(sg_name))


def delete_service_group(
    self,
    sg_name: str,
) -> bool:
    """Delete specific service group object

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - ipObjects
          - DELETE
          - /ipObjects/serviceGroup/{name}

    :param ag_name: ACL Group name
    :type ag_name: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """

    return self._delete(
        "/ipObjects/addressGroup/{}".format(sg_name),
        expected_status=[204],
        return_type="bool",
    )


def bulk_upload_service_group(
    self,
    csv_filename: str,
) -> dict:
    """Upload CSV file for bulk service group creation. The API returns
    the status and list of groups that got imported.

    .. warning::

        This function in pyedgeconnect is currently returning a 500
        error with the file upload, despite working in the UI.
        Will be fixed in future update.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - ipObjects
          - POST
          - /ipObjects/serviceGroup/bulkUpload

    :param csv_filename: Filename of CSV file to upload
    :type csv_filename: str
    :return: Returns status and data within dictionary object\n
        * keyword **success** (`bool`): ``True`` for success, ``False``
          when error encountered
        * keyword **error** (`str`): Error message, if applicable
        * keyword **groups** (`list[str]`):
        * keyword **existingGroupNames** (`list[str]`):
    :rtype: dict
    """
    # TODO - validate function, currently testing broken in SEWAN in
    # trying to upload file even in UI, need to test further before
    # completing code
    with open(csv_filename, "rb") as upload_data:
        return self._post(
            "/ipObjects/serviceGroup/bulkUpload",
            files={"data": (csv_filename, upload_data, "text/xml")},
            expected_status=[204],
            return_type="bool",
        )


def merge_service_groups(
    self,
) -> dict:
    """Trigger an immediate merge of all service groups in the DB

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - ipObjects
          - POST
          - /ipObjects/serviceGroup/merge

    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/ipObjects/serviceGroup/merge",
        expected_status=[204],
        return_type="bool",
    )
