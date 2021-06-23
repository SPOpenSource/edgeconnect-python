# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# shell : Shell Access Setting


def get_shell_access_setting(self) -> dict:
    """Get current Shell Access setting

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - shell
          - GET
          - /shell/shellAccessSetting

    :return: Returns dictionary of shell access settings
    :rtype: dict
    """
    return self._get("/shell/shellAccessSetting")


def set_shell_access_setting(
    self,
    shell_access_setting: str,
) -> bool:
    """Set Shell Access setting

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - shell
          - POST
          - /shell/shellAccessSetting

    .. warning::
        **IMPORTANT!!! THIS IS NOT REVERTABLE** - Can be changed in
        order of increasing security ``lockdown_ssa`` to ``lockdown``

    :param shell_access_setting: ``lockdown`` for Disabled Shell Access,
        ``lockdown_ssa`` for Secure Shell Access.
    :raises ValueError: ``shell_access_setting`` value must match one of
        the valid settings
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    valid = {"lockdown", "lockdown_ssa"}
    if shell_access_setting not in valid:
        raise ValueError("results: status must be one of %r." % valid)

    return self._post(
        "/shell/shellAccessSetting",
        data={"shellAccessSetting": shell_access_setting},
        expected_status=[204],
        return_type="bool",
    )
