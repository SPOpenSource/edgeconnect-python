# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# inboundShaper : ECOS inbound bandwidth shaping


def get_appliance_inbound_shaper(
    self,
    ne_id: str,
    cached: bool,
) -> dict:
    """Get inbound shaper settings from Edge Connect appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - inboundShaper
          - GET
          - /inboundShaper/{neId}?cached={cached}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns dictionary of inbound shaper configuration on
        appliance \n
        * keyword **<interface_name>** (`dict`): Interface shaper
          configuration. ``wan`` specifies system WAN shaper. \n
          * keyword **accuracy** (`int`): related to underlying shaper
            credit, not a user-configured parameter
          * keyword **dyn_bw_enable** (`bool`): If dynamic bandwidth
            is configured on interface inbound shaper
          * keyword **enable** (`bool`): If inbound shaper enabled on
            interface
          * keyword **max_bw** (`int`): Maximum bandwidth for interface
            in kbps
          * keyword **traffic-class** (`dict`): Traffic class configs \n
            * keyword **<traffic_class_int>** (`dict`): Config of
              traffic class \n
              * keyword **excess** (`int`): Excess weighting
              * keyword **flow_limit** (`int`): Flow limit
              * keyword **max_bw** (`int`): Percentage max bandwidth
              * keyword **max_bw_abs** (`int`): Absolute max bandwidth
              * keyword **max_wait** (`int`): Max wait time
              * keyword **min_bw** (`int`): Percentage min bandwidth
              * keyword **min_bw_abs** (`int`): Absolute min bandwidth
              * keyword **name** (`str`): Name of traffic class
              * keyword **priority** (`int`): Priority in traffic map
    :rtype: dict
    """
    return self._get("/inboundShaper/{}?cached={}".format(ne_id, cached))
