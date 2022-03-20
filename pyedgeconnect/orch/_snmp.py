# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# snmp : ECOS SNMP configuration


def get_appliance_snmp(
    self,
    ne_pk: str,
    cached: bool,
) -> dict:
    """Get SNMP configuration from Edge Connect appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - snmp
          - GET
          - /snmp/{nePk}?cached={cached}

    :param ne_pk: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_pk: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary of appliance SNMP configuration \n
        * keyword **access** (`dict`): Access strings \n
            * keyword **rocommunity** (`str`): SNMP read-only
              community string
        * keyword **listen** (`dict`): Listen state \n
            * keyword **enable** (`bool`): ``True`` if SNMP agent
              listening at SNMP port (161)
        * keyword **sysdescr** (`str`): SNMP MIB II object 'sysDescr'
          value
        * keyword **syscontact** (`str`): SNMP MIB II object
          'sysContact' value
        * keyword **syslocation** (`str`): SNMP MIB II object
          'sysLocation' value
        * keyword **v3** (`dict`): SNMP v3 user information \n
            * keyword **users** (`dict`): Users object \n
                * keyword **admin** (`dict`): Admin object \n
                    * keyword **self** (`str`): admin user, only admin
                      user is available as an SNMP v3 user
                    * keyword **enable** (`bool`): Is admin user enabled
                      as SNMP v3 user
                    * keyword **hash_type** (`str`): Hashing algorithm
                      used for encrypting authentication password
                    * keyword **auth_key** (`str`): Hashed
                      authentication password
                    * keyword **privacy_type** (`str`): Hashing
                      algorithm used for encrypting privacy password
                    * keyword **privacy_key** (`str`): Hashed privacy
                      password
        * keyword **traps** (`dict`): SNMP Trap enable state and access
          information \n
            * keyword **enable** (`bool`): ``True`` if SNMP trap event
              enabled
            * keyword **trap_community** (`str`): Community string for
              SNMP trap event
        * keyword **auto_launch** (`bool`): ``True`` if SNMP Agent
          enabled at system start up
    :rtype: dict
    """
    return self._get("/snmp/{}?cached={}".format(ne_pk, cached))
