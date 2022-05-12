# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# user : Orchestrator server user management


def get_all_users(
    self,
) -> list:
    """Get all user infomration from Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - user
          - GET
          - /users

    :return: Returns list of dictionaries of user information \n
        [`dict`]: user information object \n
            * keyword **userPk** (`str`): User identifier
            * keyword **username** (`str`): User name
            * keyword **firstName** (`str`): First Name
            * keyword **lastName** (`str`): Last Name
            * keyword **phone** (`str`): Phone number
            * keyword **email** (`str`): Email address
            * keyword **password** (`str`): Will be left ``Null`` for
              security reasons
            * keyword **createTime** (`int`): Time user was created, in
              unix epoch time in seconds
            * keyword **status** (`str`): Whether user is Active or
              Inactive
            * keyword **role** (`str`): User role,
              e.g. ``Admin Manager`` or ``Network Monitor``
            * keyword **isTwoFactorEmail** (`bool`): ``True`` if email
              two-factor auth is enabled
            * keyword **isTwoFactorTime** (`bool`): ``True`` if
              application two-factor auth is enabled
            * keyword **salt** (`str`): Usually left blank
    :rtype: list
    """
    return self._get("/users")


def get_user(
    self,
    username: str,
) -> dict:
    """Get specified user information

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - user
          - GET
          - /users/{userName}

    :param username: Name of user to query information for
    :type username: str
    :return: Returns dictionary of user information \n
        * keyword **userPk** (`str`): User identifier
        * keyword **username** (`str`): User name
        * keyword **firstName** (`str`): First Name
        * keyword **lastName** (`str`): Last Name
        * keyword **phone** (`str`): Phone number
        * keyword **email** (`str`): Email address
        * keyword **password** (`str`): Will be left ``Null`` for
          security reasons
        * keyword **createTime** (`int`): Time user was created, in unix
          epoch time in seconds
        * keyword **status** (`str`): Whether user is Active or Inactive
        * keyword **role** (`str`): User role,
          e.g. ``Admin Manager`` or ``Network Monitor``
        * keyword **isTwoFactorEmail** (`bool`): ``True`` if email
          two-factor auth is enabled
        * keyword **isTwoFactorTime** (`bool`): ``True`` if application
          two-factor auth is enabled
        * keyword **salt** (`str`): Usually left blank
    :rtype: dict
    """
    return self._get("/users/{}".format(username))


def delete_user(
    self,
    user_id: str,
    username: str,
) -> bool:
    """Delete user from Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - user
          - DELETE
          - /users/{userId}/{userName}

    :param user_id: UserPk value of user, can be retrieved with get_user
        function
    :type user_id: str
    :param username: Name of user to query information for
    :type username: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        "/users/{}/{}".format(user_id, username),
        expected_status=[204],
        return_type="bool",
    )


def create_or_update_user(
    self,
    new_user: bool,
    user_pk: str,
    first_name: str,
    last_name: str,
    phone: str,
    email: str,
    status: str,
    role: str,
    username: str,
    password: str,
    repeat_password: str,
    two_factor_email: bool,
    two_factor_app: bool,
    create_display_time: str = "",
) -> bool:
    """Create new user or update existing user

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - user
          - POST
          - /users/{newUser}

    :param new_user: ``True`` for creating new user, ``False`` for
        updating existing user
    :type new_user: bool
    :param user_pk: Primary key of the user object. Use empty string if
        creating new user
    :type user_pk: str
    :param first_name: First name of user
    :type first_name: str
    :param last_name: Last name of user
    :type last_name: str
    :param phone: Phone number for user
    :type phone: str
    :param email: Email address for user
    :type email: str
    :param status: Enable the user, takes values ``Active`` or
        ``Inactive``
    :type status: str
    :param role: Use value ``Admin Manager`` for admin role and
        ``Network Monitor`` for monitor role
    :type role: str
    :param username: Username for user
    :type username: str
    :param password: Password for user
    :type password: str
    :param repeat_password: Confirm matching password for user
    :type repeat_password: str
    :param two_factor_email: ``True`` to enable two-factor auth via
        email for user, ``False`` to disable
    :type two_factor_email: bool
    :param two_factor_app: ``True`` to enable two-factor auth via app
        for user, ``False`` to disable
    :type two_factor_app: bool
    :param create_display_time: Description missing from Swagger
    :type create_display_time: str, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "userPk": user_pk,
        "firstName": first_name,
        "lastName": last_name,
        "phone": phone,
        "email": email,
        "createDisplayTime": create_display_time,
        "status": status,
        "role": role,
        "username": username,
        "password": password,
        "repeatPassword": repeat_password,
        "isTwoFactorEmail": two_factor_email,
        "isTwoFactorTime": two_factor_app,
    }

    return self._post(
        "/users/{}".format(new_user),
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def change_user_password(
    self,
    username: str,
    current_password: str,
    new_password: str,
) -> bool:
    """Update an existing user's password

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - user
          - POST
          - /users/{newUser}/password

    :param username: Username for user
    :type username: str
    :param current_password: Current password for user
    :type current_password: str
    :param new_password: New password for user, Password must be at
        least 8 characters long and contain the following items: upper
        case letter, lower case letter, a number, a special character
    :type new_password: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "oldPassword": current_password,
        "newPassword": new_password,
    }

    return self._post(
        "/users/{}/password".format(username),
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def reset_user_password(
    self,
    password: str,
    repeat_password: str,
    password_id: str,
    two_factor_email: bool,
    two_factor_app: bool,
) -> dict:
    """TODO - UNSURE OF CURRENT FUNCTIONALITY, TESTING GIVES HTTP 500,
    Reset password for user

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - user
          - POST
          - /users/resetPassword

    :param password: Password for user
    :type password: str
    :param repeat_password: Confirm matching password for user
    :type repeat_password: str
    :param password_id:
    :type password_id: str
    :param two_factor_email: ``True`` to enable two-factor auth via
        email for user, ``False`` to disable
    :type two_factor_email: bool
    :param two_factor_app: ``True`` to enable two-factor auth via app
        for user, ``False`` to disable
    :type two_factor_app: bool
    :return: Returns dictionary with password reset barcode image \n
        * keyword **barcodeBase64Jpeg** (`str`): Base 64 encoded jpeg of
          barcode to scan
    :rtype: dict
    """
    data = {
        "password": password,
        "confirmPassword": repeat_password,
        "id": password_id,
        "tfaApp": two_factor_app,
        "tfaEmail": two_factor_email,
    }

    return self._post(
        "/users/resetPassword",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def user_forgot_password(
    self,
    username: str,
) -> bool:
    """Initiate forgot password for specific user

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - user
          - POST
          - /users/forgotPassword

    :param username: Username for user
    :type username: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "userName": username,
    }

    return self._post(
        "/users/forgotPassword",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def get_new_two_factor_key(
    self,
) -> dict:
    """Returns a barcode (base64 encoded) to scan with an authentication
    application to setup app-based two factor authentication for your
    account.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - user
          - GET
          - /users/newTfaKey

    Request is based for user that is authenticated making the request,
    and app-based two factor authentication has to be enabled for the
    account.

    :return: Returns dictionary with password reset barcode image \n
        * keyword **barcodeBase64Jpeg** (`str`): Base 64 encoded jpeg of
          barcode to scan
    :rtype: dict
    """
    return self._get("/users/newTfaKey")
