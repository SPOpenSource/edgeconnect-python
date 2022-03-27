# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# appSystemStateInfo : ECOS system state


def get_appliance_system_state_info(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get appliance system state information

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - appSystemStateInfo
          - GET
          - /systemInfo/{neId}?cached={cached}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary of appliance system state info \n
        * keyword **portalObjectId** (`str`): Appliance ID in Cloud
          Portal
        * keyword **hostname** (`str`): Appliance hostname
        * keyword **nepk** (`str`): Appliance ID
        * keyword **biosVersion** (`str`): BIOS version, e.g. ``6.00``
        * keyword **rebootRequired** (`bool`): ``True`` if system
          currently requires reboot
        * keyword **inlineRouter** (`bool`): ``True`` if system
          currently deployed in inline-router mode
        * keyword **timezone** (`str`): Configured timezone,
          e.g. ``Etc/UTC``
        * keyword **release** (`str`): Current running software
          release, e.g. ``ECOS 9.1.0.1_91199``
        * keyword **uuid** (`str`): UUID of appliance
        * keyword **platform** (`str`): Running platform,
          e.g. ``VMware`` for a VM EC running on ESXi
        * keyword **datetime** (`str`): Current Date/Time reported by
          appliance in format of ``YYYY/MM/DD HH:MM:SS TMZ``
        * keyword **gmtOffset** (`int`): Hours offset from GMT
        * keyword **modelShort** (`str`): Short format of model name
        * keyword **model** (`str`): Full length detailed model name
        * keyword **isLicenseInstalled** (`bool`): Legacy local license
          status, e.g. ``false``, not related to modern BW license
        * keyword **licenseRequired** (`bool`): If legacy license is
          required
        * keyword **licenseExpiryDate** (`str`):
        * keyword **licenseExpirationDaysLeft** (`int`): Days left of
          license in scientific format, e.g. ``1.79e+308``
        * keyword **uptimeString** (`str`): Uptime in string format,
          e.g. ``1d 28m 40s``
        * keyword **releaseWithoutPrefix** (`str`): Current running
          software release without ECOS prefix,
          e.g. ``9.1.0.1_91199``
        * keyword **hasUnsavedChanges** (`bool`): ``True`` if appliance
          has any current changes that have not yet been saved
        * keyword **applianceid** (`int`): Integer represetation of
          appliance id, e.g. ``1894366``
        * keyword **deploymentMode** (`str`): Current deployment mode,
          e.g. ``router``
        * keyword **uptime** (`int`): Appliance uptime in milliseconds
        * keyword **serial** (`str`): Appliance serial number
        * keyword **status** (`str`): Appliance status, e.g. ``Normal``
        * keyword **alarmSummary** (`dict`): Alarm summary object \n
            * keyword **num_cleared** (`int`): Number of cleared alarms
            * keyword **num_critical** (`int`): Number of critical
              alarms
            * keyword **num_equipment_outstanding** (`int`):
            * keyword **num_major** (`int`): Number of major alarms
            * keyword **num_minor** (`int`): Number of minor alarms
            * keyword **num_outstanding** (`int`): NEEDS DESCRIPTION
            * keyword **num_raise_ignore** (`int`): NEEDS DESCRIPTION
            * keyword **num_software_outstanding** (`int`): NEEDS
              DESCRIPTION
            * keyword **num_tca_outstanding** (`int`): NEEDS DESCRIPTION
            * keyword **num_traffic_class_outstanding** (`int`): NEEDS
              DESCRIPTION
            * keyword **num_tunnel_outstanding** (`int`): NEEDS
              DESCRIPTION
            * keyword **num_warning** (`int`): Number of warning alarms
    :rtype: dict
    """
    return self._get("/systemInfo/{}?cached={}".format(ne_id, cached))
