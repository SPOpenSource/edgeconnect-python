# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# reboot : Reboot


def request_reboot(
    self,
    clear_nm: str = "false",
    delay: int = 0,
    next_partition: str = "false",
    reboot_type: str = "Normal",
    save_db: str = "false",
    apply_before_reboot: dict = {"hostname": ""},
) -> bool:
    """Reboot Edge Connect appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - reboot
          - POST
          - /reboot

    :param clearn_nm: Clear network memory on reboot,
        defaults to "false"
    :type clear_nm: str, optional
    :param delay: Delay in seconds before reboot, defaults to 0
    :type delay: int, optional
    :param next_partition: Set next partition as boot partition,
        defaults to "false"
    :type next_partition: str, optional
    :param reboot_type: defaults to "Normal"
    :type reboot_type: str, optional
    :param save_db: save database changes prior to reboot,
        defaults to "false"
    :type save_db: str, optional
    :param apply_before_reboot: Config data applied before reboot,
        defaults to {"hostname":""}
    :type apply_before_reboot: dict, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/reboot",
        data={
            "clear_nm": clear_nm,
            "delay": delay,
            "next_partition": next_partition,
            "reboot_type": reboot_type,
            "save_db": save_db,
            "applyBeforeReboot": apply_before_reboot,
        },
        return_type="bool",
    )
