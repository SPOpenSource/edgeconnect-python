# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# vxoaHostname : Change appliance hostname


def update_appliance_hostname(
    self,
    ne_pk: str,
    hostname: str,
) -> bool:
    """Add or update hostname to Edge Connect appliance. This operation
    will take a few seconds to run.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - vxoaHostname
          - GET
          - /hostname/{nePk}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param hostname: New hostname to apply to the appliance
    :type hostname: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "hostname": hostname,
    }

    return self._post(
        "/hostname/{}".format(ne_pk),
        data=data,
        expected_status=[204],
        return_type="bool",
    )
