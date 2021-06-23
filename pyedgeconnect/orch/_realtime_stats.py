# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# realtimeStats : ECOS per second statistics


def get_realtime_stats(
    self,
    ne_pk: str,
    stat_type: str,
    stat_name: str,
    stat_filter: str,
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

    * Tunnel stats: Set ``stat_type`` to ``tunnel``. Set ``stat_name``
      to one of the tunnel names or ``pass-through`` or
      ``pass-through-unshaped``. ``stat_filter`` is not used for
      tunnel statistics.
    * TrafficType stats: Set the ``stat_type`` to ``trafficType`` to
      retrieve two aggregate real-time stats: optimized, all-traffic.
      For optimized, set ``stat_name`` to ``0`` and for all-traffic,
      set ``stat_name`` to ``3``. ``stat_filter`` is not used.
    * Application stats: Set ``stat_type`` to ``app``. Set ``stat_name``
      to application name. ``stat_filter`` is required.
    * DSCP stats: Set ``stat_type`` to ``dscp``, set name to one of DSCP
      values from ``0`` to ``63``. ``stat_filter`` is required.
      Possible ``stat_filter`` values are ``0`` for optimized_traffic,
      ``1`` for pass_through_shaped, ``2`` for pass_through_unshaped,
      and ``3`` for all_traffic
    * MOS stats: Set ``stat_name`` to a tunnel id and set ``stat_type``
      to ``tunnel``
    * Traffic Class Stats: set ``stat_type`` to ``trafficClass``, set
      ``stat_name`` to one of traffic classes from ``0`` to ``9``.
      ``stat_filter`` is required.
    * Flow stats: set ``stat_type`` to ``flow``, ``stat_name`` to ``0``
      for TCP accelerated, ``1`` for TCP unaccelerated, and ``2`` for
      non-TCP flows. ``stat_filter`` is required. Accepted values for
      ``stat_filter`` values are ``0`` for optimized_traffic, ``1`` for
      pass_through_shaped, ``2`` for pass_through_unshaped, and ``3``
      for all_traffic
    * Shaper stats: Set ``stat_type`` to ``shaper``. Set ``stat_name``
      to one of traffic classes from ``0`` to ``9``. Use ``stat_filter``
      to specify traffic direction:  ``0`` for Outbound and ``1`` for
      Inbound)
    * Drops stats: Set ``stat_type`` to ``drops``. Set ``stat_name`` to
      empty string.
    * Interface stats: Set ``stat_type`` to ``interface``. Set
      ``stat_name`` to interface name. Use ``stat_filter`` to filter
      traffic type: ``0`` for optimized_traffic, ``1`` for
      pass_through_shaped, ``2`` for pass_through_unshaped, and ``3``
      for all_traffic

    .. note::
      Appliances store per second statistics for three seconds. You must
      poll at a frequency faster than three seconds to make sure to not
      have gaps in the results. The result format for all statistics
      looks like: ``{'nameofstat': [time, value], [time,value],...}``
      where you get statistics for last three seconds.

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param stat_type: Type of statistic to retreive, accepted values
        include ``tunnel``, ``trafficType``, ``app``, ``flow``,
        ``dscp``, ``trafficClass``, ``shaper``, and ``drops``
    :type stat_type: str
    :param stat_name: Name of value to retrieve, accepted values
        dependent on value of param ``type``
    :type stat_name: str
    :param stat_filter: Filter results, accepted values are ``0``,
        ``1``, ``2``, ``3``, functions dependent on value of param
        ``type`` and ``name``
    :type stat_filter: str
    :return: Returns nested dictionary
    :rtype: dict
    """
    data = {"type": stat_type, "name": stat_name, "filter": stat_filter}

    return self._post("/realtimeStats/{}".format(ne_pk), data=data)
