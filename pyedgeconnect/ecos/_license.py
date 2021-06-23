# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# license : License


def is_reboot_required(self) -> dict:
    """Check with appliance if a reboot is required from changes

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - license
          - GET
          - /license/isRebootRequired

    :return: Dictionary with status if reboot is required \n
        * keyword **isRebootRequired** (`str`): If a reboot is required
    :rtype: dict
    """
    return self._get("/license/isRebootRequired")
