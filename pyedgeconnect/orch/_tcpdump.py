# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# tcpdump : ECOS Packet capture
from __future__ import annotations


def tcpdump_run(
    self,
    ne_pk_list: list[str],
    max_packet: str = "1000",
    ip: str = None,
    port: str = None,
) -> bool:
    """Start a tcpdump packet capture on list of appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tcpdump
          - POST
          - /tcpdump/run/

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :param max_packet: Maximum number of packets to capture,
        defaults to "1000"
    :type max_packet: str, optional
    :param ip: Filter capture for particular ip address,
        e.g. ``10.1.1.100``, defaults to None
    :type ip: str, optional
    :param port: Filter capture for particular port, e.g. ``443``,
        defaults to None
    :type port: str, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {
        "nePks": ne_pk_list,
        "max_packet": max_packet,
        "ip": ip,
        "port": port,
    }

    return self._post("/tcpdump/run", data=data, return_type="bool")


def tcpdump_status_appliance(
    self,
    ne_id: str,
) -> dict:
    """Get status of tcpdump on specified appliance. Wait a few seconds
    after initiating a tcpdump via tcpdump_run before checking status.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tcpdump
          - GET
          - /tcpdump/status/{neId}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :return: Returns dictionary of tcpdump status \n
        * keyword **active** (`bool`): Indicatates whether packet
          capture process is running
        * keyword **progress** (`float`): Indicatates progress of
          current packet capture as percentage
        * keyword **lastOneDone** (`bool`): Indicatates whether packet
          capture is already finish but still remains in post run
          processing stage
    :rtype: dict
    """
    return self._get("/tcpdump/status/{}".format(ne_id))


def tcpdump_status_all(self) -> str:
    """Get primary keys of all running tcpdumps

    .. note::
        TODO - Testing this call returns a blank string, while the
        Swagger UI returns a string with hash value in the response body

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - tcpdump
          - GET
          - /tcpdump/tcpdumpStatus

    :return: Returns string hash value
    :rtype: str
    """
    return self._get("/tcpdump/tcpdumpStatus", return_type="text")
