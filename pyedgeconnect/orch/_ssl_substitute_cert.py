# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# sslSubstituteCert : ECOS Substitute SSL certificates


def get_appliance_ssl_substitute_certs(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get all SSL substitute certificates on the appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - sslSubstituteCert
          - GET
          - /sslSubstituteCertificate/{neId}?cached={cached}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary of substitute SSL certs on appliance \n
        * keyword **enable** (`dict`): Cert substitution info \n
            * keyword **config** (`dict`): Config info \n
                * keyword **builtin_signing** (`bool`): Status of if
                  built-in certificate signing is enabled on appliance
                * keyword **cert-substitution** (`bool`): Status of if
                  certificate substitution is enabled on appliance
        * keyword **sslcert** (`dict`): SSL Cert info \n
            * keyword **signing** (`dict`): Signing info \n
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
    return self._get(
        "/sslSubstituteCertificate/{}?cached={}".format(ne_id, cached)
    )


def validate_ssl_substitute_cert(
    self,
    cert_data: str,
    is_pfx: bool,
    cert_password: str,
    cert_passphrase: str,
    is_ssl_ca_cert: bool,
) -> dict:
    """Get all SSL substitute certificates on the appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - sslSubstituteCert
          - POST
          - /sslSubstituteCertificate/validation

    :param cert_data: Certificate data
    :type cert_data: str
    :param is_pfx: To specify whether certiciate contains private key
        or not
    :type is_pfx: bool
    :param cert_password: Password for the certificate
    :type cert_password: str
    :param cert_passphrase: Passphrase for the certificate
    :type cert_passphrase: str
    :param is_ssl_ca_cert: Whether the certificate is a CA certificate
    :type is_ssl_ca_cert: bool
    :return: Returns dictionary of substitute SSL cert validation status
    :rtype: dict
    """
    data = {
        "certificateData": cert_data,
        "isPFX": is_pfx,
        "password": cert_password,
        "passPhrase": cert_passphrase,
        "isSslCACert": is_ssl_ca_cert,
    }

    return self._post(
        "/sslSubstituteCertificate/validation",
        data=data,
        expected_status=[204],
    )
