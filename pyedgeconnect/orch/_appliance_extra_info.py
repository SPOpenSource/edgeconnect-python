# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# applianceExtraInfo : Update the appliance's extra information


def get_appliance_extra_info(
    self,
    ne_pk: str,
) -> dict:
    """Get appliance extra info, including location, contact, and
    ipsecudp information

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applianceExtraInfo
          - GET
          - /appliance/extraInfo/{nePk}

    :param ne_pk: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_pk: str
    :return: Returns dictionary of appliance extra info \n
        * keyword **location** (`dict`): Location info object \n
            * keyword **address** (`str`): Street Address
            * keyword **address2** (`str`): Additional Address Info
            * keyword **city** (`str`): City
            * keyword **state** (`str`): State
            * keyword **zipCode** (`str`): Zip Code
            * keyword **country** (`str`): Country
        * keyword **contact** (`dict`): Contact info object \n
            * keyword **name** (`str`): Contact name
            * keyword **email** (`str`): Contact email
            * keyword **phoneNumber** (`str`): Contact phone number
        * keyword **overlaySettings** (`dict`): Overlay settings info
          object \n
            * keyword **ipsecUdpPort** (`str`): Port used for ipsec udp
              traffic on appliance
            * keyword **isUserDefinedIPSecUDPPort** (`bool`): ``True``
              if user has defined custom port, ``False`` if port is
              determined by Orchestrator/Appliance
    :rtype: dict
    """
    return self._get("/appliance/extraInfo/{}".format(ne_pk))


def set_appliance_extra_info(
    self,
    ne_pk: str,
    address: str = "",
    address2: str = "",
    city: str = "",
    state: str = "",
    zip_code: str = "",
    country: str = "",
    contact_name: str = "",
    contact_email: str = "",
    contact_phone: str = "",
    ipsec_udp_port: str = "",
) -> dict:
    """Set appliance extra info, including location, contact, and
    ipsecudp information

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applianceExtraInfo
          - POST
          - /appliance/extraInfo/{nePk}

    :param ne_pk: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_pk: str
    :param address: Street address location, defaults to blank string
    :type address: str, optional
    :param address2: Additional address location info, defaults to blank
        string
    :type address2: str, optional
    :param city: City, defaults to blank string
    :type city: str, optional
    :param state: State, defaults to blank string
    :type state: str, optional
    :param zip_code: Zip code, defaults to blank string
    :type zip_code: str, optional
    :param country: Country, defaults to blank string
    :type country: str, optional
    :param contact_name: Contact person name, defaults to blank string
    :type contact_name: str, optional
    :param contact_email: Contact person email, defaults to blank string
    :type contact_email: str, optional
    :param contact_phone: Contact person phone number, defaults to blank
        string
    :type contact_phone: str, optional
    :param ipsec_udp_port: Port to be used for IPSEC UDP traffic,
        defaults to blank string
    :type ipsec_udp_port: str, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "location": {
            "address": address,
            "address2": address2,
            "city": city,
            "state": state,
            "zipCode": zip_code,
            "country": country,
        },
        "contact": {
            "name": contact_name,
            "email": contact_email,
            "phoneNumber": contact_phone,
        },
    }

    # If IPSEC UDP is specified by user, populate optional section on
    # IPSEC UDP details
    if ipsec_udp_port != "":
        data["overlaySettings"] = {}
        data["overlaySettings"]["ipsecUdpPort"] = ipsec_udp_port
        data["overlaySettings"]["isUserDefinedIPSecUDPPort"] = True

    return self._post(
        "/appliance/extraInfo/{}".format(ne_pk),
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def delete_appliance_extra_info(
    self,
    ne_pk: str,
) -> dict:
    """Delete appliance extra info from appliance, includes location,
    contact, and user-defined ipsecudp information

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - applianceExtraInfo
          - DELETE
          - /appliance/extraInfo/{nePk}

    :param ne_pk: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_pk: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        "/appliance/extraInfo/{}".format(ne_pk),
        expected_status=[204],
        return_type="bool",
    )
