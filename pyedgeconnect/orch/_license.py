# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# license : License info about NX, VX, EC, and CPX appliances


def get_nx_licensed_appliances(self) -> list:
    """Returns list of NX licensed appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - license
          - GET
          - /license/nx

    :return: Returns list of NX licensed appliances in Orchestrator \n
        [`dict`]: licensed appliance object \n
            * keyword **hostname** (`str`): Hostname of appliance
            * keyword **model** (`str`): Model of appliance
            * keyword **serialNum** (`str`): Serial number of appliance
            * keyword **saasEnabled** (`bool`): Whether SaaS
              optimization is enabled on the appliance
            * keyword **applianceId** (`str`): Appliance ID
            * keyword **LicenseType** (`str`): Current license type
    :rtype: list
    """
    return self._get("/license/nx")


def get_vx_licensed_appliances(self) -> list:
    """Returns list of VX licensed appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - license
          - GET
          - /license/vx

    :return: Returns list of VX licensed appliances in Orchestrator \n
        [`dict`]: licensed appliance object \n
            * keyword **hostname** (`str`): Hostname of appliance
            * keyword **model** (`str`): Model of appliance
            * keyword **serialNum** (`str`): Serial number of appliance
            * keyword **saasEnabled** (`bool`): Whether SaaS
              optimization is enabled on the appliance
            * keyword **applianceId** (`str`): Appliance ID
            * keyword **LicenseType** (`str`): Current license type
            * keyword **licenseStartDate** (`int`): License start date
              in unix epoch
            * keyword **licenseExpirationDate** (`int`): License
              expiration date in unix epoch
    :rtype: list
    """
    return self._get("/license/vx")


def get_portal_licensed_summary(self) -> dict:
    """Retrieves summary of portal licensed appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - license
          - GET
          - /license/portal/summary

    :return: Returns summary of licensing information from Cloud Portal \n
        * keyword **licenses** (`dict`): Account info object \n
            * keyword **accountKey** (`dict`): Account key object \n
                * keyword **key** (`str`): Account key
            * keyword **fx** (`dict`): Standard EC license information \n
                * keyword **enable** (`bool`): If licenses are enabled
                * keyword **boost** (`int`): The amount of boost
                  licensed
                * keyword **mini** (`int`): Number of mini licenses
                * keyword **base** (`int`): Number of base licenses
                * keyword **plus** (`int`): Number of plus licenses
                * keyword **expire** (`int`): License expiration date in
                  unix epoch milliseconds
                * keyword **boostExpire** (`int`): Boost license
                  expiration date in unix epoch milliseconds
                * keyword **tier** (`dict`): Tiered license info \n
                    * keyword **1000000000** (`dict`): Unlimited licenses \n
                        * keyword **display** (`str`): Name of license
                        * keyword **count** (`int`): Number of licenses
                    * keyword **2000000** (`dict`): 2G licenses \n
                        * keyword **display** (`str`): Name of license
                        * keyword **count** (`int`): Number of licenses
                    * keyword **1000000** (`dict`): 1G licenses \n
                        * keyword **display** (`str`): Name of license
                        * keyword **count** (`int`): Number of licenses
                    * keyword **500000** (`dict`): 500M licenses \n
                        * keyword **display** (`str`): Name of license
                        * keyword **count** (`int`): Number of licenses
                    * keyword **200000** (`dict`): 200M licenses \n
                        * keyword **display** (`str`): Name of license
                        * keyword **count** (`int`): Number of licenses
                    * keyword **100000** (`dict`): 100M licenses \n
                        * keyword **display** (`str`): Name of license
                        * keyword **count** (`int`): Number of licenses
                    * keyword **50000** (`dict`): 50M licenses \n
                        * keyword **display** (`str`): Name of license
                        * keyword **count** (`int`): Number of licenses
                    * keyword **20000** (`dict`): 20M licenses \n
                        * keyword **display** (`str`): Name of license
                        * keyword **count** (`int`): Number of licenses
            * keyword **cpx** (`dict`): CPX license information \n
                * keyword **enable** (`bool`): If licenses are enabled
                * keyword **expire** (`int`): Expiration date in Unix
                  epoch
            * keyword **saas** (`dict`): SaaS Optimization license
              information \n
                * keyword **enable** (`bool`): If licenses are enabled
                * keyword **expire** (`int`): Expiration date in Unix
                  epoch
            * keyword **ecsp** (`dict`): Not documented \n
                * keyword **enable** (`bool`): If licenses are enabled
            * keyword **metered** (`dict`): Metered license information \n
                * keyword **enable** (`bool`): If licenses are enabled
                * keyword **expire** (`int`): Expiration date in Unix
                  epoch, ``null`` if not applicable
            * keyword **cloudOrch** (`dict`): Not documented \n
                * keyword **enable** (`bool`): If licenses are enabled,
                  ``null`` if not applicable
                * keyword **salesforceExpirationDate** (`int`):
                  Expiration date in Unix epoch, ``null`` if not
                  applicable
                * keyword **decommissionDate** (`int`): Expiration date
                  in Unix epoch, ``null`` if not applicable
        * keyword **licenseState** (`dict`): License state object \n
            * keyword **fx** (`dict`): Standard license state object \n
                * keyword **numMini** (`int`): Number of mini licenses
                * keyword **numBase** (`int`): Number of base licenses
                * keyword **numBoost** (`int`): Boost bandwidth
                * keyword **numPlus** (`int`): Number of plus licenses
                * keyword **numTier** (`dict`): Tiered licenses \n
                    * keyword **1000000000** (`int`): Unlimited licenses
                    * keyword **2000000** (`int`): 2G licenses
                    * keyword **1000000** (`int`): 1G licenses
                    * keyword **500000** (`int`): 500M licenses
                    * keyword **200000** (`int`): 200M licenses
                    * keyword **100000** (`int`): 100M licenses
                    * keyword **50000** (`int`): 50M licenses
                    * keyword **20000** (`int`): 20M licenses
    :rtype: dict
    """  # noqa: W505
    return self._get("/license/portal/summary")


def get_portal_licensed_appliances(self) -> dict:
    """Retrieves portal licensed appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - license
          - GET
          - /license/portal/appliance

    :return: Returns list of licensed appliances from Cloud Portal \n
        [`dict`]: Appliance license information object \n
            * keyword **applianceId** (`str`): Appliance id in the
              format of integer.NE e.g. ``3.NE``
            * keyword **id** (`str`): Not documented
            * keyword **enabled** (`bool`): If appliance active
            * keyword **hostname** (`str`): Hostname of appliance
            * keyword **isPortalLicensed** (`bool`): If appliance is
              licensed in Cloud Portal
            * keyword **licenses** (`dict`): License state object \n
                * keyword **fx** (`dict`): Standard license object \n
                    * keyword **base** (`dict`): Base license state \n
                        * keyword **enable** (`bool`): ``True`` if
                          active
                    * keyword **mini** (`dict`): Mini license state \n
                        * keyword **enable** (`bool`): ``True`` if
                          active
                    * keyword **plus** (`dict`): Plus license state \n
                        * keyword **enable** (`bool`): ``True`` if
                          active
                    * keyword **tier** (`dict`): Tier license state \n
                        * keyword **bandwidth** (`int`): Bandwidth
                          licensed
                        * keyword **display** (`str`): License display
                          name
                    * keyword **boost** (`dict`): Boost license state \n
                        * keyword **bandwidth** (`int`): Amount of boost
                          bandwidth in Mbps
                        * keyword **enable** (`bool`): ``True`` if
                          active
                * keyword **metered** (`dict`): Metered license object \n
                    * keyword **boost** (`dict`): Boost license state \n
                        * keyword **bandwidth** (`int`): Amount of boost
                          bandwidth in Mbps
                        * keyword **enable** (`bool`): ``True`` if
                          active
                * keyword **ecsp** (`dict`): Not documented \n
                    * keyword **licenseId** (`str`): Not documented \n
            * keyword **licenseRequest** (`dict`): License requested
              state object \n
                * keyword **fx** (`dict`): Standard license object \n
                    * keyword **base** (`dict`): Base license state \n
                        * keyword **enable** (`bool`): ``True`` if
                          active
                    * keyword **mini** (`dict`): Mini license state \n
                        * keyword **enable** (`bool`): ``True`` if
                          active
                    * keyword **plus** (`dict`): Plus license state \n
                        * keyword **enable** (`bool`): ``True`` if
                          active
                    * keyword **tier** (`dict`): Tier license state \n
                        * keyword **bandwidth** (`int`): Bandwidth
                          licensed
                        * keyword **display** (`str`): License display
                          name
                    * keyword **boost** (`dict`): Boost license state \n
                        * keyword **bandwidth** (`int`): Amount of boost
                          bandwidth in Mbps
                        * keyword **enable** (`bool`): ``True`` if active
                * keyword **metered** (`dict`): Metered license object \n
                    * keyword **boost** (`dict`): Boost license state \n
                        * keyword **bandwidth** (`int`): Amount of boost
                          bandwidth in Mbps
                        * keyword **enable** (`bool`): ``True`` if
                          active
            * keyword **model** (`str`): Hardware model, e.g. ``EC-M-B``
            * keyword **portalLicenseType** (`int`): Not documented
            * keyword **serial** (`str`): Appliance serial number
            * keyword **saasEnabled** (`bool`): ``True`` if SaaS
              Optimization is enabled
            * keyword **expirationDate** (`int`): License expiration in
              unix epoch
    :rtype: list
    """  # noqa: W505
    return self._get("/license/portal/appliance")


def change_appliance_license(
    self,
    ne_pk: str,
    boost: bool,
    boost_bw: int,
    tier_name: str = None,
    tier_bw: int = None,
    mini: bool = None,
    plus: bool = None,
    adv_sec_standard: bool = None,
    adv_sec_unlimited: bool = None,
) -> bool:
    """Changes ec appliance license settings

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - license
          - POST
          - /license/portal/ec/{nePk}

    :param ne_pk: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_pk: str
    :param boost: ``True`` to request to enable boost on appliance
    :type boost: bool
    :param boost_bw: Boost bandwidth to request, in Kbps
    :type boost_bw: int
    :param tier_bw: Tiered bandwidth to request, in Kbps. Accepted
        values are ``20000``, ``50000``, ``100000``, ``200000``,
        ``500000``, ``1000000``, ``2000000``, and for Unlimited use
        ``1000000000``, defaults to None
    :type tier_bw: int, optional
    :param tier_name: Display name of tiered license to request. Not
        required in presence of using tier_bw parameter. Defaults to
        None
    :type tier_name: str, optional
    :param mini: Apply legacy Mini license to appliance,
      defaults to None
    :type mini: bool, optional
    :param plus: Apply legacy Plus license to appliance,
      defaults to None
    :type plus: bool, optional
    :param adv_sec_standard: Apply Advanced Security Standard license
      to appliance, defaults to None
    :type adv_sec_standard: bool, optional
    :param adv_sec_unlimited: Apply Advanced Security Unlimited license
      to appliance, defaults to None
    :type adv_sec_unlimited: bool, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "license": {
            "mini": {},
            "plus": {},
            "tier": {},
            "boost": {"enable": boost, "bandwidth": boost_bw},
            "feature": {},
        }
    }

    if mini is not None:
        data["license"]["mini"]["enable"] = mini
    if plus is not None:
        data["license"]["plus"]["enable"] = plus
    if tier_name is not None:
        data["license"]["tier"]["display"] = tier_name
    if tier_bw is not None:
        data["license"]["tier"]["bandwidth"] = tier_bw
    if adv_sec_standard is not None:
        data["license"]["feature"]["adv_sec_standard"] = {
            "reqValue": 1,
            "display": "EC-AS",
        }
    if adv_sec_unlimited is not None:
        data["license"]["feature"]["adv_sec_unlimited"] = {
            "reqValue": 1,
            "display": "EC-AS-UL",
        }

    return self._post(
        "/license/portal/ec/{}".format(ne_pk),
        data=data,
        return_type="bool",
    )


def grant_appliance_base_license(
    self,
    ne_pk: str,
) -> bool:
    """Grant an appliance a base license via Cloud Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - license
          - POST
          - /license/portal/appliance/grant/{nePk}

    :param ne_pk: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_pk: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/license/portal/appliance/grant/{}".format(ne_pk),
        return_type="bool",
    )


def revoke_appliance_base_license(
    self,
    ne_pk: str,
) -> bool:
    """Revoke base license from appliance via Cloud Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - license
          - POST
          - /license/portal/appliance/revoke/{nePk}

    :param ne_pk: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_pk: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/license/portal/appliance/revoke/{}".format(ne_pk),
        return_type="bool",
    )


def delete_appliance_license_token(
    self,
    ne_pk: str,
) -> bool:
    """Delete an appliance's license token via the appliance. Used after
    revoking an appliance.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - license
          - DELETE
          - /license/portal/appliance/license/token/{nePk}

    .. warning::
        This will stop the appliance from passing traffic immediately!

    :param ne_pk: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_pk: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        "/license/portal/appliance/license/token/{}".format(ne_pk),
        return_type="bool",
    )
