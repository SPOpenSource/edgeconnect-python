# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# gmsNotification : notification banner: Get, Add, Update, Delete of
# the message


def get_gms_notification(self) -> list:
    """Get current Orchestrator notification banner message

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsNotification
          - GET
          - /notification

    :return: Returns list of configured Banner Message \n
        [`dict`]: Banner Message Config object \n
            * keyword **resourceBase** (`str`):
            * keyword **resourceKey** (`str`):
            * keyword **configData** (`dict`): Banner Message object \n
                * keyword **message** (`str`): Banner Message string
                * keyword **author** (`str`): Author of Banner Message
            * keyword **version** (`int`): Version of message,
              increments on update
            * keyword **timestamp** (`int`): Timestamp of update in unix
              epoch time
    :rtype: list
    """
    return self._get("/notification")


def update_gms_notification(
    self,
    message: str,
    author: str = "",
) -> bool:
    """Update Orchestrator notification banner message

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsNotification
          - POST
          - /notification

    :param message: Banner notification message
    :type message: str
    :param author: Author of message, defaults to ""
    :type author: str, optional
    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    data = {"message": message, "author": author}

    return self._post(
        "/notification",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def delete_gms_notification(self) -> bool:
    """Delete Orchestrator notification banner message

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - gmsNotification
          - DELETE
          - /notification

    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    return self._delete(
        "/notification", expected_status=[204], return_type="bool"
    )
