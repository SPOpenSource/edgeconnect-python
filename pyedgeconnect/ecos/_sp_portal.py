# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# spPortal : Silver Peak Portal


def register_sp_portal_status(self) -> dict:
    """Retrieve registration status of Edge Connect with Cloud Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - GET
          - /spPortal/register

    :return: Returns dictionary of registration status for appliance \n
        * keyword **account** (`str, optional`): Account associated to
        * keyword **group** (`str, optional`): Group associated to, if
          applicable
        * keyword **site** (`str, optional`): Site/Tag associated to, if
          applicable
        * keyword **accountKey** (`str, optional`): Account key
        * keyword **registered** (`bool, optional`): If currently
          registered
        * keyword **enabled** (`bool, optional`): ``True`` if enabled
        * keyword **emails** (`list[str]`): configured contact emails
    :rtype: dict
    """
    return self._get("/spPortal/register")


def register_sp_portal(
    self,
    account_key: str,
    account: str,
    group: str = "",
    site: str = "",
) -> bool:
    """Register appliance with account

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - spPortal
          - POST
          - /spPortal/register

    :param account_key: Account key for the account to associate to
    :type account_key: str
    :param account: Account to associate appliance to
    :type account: str
    :param group: Group to associate appliance to, defaults to ""
    :type group: str, optional
    :param site: Site or Tag to associate with appliance, defaults to ""
    :type site: str, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/spPortal/register",
        data={
            "accountKey": account_key,
            "account": account,
            "group": group,
            "site": site,
        },
        return_type="bool",
    )
