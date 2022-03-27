# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# ssl : ECOS SSL certificates


def get_appliance_ssl_certs(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get all SSL certificates on appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - ssl
          - GET
          - /ssl/{neId}?cached={cached}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary of config and state of SSL certs on
        appliance \n
        * keyword **config** (`dict`): Config info \n
            * keyword **host** (`dict`): Host info \n
                * keyword **<key_hash_value>** (`dict`): Cert info \n
                    * keyword **cert** (`str`): Certificate information
                    * keyword **self** (`str`): hash value
                    * keyword **key** (`str`): Key information
        * keyword **state** (`dict`): State info \n
            * keyword **host** (`dict`): Host info \n
                * keyword **<key_hash_value>** (`dict`): Cert info \n
                    * keyword **subject** (`str`): The name of the
                      individual, computer, device, or CA to whom the
                      certificate is issued.
                    * keyword **self** (`str`): hash value
                    * keyword **method** (`str`): NEEDS DESCRIPTION
                    * keyword **key_type** (`str`): NEEDS DESCRIPTION
                    * keyword **serial** (`str`): The unique serial
                      number that the issuing certification authority
                      assigns to the certificate,
                    * keyword **id** (`str`): Unique key that identify
                      the cert
                    * keyword **builtin** (`str`): If certificate is
                      builtin on appliance, boolean string,
                      e.g. ``true``
                    * keyword **valid_from** (`str`): The beginning date
                      for the period in which the certificate is valid
                    * keyword **issuer** (`str`): Information regarding
                      the CA that issued the certificate
                    * keyword **pretty** (`str`): NEEDS DESCRIPTION
                    * keyword **valid_to** (`str`): The final date for
                      the period in which the certificate is valid
                    * keyword **verified** (`bool`): Whether certificate
                      is verified or not
    :rtype: dict
    """
    return self._get("/ssl/{}?cached={}".format(ne_id, cached))
