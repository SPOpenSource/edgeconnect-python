# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# login : Login and logout - authentication for REST APIs


def login(
    self,
    user: str,
    password: str,
    mfacode: str = "",
) -> bool:
    """Basic login function supporting with our without multi-factor
    authentication.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - login
          - POST
          - /authentication/login

    .. note::
        * To use multi-factor, first call :func:`~send_mfa` to obtain a
          token

        * If the userId is using RBAC, they must have R/O or R/W access
          to the REST API functionality to access the APIs

        * The auth modes of this call support ``local``, ``RADIUS``,
          ``TACACS+``, ``OAuth``, ``JWT``, and ``SAML``. Currently the
          :class:`~Orchestrator` class only supports ``local``,
          ``RADIUS``, and ``TACACS+``.

    :param user: Username to login
    :type user: str
    :param password: Password associated with the Username
    :type password: str
    :param mfacode: String numeric code as second factor for login,
        provided by Orchestrator after calling :func:`~send_mfa`
    :type mfacode: str, optional

    :type login_type: int, optional
    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    if self.authMode == "local":
        login_type = 0
    elif self.authMode == "radius":
        login_type = 1
    elif self.authMode == "tacacs":
        login_type = 2

    if self.authMode not in self.supportedAuthModes:
        print("{}: authentication mode not supported".format(self.authMode))
        return False

    response = self._post(
        "/authentication/login",
        {
            "user": user,
            "password": password,
            "token": mfacode,
            "loginType": login_type,
        },
        return_type="full_response",
    )

    if response is not None and response.status_code == 200:
        # get and set X-XSRF-TOKEN
        for cookie in response.cookies:
            if cookie.name == "orchCsrfToken":
                self.headers["X-XSRF-TOKEN"] = cookie.value
                self.authenticated = True
                return True
        # HTTP/200 without a cookie
        self.logger.error("Login failed: HTTP 200 but no CSRF Token cookie")
        self.logger.error(response.cookies)
        return False
    else:
        self.logger.error("Login failed: see above response text for details")
        return False


def send_mfa(
    self,
    user: str,
    password: str,
    temp_code: bool,
) -> bool:
    """With a valid user/password Orchestrator will send that user an
    MFA code to be used in :func:`~login` function.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - login
          - POST
          - /authentication/loginToken

    :param user: Username to login
    :type user: str
    :param password: Password associated with the Username
    :type password: str
    :param temp_code:
    :type temp_code: bool
    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    return self._post(
        "/authentication/loginToken",
        {
            "user": user,
            "password": password,
            "TempCode": temp_code,
        },
        expected_status=[200, 204],
        return_type="bool",
    )


def logout(self) -> bool:
    """Logs out current session to Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - login
          - GET
          - /authentication/logout

    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    return self._get("/authentication/logout", return_type="bool")
