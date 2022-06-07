# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# networkMemory : ECOS erase network memory
from __future__ import annotations


def erase_appliance_network_memory(
    self,
    ne_pk_list: list[str],
    erase: bool,
) -> dict:
    """Get configured hostname of Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - networkMemory
          - POST
          - /networkMemory

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :param erase: ``True`` to erase network memory on specified
        appliances. ``False`` will not erase network memory.
    :return: Returns dictionary with response code and key \n
        * keyword **rc** (`int`): response code, value of ``-32602``
          when ``erase`` is set to ``False``. Value of ``0`` when
          ``erase`` is set to ``True``.
        * keyword **value** (`str`): Will return ``Invalid params`` when
          ``erase`` is set to ``False``. Will return hash key of action
          when ``erase`` is set to ``True``.
    :rtype: dict
    """
    data = {
        "neList": ne_pk_list,
        "erase": erase,
    }

    return self._post("/networkMemory", data=data)
