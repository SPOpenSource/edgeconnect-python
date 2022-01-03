# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# userAccount : ECOS users and login sessions


def get_appliance_user_accounts(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get all user details and sessions of appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - userAccount
          - GET
          - /userAccount/{neId}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary of configured users and sessions \n
        * keyword **users** (`dict`): Configured users objects \n
            * keyword **<username>** (`dict`): User object \n
                * keyword **self** (`str`): Username
                * keyword **enable** (`bool`): ``True`` if user is
                  enabled
                * keyword **gid** (`int`): Role ID of user, ``0`` for
                  admin, ``1001`` for monitor
                * keyword **password** (`str`): Returns blank string
                  for security purposes
                * keyword **pwtype** (`int`): NEEDS DESCRIPTION, e.g.
                  ``2``
        * keyword **sessions** (`dict`): Active sessions to appliance \n
            * keyword **<increments_from_1>** (`dict`): Session object\n
                * keyword **port** (`str`): Access method, e.g. ``web``
                * keyword **gid** (`int`): Role ID of user, ``0`` for
                  admin, ``1001`` for monitor
                * keyword **idle_time** (`str`): Idle time of user in
                  seconds, e.g. ``10``
                * keyword **login_time** (`str`): Login time of user in
                  Unix Epoch time in seconds, e.g. ``1640370768``
                * keyword **remote_host** (`str`): Remote host IP
                  address
                * keyword **username** (`str`): Logged in username
    :rtype: dict
    """
    return self._get("/userAccount/{}?cached={}".format(ne_id, cached))
