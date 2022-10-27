# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# statistics : Get statistics related information
import requests


def get_appliance_stats_minute_range(self) -> dict:
    """Get the oldest minute and latest minute for which per minute
    statistics are available

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - statistics
          - GET
          - /stats/minuteRange

    Appliance stores statistics for each minute into a file of the
    format: st2-{minute}.tgz. Time is the minute boundary expressed in
    seconds since Jan 1, 1970. This API returns the newest and oldest
    minute timestamps and users can call /stats/minuteStats/:file API to
    retrieve the actual stats. For example:
    GET /stats/minuteStats/st2-1428356220.tgz

    :return: Dictionary of newest and oldest minute stat times \n
        * keyword **newest** (`int`): Epoch seconds timestamp of latest
          available appliance minute data
        * keyword **oldest** (`int`): Epoch seconds timestamp of oldest
          available appliance minute data
    :rtype: dict
    """
    return self._get("/stats/minuteRange")


def get_appliance_stats_minute_file(
    self,
    file: str,
) -> requests.Response:
    """Get specific minute statistics file

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - statistics
          - GET
          - /stats/minuteRange

    Appliance stores statistics for each minute into a file of the
    format: st2-{minute}.tgz. Time is the minute boundary expressed in
    seconds since Jan 1, 1970. For example:
    GET /stats/minuteStats/st2-1428356220.tgz
    Each file is tar and gzip archive of a number of csv files. Each csv
    file has a header which describes the statistics contained in the
    file.

    .. code-block:: python

        import tarfile
        from pyedgeconnect import EdgeConnect
        ec = EdgeConnect(ec_ip)
        ec.login(ec_user,ec_pw)
        stat = ec.get_appliance_stats_minute_file(st2-1428356220.tgz)
        ec.logout()
        if stat.status_code==200:
            with open("stats.tgz",'wb') as stat_file:
                for chunk in stat:
                    stat_file.write(chunk)
        tar = tarfile.open("stats.tgz")
        tar.extractall()

    :param file: Filename of statistics file to download from applinace
    :type file: str
    :return: Download tgz file as part of full response data \n
    :rtype: `requests.Response` object
    """
    return self._get(
        f"/stats/minuteStats/{file}",
        return_type="full_response",
    )


def get_appliance_realtime_stats(
    self,
    stat_type: str,
    stat_name: str,
    stat_filter: str = "",
) -> dict:
    """Get real time per second statistics. This endpoint returns
    varying responses based on the parameters specified in the body.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - statistics
          - POST
          - /stats/realtimeStats

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
    data = {
        "type": stat_type,
        "name": stat_name,
        "filter": stat_filter,
    }

    return self._post(
        "/stats/realtimeStats",
        data=data,
    )
