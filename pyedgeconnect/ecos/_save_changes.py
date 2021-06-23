# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# saveChanges : Save configuration changes


def save_changes(self) -> bool:
    """Save changes on Edge Connect appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - saveChanges
          - POST
          - /saveChanges

    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._post("/saveChanges", return_type="bool")
