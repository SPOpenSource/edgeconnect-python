# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# ikeless : UDP IPSec Key Status


def get_ipsec_udp_key_status(
    self,
) -> dict:
    """Get IPSEC UDP key status for all appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - ikeless
          - GET
          - /ikeless/seedStatus

    :return: Returns dictionary ikeless key status \n
        * keyword **<ne_pk>** (`dict`): Appliance key status object \n
            * keyword **hasActiveSeed** (`bool`): If appliance has the
              active key material
            * keyword **hasNewSeed** (`bool`): If appliance has the
              new key material
            * keyword **detail** (`str`): Detail of appliance seed
              status, including date stamp ID of active and new seed
    :rtype: dict
    """
    return self._get("/ikeless/seedStatus")


def get_ipsec_udp_key_history(
    self,
) -> dict:
    """Get IPSEC UDP key history

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - ikeless
          - GET
          - /ikeless/seedHistory

    :return: Returns dictionary ikeless key history status \n
        * keyword **activeSeedPersistSeed** (`bool`): Whether active key
          material persists on appliance
        * keyword **currentActivationTime** (`int`): Epoch time of the
          activation of current active key material
        * keyword **previousActiveSeedId** (`str`): ID of previous
          active key material
        * keyword **newSeedPersistSeed** (`bool`): Whether new key
          material persists on appliance
        * keyword **newSeedId** (`str`): ID of new key material
        * keyword **activeSeedId** (`str`): ID of current active key
          material
        * keyword **newSeedLifetime** (`int`): Epoch time of the
          lifetime of new key material
        * keyword **previousActivationTime** (`int`): Epoch time of the
          activation of previous active key material
        * keyword **activeSeedLifetime** (`int`): Epoch time of the
          lifetime of active key material
    :rtype: dict
    """
    return self._get("/ikeless/seedHistory")


def get_ipsec_udp_key_config(
    self,
) -> dict:
    """Get IPSEC UDP key material configuration, seed lifetime, max
    activation wait time, and whether to persist seed on appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - ikeless
          - GET
          - /ikeless/config

    :return: Returns dictionary ikeless key config \n
        * keyword **seedLifeTimeDuration** (`int`): Key material
          lifetime in seconds
        * keyword **maxActivationWaitTime** (`int`): Max key material
          activation wait time in seconds
        * keyword **persistSeed** (`bool`): Whether persist key material
          on appliance
        * keyword **scheduleConfig** (`dict`): Key rotation object \n
            * keyword **enabled** (`bool`): Enable or disable key
              rotation
            * keyword **schedule** (`dict`): rotation schedule detail
    :rtype: dict
    """
    return self._get("/ikeless/config")


def update_ipsec_udp_key_config(
    self,
    ikeless_config: dict,
) -> dict:
    """Update IPSEC UDP key material configuration, seed lifetime, max
    activation wait time, and whether to persist seed on appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - ikeless
          - POST
          - /ikeless/config

    Example ``schedule`` config within ``ikeless_config``:

    .. code::

        ikeless_config = {
            "seedLifeTimeDuration": 0,
            "maxActivationWaitTime": 0,
            "persistSeed": false,
            "scheduleConfig": {
                "enabled": false,
                "schedule": {
                    "effectiveTime": 1431323520,
                    "recurrence": {
                        "monthly": {
                            "type1" : {
                                "firstDayOfEveryMonth": true
                            },
                            "occursAt" : {
                                "hour": 12,
                                "minute": 0
                            }
                        }
                    },
                    "timezoneOffset": "-7:00"
                }
            }
        }

    :param ikeless_config: Ikeless config object \n
        * keyword **seedLifeTimeDuration** (`int`): Key material
          lifetime in seconds
        * keyword **maxActivationWaitTime** (`int`): Max key material
          activation wait time in seconds
        * keyword **persistSeed** (`bool`): Whether persist key material
          on appliance
        * keyword **scheduleConfig** (`dict`): Key rotation object \n
            * keyword **enabled** (`bool`): Enable or disable key
              rotation
            * keyword **schedule** (`dict`): rotation schedule detail.
              See examples above and more in Swagger.
    :type ikeless_config: dict
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/ikeless/config",
        data=ikeless_config,
        return_type="bool",
    )
