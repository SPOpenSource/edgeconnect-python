# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# location : Lookup the lat/lon of an address


def get_location_coordinates_from_address(
    self,
    address: str,
) -> list:
    """Lookup the latitude and longitude of an address. It will return
    an array of locations that match the object, in the order of the
    locations that match the address the best. So if you're looking for
    the best match, you should use the first element in the array.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - location
          - GET
          - /location/addressToLocation?address={address}

    :param address: Address to find latitude and longitude coordinates,
        e.g. ``3333 Scott Blvd Santa Clara, CA 95054``
    :type address: string
    :return: Returns list of dictionaries of location coordinates \n
        [`dict`]: location object \n
            * keyword **address_components** (`list`): list of
              dictionaries of formatted components of address such as
              street, town, county, full address etc.
            * keyword **formatted_address** (`str`): Full formatted
              address
            * keyword **geometry** (`dict`): multiple lat/long pairs for
              supplied address. There are more keywords that documented
              here, but simplest to retrieve lat long is outlined. \n
                * keyword **location** (`dict`): Lat/Long location \n
                    * keyword **lat** (`float`): Latitude coordinate
                    * keyword **lng** (`float`): Longitude coordinate
    :rtype: list
    """
    return self._get("/location/addressToLocation?address={}".format(address))
