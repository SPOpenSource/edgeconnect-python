# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# systemInfo : System Information


def get_appliance_system_info(
    self,
) -> dict:
    """Get system information on the appliance.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - systemInfo
          - GET
          - /systemInfo

    :return: Returns dictionary of appliance system information \n
        * keyword **hostName** (`str`): Appliance hostname
        * keyword **applianceid** (`int`): Appliance integer ID
        * keyword **model** (`str`): Appliance Model (longform)
        * keyword **modelShort** (`str`): Appliance Model (shortform)
        * keyword **status** (`str`): Appliance Status
        * keyword **uptime** (`int`): Appliance uptime in milliseconds
        * keyword **uptimeString** (`str`): Appliance uptime as string,
          e.g., ``56d 13h 15m 29s``
        * keyword **datetime** (`str`): Current datetime on appliance,
          e.g., ``2022/09/28 13:04:47 Etc/UTC``
        * keyword **timezone** (`str`): Timezone, e.g., ``Etc/UTC``
        * keyword **gmtOffset** (`int`): GMT offset value
        * keyword **release** (`str`): Software release with ECOS,
          e.g., ``ECOS 9.1.1.3_91760``
        * keyword **releaseWithoutPrefix** (`str`): Software release,
          numbers only, e.g., ``9.1.1.3_91760``
        * keyword **serial** (`str`): Appliance serial number
        * keyword **uuid** (`str`): Appliance uuid
        * keyword **deploymentMode** (`str`): Appliance deployment mode,
          e.g., ``router``
        * keyword **inlineRouter** (`bool`): ``True`` if appliance is in
          inline-router mode
        * keyword **licenseRequired** (`bool`): Legacy license
          requirement check
        * keyword **isLicenseInstalled** (`bool`): Legacy license
          install check
        * keyword **licenseExpiryDate** (`str`): Legacy license expire
          date
        * keyword **licenseExpirationDaysLeft** (`int`): Legacy license
          expire days left
        * keyword **hasUnsavedChanges** (`bool`): ``True`` if appliance
          has unsaved configuration changes
        * keyword **rebootRequired** (`bool`): ``True`` if appliance
          requires reboot
        * keyword **biosVersion** (`str`): BIOS version on appliance
        * keyword **alarmSummary** (`dict`): Alarm summary \n
            * keyword **num_cleared** (`int`): Number of alarms cleared
            * keyword **num_critical** (`int`): Number of critical
              alarms
            * keyword **num_equipment_outstanding** (`int`): Number of
              hardware alarms outstanding
            * keyword **num_major** (`int`): Number of major alarms
            * keyword **num_minor** (`int`): Number of minor alarms
            * keyword **num_outstanding** (`int`): Number of
              outstanding alarms
            * keyword **num_raise_ignore** (`int`): Number of raise
              ignore
            * keyword **num_software_outstanding** (`int`): Number of
              software alarms outstanding
            * keyword **num_tca_outstanding** (`int`): Number of TCA
              alarms outstanding
            * keyword **num_traffic_class_outstanding** (`int`): Number
              of traffic class alarms outstanding
            * keyword **num_tunnel_outstanding** (`int`): Number of
              tunnel alarms outstanding
            * keyword **num_warning** (`int`): Number of warning alarms
    :rtype: dict
    """
    return self._get("/systemInfo")
