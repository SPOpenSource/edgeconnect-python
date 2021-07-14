# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# customCerts : Custom CA Certificate Trust Store


def get_custom_certs(self) -> list:
    """Returns list of custom CA certificates from Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - customCerts
          - GET
          - /customCert

    :return: Returns list of custom certificates in Orchestrator \n
        * keyword **alias** (`str`): Alias used to identify the CA
          Certificate
        * keyword **key** (`str`): The CA Certificate
        * keyword **lastUpdatedTimestamp** (`str`): The timestamp of the
          last time the CA Certificate was updated in Orchestrator
        * keyword **expiration** (`str`): CA Certificate's expiration
          date
        * keyword **issuer** (`str`): CA Certificate's issuer
        * keyword **issuedTo** (`str`): CA Certificate's issued to
    :rtype: list
    """
    return self._get("/customCert")


def update_custom_certs(
    self,
    alias: str,
    key: str,
    expiration: str,
    issuer: str,
    issued_to: str,
    last_timestamp: str = "",
) -> bool:
    """Add new or update existing custom CA certificate

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - customCerts
          - POST
          - /customCert

    :param alias: Alias used to identify the CA Certificate
    :type alias: str
    :param key: The CA Certificate
    :type key: str
    :param expiration: CA Certificate's expiration date
    :type expiration: str
    :param issuer: CA Certificate's issuer
    :type issuer: str
    :param issued_to: CA Certificate's issued to
    :type issued_to: str
    :param last_timestamp: The timestamp of the last time the CA
        Certificate was updated in Orchestrator
    :type last_timestamp: str, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "alias": alias,
        "key": key,
        "lastUpdatedTimestamp": last_timestamp,
        "expiration": expiration,
        "issuer": issuer,
        "issuedTo": issued_to,
    }

    return self._post(
        "/customCert",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def delete_custom_cert(
    self,
    alias: str,
) -> bool:
    """Delete custom CA certificate

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - customCerts
          - DELETE
          - /customCert/{alias}

    :param alias: Alias used to identify the CA Certificate
    :type alias: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        "/customCert/{}".format(alias),
        expected_status=[204],
        return_type="bool",
    )


def get_custom_certs_enabled(self) -> dict:
    """Returns whether or not Orchestrator is currently using custom CA
    certificate trust store

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - customCerts
          - GET
          - /customCert/enable

    :return: Returns dictionary of custom certificates status \n
        * keyword **enabled** (`bool`): ``True`` if custom CA
          certificate trust store is in use, ``False`` if not in use
    :rtype: dict
    """
    return self._get("/customCert/enable")


def set_custom_certs_enabled(
    self,
    enabled: bool,
) -> dict:
    """Enable or disable custom CA certificate trust store

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - customCerts
          - POST
          - /customCert/enable

    :param enabled: Set to ``True`` to enable use of custom CA
      certificates trust store, ``False`` to use default certificates
      trust store
    :type enabled: bool
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {"Enabled": enabled}

    return self._post(
        "/customCert/enable",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def check_custom_certs_orchestrator_to_portal(
    self,
    custom_certs: bool,
) -> dict:
    """Checks whether Orchestrator can connect to Portal using the
    default or custom CA certificates

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - customCerts
          - GET
          - /customCert/orchestratorConnectivity/{custom}

    :return: TBD
    :rtype: TBD
    """
    return self._get(
        "/customCert/orchestratorConnectivity/{}".format(custom_certs)
    )


def check_custom_certs_appliances_to_portal(
    self,
    custom_certs: bool,
) -> dict:
    """Checks whether appliances can connect to Portal and Orchestrator
    using the default or custom CA certificates

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - customCerts
          - GET
          - /customCert/applianceConnectivity/{custom}

    :return: TBD
    :rtype: TBD
    """
    return self._get(
        "/customCert/applianceConnectivity/{}".format(custom_certs)
    )


def verify_custom_cert(
    self,
    alias: str,
    key: str,
    expiration: str,
    issuer: str,
    issued_to: str,
    last_timestamp: str = "",
) -> bool:
    """Verify the custom CA certificate

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - customCerts
          - POST
          - /customCert/verify

    :param alias: Alias used to identify the CA Certificate
    :type alias: str
    :param key: The CA Certificate
    :type key: str
    :param expiration: CA Certificate's expiration date
    :type expiration: str
    :param issuer: CA Certificate's issuer
    :type issuer: str
    :param issued_to: CA Certificate's issued to
    :type issued_to: str
    :param last_timestamp: The timestamp of the last time the CA
        Certificate was updated in Orchestrator
    :type last_timestamp: str, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "alias": alias,
        "key": key,
        "lastUpdatedTimestamp": last_timestamp,
        "expiration": expiration,
        "issuer": issuer,
        "issuedTo": issued_to,
    }

    return self._post(
        "/customCert/verify",
        data=data,
        expected_status=[204],
        return_type="bool",
    )
