# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# haGroups : High Availability (HA) appliance groups


def get_ha_groups(self) -> dict:
    """Get all appliances paired in HA configuration

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - haGroups
          - GET
          - /haGroups

    :return: Returns dictionary of all HA appliance pairs
    :rtype: dict
    """
    return self._get("/haGroups")


def modify_ha_groups(
    self,
    index_num: int = None,
    ne_pk_1: str = None,
    ne_pk_2: str = None,
    ha_subnet: str = "169.254.1.0/24",
    ha_mask: int = 30,
    ha_vlan_start: int = 100,
    ha_groups: dict = None,
) -> bool:
    """Modify appliances paired in HA configuration.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - haGroups
          - POST
          - /haGroups

    * To modify a single HA pair, use the ``index_num``, ``ne_pk_1``,
      ``ne_pk_2``, ``ha_subnet``, ``ha_mask``, and ``ha_vlant_start``
      parameters.
    * To modify multiple HA pairs at once, only pass a dictionary to
      ``ha_groups`` parameter.

    :param index_num: Index number to identify the HA pair,
        defaults to None
    :type index_num: int, optional
    :param ne_pk_1: Network Primary Key (nePk) of first appliance,
        e.g. ``3.NE``, defaults to None
    :type ne_pk_1: str, optional
    :param ne_pk_2: Network Primary Key (nePk) of second appliance,
        e.g. ``3.NE``, defaults to None
    :type ne_pk_2: str, optional
    :param ha_subnet: Subnet to use for HA connections between
        appliances, default "169.254.1.0/24"
    :type ha_subnet: str, optional
    :param ha_mask: Subnet mask for each HA connection between
        appliances, defaults to 30
    :type ha_mask: int, optional
    :param ha_vlan_start: VLAN number to start for each HA connection
        between appliances, increments per connection, defaults to 100
    :type ha_vlan_start: int, optional
    :param ha_groups: Dictionary of multiple appliance HA pairs,
        defaults to None \n
        * keyword **appliance** (`list[dict]`): Appliance pair,
          identified by dictionary per appliance ne_pk,
          e.g. ``[{"nePk":"3.NE"},{"nePk":"4.NE"}]``
        * keyword **subnet** (`str`): Subnet to be used to allocate IPs
          to internal HA VLAN interfaces, defaults to 169.254.1.0/24.
        * keyword **mask** (`int`): Subnet mask value to be assigned
          to internal HA VLAN interfaces. This value will be used to
          carve out smaller ip blocks from above larger subnet,
          defaults to 30
        * keyword **vlanStart** (`int`): Starting VLAN id value to be
          assigned to internal HA VLAN interfaces. Will increment by 1
          for multiple VLAN interfaces, defaults to 100
    :return: Returns True/False based on successful call.
    :rtype: bool
    """
    if ha_groups is not None:
        data = ha_groups
    else:
        data = {}
        data[index_num] = {
            "appliances": [{"nePk": ne_pk_1}, {"nePk": ne_pk_2}],
            "subnet": ha_subnet,
            "mask": ha_mask,
            "vlanStart": ha_vlan_start,
        }

    return self._post(
        "/haGroups",
        data=data,
        expected_status=[204],
        return_type="bool",
    )
