# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# vrrp : ECOS VRRP configuration


def get_vrrp_interfaes(
    self,
    ne_id: str,
    cached: bool,
) -> list:
    """Get configured vrrp interfaces on appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - vrrp
          - GET
          - /vrrp/{neId}?cached={cached}

    :param ne_id: Appliance id in the format of integer.NE e.g. ``3.NE``
    :type ne_id: str
    :param cached: ``True`` retrieves last known value to Orchestrator,
        ``False`` retrieves values directly from Appliance
    :type cached: bool
    :return: Returns list of dictionaries of VRRP interface
        configurations \n
        [`dict`]: VRRP interface configuration object \n
            * keyword **pkt_trace** (`bool`): Default is ``False``
            * keyword **adv_timer** (`int`): Time interval between
              advertisements. Default is 1 second. Must be between 1-255
            * keyword **preempt** (`bool`): If ``True`` the appliance
              with the highest priority comes back online and again
              assumes primary responsibility. Default is true
            * keyword **holddown** (`int`): Default is ``10``. Must be
              between 1-255
            * keyword **auth** (`str`): Authentication string. Maximum 8
              characters
            * keyword **desc** (`str`): Description string. Maximum 64
              characters
            * keyword **enable** (`str`): Enable/Disable the VRRP
              instance, valid options are ``Up`` or ``Down``
            * keyword **priority** (`int`): The greater the number, the
              higher the priority. The appliance with the higher
              priority is the VRRP Master. Must be between 1-254
            * keyword **vipaddr** (`str`): Must be valid ip address and
              not match any of the existing interface ips on the
              appliance
            * keyword **interface** (`str`): Name of interface that VRRP
              is using for peering. Eg. ``wan0``
            * keyword **groupId** (`int`): Identifier assigned to the
              two peers. Depending on the deployment, the group can
              consist of an appliance and a router (or L3 switch), or
              two appliances. Must be between 1-255
            * keyword **mode** (`str`): There are three options for the
              VRRP instance - Backup : Instance is in VRRP backup state.
              Init : Instance is initializing, it's disabled, or the
              interface is down. Master : Instance is the current VRRP
              master
            * keyword **master_transitions** (`int`): Number of times
              the VRRP instance went from Master to Backup and vice
              versa. A high number of transitions indicates a
              problematic VRRP configuration or environment. If this is
              the case, check the configuration of all local appliances
              and routers, and review the log files
            * keyword **masterip** (`str`): Current VRRP Master's
              Interface or local IP address
            * keyword **uptime** (`str`): Time elapsed since the VRRP
              instance entered the state it's in.
              Sample format: ``0 days 11 hrs 49 mins 41 secs``
            * keyword **vipowner** (`bool`): An Edge Connect appliance
              cannot use one of its own IP addresses as the VRRP IP, so
              this will always be ``False``
            * keyword **vmac** (`str`): MAC Address that the VRRP
              instance is using. On an NX Appliance, this is in
              00-00-5E-00-01-{VRID} format. On virtual appliances, the
              VRRP instance uses the interface's assigned MAC Address
              (for example, the MAC address that the hypervisor assigned
              to wan0)
    :rtype: list
    """
    return self._get("/vrrp/{}?cached={}".format(ne_id, cached))
