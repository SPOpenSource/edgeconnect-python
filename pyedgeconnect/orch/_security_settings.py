# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# securitySettings : Security Settings


def get_security_settings(self) -> dict:
    """Get advanced security settings

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - securitySettings
          - GET
          - /security/advancedSettings

    :return: Returns dictionary of advanced security settings
    :rtype: dict
    """
    return self._get("/security/advancedSettings")


def set_security_settings(
    self,
    verify_orch_cert: bool = None,
    verify_portal_cert: bool = None,
    enforce_csrf_check: bool = None,
    enforce_binary_check: bool = None,
    enforce_image_check: bool = None,
) -> bool:
    """Set advanced security settings for Edge Connect appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - securitySettings
          - POST
          - /security/advancedSettings

    .. note::
        The function will call :func:`~get_security_settings` and for
        any parameters that are not specified (defaulting to ``None``)
        the current values for those parameters will be used.

    :param verify_orch_cert: Appliances will try to validate the
        Orchestrator certificate, as None will use current setting,
        defaults to None \n
        Do not enable if any of the following are true:
            #. Orchestrator is using a self-signed certificate
            #. Orchestrator is behind a proxy
            #. The appliance is not configured with the Orchestrator
               domain name
            #. If EdgeConnect is using Orchestrator as a proxy to reach
               Portal, then do not turn this on unless Orchestrator has
               a valid certificate
    :type verify_orch_cert: bool, optional
    :param verify_portal_cert: Appliances will try to validate the Cloud
        Portal certificate, as None will use current setting,
        defaults to None \n
        Do not enable if any of the following are true:
            #. The appliance is behind a proxy
            #. Orchestrator is not configured with the Cloud Portal
               domain name
            #. The appliance is not configured with the Cloud Portal
               domain name
    :type verify_portal_cert: bool, optional
    :param enforce_csrf_check: Appliances and Orchestrator will enforce
        CSRF check, as None will use current setting, defaults to None
    :type enforce_csrf_check: bool, optional
    :param enforce_binary_check: Appliance verifies integrity of library
        and executable files on boot, as None will use current setting,
        defaults to None \n
            **Important**: Increases bootup time. Not applicable for
            FIPS appliances, as verification is always enabled for FIPS.
    :type enforce_binary_check: bool, optional
    :param enforce_image_check: Appliance verifies digital signature of
        software image before install or upgrade, as None will use
        current setting, defaults to None \n
            **Important**: Not applicable for FIPS appliances, as
            verification is always enabled for FIPS.
    :type enforce_image_check: bool, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    # If any of the options aren't passed they are set to None
    # Get the current options and for any options that were None,
    # set the values to the current values
    current_settings = self.get_security_settings()
    if verify_orch_cert is None:
        verify_orch_cert = current_settings["verifyOrchestratorCert"]
    if verify_portal_cert is None:
        verify_portal_cert = current_settings["verifyPortalCert"]
    if enforce_csrf_check is None:
        enforce_csrf_check = current_settings["enforceCSRFCheck"]
    if enforce_binary_check is None:
        enforce_binary_check = current_settings["enforceBinaryCheck"]
    if enforce_image_check is None:
        enforce_image_check = current_settings["enforceImageCheck"]

    data = {
        "verifyOrchestratorCert": verify_orch_cert,
        "verifyPortalCert": verify_portal_cert,
        "enforceCSRFCheck": enforce_csrf_check,
        "enforceBinaryCheck": enforce_binary_check,
        "enforceImageCheck": enforce_image_check,
    }

    return self._post(
        "/security/advancedSettings",
        data=data,
        expected_status=[204],
        return_type="bool",
    )
