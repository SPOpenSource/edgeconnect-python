# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# timeseriesStats : ECOS time series statistics
from __future__ import annotations


def get_timeseries_stats_appliance_process_state(
    self,
    ne_pk: str,
) -> list:
    """Get time series appliance process state statistics

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - GET
          - /stats/timeseries/applianceProcessState/{nePk}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :return: Returns list of dictionaries
    :rtype: list
    """
    return self._get(
        "/stats/timeseries/applianceProcessState/{}".format(ne_pk)
    )


def get_timeseries_stats_orchestrator_memory(
    self,
    start_time: int,
    end_time: int,
    key: str = None,
) -> list:
    """Get time series memory statistics for Orchestrator

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - GET
          - /stats/timeseries/metrics

    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param key: Swagger docs "For now it should be empty",
        defaults to None
    :type key: str, optional
    :return: Returns list of dictionaries, all memory values are in KB
    :rtype: list
    """
    path = "/stats/timeseries/metrics?startTime={}&endTime={}".format(
        start_time, end_time
    )

    if key is not None:
        path = path + "&key={}".format(key)

    return self._get(path)


def get_timeseries_stats_tunnel_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    tunnel_name: str,
    granularity: str,
    limit: int = None,
    data_format: str = None,
    ip: bool = None,
    latest: int = None,
) -> dict:
    """Get time series tunnel statistics for single appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - GET
          - /stats/timeseries/tunnel/{nePk}

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param tunnel_name: Filter for data which belongs to specified
        tunnel name
    :type tunnel_name: str
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :param limit: Limit the number of stats entity retrieved. When
        unspecified, defaults to 10,000 which is also the maximum
        allowed value, defaults to None
    :type limit: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param ip: ``True`` to use IP address as key to sort results and
        ``False`` or ``None`` to sort by appliance ID, defaults to None
    :type ip: bool, optional
    :param latest: Latest time window to retrieve stats from. Unit is
        minute. e.g. ``10``. Default is to use ``start_time`` and
        ``end_time`` but if ``latest`` is not ``None`` then it takes
        priority, defaults to None
    :type latest: int, optional
    :return: Returns nested dictionary
    :rtype: dict
    """
    path = (
        "/stats/timeseries/tunnel/"
        + "{}?startTime={}&endTime={}&granularity={}&tunnelName={}".format(
            ne_pk, start_time, end_time, granularity, tunnel_name
        )
    )

    if limit is not None:
        path = path + "&limit={}".format(limit)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if latest is not None:
        path = path + "&latest={}".format(latest)

    return self._get(path)


def get_timeseries_stats_appliances(
    self,
    start_time: int,
    end_time: int,
    granularity: str,
    group_pk: str = None,
    traffic_type: str = "all_traffic",
    limit: int = None,
    data_format: str = None,
    ip: bool = None,
    latest: int = None,
) -> dict:
    """Get time series appliance statistics

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - GET
          - /stats/timeseries/appliance

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :param group_pk: Filter by appliance group identifier,
        e.g. ``0.Network`` is root group, ``1.Network`` is internal use,
        ``2.Network`` is auto-discovered groups, ``3.Network`` and
        beyond is user-defined groups, defaults to None
    :type group_pk: str, optional
    :param traffic_type: Filter for data for given traffic type,
        accepted values are ``optimized_traffic``,
        ``pass_through_shaped``, ``pass_through_unshaped``, and
        ``all_traffic``, defaults to None
    :type traffic_type: str, optional
    :param limit: Limit the number of stats entity retrieved. When
        unspecified, defaults to 10,000 which is also the maximum
        allowed value, defaults to None
    :type limit: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param ip: ``True`` to use IP address as key to sort results and
        ``False`` or ``None`` to sort by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param latest: Latest time window to retrieve stats from. Unit is
        minute. e.g. ``10``. Default is to use ``start_time`` and
        ``end_time`` but if ``latest`` is not ``None`` then it takes
        priority, defaults to None
    :type latest: int, optional
    :return: Returns nested dictionary
    :rtype: dict
    """
    path = (
        "/stats/timeseries/appliance?startTime="
        + "{}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if group_pk is not None:
        path = path + "&groupPk={}".format(group_pk)

    path = path + "&trafficType={}".format(traffic_type)

    if limit is not None:
        path = path + "&limit={}".format(limit)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if latest is not None:
        path = path + "&latest={}".format(latest)

    return self._get(path)


def get_timeseries_stats_appliances_ne_pk_list(
    self,
    ne_pk_list: list[str],
    start_time: int,
    end_time: int,
    granularity: str,
    traffic_type: str = "all_traffic",
    limit: int = None,
    data_format: str = None,
    ip: bool = None,
    latest: int = None,
) -> dict:
    """Get time series appliance statistics for list of appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - POST
          - /stats/timeseries/appliance

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :param traffic_type: Filter for data for given traffic type,
        accepted values are "optimized_traffic" "pass_through_shaped"
        "pass_through_unshaped" "all_traffic", defaults to None
    :type traffic_type: str, optional
    :param limit: Limit the number of stats entity retrieved. When
        unspecified, defaults to 10,000 which is also the maximum
        allowed value, defaults to None
    :type limit: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param ip: ``True`` to use IP address as key to sort results and
        ``False`` or ``None`` to sort by appliance ID, defaults to None
    :type ip: bool, optional
    :param latest: Latest time window to retrieve stats from. Unit is
        minute. e.g. ``10``. Default is to use ``start_time`` and
        ``end_time`` but if ``latest`` is not ``None`` then it takes
        priority, defaults to None
    :type latest: int, optional
    :return: Returns nested dictionary
    :rtype: dict
    """
    path = (
        "/stats/timeseries/appliance?startTime="
        + "{}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    path = path + "&trafficType={}".format(traffic_type)

    if limit is not None:
        path = path + "&limit={}".format(limit)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if latest is not None:
        path = path + "&latest={}".format(latest)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_timeseries_stats_appliances_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    granularity: str,
    traffic_type: str = "all_traffic",
    limit: int = None,
    data_format: str = None,
    ip: bool = None,
    latest: int = None,
) -> dict:
    """
    Get time series appliance statistics for single appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - GET
          - /stats/timeseries/appliance/{nePk}

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :param traffic_type: Filter for data for given traffic type,
        accepted values are ``optimized_traffic``,
        ``pass_through_shaped``, ``pass_through_unshaped``, and
        ``all_traffic``, defaults to None
    :type traffic_type: str, optional
    :param limit: Limit the number of stats entity retrieved. When
        unspecified, defaults to 10,000 which is also the maximum
        allowed value, defaults to None
    :type limit: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param ip: ``True`` to use IP address as key to sort results and
        ``False`` or ``None`` to sort by appliance ID, defaults to None
    :type ip: bool, optional
    :param latest: Latest time window to retrieve stats from. Unit is
        minute. e.g. ``10``. Default is to use ``start_time`` and
        ``end_time`` but if ``latest`` is not ``None`` then it takes
        priority, defaults to None
    :type latest: int, optional
    :return: Returns nested dictionary
    :rtype: dict
    """
    path = (
        "/stats/timeseries/appliance/"
        + "{}?startTime={}&endTime={}&granularity={}".format(
            ne_pk, start_time, end_time, granularity
        )
    )

    path = path + "&trafficType={}".format(traffic_type)

    if limit is not None:
        path = path + "&limit={}".format(limit)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if latest is not None:
        path = path + "&latest={}".format(latest)

    return self._get(path)


def get_timeseries_stats_traffic_class(
    self,
    start_time: int,
    end_time: int,
    granularity: str,
    traffic_type: str,
    traffic_class: int,
    group_pk: str = None,
    limit: int = None,
    data_format: str = None,
    ip: bool = None,
    latest: int = None,
) -> dict:
    """Get time series traffic class statistics

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - GET
          - /stats/timeseries/trafficClass

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :param traffic_type: Filter for data for given traffic type,
        accepted values are ``optimized_traffic``,
        ``pass_through_shaped``, ``pass_through_unshaped``, and
        ``all_traffic``
    :type traffic_type: str
    :param traffic_class: Filter for data which belongs to particular
        traffic class, accepted values between 1-10
    :type traffic_class: int
    :param group_pk: Filter by appliance group identifier,
        e.g. ``0.Network`` is root group, ``1.Network`` is internal use,
        ``2.Network`` is auto-discovered groups, ``3.Network`` and
        beyond is user-defined groups, defaults to None
    :type group_pk: str, optional
    :param limit: Limit the number of stats entity retrieved. When
        unspecified, defaults to 10,000 which is also the maximum
        allowed value, defaults to None
    :type limit: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param ip: ``True`` to use IP address as key to sort results and
        ``False`` or ``None`` to sort by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param latest: Latest time window to retrieve stats from. Unit is
        minute. e.g. ``10``. Default is to use ``start_time`` and
        ``end_time`` but if ``latest`` is not ``None`` then it takes
        priority, defaults to None
    :type latest: int, optional
    :return: Returns nested dictionary
    :rtype: dict
    """
    path = (
        "/stats/timeseries/trafficClass?startTime="
        + "{}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if group_pk is not None:
        path = path + "&groupPk={}".format(group_pk)

    path = path + "&trafficType={}".format(traffic_type)
    path = path + "&trafficClass={}".format(traffic_class)

    if limit is not None:
        path = path + "&limit={}".format(limit)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if latest is not None:
        path = path + "&latest={}".format(latest)

    return self._get(path)


def get_timeseries_stats_traffic_class_ne_pk_list(
    self,
    ne_pk_list: list[str],
    start_time: int,
    end_time: int,
    granularity: str,
    traffic_type: str,
    traffic_class: int,
    limit: int = None,
    data_format: str = None,
    ip: bool = None,
    latest: int = None,
) -> dict:
    """Get time series traffic class statistics for list of appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - POST
          - /stats/timeseries/trafficClass

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :param traffic_type: Filter for data for given traffic type,
        accepted values are ``optimized_traffic``,
        ``pass_through_shaped``, ``pass_through_unshaped``, and
        ``all_traffic``
    :type traffic_type: str
    :param traffic_class: Filter for data which belongs to particular
        traffic class, accepted values between 1-10
    :type traffic_class: int
    :param limit: Limit the number of stats entity retrieved. When
        unspecified, defaults to 10,000 which is also the maximum
        allowed value, defaults to None
    :type limit: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param ip: ``True`` to use IP address as key to sort results and
        ``False`` or ``None`` to sort by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param latest: Latest time window to retrieve stats from. Unit is
        minute. e.g. ``10``. Default is to use ``start_time`` and
        ``end_time`` but if ``latest`` is not ``None`` then it takes
        priority, defaults to None
    :type latest: int, optional
    :return: Returns nested dictionary
    :rtype: dict
    """
    path = (
        "/stats/timeseries/trafficClass?startTime="
        + "{}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    path = path + "&trafficType={}".format(traffic_type)
    path = path + "&trafficClass={}".format(traffic_class)

    if limit is not None:
        path = path + "&limit={}".format(limit)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if latest is not None:
        path = path + "&latest={}".format(latest)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_timeseries_stats_traffic_class_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    granularity: str,
    traffic_type: str,
    traffic_class: int,
    limit: int = None,
    data_format: str = None,
    ip: bool = None,
    latest: int = None,
) -> dict:
    """Get time series traffic class statistics for a single appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - GET
          - /stats/timeseries/trafficClass/{nePk}

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :param traffic_type: Filter for data for given traffic type,
        accepted values are ``optimized_traffic``,
        ``pass_through_shaped``, ``pass_through_unshaped``, and
        ``all_traffic``
    :type traffic_type: str
    :param traffic_class: Filter for data which belongs to particular
        traffic class, accepted values between 1-10
    :type traffic_class: int
    :param limit: Limit the number of stats entity retrieved. When
        unspecified, defaults to 10,000 which is also the maximum
        allowed value, defaults to None
    :type limit: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param ip: ``True`` to use IP address as key to sort results and
        ``False`` or ``None`` to sort by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param latest: Latest time window to retrieve stats from. Unit is
        minute. e.g. ``10``. Default is to use ``start_time`` and
        ``end_time`` but if ``latest`` is not ``None`` then it takes
        priority, defaults to None
    :type latest: int, optional
    :return: Returns nested dictionary
    :rtype: dict
    """
    path = (
        "/stats/timeseries/trafficClass?startTime="
        + "{}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    path = path + "&trafficType={}".format(traffic_type)
    path = path + "&trafficClass={}".format(traffic_class)

    if limit is not None:
        path = path + "&limit={}".format(limit)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if latest is not None:
        path = path + "&latest={}".format(latest)

    return self._get(path)


def get_timeseries_stats_flow(
    self,
    start_time: int,
    end_time: int,
    granularity: str,
    group_pk: str = None,
    traffic_type: str = "all_traffic",
    flow_type: str = "TCP_ACCELERATED",
    limit: int = None,
    data_format: str = None,
    ip: bool = None,
    latest: int = None,
) -> dict:
    """Get time series flow statistics

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - GET
          - /stats/timeseries/flow

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :param group_pk: Filter by appliance group identifier,
        e.g. ``0.Network`` is root group, ``1.Network`` is internal use,
        ``2.Network`` is auto-discovered groups, ``3.Network`` and
        beyond is user-defined groups, defaults to None
    :type group_pk: str, optional
    :param traffic_type: Filter for data for given traffic type,
        accepted values are ``optimized_traffic``,
        ``pass_through_shaped``, ``pass_through_unshaped``, and
        ``all_traffic``, defaults to "all_traffic"
    :type traffic_type: str, optional
    :param flow_type: Filter for data belonging to a particular flow
        type, accepted values are ``TCP_ACCELERATED``,
        ``TCP_NON_ACCELERATED``, and ``NON_TCP``,
        defaults to "TCP_ACCELERATED"
    :type flow_type: str, optional
    :param limit: Limit the number of stats entity retrieved. When
        unspecified, defaults to 10,000 which is also the maximum
        allowed value, defaults to None
    :type limit: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param ip: ``True`` to use IP address as key to sort results and
        ``False`` or ``None`` to sort by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param latest: Latest time window to retrieve stats from. Unit is
        minute. e.g. ``10``. Default is to use ``start_time`` and
        ``end_time`` but if ``latest`` is not ``None`` then it takes
        priority, defaults to None
    :type latest: int, optional
    :return: Returns nested dictionary
    :rtype: dict
    """
    path = (
        "/stats/timeseries/flow?startTime="
        + "{}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if group_pk is not None:
        path = path + "&groupPk={}".format(group_pk)

    path = path + "&trafficType={}".format(traffic_type)

    path = path + "&flowType={}".format(flow_type)

    if limit is not None:
        path = path + "&limit={}".format(limit)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if latest is not None:
        path = path + "&latest={}".format(latest)

    return self._get(path)


def get_timeseries_stats_flow_ne_pk_list(
    self,
    ne_pk_list: list[str],
    start_time: int,
    end_time: int,
    granularity: str,
    traffic_type: str = "all_traffic",
    flow_type: str = "TCP_ACCELERATED",
    limit: int = None,
    data_format: str = None,
    ip: bool = None,
    latest: int = None,
) -> dict:
    """Get time series flow statistics for list of appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - POST
          - /stats/timeseries/flow

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :param traffic_type: Filter for data for given traffic type,
        accepted values are ``optimized_traffic``,
        ``pass_through_shaped``, ``pass_through_unshaped``, and
        ``all_traffic``, defaults to "all_traffic"
    :type traffic_type: str
    :param flow_type: Filter for data belonging to a particular flow
        type, accepted values are ``TCP_ACCELERATED``,
        ``TCP_NON_ACCELERATED``, and ``NON_TCP``,
        defaults to "TCP_ACCELERATED"
    :type flow_type: str
    :param limit: Limit the number of stats entity retrieved.
        When unspecified, defaults to 10,000 which is also the maximum
        allowed value, defaults to None
    :type limit: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param ip: ``True`` to use IP address as key to sort results and
        ``False`` or ``None`` to sort by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param latest: Latest time window to retrieve stats from. Unit is
        minute. e.g. ``10``. Default is to use ``start_time`` and
        ``end_time`` but if ``latest`` is not ``None`` then it takes
        priority, defaults to None
    :type latest: int, optional
    :return: Returns nested dictionary
    :rtype: dict
    """
    path = (
        "/stats/timeseries/flow?startTime="
        + "{}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    path = path + "&trafficType={}".format(traffic_type)

    path = path + "&flowType={}".format(flow_type)

    if limit is not None:
        path = path + "&limit={}".format(limit)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if latest is not None:
        path = path + "&latest={}".format(latest)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_timeseries_stats_flow_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    granularity: str,
    traffic_type: str = "all_traffic",
    flow_type: str = "TCP_ACCELERATED",
    limit: int = None,
    data_format: str = None,
    ip: bool = None,
    latest: int = None,
) -> dict:
    """Get time series flow statistics for single appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - GET
          - /stats/timeseries/flow/{nePk}

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :param traffic_type: Filter for data for given traffic type,
        accepted values are ``optimized_traffic``,
        ``pass_through_shaped``, ``pass_through_unshaped``, and
        ``all_traffic``, defaults to "all_traffic"
    :type traffic_type: str
    :param flow_type: Filter for data belonging to a particular flow
        type, accepted values are ``TCP_ACCELERATED``,
        ``TCP_NON_ACCELERATED``, and ``NON_TCP``,
        defaults to "TCP_ACCELERATED"
    :type flow_type: str
    :param limit: Limit the number of stats entity retrieved.
        When unspecified, defaults to 10,000 which is also the maximum
        allowed value, defaults to None
    :type limit: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param ip: ``True`` to use IP address as key to sort results and
        ``False`` or ``None`` to sort by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param latest: Latest time window to retrieve stats from. Unit is
        minute. e.g. ``10``. Default is to use ``start_time`` and
        ``end_time`` but if ``latest`` is not ``None`` then it takes
        priority, defaults to None
    :type latest: int, optional
    :return: Returns nested dictionary
    :rtype: dict
    """
    path = (
        "/stats/timeseries/flow/"
        + "{}?startTime={}&endTime={}&granularity={}".format(
            ne_pk, start_time, end_time, granularity
        )
    )

    path = path + "&trafficType={}".format(traffic_type)

    path = path + "&flowType={}".format(flow_type)

    if limit is not None:
        path = path + "&limit={}".format(limit)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if latest is not None:
        path = path + "&latest={}".format(latest)

    return self._get(path)


def get_timeseries_stats_dscp(
    self,
    start_time: int,
    end_time: int,
    granularity: str,
    dscp: int,
    group_pk: str = None,
    traffic_type: str = "all_traffic",
    limit: int = None,
    data_format: str = None,
    ip: bool = None,
    latest: int = None,
) -> dict:
    """Get time series dscp statistics

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - GET
          - /stats/timeseries/dscp

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :param dscp: Filter for data which belongs to a certain DSCP type,
        valid values are ``0`` through ``63``
    :type dscp: int
    :param group_pk: Filter by appliance group identifier,
        e.g. ``0.Network`` is root group, ``1.Network`` is internal use,
        ``2.Network`` is auto-discovered groups, ``3.Network`` and
        beyond is user-defined groups, defaults to None
    :type group_pk: str
    :param traffic_type: Filter for data for given traffic type,
        accepted values are ``optimized_traffic``,
        ``pass_through_shaped``, ``pass_through_unshaped``, and
        ``all_traffic``, defaults to "all_traffic"
    :type traffic_type: str
    :param limit: Limit the number of stats entity retrieved. When
        unspecified, defaults to 10,000 which is also the maximum
        allowed value, defaults to None
    :type limit: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param ip: ``True`` to use IP address as key to sort results and
        ``False`` or ``None`` to sort by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param latest: Latest time window to retrieve stats from. Unit is
        minute. e.g. ``10``. Default is to use ``start_time`` and
        ``end_time`` but if ``latest`` is not ``None`` then it takes
        priority, defaults to None
    :type latest: int, optional
    :return: Returns nested dictionary
    :rtype: dict
    """
    path = (
        "/stats/timeseries/dscp?startTime="
        + "{}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if group_pk is not None:
        path = path + "&groupPk={}".format(group_pk)

    path = path + "&trafficType={}".format(traffic_type)

    path = path + "&dscp={}".format(dscp)

    if limit is not None:
        path = path + "&limit={}".format(limit)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if latest is not None:
        path = path + "&latest={}".format(latest)

    return self._get(path)


def get_timeseries_stats_dscp_ne_pk_list(
    self,
    ne_pk_list: list[str],
    start_time: int,
    end_time: int,
    granularity: str,
    dscp: int,
    traffic_type: str = "all_traffic",
    limit: int = None,
    data_format: str = None,
    ip: bool = None,
    latest: int = None,
) -> dict:
    """Get time series dscp statistics for list of appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - POST
          - /stats/timeseries/dscp

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :param dscp: Filter for data which belongs to a certain DSCP type,
        accepted values are within the range ``[0,63]``
    :type dscp: int
    :param traffic_type: Filter for data for given traffic type,
        accepted values are ``optimized_traffic``,
        ``pass_through_shaped``, ``pass_through_unshaped``, and
        ``all_traffic``, defaults to "all_traffic"
    :type traffic_type: str
    :param limit: Limit the number of stats entity retrieved. When
        unspecified, defaults to 10,000 which is also the maximum
        allowed value, defaults to None
    :type limit: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param ip: ``True`` to use IP address as key to sort results and
        ``False`` or ``None`` to sort by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param latest: Latest time window to retrieve stats from. Unit is
        minute. e.g. ``10``. Default is to use ``start_time`` and
        ``end_time`` but if ``latest`` is not ``None`` then it takes
        priority, defaults to None
    :type latest: int, optional
    :return: Returns nested dictionary
    :rtype: dict
    """
    path = (
        "/stats/timeseries/dscp?startTime="
        + "{}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    path = path + "&trafficType={}".format(traffic_type)

    path = path + "&dscp={}".format(dscp)

    if limit is not None:
        path = path + "&limit={}".format(limit)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if latest is not None:
        path = path + "&latest={}".format(latest)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_timeseries_stats_dscp_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    granularity: str,
    dscp: int,
    traffic_type: str = "all_traffic",
    limit: int = None,
    data_format: str = None,
    ip: bool = None,
    latest: int = None,
) -> dict:
    """Get time series dscp statistics for single appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - GET
          - /stats/timeseries/dscp/{nePk}

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :param dscp: Filter for data which belongs to a certain DSCP type,
        accepted values are within the range ``[0,63]``
    :type dscp: int
    :param traffic_type: Filter for data for given traffic type,
        accepted values are ``optimized_traffic``,
        ``pass_through_shaped``, ``pass_through_unshaped``, and
        ``all_traffic``, defaults to "all_traffic"
    :type traffic_type: str
    :param limit: Limit the number of stats entity retrieved. When
        unspecified, defaults to 10,000 which is also the maximum
        allowed value, defaults to None
    :type limit: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param ip: ``True`` to use IP address as key to sort results and
        ``False`` or ``None`` to sort by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param latest: Latest time window to retrieve stats from. Unit is
        minute. e.g. ``10``. Default is to use ``start_time`` and
        ``end_time`` but if ``latest`` is not ``None`` then it takes
        priority, defaults to None
    :type latest: int, optional
    :return: Returns nested dictionary
    :rtype: dict
    """
    path = (
        "/stats/timeseries/dscp/"
        + "{}?startTime={}&endTime={}&granularity={}".format(
            ne_pk, start_time, end_time, granularity
        )
    )

    path = path + "&trafficType={}".format(traffic_type)

    path = path + "&dscp={}".format(dscp)

    if limit is not None:
        path = path + "&limit={}".format(limit)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if latest is not None:
        path = path + "&latest={}".format(latest)

    return self._get(path)


def get_timeseries_stats_shaper(
    self,
    start_time: int,
    end_time: int,
    granularity: str,
    traffic_class: int,
    direction: int,
    group_pk: str = None,
    data_format: str = None,
    ip: bool = None,
) -> dict:
    """Get time series shaper statistics

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - GET
          - /stats/timeseries/shaper

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :param traffic_class: Filter for data which belongs to particular
        traffic class, accepted values are within the range ``[1,10]``
    :type traffic_class: int
    :param direction: 0 for Outbound, 1 for inbound
    :type direction: int
    :param group_pk: Filter by appliance group identifier,
        e.g. ``0.Network`` is root group, ``1.Network`` is internal use,
        ``2.Network`` is auto-discovered groups, ``3.Network`` and
        beyond is user-defined groups, defaults to None
    :type group_pk: str, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param ip: ``True`` to use IP address as key to sort results and
        ``False`` or ``None`` to sort by appliance ID,
        defaults to None
    :type ip: bool, optional
    :return: Returns nested dictionary
    :rtype: dict
    """
    path = (
        "/stats/timeseries/shaper?startTime="
        + "{}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if group_pk is not None:
        path = path + "&groupPk={}".format(group_pk)

    path = path + "&trafficClass={}".format(traffic_class)

    path = path + "&direction={}".format(direction)

    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if ip is not None:
        path = path + "&ip={}".format(ip)

    return self._get(path)


def get_timeseries_stats_shaper_ne_pk_list(
    self,
    ne_pk_list: list[str],
    start_time: int,
    end_time: int,
    granularity: str,
    traffic_class: int,
    direction: int,
    data_format: str = None,
    ip: bool = None,
) -> dict:
    """Get time series shaper statistics for list of appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - POST
          - /stats/timeseries/shaper

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :param traffic_class: Filter for data which belongs to particular
        traffic class, accepted values are within the range ``[1,10]``
    :type traffic_class: int
    :param direction: 0 for Outbound, 1 for inbound
    :type direction: int
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param ip: ``True`` to use IP address as key to sort results and
        ``False`` or ``None`` to sort by appliance ID,
        defaults to None
    :type ip: bool, optional
    :return: Returns nested dictionary
    :rtype: dict
    """
    path = (
        "/stats/timeseries/shaper?startTime="
        + "{}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    path = path + "&trafficClass={}".format(traffic_class)

    path = path + "&direction={}".format(direction)

    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if ip is not None:
        path = path + "&ip={}".format(ip)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_timeseries_stats_internal_drops_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    granularity: str,
) -> dict:
    """Get time series internal drops statistics for single appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - GET
          - /stats/timeseries/internalDrops/{nePk}

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :return: Returns nested dictionary
    :rtype: dict
    """
    path = (
        "/stats/timeseries/internalDrops/"
        + "{}?startTime={}&endTime={}&granularity={}".format(
            ne_pk, start_time, end_time, granularity
        )
    )

    return self._get(path)


def get_timeseries_stats_drc(
    self,
    start_time: int,
    end_time: int,
    granularity: str,
    group_pk: str = None,
    limit: int = None,
    data_format: str = None,
    ip: bool = None,
    latest: int = None,
) -> dict:
    """Get time series drc statistics

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - GET
          - /stats/timeseries/drc

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :param group_pk: Filter by appliance group identifier,
        e.g. ``0.Network`` is root group, ``1.Network`` is internal use,
        ``2.Network`` is auto-discovered groups, ``3.Network`` and
        beyond is user-defined groups, defaults to None
    :type group_pk: str, optional
    :param limit: Limit the number of stats entity retrieved. When
        unspecified, defaults to 10,000 which is also the maximum
        allowed value, defaults to None
    :type limit: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param ip: ``True`` to use IP address as key to sort results and
        ``False`` or ``None`` to sort by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param latest: Latest time window to retrieve stats from. Unit is
        minute. e.g. ``10``. Default is to use ``start_time`` and
        ``end_time`` but if ``latest`` is not ``None`` then it takes
        priority, defaults to None
    :type latest: int, optional
    :return: Returns nested dictionary
    :rtype: dict
    """
    path = (
        "/stats/timeseries/drc?startTime="
        + "{}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if group_pk is not None:
        path = path + "&groupPk={}".format(group_pk)
    if limit is not None:
        path = path + "&limit={}".format(limit)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if latest is not None:
        path = path + "&latest={}".format(latest)

    return self._get(path)


def get_timeseries_stats_drc_ne_pk_list(
    self,
    ne_pk_list: list[str],
    start_time: int,
    end_time: int,
    granularity: str,
    limit: int = None,
    data_format: str = None,
    ip: bool = None,
    latest: int = None,
) -> dict:
    """Get time series drc statistics for list of appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - POST
          - /stats/timeseries/drc

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :param limit: Limit the number of stats entity retrieved. When
        unspecified, defaults to 10,000 which is also the maximum
        allowed value, defaults to None
    :type limit: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param ip: ``True`` to use IP address as key to sort results and
        ``False`` or ``None`` to sort by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param latest: Latest time window to retrieve stats from. Unit is
        minute. e.g. ``10``. Default is to use ``start_time`` and
        ``end_time`` but if ``latest`` is not ``None`` then it takes
        priority, defaults to None
    :type latest: int, optional
    :return: Returns nested dictionary
    :rtype: dict
    """
    path = (
        "/stats/timeseries/drc?startTime="
        + "{}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if limit is not None:
        path = path + "&limit={}".format(limit)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if latest is not None:
        path = path + "&latest={}".format(latest)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_timeseries_stats_drc_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    granularity: str,
    tunnel_name: str,
    limit: int = None,
    data_format: str = None,
    ip: bool = None,
    latest: int = None,
) -> dict:
    """Get time series drc statistics for single appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - GET
          - /stats/timeseries/drc/{nePk}

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :param tunnel_name: Filter for data which belongs to specified
        tunnel name
    :type tunnel_name: str
    :param limit: Limit the number of stats entity retrieved. When
        unspecified, defaults to 10,000 which is also the maximum
        allowed value, defaults to None
    :type limit: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param ip: ``True`` to use IP address as key to sort results and
        ``False`` or ``None`` to sort by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param latest: Latest time window to retrieve stats from. Unit is
        minute. e.g. ``10``. Default is to use ``start_time`` and
        ``end_time`` but if ``latest`` is not ``None`` then it takes
        priority, defaults to None
    :type latest: int, optional
    :return: Returns nested dictionary
    :rtype: dict
    """
    path = (
        "/stats/timeseries/drc/"
        + "{}?startTime={}&endTime={}&granularity={}".format(
            ne_pk, start_time, end_time, granularity
        )
    )

    path = path + "&tunnelName={}".format(tunnel_name)

    if limit is not None:
        path = path + "&limit={}".format(limit)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if latest is not None:
        path = path + "&latest={}".format(latest)

    return self._get(path)


def get_timeseries_stats_interface_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    granularity: str,
    traffic_type: str = "all_traffic",
    interface_name: str = None,
    limit: int = None,
) -> list:
    """Get time series interface statistics for single appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - GET
          - /stats/timeseries/interface/{nePk}

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :param traffic_type: Filter for data for given traffic type,
        accepted values are ``optimized_traffic``,
        ``pass_through_shaped``, ``pass_through_unshaped``, and
        ``all_traffic``, defaults to "all_traffic"
    :type traffic_type: str
    :param interface_name: Filter data by interface name,
        defaults to None
    :type interface_name: str, optional
    :param limit: Limit the number of stats entity retrieved. When
        unspecified, defaults to 10,000 which is also the maximum
        allowed value, defaults to None
    :type limit: int, optional
    :return: Returns list of dictionaries
    :rtype: list
    """
    path = (
        "/stats/timeseries/interface/"
        + "{}?startTime={}&endTime={}&granularity={}".format(
            ne_pk, start_time, end_time, granularity
        )
    )

    path = path + "&trafficType={}".format(traffic_type)

    if interface_name is not None:
        path = path + "&interfaceName={}".format(interface_name)
    if limit is not None:
        path = path + "&limit={}".format(limit)

    return self._get(path)


def get_timeseries_stats_interface_overlay_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    granularity: str,
    overlay: str = None,
    tunnel_type: int = None,
    label_id: int = None,
    is_wan_side: bool = None,
    interface_name: str = None,
    limit: int = None,
) -> list:
    """Get time series interface overlay statistics for single appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - GET
          - /stats/timeseries/interfaceOverlay/{nePk}

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :param overlay: When set to ``all``,return all bonded tunnels; when
        set to ``0``, return all physical tunnels; when not used, return
        all bonded and physical tunnels; otherwise, return bonded
        tunnels associated with the specified overlay id,
        defaults to None
    :type overlay: str, optional
    :param tunnel_type: Accepted values for overlays are:
        ``0`` – SD-WAN, ``2`` – Breakout, ``3`` – Services. Accepted
        values for non-overlays are: ``1`` - Underlay, ``2`` –
        Pass-through, and ``3`` – Services, defaults to None
    :type tunnel_type: int, optional
    :param label_id: Label internal id, defaults to None
    :type label_id: int, optional
    :param is_wan_side: True, Get WAN side data or False to get LAN side
        data, defaults to None
    :type is_wan_side: bool, optional
    :param interface_name: Filter data by interface name,
        defaults to None
    :type interface_name: str, optional
    :param limit: Limit the number of stats entity retrieved. When
        unspecified, defaults to 10,000 which is also the maximum
        allowed value, defaults to None
    :type limit: int, optional
    :return: Returns list of dictionaries
    :rtype: list
    """
    path = (
        "/stats/timeseries/interfaceOverlay/"
        + "{}?startTime={}&endTime={}&granularity={}".format(
            ne_pk, start_time, end_time, granularity
        )
    )

    if overlay is not None:
        path = path + "&overlay={}".format(overlay)
    if tunnel_type is not None:
        path = path + "&tunnelType={}".format(tunnel_type)
    if label_id is not None:
        path = path + "&labelId={}".format(label_id)
    if is_wan_side is not None:
        path = path + "&isWanSide={}".format(is_wan_side)
    if interface_name is not None:
        path = path + "&interfaceName={}".format(interface_name)
    if limit is not None:
        path = path + "&limit={}".format(limit)

    return self._get(path)


def get_timeseries_stats_mos_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    granularity: str,
    tunnel_name: str,
    limit: int = None,
) -> list:
    """Get time series MOS statistics for single appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - GET
          - /stats/timeseries/mos/{nePk}

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :param tunnel_name: Filter for data which belongs to tunnel with
        matching name
    :type tunnel_name: str
    :param limit: Limit the number of stats entity retrieved. When
        unspecified, defaults to 10,000 which is also the maximum
        allowed value, defaults to None
    :type limit: int, optional
    :return: Returns list of dictionaries
    :rtype: list
    """
    path = (
        "/stats/timeseries/mos/"
        + "{}?startTime={}&endTime={}&granularity={}".format(
            ne_pk, start_time, end_time, granularity
        )
    )

    path = path + "&tunnel={}".format(tunnel_name)

    if limit is not None:
        path = path + "&limit={}".format(limit)

    return self._get(path)


def get_timeseries_stats_application(
    self,
    start_time: int,
    end_time: int,
    application: str,
    group_pk: str = None,
    data_format: str = None,
    total: bool = None,
    latest: int = None,
) -> dict:
    """Get time series application statistics

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - GET
          - /stats/timeseries/application2

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param application: Filter for data belonging to appliaction with
        matching name
    :type application: str
    :param group_pk: Filter by appliance group identifier,
        e.g. ``0.Network`` is root group, ``1.Network`` is internal use,
        ``2.Network`` is auto-discovered groups, ``3.Network`` and
        beyond is user-defined groups, defaults to None
    :type group_pk: str, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param total: Get application's total value if True,
        defaults to None
    :type total: bool, optional
    :param latest: Latest time window to retrieve stats from. Unit is
        minute. e.g. ``10``. Default is to use ``start_time`` and
        ``end_time`` but if ``latest`` is not ``None`` then it takes
        priority, defaults to None
    :type latest: int, optional
    :return: Returns nested dictionary
    :rtype: dict
    """
    path = (
        "/stats/timeseries/application2?startTime="
        + "{}&endTime={}&application={}".format(
            start_time, end_time, application
        )
    )

    if group_pk is not None:
        path = path + "&groupPk={}".format(group_pk)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if total is not None:
        path = path + "&total={}".format(total)
    if latest is not None:
        path = path + "&latest={}".format(latest)

    return self._get(path)


def get_timeseries_stats_application_ne_pk_list(
    self,
    ne_pk_list: list[str],
    start_time: int,
    end_time: int,
    application: str,
    data_format: str = None,
    total: bool = None,
    latest: int = None,
) -> dict:
    """Get time series application statistics for list of appliances

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - POST
          - /stats/timeseries/application2

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param application: Filter for data belonging to appliaction with
        matching name
    :type application: str
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param total: Get application's total value if True,
        defaults to None
    :type total: bool, optional
    :param latest: Latest time window to retrieve stats from. Unit is
        minute. e.g. ``10``. Default is to use ``start_time`` and
        ``end_time`` but if ``latest`` is not ``None`` then it takes
        priority, defaults to None
    :type latest: int, optional
    :return: Returns nested dictionary
    :rtype: dict
    """
    path = (
        "/stats/timeseries/application2?startTime="
        + "{}&endTime={}&application={}".format(
            start_time, end_time, application
        )
    )

    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if total is not None:
        path = path + "&total={}".format(total)
    if latest is not None:
        path = path + "&latest={}".format(latest)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_timeseries_stats_application_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    application: str,
    total: bool = None,
    data_format: str = None,
) -> dict:
    """Get time series application statistics for single appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - GET
          - /stats/timeseries/application2/{nePk}

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param application: Filter for data belonging to appliaction with
        matching name
    :type application: str
    :param total: Get application's total value if True,
        defaults to None
    :type total: bool, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :return: Returns nested dictionary
    :rtype: dict
    """
    path = (
        "/stats/timeseries/application2/"
        + "{}?startTime={}&endTime={}&application={}".format(
            ne_pk, start_time, end_time, application
        )
    )

    if total is not None:
        path = path + "&total={}".format(total)
    if data_format is not None:
        path = path + "&format={}".format(data_format)

    return self._get(path)


def get_timeseries_stats_boost_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    granularity: str,
    limit: int = None,
) -> list:
    """Get time series boost statistics for single appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - GET
          - /stats/timeseries/boost/{nePk}

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :param limit: Limit the number of stats entity retrieved. When
        unspecified, defaults to 10,000 which is also the maximum
        allowed value, defaults to None
    :type limit: int, optional
    :return: Returns list of dictionaries
    :rtype: list
    """
    path = (
        "/stats/timeseries/boost/"
        + "{}?startTime={}&endTime={}&granularity={}".format(
            ne_pk, start_time, end_time, granularity
        )
    )

    if limit is not None:
        path = path + "&limit={}".format(limit)

    return self._get(path)


def get_timeseries_stats_security_policy_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    granularity: str,
    from_zone: str,
    to_zone: str,
) -> dict:
    """Get time series security policy statistics for single appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - GET
          - /stats/timeseries/securityPolicy/{nePk}

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :param from_zone: Filter for data which come from the zone indicated
        by this zone internal ID
    :type from_zone: str
    :param to_zone:	Filter for data which go to the zone indicated by
        this zone internal ID
    :type to_zone: str
    :return: Returns nested dictionary
    :rtype: dict
    """
    path = (
        "/stats/timeseries/securityPolicy/"
        + "{}?startTime={}&endTime={}".format(ne_pk, start_time, end_time)
        + "&granularity={}&fromZone={}&toZone={}".format(
            granularity, from_zone, to_zone
        )
    )
    return self._get(path)


def get_timeseries_stats_jitter_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    granularity: str,
    tunnel_name: str,
    data_format: str = None,
    limit: int = None,
) -> dict:
    """Get time series security policy statistics for single appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - timeseriesStats
          - GET
          - /stats/timeseries/jitter/{nePk}

    This operation returns a JSON object containing COLUMN_DEF and DATA.
    COLUMN_DEF is an array containing the names indicating what
    corresponding number in data array means. Data objects of each
    appliance is an array of data arrays, each data array contains the
    stats for a particular timestamp. Each number is data array
    corresponds to a name in COLUMN_DEF.
    DATA object contains only values not keys.

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :param tunnel_name: Filter for data which belongs to specified
        tunnel name
    :type tunnel_name: str
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param limit: Limit the number of stats entity retrieved. When
        unspecified, defaults to 10,000 which is also the maximum
        allowed value, defaults to None
    :type limit: int, optional
    :return: Returns nested dictionary
    :rtype: dict
    """
    path = (
        "/stats/timeseries/jitter/"
        + "{}?startTime={}&endTime={}&granularity={}&tunnel={}".format(
            ne_pk, start_time, end_time, granularity, tunnel_name
        )
    )

    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if limit is not None:
        path = path + "&limit={}".format(limit)

    return self._get(path)
