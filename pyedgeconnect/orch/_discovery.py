# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# discovery : Get and modify the discovery configuration
from __future__ import annotations


def get_appliance_discovery_emails(
    self,
) -> dict:
    """Get email addresses configured to be notified for discovery of
    new appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - discovery
          - GET
          - /gms/discovery

    :return: Returns dictionary of configured email addresses \n
        * keyword **emails** (`list[str]`): email addresses to notify on
          discovery of new appliance
    :rtype: dict
    """

    return self._get("/gms/discovery")


def set_appliance_discovery_emails(
    self,
    email_list: list[str],
) -> bool:
    """Update email addresses configured to be notified for discovery of
    new appliances.

    .. warning::
        Replaces the current configured list with the new list. To
        add an email, first retrieve the current emails and pass all
        desired emails in the new list.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - discovery
          - POST
          - /gms/discovery

    :param email_list: List of email addresses to be notified for
        appliance discovery
    :type email_list: list[str]
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "emails": email_list,
    }

    return self._post(
        "/gms/discovery",
        data=data,
        expected_status=[204],
        return_type="bool",
    )
