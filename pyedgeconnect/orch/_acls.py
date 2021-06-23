# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# acls : ECOS ACLs (access control lists)


def get_appliance_acls(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get Access list settings configurations from Edge Connect
    appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - acls
          - GET
          - /acls/{neId}?cached={cached}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary where each key is name of an ACL, each
        value is an object of the ACL's settings. Each ACL's settings
        contains 'entry' and 'rmap'. 'rmap' give info about the
        routemap which uses this ACL.
    :rtype: dict
    """

    return self._get("/acls/{}?cached={}".format(ne_id, cached))
