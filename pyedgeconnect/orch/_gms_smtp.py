# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# gmsSMTP : Orchestrator server SMTP configuration


def get_gms_smtp_settings(
    self,
) -> dict:
    """Get Orchestrator SMTP configuration

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsSMTP
          - GET
          - /gmsSMTP

    :return: Returns nested dictionary with smtp configuration details\n
        * keyword **smtp** (`dict`): dictionary of smtp configuration \n
            * keyword **emailAuthentication** (`bool`): Values for
              emailAuthentication
            * keyword **password** (`str`): E-mail server password,
              Will be ``null`` for security reasons
            * keyword **userID** (`str`): E-mail server user ID
            * keyword **emailSender** (`str`): E-mail address used to
              send E-mails
            * keyword **emailSsl** (`bool`): Enable or disable Enable
              SSL
            * keyword **server** (`str`): Address of the E-mail server
            * keyword **smtpPort** (`int`): SMTP server port
            * keyword **requireEmailVerification** (`bool`):
              Verification required before sending email
    :rtype: dict
    """
    return self._get("/gmsSMTP")


def set_gms_smtp_settings(
    self,
    email_authentication: bool = False,
    user_id: str = "",
    password: str = "",
    email_sender: str = "",
    email_ssl: bool = False,
    server: str = "",
    smtp_port: int = 25,
    require_verification: bool = False,
) -> bool:
    """Set Orchestrator SMTP configuration

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsSMTP
          - POST
          - /gmsSMTP

    .. note::
        If server and sender are unspecified, email will come from
        orchestrator@silverpeak.cloud sent via amazonses.com

    :param email_authentication: ``True`` for if using authentication
        for email, ``False`` if not, defaults to False
    :type email_authentication: bool, optional
    :param user_id: E-mail server user, defaults to ""
    :type user_id: str, optional
    :param password: E-mail server password, defaults to ""
    :type password: str, optional
    :param email_sender: E-mail address used to send E-mails,
        defaults to ""
    :type email_sender: str, optional
    :param email_ssl: ``True`` to Enable or ``False`` disable Enable SSL
        for email, defaults to False
    :type email_ssl: bool, optional
    :param server: Address of the E-mail server, defaults to ""
    :type server: str, optional
    :param smtp_port: SMTP server port, defaults to 25
    :type smtp_port: int, optional
    :param require_verification: ``True`` to set verification required
        before sending email, ``False`` to not require verifcation,
        defaults to False
    :type require_verification: bool, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "emailAuthentication": email_authentication,
        "password": password,
        "userID": user_id,
        "emailSender": email_sender,
        "emailSsl": email_ssl,
        "server": server,
        "smtpPort": smtp_port,
        "requireEmailVerification": require_verification,
    }

    return self._post(
        "/gmsSMTP", data=data, expected_status=[204], return_type="bool"
    )


def delete_gms_smtp_settings(self) -> bool:
    """Delete Orchestrator SMTP configuration

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsSMTP
          - DELETE
          - /gmsSMTP

    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete("/gmsSMTP", expected_status=[204], return_type="bool")


def test_gms_smtp_settings(
    self,
    test_email: str,
    email_authentication: bool = False,
    user_id: str = "",
    password: str = "",
    email_sender: str = "",
    email_ssl: bool = False,
    server: str = "",
    smtp_port: int = 25,
    require_verification: bool = False,
) -> bool:
    """Send test email with Orchestrator SMTP configuration

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsSMTP
          - POST
          - /gmsSMTP/testEmail

    .. note::
        If server and sender are unspecified, email will come from
        orchestrator@silverpeak.cloud sent via amazonses.com

    :param test_email: Email address to send test message to
    :type test_email: str
    :param email_authentication: ``True`` for if using authentication
        for email, ``False`` if not, defaults to False
    :type email_authentication: bool, optional
    :param user_id: E-mail server user, defaults to ""
    :type user_id: str, optional
    :param password: E-mail server password, defaults to ""
    :type password: str, optional
    :param email_sender: E-mail address used to send E-mails,
        defaults to ""
    :type email_sender: str, optional
    :param email_ssl: ``True`` to Enable or ``False`` disable Enable SSL
        for email, defaults to False
    :type email_ssl: bool, optional
    :param server: Address of the E-mail server, defaults to ""
    :type server: str, optional
    :param smtp_port: SMTP server port, defaults to 25
    :type smtp_port: int, optional
    :param require_verification: ``True`` to set verification required
        before sending email, ``False`` to not require verifcation,
        defaults to False
    :type require_verification: bool, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "smtp": {
            "emailAuthentication": email_authentication,
            "password": password,
            "userID": user_id,
            "emailSender": email_sender,
            "emailSsl": email_ssl,
            "server": server,
            "smtpPort": smtp_port,
            "requireEmailVerification": require_verification,
        },
        "emailRecepients": "",
    }

    return self._post(
        "/gmsSMTP/testEmail",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def verify_email_address(
    self,
    verification_id: str,
) -> bool:
    """Verify an email address in Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsSMTP
          - GET
          - /gmsSMTP/verifyAddress

    :param verification_id: Secure random string in verification email
        to identify the email address
    :type verification_id: str
    :return: Returns string that email was verified
    :rtype: str
    """
    return self._get(
        "/gmsSMTP/verifyAddress?id={}".format(verification_id),
        expected_status=[204],
        return_type="text",
    )


def get_unverified_email_addresses(
    self,
) -> list:
    """Get all unverified email addresses in Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsSMTP
          - GET
          - /gmsSMTP/unverifiedEmails

    :return: Returns list of strings with unverified email addresses
    :rtype: list
    """
    return self._get("/gmsSMTP/unverifiedEmails")


def delete_unverified_email_addresses(
    self,
    email_addresses: list,
) -> list:
    """Delete specified unverified email addresses from Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsSMTP
          - POST
          - /gmsSMTP/delUnverifiedEmails

    :param email_addresses: List of unverified email addresses as
        strings to delete
    :type email_addresses: list
    :return: Returns string that emails were removed
    :rtype: str
    """
    data = email_addresses

    return self._post(
        "/gmsSMTP/delUnverifiedEmails", data=data, return_type="text"
    )


def send_verification_email(
    self,
    email_address: str,
) -> list:
    """Send verification email to address which will include a
    verification link

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsSMTP
          - POST
          - /gmsSMTP/sendVerificationEmail

    :param email_address: E-mail address to send verification link to
    :type email_address: str
    :return: Returns string that email was sent or if no unverified
        emails found for specified address
    :rtype: str
    """
    return self._post(
        "/gmsSMTP/sendVerificationEmail?address={}".format(email_address),
        return_type="text",
    )
