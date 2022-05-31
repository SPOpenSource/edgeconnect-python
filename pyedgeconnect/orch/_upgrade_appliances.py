# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# upgradeAppliances : Validate and upgrade appliances
from __future__ import annotations


def validate_appliance_upgrade(
    self,
    versions: list[str],
    ne_pk_list: list[str] = [],
) -> dict:
    """Check ECOS version compatibility for appliance upgrades through
    Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - upgradeAppliances
          - POST
          - /validateApplianceUpgrade

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk) of appliances to validate, e.g. ``["3.NE","5.NE"]``.
        If not provided, all appliances in the Orchestrator network are
        validated, defaults to ``[]``
    :type ne_pk_list: list[str], optional
    :param versions: List of version numbers to validate, e.g.
        ``["9.1.0.2", "9.1.0.1"]``
    :type versions: list[str]
    :return: Returns dictionary of upgrade validation data \n
        * keyword **versions** (`list[str]`): ECOS versions available
          for upgrade
        * keyword **appliances** (`list[dict]`): Appliance details \n
            * [`dict`]: Appliance object \n
                * keyword **nePk** (`str`): The appliance ID
                * keyword **model** (`str`): The appliance model
                * keyword **platform** (`str`): The appliance platform
                * keyword **version** (`str`): The current appliance
                  version
                * keyword **upgradable** (`list[list[int]]`): ECOS
                  versions that the appliance can upgrade to from the
                  versions list, each sub-list contains ordered list of
                  integers as the version number,
                  e.g. ``[...,[9,1,0,2],...`` if appliance can be
                  upgraded to ``9.1.0.2``. If none available will be
                  blank list ``[]``
        * keyword **orchestrator** (`str`): Current version of
          Orchestrator
        * keyword **orchSupports** (`str`): The maximum ECOS version
          that Orchestrator can support
    :rtype: dict
    """
    data = {
        "nePks": ne_pk_list,
        "versions": versions,
    }

    return self._post(
        "/validateApplianceUpgrade",
        data=data,
    )


def upgrade_appliances(
    self,
    ne_pk_list: list[str],
    version: list[str],
    install_option: str,
    image_name: str,
    from_portal: bool,
    from_url: bool,
) -> dict:
    """Check ECOS version compatibility for appliance upgrades through
    Portal

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - upgradeAppliances
          - POST
          - /validateApplianceUpgrade

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk) of appliances to upgrade, e.g. ``["3.NE","5.NE"]``.
    :type ne_pk_list: list[str]
    :param version: Version of software to upgrade to, e.g. "9.1.0.1"
    :type version: str
    :param install_option: The install option. Accepted values are
        ``install_only``, ``install_switch`` which will set the next
        boot partition but not reboot, and ``install_reboot`` which will
        install, set the boot partition, and perform a reboot.
    :type install_option: str
    :param image_name: The image name that will use to upgrade for the
        appliances, e.g. ``pdimage-9.1.0.2_91232.img`` these can be
        retrieved with
        :func:`pyedgeconnect.Orchestrator.get_ecos_images`
    :type image_name: str
    :param from_portal: The image is on Cloud Portal or not
    :type from_portal: bool
    :param from_url: The image is specified in Provide URL edit box
    :type from_url: bool
    :return: Returns dictionary of appliance upgrade background task \n
        * keyword **clientKey** (`str`): The client key of appliances
          upgrade background task
    :rtype: dict
    """
    data = {
        "neList": ne_pk_list,
        "installOption": install_option,
        "imageName": image_name,
        "version": version,
        "fromPortal": from_portal,
        "usingUrl": from_url,
    }

    return self._post(
        "/validateApplianceUpgrade",
        data=data,
    )
