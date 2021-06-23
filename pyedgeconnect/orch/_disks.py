# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# disks : ECOS disk information


def get_appliance_disk_information(
    self,
    ne_id: str,
) -> dict:
    """Get disk information from appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - disks
          - GET
          - /configReportDisk/{neId}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :return: Returns dictionary of disk information \n
        * keyword **disks** (`dict`): Dictionary of disks in Edge
          Connect appliance. Disks are identified by numeric strings,
          e.g. ``"0"``
        * keyword **controller** (`dict`): Dictionary of controller
          information
        * keyword **diskImage** (`str`): Filename of disk image
    :rtype: dict
    """
    return self._get("/configReportDisk/{}".format(ne_id))
