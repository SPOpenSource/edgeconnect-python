# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# login : Login/Logout


def login(
    self,
    user: str,
    password: str,
) -> bool:
    """Login to Edge Connect appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - login
          - POST
          - /login

    :param user: Username to login to appliance
    :type user: str
    :param password: Password to login to appliance
    :type password: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    try:
        response = self._post(
            "/login",
            {"user": user, "password": password},
            return_type="full_response",
        )

        if response is not None and response.status_code == 200:
            # get and set X-XSRF-TOKEN
            for cookie in response.cookies:
                if cookie.name == "edgeosCsrfToken":
                    self.headers["X-XSRF-TOKEN"] = cookie.value
                    return True
                elif cookie.name == "vxoaSessionID":
                    self.headers["vxoaSessionID"] = cookie.value
                    return True
                else:
                    pass
            # HTTP/200 without a cookie
            self.logger.error(
                "Login failed: HTTP 200 but no CSRF Token cookie"
            )
            self.logger.error(response.cookies)
            return False
        else:
            self.logger.error(
                "Login failed: see above response text for details"
            )
            return False

    except Exception as ex:
        self.logger.error("login error: {}".format(ex))
        return False


def logout(self) -> bool:
    """Logout to Edge Connect appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - login
          - GET
          - /logout

    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._get("/logout", return_type="bool")
