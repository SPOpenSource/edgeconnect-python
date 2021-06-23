# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# uiUsageStats : Add usage count for one UI feature


def add_ui_usage_count(
    self,
    ui_name: str,
) -> bool:
    """Add usage count for UI feature by name

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - uiUsageStats
          - GET
          - /uiUsageStats/{uiName}

    :param ui_name: Name of UI feature
    :type ui_name: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post(
        "/uiUsageStats/{}".format(ui_name),
        expected_status=[204],
        return_type="bool",
    )
