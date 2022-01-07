# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# upgradeAppliances : Validate and upgrade appliances


def get_ecos_images(
    self,
) -> list:
    """Get ECOS images data including file name, version, and build date
    and time

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applianceUpgrade
          - GET
          - /vxoaImages

    :return: Returns list of dictionaries of ECOS image details \n
        * [`dict`]: Image object \n
            * keyword **NxImage.fileName** (`str`): image filename,
              e.g. ``pdimage-9.0.3.2_89687.img``
            * keyword **NxImage.buildDate** (`str`): image build date
              time, e.g. ``2021-09-02 20:39:05``
            * keyword **NxImage.version** (`str`): image version,
              e.g. ``9.0.3.2_89687``
            * keyword **NxImage.lastModified** (`int`): image last
              modified time in Unix Epoch milliseconds
            * keyword **portalDownloaded** (`bool`): If image is
              downloaded from Cloud Portal
    :rtype: dict
    """
    return self._get("/vxoaImages")


def delete_ecos_image(
    self,
    image_name: str,
) -> dict:
    """Delete ECOS image

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - upgradeAppliances
          - DELETE
          - /vxoaImages/{imageFile}

    :param image_name: The image name to delete,
        e.g. ``pdimage-9.1.0.2_91232.img``
    :type image_name: str
    :return: Returns dictionary of appliance upgrade background task \n
        * keyword **clientKey** (`str`): The client key of appliances
          upgrade background task
    :rtype: dict
    """
    return self._delete(
        "/vxoaImages/{}".format(image_name), return_type="text"
    )
