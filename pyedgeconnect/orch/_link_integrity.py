# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# linkIntegrity : Link integrity and bandwidth test


def get_link_integrity_test_result(
    self,
    ne_id: str,
) -> dict:
    """Retrieve current link integrity test status/results from
    appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - linkIntegrity
          - GET
          - /linkIntegrityTest/status/{neId}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :return: Returns dictionary of test status and related results
    :rtype: dict
    """
    return self._get("/linkIntegrityTest/status/{}".format(ne_id))


def link_integrity_test(
    self,
    ne_pk_1: str,
    bandwidth_1: str,
    path_1: str,
    ne_pk_2: str,
    bandwidth_2: str,
    path_2: str,
    duration: int,
    test_program: str,
    dscp: str = "any",
) -> bool:
    """Start a link integrity test between two appliances using
    specified parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - linkIntegrity
          - POST
          - /linkIntegrityTest/run

    :param ne_pk_1: Network Primary Key (nePk) of first appliance
    :type ne_pk_1: str
    :param bandwidth_1: Data transfer rate to use from first appliance
    :type bandwidth_1: str
    :param path_1: Traffic path for first appliance. Can have values of
        "pass-through", "pass-through-unshaped" or "{tunnelID}"
        e.g. "tunnel_1".
    :type path_1: str
    :param ne_pk_2: Network Primary Key (nePk) of second appliance
    :type ne_pk_2: str
    :param bandwidth_2: Data transfer rate to use from second appliance
    :type bandwidth_2: str
    :param path_2: Traffic path for first appliance. Can have values of
        "pass-through", "pass-through-unshaped" or "{tunnelID}"
        e.g. "tunnel_1".
    :type path_2: str
    :param duration: Duration of test in seconds
    :type duration: int
    :param test_program: Test program to be used for this test. Can have
        values of "iperf" or "tcpperf"
    :type test_program: str
    :param dscp: DSCP value for test traffic, defaults to "any"
    :type dscp: str, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "appA": {"nePk": ne_pk_1, "bandwidth": bandwidth_1, "path": path_1},
        "appB": {"nePk": ne_pk_2, "bandwidth": bandwidth_2, "path": path_2},
        "duration": duration,
        "testProgram": test_program,
        "DSCP": dscp,
    }

    return self._post("/linkIntegrityTest/run", data=data, return_type="bool")
