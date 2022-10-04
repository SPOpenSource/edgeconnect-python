# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# realtimeStats : ECOS per second statistics


def get_realtime_stats(
    self,
    ne_pk: str,
    stat_type: str,
    stat_name: str,
    stat_filter: str = "",
) -> dict:
    """Get real time statistics from appliance based on query parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - realtimeStats
          - POST
          - /realtimeStats/{nePk}


    .. note::

        Appliances store per second statistics for only 3 seconds. You
        must poll at a frequency faster than 3 seconds to not have gaps
        in the results when trying to collect continious values.


    * For **Tunnel stats**: Set ``stat_type`` to ``tunnel`` and set
      ``stat_name`` to one of the tunnel names or ``pass-through`` or
      ``pass-through-unshaped``. ``stat_filter`` is not used for tunnel
      statistics.

    * For **TrafficType stats**: Set the ``stat_type`` to
      ``trafficType`` to retrieve two aggregate real-time stats:
      optimized and all-traffic. For optimized, set ``stat_name`` to
      ``0`` and for all-traffic, set ``stat_name`` to ``3``.
      ``stat_filter`` is not used.

    * For **Application stats**: Set ``stat_type`` to ``app``. Set
      ``stat_name`` to application name. ``stat_filter`` is required.
      Accepted values are ``0`` for optimized traffic, ``1`` for
      passthrough shaped, ``2`` for passthrough unshaped, and ``3`` for
      all traffic.

    * For **DSCP stats**: Set ``stat_type`` to ``dscp``, set
      ``stat_name`` to one of DSCP values from ``0`` to ``63``.
      ``stat_filter`` is required. Accepted values are ``0`` for
      optimized traffic, ``1`` for passthrough shaped, ``2`` for
      passthrough unshaped, and ``3`` for all traffic.

    * For **Traffic Class Stats**: set ``stat_type`` to 'trafficClass',
      set ``stat_name`` to one of traffic classes from ``0`` to ``9``.
      ``stat_filter`` is required. Accepted values are ``0`` for
      optimized traffic, ``1`` for passthrough shaped, ``2`` for
      passthrough unshaped, and ``3`` for all traffic.

    * For **Flow stats**: set type to ``flow``, name to ``0`` for TCP
      accelerated, ``1`` for TCP unaccelerated and ``2`` for non-TCP
      flows. ``3`` for all traffic. ``stat_filter`` is required.
      Accepted values are ``0`` for optimized traffic, ``1`` for
      passthrough shaped, ``2`` for passthrough unshaped, and ``3``
      for all traffic.

    * For **Shaper stats**: Set ``stat_type`` to ``shaper``. Set
      ``stat_name`` to one of traffic classes from ``0`` to ``9``.
      ``stat_filter`` to traffic direction, ``0`` for Outbound and ``1``
      for Inbound.

    * For **Drops stats**: Set ``stat_type`` to ``drops``. Set
      ``stat_name`` to empty string

    * For **Interface stats**: set type to ``interface``, and
      ``stat_name`` to interface name. Use ``stat_filter`` to filter
      traffic type, ``0`` for optimized traffic, ``1`` for
      passthrough shaped, ``2`` for passthrough unshaped, and ``3``
      for all traffic.

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param stat_type: Category/Type of statistics to retrieve, accepted
      values included ``tunnel``, ``trafficType``, ``app``, ``flow``,
      ``dscp``, ``trafficClass``, ``shaper``, ``drops``, and
      ``interface``
    :type stat_type: str
    :param stat_name: Name of value to retrieve, accepted values
      dependent on value of param ``stat_type``
    :type stat_name: str
    :param stat_filter: Required for certain stat types, accepted values
      are ``0``, ``1``, ``2``, ``3``, function of which is dependent
      on value of ``stat_type`` and ``stat_name``, defaults to ""
    :type stat_filter: str, optional
    :return: Dictionary of realtime stats for specified parameters \n
        * keyword **<name_of_stat>** (`list`): 3 second stat object,
          number of keys varies based on stat type queried \n
          * [`list`]: First second list of stat timestamp and value \n
            * [0] (`int`): Epoch timestamp in microseconds
            * [1] (`int`): Stat value, unit dependent on stat type
          * [`list`]: Second second list of stat timestamp and value \n
            * [0] (`int`): Epoch timestamp in microseconds
            * [1] (`int`): Stat value, unit dependent on stat type
          * [`list`]: Third second list of stat timestamp and value \n
            * [0] (`int`): Epoch timestamp in microseconds
            * [1] (`int`): Stat value, unit dependent on stat type
    :rtype: dict
    """
    data = {"type": stat_type, "name": stat_name, "filter": stat_filter}

    return self._post("/realtimeStats/{}".format(ne_pk), data=data)
