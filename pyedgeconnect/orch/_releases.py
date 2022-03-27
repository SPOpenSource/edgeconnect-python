# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# releases : Recommended ECOS and Orchestrator releases


def get_releases_for_orchestrator_and_ecos(
    self,
    filter_new: bool,
) -> dict:
    """Get all releases for Orchestrator and ECOS

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - releases
          - GET
          - /release

    :param filter_new: ``True`` to return only new releases of
        Orchestrator and ECOS
    :type filter_new: bool
    :return: Returns dictionary of software release information \n
        * keyword **gmsbuilds** (`list[dict]`): Orchestrator releases \n
            * keyword **version** (`str`): Version of the release
            * keyword **product** (`str`): orchestrator or ECOS (vxoa)
            * keyword **releaseType** (`str`): Type of release,
              e.g. ``FCS`` or ``GA``
            * keyword **releaseDate** (`int`): Release date in Unix
              EPOCH in milliseconds
            * keyword **description** (`str`): Release description text
            * keyword **modifiedTime** (`int`): Last modified time in
              Unix EPOCH in milliseconds
            * keyword **noteId** (`str`): Release ID hash, if release
              notes are included, otherwise ``null``
            * keyword **notesS3Metadata** (`dict`): S3 metadata for
              release notes, if applicable \n
                * keyword **ETag** (`str`): Entity tag of asset in S3,
                  hash of object content (not metadata)
                * keyword **Location** (`str`): URL to asset
                * keyword **Key** (`str`): Filename of asset
                * keyword **key** (`str`): Filename of asset
                * keyword **Bucket** (`str`): S3 Bucket name,
                  e.g. ``prod-portal-release-images``
                * keyword **uploadTimestamp** (`int`): Time uploaded
                  to S3 in Unix EPOCH milliseconds
            * keyword **imageId** (`str`): Release ID hash, if image
              is included, otherwise ``null``
            * keyword **imageS3Metadata** (`dict`): S3 metadata for
              image, if applicable \n
                * keyword **ETag** (`str`): Entity tag of asset in S3,
                  hash of object content (not metadata)
                * keyword **Location** (`str`): URL to asset
                * keyword **Key** (`str`): Filename of asset
                * keyword **key** (`str`): Filename of asset
                * keyword **Bucket** (`str`): S3 Bucket name,
                  e.g. ``prod-portal-release-images``
                * keyword **uploadTimestamp** (`int`): Time uploaded
                  to S3 in Unix EPOCH milliseconds
            * keyword **enabled** (`bool`): If image is available
            * keyword **haveNotifiedInEmail** (`bool`): If release
              email notification has been sent
            * keyword **createdAt** (`int`): Release creation time in
              Unix EPOCH milliseconds
            * keyword **releaseType** (`str`): Release type, e.g. ``GA``
              or ``FCS``
            * keyword **lastDownloadTime** (`int`): Time last downloaded
              in Unix EPOCH milliseconds, ``null`` if not yet downloaded
            * keyword **_id** (`str`): Release ID hash
            * keyword **uploadedBy** (`null`): ``null``
        * keyword **vxoabuilds** (`list[dict]`): ECOS (vxoa) releases \n
            * keyword **version** (`str`): Version of the release
            * keyword **product** (`str`): orchestrator or ECOS (vxoa)
            * keyword **releaseType** (`str`): Type of release,
              e.g. ``FCS`` or ``GA``
            * keyword **releaseDate** (`int`): Release date in Unix
              EPOCH in milliseconds
            * keyword **description** (`str`): Release description text
            * keyword **modifiedTime** (`int`): Last modified time in
              Unix EPOCH in milliseconds
            * keyword **noteId** (`str`): Release ID hash, if release
              notes are included, otherwise ``null``
            * keyword **notesS3Metadata** (`dict`): S3 metadata for
              release notes, if applicable \n
                * keyword **ETag** (`str`): Entity tag of asset in S3,
                  hash of object content (not metadata)
                * keyword **Location** (`str`): URL to asset
                * keyword **Key** (`str`): Filename of asset
                * keyword **key** (`str`): Filename of asset
                * keyword **Bucket** (`str`): S3 Bucket name,
                  e.g. ``prod-portal-release-images``
                * keyword **uploadTimestamp** (`int`): Time uploaded
                  to S3 in Unix EPOCH milliseconds
            * keyword **imageId** (`str`): Release ID hash, if image
              is included, otherwise ``null``
            * keyword **imageS3Metadata** (`dict`): S3 metadata for
              image, if applicable \n
                * keyword **ETag** (`str`): Entity tag of asset in S3,
                  hash of object content (not metadata)
                * keyword **Location** (`str`): URL to asset
                * keyword **Key** (`str`): Filename of asset
                * keyword **key** (`str`): Filename of asset
                * keyword **Bucket** (`str`): S3 Bucket name,
                  e.g. ``prod-portal-release-images``
                * keyword **uploadTimestamp** (`int`): Time uploaded
                  to S3 in Unix EPOCH milliseconds
            * keyword **enabled** (`bool`): If image is available
            * keyword **haveNotifiedInEmail** (`bool`): If release
              email notification has been sent
            * keyword **createdAt** (`int`): Release creation time in
              Unix EPOCH milliseconds
            * keyword **releaseType** (`str`): Release type, e.g. ``GA``
              or ``FCS``
            * keyword **lastDownloadTime** (`int`): Time last downloaded
              in Unix EPOCH milliseconds, ``null`` if not yet downloaded
            * keyword **_id** (`str`): Release ID hash
            * keyword **uploadedBy** (`null`): ``null``
    :rtype: dict
    """
    return self._get("/release?filter={}".format(filter_new))


def get_releases_notifications(
    self,
) -> list:
    """This API will return all the notifications that are meant to be
    shown in Orchestrator. This means the notification is new, it's
    'remind me' date is past, and it has not been dismissed.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - releases
          - GET
          - /release/notifications

    :return: Returns list of software release notifications \n
        * [`dict`]: Release notification object \n
            * keyword **product** (`int`): Product identifier, ``1`` for
              Orchestrator, ``2`` for ECOS
            * keyword **description** (`str`): Description notes of
              notification message
            * keyword **version** (`str`): Release version,
              e.g. ``9.1.0.40524``
    :rtype: list
    """
    return self._get("/release/notifications")


def delay_release_notification(
    self,
    version: str,
    hour_delay: int,
) -> bool:
    """Delay the notifcation by a number of hours

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - releases
          - GET
          - /release/notifications/delay/{version}

    :return: Returns list of software release notifications \n
    :rtype: list
    """
    data = {"delayByHours": hour_delay}

    return self._post(
        "/release/notifications/delay/{}".format(version),
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def dismiss_release_notification(
    self,
    version: str,
) -> bool:
    """Dismiss a release, so it's no longer shown to the user

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - releases
          - GET
          - /release/notifications/dismiss/{version}

    :return: Returns True/False based on successful call
    :rtype: bool
    """

    return self._post(
        "/release/notifications/dismiss/{}".format(version),
        expected_status=[204],
        return_type="bool",
    )
