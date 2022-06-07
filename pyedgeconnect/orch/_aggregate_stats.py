# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# aggregateStats : ECOS aggregate statistics
from __future__ import annotations


def get_aggregate_stats_tunnels(
    self,
    start_time: int,
    end_time: int,
    granularity: str,
    group_pk: str = None,
    ip: bool = None,
    metric: str = None,
    top: int = None,
    overlay: str = None,
    data_format: str = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate tunnel stats data filter by query parameters.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/tunnel

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
        ``2.Network`` is auto-discovered groups. ``3.Network`` and
        beyond is user-defined groups, defaults to None
    :type group_pk: str, optional
    :param ip: ``True`` to use IP address as key to sort results or
        ``False`` or ``None`` for default sorting by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param metric: Sort stats by the provided metric, can also be used
        with the param 'top' to limit number of items received,
        e.g. ``throughput``, defaults to None
    :type metric: str, optional
        :param top: This parameter should be provided together with
        param ``metric`` to indicate top x items of a metric. e.g. if
        ``metric`` is set to ``throughput`` and ``top`` is ``10``,
        retrieves top 10 tunnels by throughput, defaults to None
    :type top: int, optional
    :param overlay: When set to ``all``,return all bonded tunnels; when
        set to ``0``,return all physical tunnels; when not used, return
        all bonded and physical tunnels; otherwise,return bonded tunnels
        associated with the specified overlay id, defaults to None
    :type overlay: str, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/tunnel?"
        + "startTime={}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if group_pk is not None:
        path = path + "&groupPk={}".format(group_pk)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if metric is not None:
        path = path + "&metric={}".format(metric)
    if top is not None:
        path = path + "&top={}".format(top)
    if overlay is not None:
        path = path + "&overlay={}".format(overlay)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if group_by_ne is not None:
        path = path + "&groupByNE={}".format(group_by_ne)

    return self._get(path)


def get_aggregate_stats_tunnels_ne_pk_list(
    self,
    ne_pk_list: list[str],
    start_time: int,
    end_time: int,
    granularity: str,
    ip: bool = None,
    metric: str = None,
    top: int = None,
    overlay: str = None,
    data_format: str = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate tunnel stats data filter by query parameters.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats/aggregate/tunnel

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
    :param ip: ``True`` to use IP address as key to sort results or
        ``False`` or ``None`` for default sorting by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param metric: Sort stats by the provided metric, can also be used
        with the param 'top' to limit number of items received,
        e.g. ``throughput``, defaults to None
    :type metric: str, optional
        :param top: This parameter should be provided together with
        param ``metric`` to indicate top x items of a metric. e.g. if
        ``metric`` is set to ``throughput`` and ``top`` is ``10``,
        retrieves top 10 tunnels by throughput, defaults to None
    :type top: int, optional
    :param overlay: When set to ``all``,return all bonded tunnels; when
        set to ``0``,return all physical tunnels; when not used, return
        all bonded and physical tunnels; otherwise,return bonded tunnels
        associated with the specified overlay id, defaults to None
    :type overlay: str, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/tunnel?"
        + "startTime={}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if ip is not None:
        path = path + "&ip={}".format(ip)
    if metric is not None:
        path = path + "&metric={}".format(metric)
    if top is not None:
        path = path + "&top={}".format(top)
    if overlay is not None:
        path = path + "&overlay={}".format(overlay)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if group_by_ne is not None:
        path = path + "&groupByNE={}".format(group_by_ne)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_aggregate_stats_tunnels_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    granularity: str,
    tunnel_name: str = None,
    ip: bool = None,
    metric: str = None,
    top: int = None,
    overlay: str = None,
    data_format: str = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate tunnel stats data for a single appliance filter by
    query parameters.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/tunnel/{nePk}

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
    :param tunnel_name: Filter response data for specified tunnel name,
        defaults to None
    :type tunnel_name: str, optional
    :param ip: ``True`` to use IP address as key to sort results or
        ``False`` or ``None`` for default sorting by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param metric: Sort stats by the provided metric, can also be used
        with the param 'top' to limit number of items received,
        e.g. ``throughput``, defaults to None
    :type metric: str, optional
    :param top: This parameter should be provided together with param
        ``metric`` to indicate top x items of a metric. e.g. if
        ``metric`` is set to ``throughput`` and ``top`` is ``10``,
        retrieves top 10 tunnels by throughput, defaults to None
    :type top: int, optional
    :param overlay: When set to ``all``,return all bonded tunnels; when
        set to ``0``,return all physical tunnels; when not used, return
        all bonded and physical tunnels; otherwise,return bonded tunnels
        associated with the specified overlay id, defaults to None
    :type overlay: str, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/tunnel/"
        + "{}?startTime={}&endTime={}&granularity={}".format(
            ne_pk, start_time, end_time, granularity
        )
    )

    if tunnel_name is not None:
        path = path + "&tunnelName={}".format(tunnel_name)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if metric is not None:
        path = path + "&metric={}".format(metric)
    if top is not None:
        path = path + "&top={}".format(top)
    if overlay is not None:
        path = path + "&overlay={}".format(overlay)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if group_by_ne is not None:
        path = path + "&groupByNE={}".format(group_by_ne)

    return self._get(path)


def get_aggregate_stats_appliances(
    self,
    start_time: int,
    end_time: int,
    granularity: str,
    group_pk: str = None,
    traffic_type: str = None,
    ip: bool = None,
    metric: str = None,
    top: int = None,
    overlay: str = None,
    data_format: str = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate appliance stats data filter by query parameters.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/appliance

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
        ``2.Network`` is auto-discovered groups. ``3.Network`` and
        beyond is user-defined groups, defaults to None
    :type group_pk: str, optional
    :param traffic_type: Filter for data for given traffic type,
        accepted values are ``optimized_traffic``,
        ``pass_through_shaped``, ``pass_through_unshaped``, and
        ``all_traffic``, defaults to None
    :type traffic_type: str, optional
    :param ip: ``True`` to use IP address as key to sort results or
        ``False`` or ``None`` for default sorting by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param metric: Sort stats by the provided metric, can also be used
        with the param 'top' to limit number of items received,
        e.g. ``throughput``, defaults to None
    :type metric: str, optional
    :param top: This parameter should be provided together with param
        ``metric`` to indicate top x items of a metric. e.g. if
        ``metric`` is set to ``throughput`` and ``top`` is ``10``,
        retrieves top 10 tunnels by throughput, defaults to None
    :type top: int, optional
    :param overlay: When set to ``all``,return all bonded tunnels; when
        set to ``0``,return all physical tunnels; when not used, return
        all bonded and physical tunnels; otherwise,return bonded tunnels
        associated with the specified overlay id, defaults to None
    :type overlay: str, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/appliance?"
        + "startTime={}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if group_pk is not None:
        path = path + "&groupPk={}".format(group_pk)
    if traffic_type is not None:
        path = path + "&trafficType={}".format(traffic_type)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if metric is not None:
        path = path + "&metric={}".format(metric)
    if top is not None:
        path = path + "&top={}".format(top)
    if overlay is not None:
        path = path + "&overlay={}".format(overlay)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if group_by_ne is not None:
        path = path + "&groupByNE={}".format(group_by_ne)

    return self._get(path)


def get_aggregate_stats_appliances_ne_pk_list(
    self,
    ne_pk_list: list[str],
    start_time: int,
    end_time: int,
    granularity: str,
    traffic_type: str = None,
    ip: bool = None,
    metric: str = None,
    top: int = None,
    overlay: str = None,
    data_format: str = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate appliance stats data filter by query parameters.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats/aggregate/appliance

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
        ``all_traffic``, defaults to None
    :type traffic_type: str, optional
    :param ip: ``True`` to use IP address as key to sort results or
        ``False`` or ``None`` for default sorting by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param metric: Sort stats by the provided metric, can also be used
        with the param 'top' to limit number of items received,
        e.g. ``throughput``, defaults to None
    :type metric: str, optional
    :param top: This parameter should be provided together with param
        ``metric`` to indicate top x items of a metric. e.g. if
        ``metric`` is set to ``throughput`` and ``top`` is ``10``,
        retrieves top 10 tunnels by throughput, defaults to None
    :type top: int, optional
    :param overlay: When set to ``all``,return all bonded tunnels; when
        set to ``0``,return all physical tunnels; when not used, return
        all bonded and physical tunnels; otherwise,return bonded tunnels
        associated with the specified overlay id, defaults to None
    :type overlay: str, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/appliance?"
        + "startTime={}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if traffic_type is not None:
        path = path + "&trafficType={}".format(traffic_type)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if metric is not None:
        path = path + "&metric={}".format(metric)
    if top is not None:
        path = path + "&top={}".format(top)
    if overlay is not None:
        path = path + "&overlay={}".format(overlay)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if group_by_ne is not None:
        path = path + "&groupByNE={}".format(group_by_ne)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_aggregate_stats_appliances_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    granularity: str,
    traffic_type: str = None,
    ip: bool = None,
    metric: str = None,
    top: int = None,
    overlay: str = None,
    data_format: str = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate appliance stats data for a single appliance filter
    by query parameters.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/appliance/{nePk}

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
    :param ip: ``True`` to use IP address as key to sort results or
        ``False`` or ``None`` for default sorting by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param metric: Sort stats by the provided metric, can also be used
        with the param 'top' to limit number of items received,
        e.g. ``throughput``, defaults to None
    :type metric: str, optional
    :param top: This parameter should be provided together with param
        ``metric`` to indicate top x items of a metric. e.g. if
        ``metric`` is set to ``throughput`` and ``top`` is ``10``,
        retrieves top 10 tunnels by throughput, defaults to None
    :type top: int, optional
    :param overlay: When set to ``all``,return all bonded tunnels; when
        set to ``0``,return all physical tunnels; when not used, return
        all bonded and physical tunnels; otherwise,return bonded tunnels
        associated with the specified overlay id, defaults to None
    :type overlay: str, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/appliance/"
        + "{}?startTime={}&endTime={}&granularity={}".format(
            ne_pk, start_time, end_time, granularity
        )
    )

    if traffic_type is not None:
        path = path + "&trafficType={}".format(traffic_type)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if metric is not None:
        path = path + "&metric={}".format(metric)
    if top is not None:
        path = path + "&top={}".format(top)
    if overlay is not None:
        path = path + "&overlay={}".format(overlay)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if group_by_ne is not None:
        path = path + "&groupByNE={}".format(group_by_ne)

    return self._get(path)


def get_aggregate_stats_applications(
    self,
    start_time: int,
    end_time: int,
    group_pk: str = None,
    application: str = None,
    top: int = None,
    data_format: str = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate application stats data filter by query parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/application2

    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param group_pk: Filter by appliance group identifier,
        e.g. ``0.Network`` is root group, ``1.Network`` is internal use,
        ``2.Network`` is auto-discovered groups. ``3.Network`` and
        beyond is user-defined groups, defaults to None
    :type group_pk: str, optional
    :param application: Filter for data belonging to appliaction with
        matching name, defaults to None
    :type application: str, optional
    :param top: Return top x applications by throughput. e.g., if
        ``10`` is provided, retrieve top 10 applications by throughput,
        defaults to None
    :type top: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = "/stats/aggregate/application2?" + "startTime={}&endTime={}".format(
        start_time,
        end_time,
    )

    if group_pk is not None:
        path = path + "&groupPk={}".format(group_pk)
    if application is not None:
        path = path + "&application={}".format(application)
    if top is not None:
        path = path + "&top={}".format(top)
    if top is not None:
        path = path + "&top={}".format(top)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if group_by_ne is not None:
        path = path + "&groupByNE={}".format(group_by_ne)

    return self._get(path)


def get_aggregate_stats_applications_ne_pk_list(
    self,
    ne_pk_list: list[str],
    start_time: int,
    end_time: int,
    application: str = None,
    top: int = None,
    data_format: str = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate application stats data filter by query parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats/aggregate/application2

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
        matching name, defaults to None
    :type application: str, optional
    :param top: Return top x applications by throughput. e.g., if
        ``10`` is provided, retrieve top 10 applications by throughput,
        defaults to None
    :type top: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = "/stats/aggregate/application2?" + "startTime={}&endTime={}".format(
        start_time,
        end_time,
    )

    if application is not None:
        path = path + "&application={}".format(application)
    if top is not None:
        path = path + "&top={}".format(top)
    if top is not None:
        path = path + "&top={}".format(top)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if group_by_ne is not None:
        path = path + "&groupByNE={}".format(group_by_ne)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_aggregate_stats_applications_single_appliance(
    self,
    ne_pk: str,
    ne_pk_list: list[str],
    start_time: int,
    end_time: int,
    application: str = None,
    top: int = None,
    overlay: str = None,
    data_format: str = None,
) -> dict:
    """Get aggregate application stats data filter by query parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/application2/{nePk}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
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
        matching name, defaults to None
    :type application: str, optional
    :param top: Return top x applications by throughput. e.g., if
        ``10`` is provided, retrieve top 10 applications by throughput,
        defaults to None
    :type top: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/application2/"
        + "{}?startTime={}&endTime={}".format(
            ne_pk,
            start_time,
            end_time,
        )
    )

    if application is not None:
        path = path + "&application={}".format(application)
    if top is not None:
        path = path + "&top={}".format(top)
    if top is not None:
        path = path + "&top={}".format(top)
    if data_format is not None:
        path = path + "&format={}".format(data_format)

    return self._get(path)


def get_aggregate_stats_traffic_class(
    self,
    start_time: int,
    end_time: int,
    granularity: str,
    group_pk: str = None,
    traffic_class: int = None,
    traffic_type: str = None,
    ip: bool = None,
    metric: str = None,
    top: int = None,
    data_format: str = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate traffic class stats data filter by query parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/trafficClass

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
        ``2.Network`` is auto-discovered groups. ``3.Network`` and
        beyond is user-defined groups, defaults to None
    :type group_pk: str, optional
    :param traffic_class: Filter for data which belongs to particular
        traffic class, accepted values between 1-10, defaults to None
    :type traffic_class: int, optional
    :param traffic_type: Filter for data for given traffic type,
        accepted values are ``optimized_traffic``,
        ``pass_through_shaped``, ``pass_through_unshaped``, and
        ``all_traffic``, defaults to None
    :type traffic_type: str, optional
    :param ip: ``True`` to use IP address as key to sort results or
        ``False`` or ``None`` for default sorting by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param metric: Sort stats by the provided metric, can also be used
        with the param 'top' to limit number of items received,
        e.g. ``throughput``, defaults to None
    :type metric: str, optional
    :param top: This parameter should be provided together with param
        ``metric`` to indicate top x items of a metric. e.g. if
        ``metric`` is set to ``throughput`` and ``top`` is ``10``,
        retrieves top 10 tunnels by throughput, defaults to None
    :type top: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/trafficClass?"
        + "startTime={}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if group_pk is not None:
        path = path + "&groupPk={}".format(group_pk)
    if traffic_class is not None:
        path = path + "&trafficClass={}".format(traffic_class)
    if traffic_type is not None:
        path = path + "&trafficType={}".format(traffic_type)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if metric is not None:
        path = path + "&metric={}".format(metric)
    if top is not None:
        path = path + "&top={}".format(top)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if group_by_ne is not None:
        path = path + "&groupByNE={}".format(group_by_ne)

    return self._get(path)


def get_aggregate_stats_traffic_class_ne_pk_list(
    self,
    ne_pk_list: list[str],
    start_time: int,
    end_time: int,
    granularity: str,
    traffic_class: int = None,
    traffic_type: str = None,
    ip: bool = None,
    metric: str = None,
    top: int = None,
    data_format: str = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate traffic class stats data filter by query parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats/aggregate/trafficClass

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
        traffic class, accepted values between 1-10, defaults to None
    :type traffic_class: int, optional
    :param traffic_type: Filter for data for given traffic type,
        accepted values are ``optimized_traffic``,
        ``pass_through_shaped``, ``pass_through_unshaped``, and
        ``all_traffic``, defaults to None
    :type traffic_type: str, optional
    :param ip: ``True`` to use IP address as key to sort results or
        ``False`` or ``None`` for default sorting by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param metric: Sort stats by the provided metric, can also be used
        with the param 'top' to limit number of items received,
        e.g. ``throughput``, defaults to None
    :type metric: str, optional
    :param top: This parameter should be provided together with param
        ``metric`` to indicate top x items of a metric. e.g. if
        ``metric`` is set to ``throughput`` and ``top`` is ``10``,
        retrieves top 10 tunnels by throughput, defaults to None
    :type top: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/trafficClass?"
        + "startTime={}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if traffic_class is not None:
        path = path + "&trafficClass={}".format(traffic_class)
    if traffic_type is not None:
        path = path + "&trafficType={}".format(traffic_type)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if metric is not None:
        path = path + "&metric={}".format(metric)
    if top is not None:
        path = path + "&top={}".format(top)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if group_by_ne is not None:
        path = path + "&groupByNE={}".format(group_by_ne)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_aggregate_stats_traffic_class_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    granularity: str,
    traffic_class: int = None,
    traffic_type: str = None,
    ip: bool = None,
    metric: str = None,
    top: int = None,
    data_format: str = None,
) -> dict:
    """Get aggregate trafficClass stats data for a single appliance
    filter by query parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/trafficClass/{nePk}

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
    :param traffic_class: Filter for data which belongs to particular
        traffic class, accepted values between 1-10, defaults to None
    :type traffic_class: int, optional
    :param traffic_type: Filter for data for given traffic type,
        accepted values are ``optimized_traffic``,
        ``pass_through_shaped``, ``pass_through_unshaped``, and
        ``all_traffic``, defaults to None
    :type traffic_type: str, optional
    :param ip: ``True`` to use IP address as key to sort results or
        ``False`` or ``None`` for default sorting by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param metric: Sort stats by the provided metric, can also be used
        with the param 'top' to limit number of items received,
        e.g. ``throughput``, defaults to None
    :type metric: str, optional
    :param top: This parameter should be provided together with param
        ``metric`` to indicate top x items of a metric. e.g. if
        ``metric`` is set to ``throughput`` and ``top`` is ``10``,
        retrieves top 10 tunnels by throughput, defaults to None
    :type top: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/trafficClass/"
        + "{}?startTime={}&endTime={}&granularity={}".format(
            ne_pk, start_time, end_time, granularity
        )
    )

    if traffic_class is not None:
        path = path + "&trafficClass={}".format(traffic_class)
    if traffic_type is not None:
        path = path + "&trafficType={}".format(traffic_type)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if metric is not None:
        path = path + "&metric={}".format(metric)
    if top is not None:
        path = path + "&top={}".format(top)
    if data_format is not None:
        path = path + "&format={}".format(data_format)

    return self._get(path)


def get_aggregate_stats_flows(
    self,
    start_time: int,
    end_time: int,
    granularity: str,
    group_pk: str = None,
    flow: str = None,
    traffic_type: str = None,
    ip: bool = None,
    data_format: str = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate flow stats data filter by query parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/flow

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
        ``2.Network`` is auto-discovered groups. ``3.Network`` and
        beyond is user-defined groups, defaults to None
    :type group_pk: str, optional
    :param flow: Filter for data of a particular flow type. Accepted
        values are "TCP_ACCELERATED" "TCP_NOT_ACCELERATED" "NON_TCP",
        defaults to None
    :type flow: str, optional
    :param traffic_type: Filter for data for given traffic type,
        accepted values are ``optimized_traffic``,
        ``pass_through_shaped``, ``pass_through_unshaped``, and
        ``all_traffic``, defaults to None
    :type traffic_type: str, optional
    :param ip: ``True`` to use IP address as key to sort results or
        ``False`` or ``None`` for default sorting by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/flow?startTime="
        + "{}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if group_pk is not None:
        path = path + "&groupPk={}".format(group_pk)
    if flow is not None:
        path = path + "&flow={}".format(flow)
    if traffic_type is not None:
        path = path + "&trafficType={}".format(traffic_type)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if group_by_ne is not None:
        path = path + "&groupByNE={}".format(group_by_ne)

    return self._get(path)


def get_aggregate_stats_flows_ne_pk_list(
    self,
    ne_pk_list: list[str],
    start_time: int,
    end_time: int,
    granularity: str,
    group_pk: str = None,
    flow: str = None,
    traffic_type: str = None,
    ip: bool = None,
    data_format: str = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate flow stats data filter by query parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats/aggregate/flow

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
    :param group_pk: Filter by appliance group identifier,
        e.g. ``0.Network`` is root group, ``1.Network`` is internal use,
        ``2.Network`` is auto-discovered groups. ``3.Network`` and
        beyond is user-defined groups, defaults to None
    :type group_pk: str, optional
    :param flow: Filter for data of a particular flow type. Accepted
        values are "TCP_ACCELERATED" "TCP_NOT_ACCELERATED" "NON_TCP",
        defaults to None
    :type flow: str, optional
    :param traffic_type: Filter for data for given traffic type,
        accepted values are ``optimized_traffic``,
        ``pass_through_shaped``, ``pass_through_unshaped``, and
        ``all_traffic``, defaults to None
    :type traffic_type: str, optional
    :param ip: ``True`` to use IP address as key to sort results or
        ``False`` or ``None`` for default sorting by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/flow?startTime="
        + "{}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if group_pk is not None:
        path = path + "&groupPk={}".format(group_pk)
    if flow is not None:
        path = path + "&flow={}".format(flow)
    if traffic_type is not None:
        path = path + "&trafficType={}".format(traffic_type)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if group_by_ne is not None:
        path = path + "&groupByNE={}".format(group_by_ne)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_aggregate_stats_active_flows(
    self,
    ne_pk_list: list[str],
    top: int = None,
) -> dict:
    """Get active flow counts by NE id

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats/aggregate/flow/active

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :param top: Top number of flows to return, defaults to None
    :type top: int, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = "/stats/aggregate/flow/active"

    if top is not None:
        path = path + "&top={}".format(top)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_aggregate_stats_flows_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    granularity: str,
    traffic_class: int = None,
    flow: str = None,
    ip: str = None,
    data_format: str = None,
) -> dict:
    """Get aggregate flow stats data for a single appliance filter by
    query parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/flow/{nePk}

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
    :param traffic_class: Filter for data which belongs to particular
        traffic class, accepted values between 1-10, defaults to None
    :type traffic_class: int, optional
    :param flow: Filter for data of a particular flow type. Accepted
        values are "TCP_ACCELERATED" "TCP_NOT_ACCELERATED" "NON_TCP",
        defaults to None
    :type flow: str, optional
    :param ip: ``True`` to use IP address as key to sort results or
        ``False`` or ``None`` for default sorting by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/flow/"
        + "{}?startTime={}&endTime={}&granularity={}".format(
            ne_pk, start_time, end_time, granularity
        )
    )

    if traffic_class is not None:
        path = path + "&trafficClass={}".format(traffic_class)
    if flow is not None:
        path = path + "&flow={}".format(flow)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if data_format is not None:
        path = path + "&format={}".format(data_format)

    return self._get(path)


def get_aggregate_stats_dscp(
    self,
    start_time: int,
    end_time: int,
    granularity: str,
    group_pk: str = None,
    dscp: int = None,
    traffic_type: str = None,
    ip: bool = None,
    metric: str = None,
    top: int = None,
    data_format: str = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate traffic class stats data filter by query parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/dscp

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
        ``2.Network`` is auto-discovered groups. ``3.Network`` and
        beyond is user-defined groups, defaults to None
    :type group_pk: str, optional
    :param dscp: Filter for data which belongs to a certain flow type.
        Valid values are 0-63, defaults to None
    :type dscp: int, optional
    :param traffic_type: Filter for data for given traffic type,
        accepted values are ``optimized_traffic``,
        ``pass_through_shaped``, ``pass_through_unshaped``, and
        ``all_traffic``, defaults to None
    :type traffic_type: str, optional
    :param ip: ``True`` to use IP address as key to sort results or
        ``False`` or ``None`` for default sorting by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param metric: Sort stats by the provided metric, can also be used
        with the param 'top' to limit number of items received,
        e.g. ``throughput``, defaults to None
    :type metric: str, optional
    :param top: This parameter should be provided together with param
        ``metric`` to indicate top x items of a metric. e.g. if
        ``metric`` is set to ``throughput`` and ``top`` is ``10``,
        retrieves top 10 tunnels by throughput, defaults to None
    :type top: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/dscp?"
        + "startTime={}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if group_pk is not None:
        path = path + "&groupPk={}".format(group_pk)
    if dscp is not None:
        path = path + "&dscp={}".format(dscp)
    if traffic_type is not None:
        path = path + "&trafficType={}".format(traffic_type)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if metric is not None:
        path = path + "&metric={}".format(metric)
    if top is not None:
        path = path + "&top={}".format(top)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if group_by_ne is not None:
        path = path + "&groupByNE={}".format(group_by_ne)

    return self._get(path)


def get_aggregate_stats_dscp_ne_pk_list(
    self,
    ne_pk_list: list[str],
    start_time: int,
    end_time: int,
    granularity: str,
    dscp: int = None,
    traffic_type: str = None,
    ip: bool = None,
    metric: str = None,
    top: int = None,
    data_format: str = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate traffic class stats data filter by query parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats/aggregate/dscp

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
    :param dscp: Filter for data which belongs to a certain flow type.
        Valid values are 0-63, defaults to None
    :type dscp: int, optional
    :param traffic_type: Filter for data for given traffic type,
        accepted values are ``optimized_traffic``,
        ``pass_through_shaped``, ``pass_through_unshaped``, and
        ``all_traffic``, defaults to None
    :type traffic_type: str, optional
    :param ip: ``True`` to use IP address as key to sort results or
        ``False`` or ``None`` for default sorting by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param metric: Sort stats by the provided metric, can also be used
        with the param 'top' to limit number of items received,
        e.g. ``throughput``, defaults to None
    :type metric: str, optional
    :param top: This parameter should be provided together with param
        ``metric`` to indicate top x items of a metric. e.g. if
        ``metric`` is set to ``throughput`` and ``top`` is ``10``,
        retrieves top 10 tunnels by throughput, defaults to None
    :type top: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/dscp?"
        + "startTime={}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if dscp is not None:
        path = path + "&dscp={}".format(dscp)
    if traffic_type is not None:
        path = path + "&trafficType={}".format(traffic_type)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if metric is not None:
        path = path + "&metric={}".format(metric)
    if top is not None:
        path = path + "&top={}".format(top)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if group_by_ne is not None:
        path = path + "&groupByNE={}".format(group_by_ne)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_aggregate_stats_dscp_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    traffic_type: str,
    granularity: str,
    group_pk: str = None,
    dscp: int = None,
    traffic_class: int = None,
    ip: bool = None,
    metric: str = None,
    top: int = None,
    data_format: str = None,
) -> dict:
    """Get aggregate dscp stats data for a single appliance filter by
    query parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/dscp/{nePk}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param traffic_type: Filter for data for given traffic type,
        accepted values are ``optimized_traffic``,
        ``pass_through_shaped``, ``pass_through_unshaped``, and
        ``all_traffic``
    :type traffic_type: str
    :param granularity: Data granularity filtering whether data is
        minutely data, hourly data or daily data. Accepted values are
        ``minute``, ``hour``, and ``day``
    :type granularity: str
    :param group_pk: Filter by appliance group identifier,
        e.g. ``0.Network`` is root group, ``1.Network`` is internal use,
        ``2.Network`` is auto-discovered groups. ``3.Network`` and
        beyond is user-defined groups, defaults to None
    :type group_pk: str, optional
    :param dscp: Filter for data which belongs to a certain flow type.
        Valid values are 0-63, defaults to None
    :type dscp: int, optional
    :param traffic_class: Filter for data which belongs to particular
        traffic class, accepted values between 1-10, defaults to None
    :type traffic_class: int, optional
    :param ip: ``True`` to use IP address as key to sort results or
        ``False`` or ``None`` for default sorting by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param metric: Sort stats by the provided metric, can also be used
        with the param 'top' to limit number of items received,
        e.g. ``throughput``, defaults to None
    :type metric: str, optional
    :param top: This parameter should be provided together with param
        ``metric`` to indicate top x items of a metric. e.g. if
        ``metric`` is set to ``throughput`` and ``top`` is ``10``,
        retrieves top 10 tunnels by throughput, defaults to None
    :type top: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/dscp/"
        + "{}?startTime={}&endTime={}&trafficType={}&".format(
            ne_pk, start_time, end_time, traffic_type
        )
        + "granularity={}".format(granularity)
    )

    if traffic_class is not None:
        path = path + "&trafficClass={}".format(traffic_class)
    if dscp is not None:
        path = path + "&dscp={}".format(dscp)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if metric is not None:
        path = path + "&metric={}".format(metric)
    if top is not None:
        path = path + "&top={}".format(top)
    if data_format is not None:
        path = path + "&format={}".format(data_format)

    return self._get(path)


def get_aggregate_stats_dns_ne_pk_list(
    self,
    ne_pk_list: list[str],
    start_time: int,
    end_time: int,
    is_source: int = None,
    split_type: int = None,
    top: int = None,
    split_by_ne: bool = None,
    group_by: str = None,
    group_by_subdomains: int = None,
) -> dict:
    """Get aggregate dns stats data filter by query parameters.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats/aggregate/dns

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param is_source: Integer value representing whether dns is from
        source or destination. 0 for source, 1 for destination,
        defaults to None
    :type is_source: int, optional
    :param split_type: Filter data for specific type, 0 for 'http',
        1 for 'https', 2 for 'unassigned' and 3 for 'others,
        defaults to None
    :type split_type: int, optional
    :param top: Return top x rows of data, defaults to None
    :type top: int, optional
    :param split_by_ne: ``True`` to split aggregate stats by appliance,
        if ``True``, there will be an extra level of key inside each
        stats object indicating what appliance the inner stats object
        belongs to, defaults to None
    :type split_by_ne: bool, optional
    :param group_by: Group the data based on this value, default
        behavior if unspecified is to group by dns, defaults to None
    :type group_by: str, optional
    :param group_by_subdomains: Group the data based on the number of
        subdomains, if unspecified the default value is 2,
        defaults to None
    :type group_by_subdomains: int, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = "/stats/aggregate/dns?startTime={}&endTime={}".format(
        start_time,
        end_time,
    )

    if is_source is not None:
        path = path + "&isSource={}".format(is_source)
    if split_type is not None:
        path = path + "&splitType={}".format(split_type)
    if top is not None:
        path = path + "&top={}".format(top)
    if split_by_ne is not None:
        path = path + "&splitByNe={}".format(split_by_ne)
    if group_by is not None:
        path = path + "&groupBy={}".format(group_by)
    if group_by_subdomains is not None:
        path = path + "&groupBySubdomains={}".format(group_by_subdomains)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_aggregate_stats_dns_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    is_source: int = None,
    split_type: int = None,
    top: int = None,
    split_by_ne: bool = None,
    group_by: str = None,
    group_by_subdomains: int = None,
) -> dict:
    """Get aggregate dns stats data for a single appliance filter by
    query parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats/aggregate/dns/{nePk}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param is_source: Integer value representing whether dns is from
        source or destination. 0 for source, 1 for destination,
        defaults to None
    :type is_source: int, optional
    :param split_type: Filter data for specific type, 0 for 'http',
        1 for 'https', 2 for 'unassigned' and 3 for 'others,
        defaults to None
    :type split_type: int, optional
    :param top: Return top x rows of data, defaults to None
    :type top: int, optional
    :param split_by_ne: ``True`` to split aggregate stats by appliance,
        if ``True``, there will be an extra level of key inside each
        stats object indicating what appliance the inner stats object
        belongs to, defaults to None
    :type split_by_ne: bool, optional
    :param group_by: Group the data based on this value, default
        behavior if unspecified is to group by dns, defaults to None
    :type group_by: str, optional
    :param group_by_subdomains: Group the data based on the number of
        subdomains, if unspecified the default value is 2,
        defaults to None
    :type group_by_subdomains: int, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = "/stats/aggregate/dns/{}?startTime={}&endTime={}".format(
        ne_pk,
        start_time,
        end_time,
    )

    if is_source is not None:
        path = path + "&isSource={}".format(is_source)
    if split_type is not None:
        path = path + "&splitType={}".format(split_type)
    if top is not None:
        path = path + "&top={}".format(top)
    if split_by_ne is not None:
        path = path + "&splitByNe={}".format(split_by_ne)
    if group_by is not None:
        path = path + "&groupBy={}".format(group_by)
    if group_by_subdomains is not None:
        path = path + "&groupBySubdomains={}".format(group_by_subdomains)

    return self._get(path)


def get_aggregate_stats_ports_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    is_source: int = None,
    is_known: int = None,
    protocol: int = None,
    port: int = None,
    top: int = None,
    split_by_ne: bool = None,
    last_hour: bool = None,
) -> dict:
    """Get aggregate ports stats data for a single appliance filter by
    query parameters.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/ports/{nePk}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param is_source: 0 to specifiy port as source port, 1 to specifiy
        port as destination port, defaults to None
    :type is_source: int, optional
    :param is_known: 1 to specify if port is assigned to an application,
        0 if not, defaults to None
    :type is_known: int, optional
    :param protocol: Integer value representing protocol used by port,
        defaults to None
    :type protocol: int, optional
    :param port: Integer value of port number, defaults to None
    :type port: int, optional
    :param top: Number of rows to return from query, defaults to None
    :type top: int, optional
    :param split_by_ne: ``True`` to split aggregate stats by appliance,
        if ``True``, there will be an extra level of key inside each
        stats object indicating what appliance the inner stats object
        belongs to, defaults to None
    :type split_by_ne: bool, optional
    :param last_hour: If ``True``, fetch data one hour behind from last
        hour if no data within last hour range, defaults to None
    :type last_hour: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = "/stats/aggregate/ports/{}?startTime={}&endTime={}".format(
        ne_pk,
        start_time,
        end_time,
    )

    if is_source is not None:
        path = path + "&isSource={}".format(is_source)
    if is_known is not None:
        path = path + "&isKnown={}".format(is_known)
    if protocol is not None:
        path = path + "&protocol={}".format(protocol)
    if port is not None:
        path = path + "&port={}".format(port)
    if top is not None:
        path = path + "&top={}".format(top)
    if split_by_ne is not None:
        path = path + "&splitByNe={}".format(split_by_ne)
    if last_hour is not None:
        path = path + "&lastHour={}".format(last_hour)

    return self._get(path)


def get_aggregate_stats_ports(
    self,
    start_time: int,
    end_time: int,
    is_source: int = None,
    is_known: int = None,
    protocol: int = None,
    port: int = None,
    top: int = None,
    split_by_ne: bool = None,
    last_hour: bool = None,
    data_format: str = None,
) -> dict:
    """Get aggregate ports stats data filter by query parameters.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/ports

    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param is_source: 0 to specifiy port as source port, 1 to specifiy
        port as destination port, defaults to None
    :type is_source: int, optional
    :param is_known: 1 to specify if port is assigned to an application,
        0 if not, defaults to None
    :type is_known: int, optional
    :param protocol: Integer value representing protocol used by port,
        defaults to None
    :type protocol: int, optional
    :param port: Integer value of port number, defaults to None
    :type port: int, optional
    :param top: Number of rows to return from query, defaults to None
    :type top: int, optional
    :param split_by_ne: ``True`` to split aggregate stats by appliance,
        if ``True``, there will be an extra level of key inside each
        stats object indicating what appliance the inner stats object
        belongs to, defaults to None
    :type split_by_ne: bool, optional
    :param last_hour: If ``True``, fetch data one hour behind from last
        hour if no data within last hour range, defaults to None
    :type last_hour: bool, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = "/stats/aggregate/ports?startTime={}&endTime={}".format(
        start_time,
        end_time,
    )

    if is_source is not None:
        path = path + "&isSource={}".format(is_source)
    if is_known is not None:
        path = path + "&isKnown={}".format(is_known)
    if protocol is not None:
        path = path + "&protocol={}".format(protocol)
    if port is not None:
        path = path + "&port={}".format(port)
    if top is not None:
        path = path + "&top={}".format(top)
    if split_by_ne is not None:
        path = path + "&splitByNe={}".format(split_by_ne)
    if last_hour is not None:
        path = path + "&lastHour={}".format(last_hour)
    if data_format is not None:
        path = path + "&format={}".format(data_format)

    return self._get(path)


def get_aggregate_stats_ports_ne_pk_list(
    self,
    ne_pk_list: list[str],
    start_time: int,
    end_time: int,
    is_source: int = None,
    is_known: int = None,
    protocol: int = None,
    port: int = None,
    top: int = None,
    split_by_ne: bool = None,
    last_hour: bool = None,
) -> dict:
    """Get aggregate ports stats data filter by query parameters.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats/aggregate/ports

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param is_source: 0 to specifiy port as source port, 1 to specifiy
        port as destination port, defaults to None
    :type is_source: int, optional
    :param is_known: 1 to specify if port is assigned to an application,
        0 if not, defaults to None
    :type is_known: int, optional
    :param protocol: Integer value representing protocol used by port,
        defaults to None
    :type protocol: int, optional
    :param port: Integer value of port number, defaults to None
    :type port: int, optional
    :param top: Number of rows to return from query, defaults to None
    :type top: int, optional
    :param split_by_ne: ``True`` to split aggregate stats by appliance,
        if ``True``, there will be an extra level of key inside each
        stats object indicating what appliance the inner stats object
        belongs to, defaults to None
    :type split_by_ne: bool, optional
    :param last_hour: If ``True``, fetch data one hour behind from last
        hour if no data within last hour range, defaults to None
    :type last_hour: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = "/stats/aggregate/ports?startTime={}&endTime={}".format(
        start_time,
        end_time,
    )

    if is_source is not None:
        path = path + "&isSource={}".format(is_source)
    if is_known is not None:
        path = path + "&isKnown={}".format(is_known)
    if protocol is not None:
        path = path + "&protocol={}".format(protocol)
    if port is not None:
        path = path + "&port={}".format(port)
    if top is not None:
        path = path + "&top={}".format(top)
    if split_by_ne is not None:
        path = path + "&splitByNe={}".format(split_by_ne)
    if last_hour is not None:
        path = path + "&lastHour={}".format(last_hour)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_aggregate_stats_top_talkers(
    self,
    start_time: int,
    end_time: int,
    top: int = None,
    split_by_ne: bool = None,
    data_format: str = None,
) -> dict:
    """Get aggregate topTalkers stats data filter by query parameters.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/topTalkers

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param top: Number of rows to return from query, defaults to None
    :type top: int, optional
    :param split_by_ne: ``True`` to split aggregate stats by appliance,
        if ``True``, there will be an extra level of key inside each
        stats object indicating what appliance the inner stats object
        belongs to, defaults to None
    :type split_by_ne: bool, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = "/stats/aggregate/topTalkers?startTime={}&endTime={}".format(
        start_time,
        end_time,
    )

    if top is not None:
        path = path + "&top={}".format(top)
    if split_by_ne is not None:
        path = path + "&splitByNe={}".format(split_by_ne)
    if data_format is not None:
        path = path + "&format={}".format(data_format)

    return self._get(path)


def get_aggregate_stats_top_talkers_ne_pk_list(
    self,
    ne_pk_list: list[str],
    start_time: int,
    end_time: int,
    top: int = None,
    split_by_ne: bool = None,
    data_format: str = None,
) -> dict:
    """Get aggregate topTalkers stats data filter by query parameters.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats/aggregate/topTalkers

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param top: Number of rows to return from query, defaults to None
    :type top: int, optional
    :param split_by_ne: ``True`` to split aggregate stats by appliance,
        if ``True``, there will be an extra level of key inside each
        stats object indicating what appliance the inner stats object
        belongs to, defaults to None
    :type split_by_ne: bool, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = "/stats/aggregate/topTalkers?startTime={}&endTime={}".format(
        start_time,
        end_time,
    )

    if top is not None:
        path = path + "&top={}".format(top)
    if split_by_ne is not None:
        path = path + "&splitByNe={}".format(split_by_ne)
    if data_format is not None:
        path = path + "&format={}".format(data_format)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_aggregate_stats_top_talkers_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    top: int = None,
) -> dict:
    """Get aggregate topTalkers stats data for a single appliance filter
    by query parameters.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/topTalkers/{nePk}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param top: Number of rows to return from query, defaults to None
    :type top: int, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = "/stats/aggregate/topTalkers/{}?startTime={}&endTime={}".format(
        ne_pk,
        start_time,
        end_time,
    )

    if top is not None:
        path = path + "&top={}".format(top)

    return self._get(path)


def get_aggregate_stats_top_talkers_split_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    source_ip: str = None,
) -> dict:
    """Get aggregate topTalkers stats data for a single appliance filter
    by query parameters.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/topTalkers/split/{nePk}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param source_ip: Filter source IP address, defaults to None
    :type source_ip: str, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/topTalkers/split/"
        + "{}?startTime={}&endTime={}".format(
            ne_pk,
            start_time,
            end_time,
        )
    )

    if source_ip is not None:
        path = path + "&sourceIp={}".format(source_ip)

    return self._get(path)


def get_aggregate_stats_traffic_behavior(
    self,
    start_time: int,
    end_time: int,
    group_pk: str = None,
    behavioral_cat: str = None,
    data_format: str = None,
) -> dict:
    """Get aggregate Traffic Behavioral stats data filter by query
    parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/trafficBehavior

    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param group_pk: Filter by appliance group identifier,
        e.g. ``0.Network`` is root group, ``1.Network`` is internal use,
        ``2.Network`` is auto-discovered groups. ``3.Network`` and
        beyond is user-defined groups, defaults to None
    :type group_pk: str, optional
    :param behavioral_cat: Filter for data which belongs to behavioral
        category in query, defaults to None
    :type behavioral_cat: str, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = "/stats/aggregate/trafficBehavior?startTime={}&endTime={}".format(
        start_time,
        end_time,
    )

    if group_pk is not None:
        path = path + "&groupPk={}".format(group_pk)
    if behavioral_cat is not None:
        path = path + "&behavioralCate={}".format(behavioral_cat)
    if data_format is not None:
        path = path + "&format={}".format(data_format)

    return self._get(path)


def get_aggregate_stats_traffic_behavior_ne_pk_list(
    self,
    ne_pk_list: list[str],
    start_time: int,
    end_time: int,
    behavioral_cat: str = None,
    application: str = None,
    data_format: str = None,
    top: int = None,
    last_hour: bool = None,
    is_aggregated: bool = None,
) -> dict:
    """Get aggregate Traffic Behavioral stats data filter by query
    parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats/aggregate/trafficBehavior

    :param ne_pk_list: List of one or more appliance Network Primary
        Keys (nePk), e.g. ``["3.NE","5.NE"]``
    :type ne_pk_list: list[str]
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param behavioral_cat: Filter for data which belongs to behavioral
        category in query, defaults to None
    :type behavioral_cat: str, optional
    :param application: Filter for data belonging to appliaction with
        matching name, defaults to None
    :type application: str, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param top: Restrict applications for each behavior category to
        top N, defaults to None
    :type top: int, optional
    :param last_hour: If ``True``, fetch data one hour behind from last
        hour if no data within last hour range, defaults to None
    :type last_hour: bool, optional
    :param is_aggregated: If ``True``, get aggregate traffic behavioral
        stats data, defaults to None
    :type is_aggregated: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = "/stats/aggregate/trafficBehavior?startTime={}&endTime={}".format(
        start_time,
        end_time,
    )

    if behavioral_cat is not None:
        path = path + "&behavioralCate={}".format(behavioral_cat)
    if application is not None:
        path = path + "&application={}".format(application)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if top is not None:
        path = path + "&top={}".format(top)
    if last_hour is not None:
        path = path + "&lastHour={}".format(last_hour)
    if is_aggregated is not None:
        path = path + "&isAggregated={}".format(is_aggregated)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_aggregate_stats_traffic_behavior_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    behavioral_cat: str = None,
    application: str = None,
    top: int = None,
    last_hour: bool = None,
) -> dict:
    """Get aggregate Traffic Behavioral stats data for a single
    appliance filter by query parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/trafficBehavior/{nePk}

    :param ne_pk: Network Primary Key (nePk) of appliance, e.g. ``3.NE``
    :type ne_pk: str
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param behavioral_cat: Filter for data which belongs to behavioral
        category in query, defaults to None
    :type behavioral_cat: str, optional
    :param application: Filter for data belonging to appliaction with
        matching name, defaults to None
    :type application: str, optional
    :param top: Restrict applications for each behavior category to
        top N, defaults to None
    :type top: int, optional
    :param last_hour: If ``True``, fetch data one hour behind from last
        hour if no data within last hour range, defaults to None
    :type last_hour: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/trafficBehavior/"
        + "{}?startTime={}&endTime={}".format(
            ne_pk,
            start_time,
            end_time,
        )
    )

    if behavioral_cat is not None:
        path = path + "&behavioralCate={}".format(behavioral_cat)
    if application is not None:
        path = path + "&application={}".format(application)
    if top is not None:
        path = path + "&top={}".format(top)
    if last_hour is not None:
        path = path + "&lastHour={}".format(last_hour)

    return self._get(path)


def get_aggregate_stats_jitter(
    self,
    start_time: int,
    end_time: int,
    granularity: str,
    ip: bool = None,
    overlay: str = None,
    group_by_ne: bool = None,
    data_format: str = None,
) -> dict:
    """Get aggregate jitter stats data filter by query parameters.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/jitter

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
    :param ip: ``True`` to use IP address as key to sort results or
        ``False`` or ``None`` for default sorting by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param overlay: When set to ``all``,return all bonded tunnels; when
        set to ``0``,return all physical tunnels; when not used, return
        all bonded and physical tunnels; otherwise,return bonded tunnels
        associated with the specified overlay id, defaults to None
    :type overlay: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/jitter?"
        + "startTime={}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if ip is not None:
        path = path + "&ip={}".format(ip)
    if overlay is not None:
        path = path + "&overlay={}".format(overlay)
    if group_by_ne is not None:
        path = path + "&groupByNe={}".format(group_by_ne)
    if data_format is not None:
        path = path + "&format={}".format(data_format)

    return self._get(path)


def get_aggregate_stats_jitter_ne_pk_list(
    self,
    ne_pk_list: list[str],
    start_time: int,
    end_time: int,
    granularity: str,
    ip: bool = None,
    top: int = None,
    overlay: str = None,
    group_by_ne: bool = None,
    data_format: str = None,
) -> dict:
    """Get aggregate jitter stats data filter by query parameters.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats/aggregate/jitter

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
    :param ip: ``True`` to use IP address as key to sort results or
        ``False`` or ``None`` for default sorting by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param top: Number of rows to return from query, defaults to None
    :type top: int, optional
    :param overlay: When set to ``all``,return all bonded tunnels; when
        set to ``0``,return all physical tunnels; when not used, return
        all bonded and physical tunnels; otherwise,return bonded tunnels
        associated with the specified overlay id, defaults to None
    :type overlay: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/jitter?"
        + "startTime={}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if ip is not None:
        path = path + "&ip={}".format(ip)
    if top is not None:
        path = path + "&top={}".format(top)
    if overlay is not None:
        path = path + "&overlay={}".format(overlay)
    if group_by_ne is not None:
        path = path + "&groupByNe={}".format(group_by_ne)
    if data_format is not None:
        path = path + "&format={}".format(data_format)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_aggregate_stats_jitter_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    granularity: str,
    ip: bool = None,
    top: int = None,
    overlay: str = None,
    group_by_ne: bool = None,
    tunnel_name: str = None,
    data_format: str = None,
) -> dict:
    """Get aggregate jitter stats data for single appliance filter by
    query parameters.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/jitter/{nePk}

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
    :param ip: ``True`` to use IP address as key to sort results or
        ``False`` or ``None`` for default sorting by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param top: Number of rows to return from query, defaults to None
    :type top: int, optional
    :param overlay: When set to ``all``,return all bonded tunnels; when
        set to ``0``,return all physical tunnels; when not used, return
        all bonded and physical tunnels; otherwise,return bonded tunnels
        associated with the specified overlay id, defaults to None
    :type overlay: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :param tunnel_name: Filter response data for specified tunnel name,
        defaults to None
    :type tunnel_name: str, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/jitter/"
        + "{}?startTime={}&endTime={}&granularity={}".format(
            ne_pk, start_time, end_time, granularity
        )
    )

    if ip is not None:
        path = path + "&ip={}".format(ip)
    if top is not None:
        path = path + "&top={}".format(top)
    if overlay is not None:
        path = path + "&overlay={}".format(overlay)
    if group_by_ne is not None:
        path = path + "&groupByNe={}".format(group_by_ne)
    if tunnel_name is not None:
        path = path + "&tunnelName={}".format(tunnel_name)
    if data_format is not None:
        path = path + "&format={}".format(data_format)

    return self._get(path)


def get_aggregate_stats_drc(
    self,
    start_time: int,
    end_time: int,
    granularity: str,
    group_pk: str = None,
    top: int = None,
    overlay: str = None,
    data_format: str = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate tunnel drc stats data filter by query parameters.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/drc

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
        ``2.Network`` is auto-discovered groups. ``3.Network`` and
        beyond is user-defined groups, defaults to None
    :type group_pk: str, optional
    :param top: Number of rows to return from query, defaults to None
    :type top: int, optional
    :param overlay: When set to ``all``,return all bonded tunnels; when
        set to ``0``,return all physical tunnels; when not used, return
        all bonded and physical tunnels; otherwise,return bonded tunnels
        associated with the specified overlay id, defaults to None
    :type overlay: str, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/drc?"
        + "startTime={}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if group_pk is not None:
        path = path + "&groupPk={}".format(group_pk)
    if top is not None:
        path = path + "&top={}".format(top)
    if overlay is not None:
        path = path + "&overlay={}".format(overlay)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if group_by_ne is not None:
        path = path + "&groupByNe={}".format(group_by_ne)

    return self._get(path)


def get_aggregate_stats_drc_ne_pk_list(
    self,
    ne_pk_list: list[str],
    start_time: int,
    end_time: int,
    granularity: str,
    top: int = None,
    overlay: str = None,
    data_format: str = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate tunnel drc stats data filter by query parameters.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats/aggregate/drc

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
    :param top: Number of rows to return from query, defaults to None
    :type top: int, optional
    :param overlay: When set to ``all``,return all bonded tunnels; when
        set to ``0``,return all physical tunnels; when not used, return
        all bonded and physical tunnels; otherwise,return bonded tunnels
        associated with the specified overlay id, defaults to None
    :type overlay: str, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/drc?"
        + "startTime={}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if top is not None:
        path = path + "&top={}".format(top)
    if overlay is not None:
        path = path + "&overlay={}".format(overlay)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if group_by_ne is not None:
        path = path + "&groupByNe={}".format(group_by_ne)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_aggregate_stats_drc_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    granularity: str,
    tunnel_name: str = None,
    top: int = None,
    overlay: str = None,
    data_format: str = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate tunnel drc stats data for a single appliance filter
    by query parameters.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/drc/{nePk}

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
    :param tunnel_name: Filter response data for specified tunnel name,
        defaults to None
    :type tunnel_name: str, optional
    :param top: Number of rows to return from query, defaults to None
    :type top: int, optional
    :param overlay: When set to ``all``,return all bonded tunnels; when
        set to ``0``,return all physical tunnels; when not used, return
        all bonded and physical tunnels; otherwise,return bonded tunnels
        associated with the specified overlay id, defaults to None
    :type overlay: str, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/drc/"
        + "{}?startTime={}&endTime={}&granularity={}".format(
            ne_pk, start_time, end_time, granularity
        )
    )

    if tunnel_name is not None:
        path = path + "&tunnelName={}".format(tunnel_name)
    if top is not None:
        path = path + "&top={}".format(top)
    if overlay is not None:
        path = path + "&overlay={}".format(overlay)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if group_by_ne is not None:
        path = path + "&groupByNe={}".format(group_by_ne)

    return self._get(path)


def get_aggregate_stats_interface(
    self,
    start_time: int,
    end_time: int,
    granularity: str,
    traffic_type: str,
    data_format: str = None,
) -> dict:
    """Get aggregate interface stats data for a all appliance filter by
    query parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/interface

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
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/interface?"
        + "startTime={}&endTime={}&granularity={}&trafficType={}".format(
            start_time, end_time, granularity, traffic_type
        )
    )

    if data_format is not None:
        path = path + "&format={}".format(data_format)

    return self._get(path)


def get_aggregate_stats_interface_ne_pk_list(
    self,
    ne_pk_list: list[str],
    start_time: int,
    end_time: int,
    granularity: str,
    traffic_type: str,
    data_format: str = None,
) -> dict:
    """Get aggregate interface stats data for a all appliance filter by
    query parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats/aggregate/interface

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
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/interface?"
        + "startTime={}&endTime={}&granularity={}&trafficType={}".format(
            start_time, end_time, granularity, traffic_type
        )
    )

    if data_format is not None:
        path = path + "&format={}".format(data_format)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_aggregate_stats_interface_overlay_transport_ne_pk_list(
    self,
    ne_pk_list: list[str],
    start_time: int,
    end_time: int,
    granularity: str,
    interface_name: str = None,
    overlay: str = None,
    data_format: str = None,
) -> dict:
    """Get aggregate interface overlay transport stats data

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats/aggregate/interfaceOverlay

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
    :param interface_name: Filter data by interface name,
        defaults to None
    :type interface_name: str, optional
    :param overlay: When set to ``all``,return all bonded tunnels; when
        set to ``0``,return all physical tunnels; when not used, return
        all bonded and physical tunnels; otherwise,return bonded tunnels
        associated with the specified overlay id, defaults to None
    :type overlay: str, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/interfaceOverlay?"
        + "startTime={}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if interface_name is not None:
        path = path + "&interfaceName={}".format(interface_name)
    if overlay is not None:
        path = path + "&overlay={}".format(overlay)
    if data_format is not None:
        path = path + "&format={}".format(data_format)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_aggregate_stats_mos_ne_pk_list(
    self,
    ne_pk_list: list[str],
    start_time: int,
    end_time: int,
    granularity: str,
    top: int = None,
    overlay: str = None,
    data_format: str = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate Mean Opinion Score stats data

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats/aggregate/mos

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
    :param top: Number of rows to return from query, defaults to None
    :type top: int, optional
    :param overlay: When set to ``all``,return all bonded tunnels; when
        set to ``0``,return all physical tunnels; when not used, return
        all bonded and physical tunnels; otherwise,return bonded tunnels
        associated with the specified overlay id, defaults to None
    :type overlay: str, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/mos?"
        + "startTime={}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if top is not None:
        path = path + "&top={}".format(top)
    if overlay is not None:
        path = path + "&overlay={}".format(overlay)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if group_by_ne is not None:
        path = path + "&groupByNe={}".format(group_by_ne)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_aggregate_stats_mos_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    granularity: str,
    tunnel_name: str = None,
    top: int = None,
    overlay: str = None,
    data_format: str = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate Mean Opinion Score stats data for single appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/mos/{nePk}

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
    :param tunnel_name: Filter response data for specified tunnel name,
        defaults to None
    :type tunnel_name: str, optional
    :param top: Number of rows to return from query, defaults to None
    :type top: int, optional
    :param overlay: When set to ``all``,return all bonded tunnels; when
        set to ``0``,return all physical tunnels; when not used, return
        all bonded and physical tunnels; otherwise,return bonded tunnels
        associated with the specified overlay id, defaults to None
    :type overlay: str, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/mos/"
        + "{}?startTime={}&endTime={}&granularity={}".format(
            ne_pk, start_time, end_time, granularity
        )
    )

    if tunnel_name is not None:
        path = path + "&tunnelName={}".format(tunnel_name)
    if top is not None:
        path = path + "&top={}".format(top)
    if overlay is not None:
        path = path + "&overlay={}".format(overlay)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if group_by_ne is not None:
        path = path + "&groupByNe={}".format(group_by_ne)

    return self._get(path)


def get_aggregate_stats_boost_ne_pk_list(
    self,
    ne_pk_list: list[str],
    start_time: int,
    end_time: int,
    granularity: str,
    data_format: str = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate boost stats data

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats/aggregate/boost

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
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/boost?"
        + "startTime={}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if group_by_ne is not None:
        path = path + "&groupByNe={}".format(group_by_ne)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_aggregate_stats_boost_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    granularity: str,
    tunnel_name: str = None,
    overlay: str = None,
    data_format: str = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate boost stats data for a single appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/boost/{nePk}

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
    :param tunnel_name: Filter response data for specified tunnel name,
        defaults to None
    :type tunnel_name: str, optional
    :param overlay: When set to ``all``,return all bonded tunnels; when
        set to ``0``,return all physical tunnels; when not used, return
        all bonded and physical tunnels; otherwise,return bonded tunnels
        associated with the specified overlay id, defaults to None
    :type overlay: str, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/boost/"
        + "{}?startTime={}&endTime={}&granularity={}".format(
            ne_pk, start_time, end_time, granularity
        )
    )

    if tunnel_name is not None:
        path = path + "&tunnelName={}".format(tunnel_name)
    if overlay is not None:
        path = path + "&overlay={}".format(overlay)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if group_by_ne is not None:
        path = path + "&groupByNe={}".format(group_by_ne)

    return self._get(path)


def get_aggregate_stats_security_policy_ne_pk_list(
    self,
    ne_pk_list: list[str],
    start_time: int,
    end_time: int,
    granularity: str,
    top: int = None,
    data_format: str = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate security policy stats data

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats/aggregate/securityPolicy

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
    :param top: Return top x rows of data, defaults to None
    :type top: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/securityPolicy?"
        + "startTime={}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if top is not None:
        path = path + "&top={}".format(top)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if group_by_ne is not None:
        path = path + "&groupByNe={}".format(group_by_ne)

    data = {"ids": ne_pk_list}

    return self._post(path, data=data)


def get_aggregate_stats_security_policy_single_appliance(
    self,
    ne_pk: str,
    start_time: int,
    end_time: int,
    granularity: str,
    from_zone: str,
    to_zone: str,
    top: int = None,
    data_format: str = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate security policy stats data for single appliance

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - GET
          - /stats/aggregate/securityPolicy/{nePk}

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
    :param top: Return top x rows of data, defaults to None
    :type top: int, optional
    :param data_format: The only format other than JSON currently
        supported is CSV, accepted value is ``csv``, defaults to None
    :type data_format: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats/aggregate/securityPolicy/"
        + "{}?startTime={}&endTime={}&granularity={}&".format(
            ne_pk, start_time, end_time, granularity
        )
        + "fromZone={}&toZone={}".format(from_zone, to_zone)
    )

    if top is not None:
        path = path + "&top={}".format(top)
    if data_format is not None:
        path = path + "&format={}".format(data_format)
    if group_by_ne is not None:
        path = path + "&groupByNe={}".format(group_by_ne)

    return self._get(path)


def get_aggregate_stats_tunnels_ne_pk_tunnels(
    self,
    ne_pk_tunnel_list: list[str],
    start_time: int,
    end_time: int,
    granularity: str,
    metric: str = None,
    top: int = None,
    overlay: str = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate tunnel stats data filter by query parameters.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats2/aggregate/tunnel

    :param ne_pk_tunnel_list: List of dictionaries of appliance nePk
        values and optional tunnel id's,
        e.g. ``[{"nePk":"77.NE", "tunnelId":"tunnel_8"}, ...]`` \n
        * keyword **ids** (`str`): Network Primary Key (nePk) of
          appliance, e.g. ``3.NE`` \n
        * keyword **tunnelId** (`str`): tunnel id, e.g. ``Tunnel_12``,
          mandatory field but can be blank string "" \n
    :type ne_pk_tunnel_list: list[str]
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
    :param metric: Sort stats by the provided metric, can also be used
        with the param 'top' to limit number of items received,
        e.g. ``throughput``, defaults to None
    :type metric: str, optional
    :param top: This parameter should be provided together with param
        ``metric`` to indicate top x items of a metric. e.g. if
        ``metric`` is set to ``throughput`` and ``top`` is ``10``,
        retrieves top 10 tunnels by throughput, defaults to None
    :type top: int, optional
    :param overlay: When set to ``all``,return all bonded tunnels; when
        set to ``0``,return all physical tunnels; when not used, return
        all bonded and physical tunnels; otherwise,return bonded tunnels
        associated with the specified overlay id, defaults to None
    :type overlay: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats2/aggregate/tunnel?"
        + "startTime={}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if metric is not None:
        path = path + "&metric={}".format(metric)
    if top is not None:
        path = path + "&top={}".format(top)
    if overlay is not None:
        path = path + "&overlay={}".format(overlay)
    if group_by_ne is not None:
        path = path + "&groupByNe={}".format(group_by_ne)

    data = ne_pk_tunnel_list

    return self._post(path, data=data)


def get_aggregate_stats_top_talkers_ne_pk_tunnels(
    self,
    ne_pk_tunnel_list: list[str],
    start_time: int,
    end_time: int,
    top: int = None,
    split_by_ne: bool = None,
) -> dict:
    """Get aggregate topTalkers stats data filter by query parameters.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats2/aggregate/topTalkers

    :param ne_pk_tunnel_list: List of dictionaries of appliance nePk
        values and optional tunnel id's,
        e.g. ``[{"nePk":"77.NE", "tunnelId":"tunnel_8"}, ...]`` \n
        * keyword **ids** (`str`): Network Primary Key (nePk) of
          appliance, e.g. ``3.NE`` \n
        * keyword **tunnelId** (`str`): tunnel id, e.g. ``Tunnel_12``,
          mandatory field but can be blank string "" \n
    :type ne_pk_tunnel_list: list[str]
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param top: This parameter should be provided together with param
        ``metric`` to indicate top x items of a metric. e.g. if
        ``metric`` is set to ``throughput`` and ``top`` is ``10``,
        retrieves top 10 tunnels by throughput, defaults to None
    :type top: int, optional
    :param split_by_ne: ``True`` to split aggregate stats by appliance,
        if ``True``, there will be an extra level of key inside each
        stats object indicating what appliance the inner stats object
        belongs to, defaults to None
    :type split_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = "/stats2/aggregate/topTalkers?" + "startTime={}&endTime={}".format(
        start_time, end_time
    )

    if top is not None:
        path = path + "&top={}".format(top)
    if split_by_ne is not None:
        path = path + "&splitByNe={}".format(split_by_ne)

    data = ne_pk_tunnel_list

    return self._post(path, data=data)


def get_aggregate_stats_dns_ne_pk_tunnels(
    self,
    ne_pk_tunnel_list: list[str],
    start_time: int,
    end_time: int,
    is_source: int = None,
    split_type: int = None,
    top: int = None,
    split_by_ne: bool = None,
    group_by: str = None,
    group_by_subdomains: int = None,
) -> dict:
    """Get aggregate dns stats data filter by query parameters.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats2/aggregate/dns

    :param ne_pk_tunnel_list: List of dictionaries of appliance nePk
        values and optional tunnel id's,
        e.g. ``[{"nePk":"77.NE", "tunnelId":"tunnel_8"}, ...]`` \n
        * keyword **ids** (`str`): Network Primary Key (nePk) of
          appliance, e.g. ``3.NE`` \n
        * keyword **tunnelId** (`str`): tunnel id, e.g. ``Tunnel_12``,
          mandatory field but can be blank string "" \n
    :type ne_pk_tunnel_list: list[str]
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param is_source: Integer value representing whether dns is from
        source or destination. 0 for source, 1 for destination,
        defaults to None
    :type is_source: int, optional
    :param split_type: Filter data for specific type, 0 for 'http',
        1 for 'https', 2 for 'unassigned' and 3 for 'others,
        defaults to None
    :type split_type: int, optional
    :param top: Return top x rows of data, defaults to None
    :type top: int, optional
    :param split_by_ne: ``True`` to split aggregate stats by appliance,
        if ``True``, there will be an extra level of key inside each
        stats object indicating what appliance the inner stats object
        belongs to, defaults to None
    :type split_by_ne: bool, optional
    :param group_by: Group the data based on this value, default
        behavior if unspecified is to group by dns, defaults to None
    :type group_by: str, optional
    :param group_by_subdomains: Group the data based on the number of
        subdomains, if unspecified the default value is 2,
        defaults to None
    :type group_by_subdomains: int, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = "/stats2/aggregate/dns?startTime={}&endTime={}".format(
        start_time, end_time
    )

    if is_source is not None:
        path = path + "&isSource={}".format(is_source)
    if split_type is not None:
        path = path + "&splitType={}".format(split_type)
    if top is not None:
        path = path + "&top={}".format(top)
    if split_by_ne is not None:
        path = path + "&splitByNe={}".format(split_by_ne)
    if group_by is not None:
        path = path + "&groupBy={}".format(group_by)
    if group_by_subdomains is not None:
        path = path + "&groupBySubdomains={}".format(group_by_subdomains)

    data = ne_pk_tunnel_list

    return self._post(path, data=data)


def get_aggregate_stats_ports_ne_pk_tunnels(
    self,
    ne_pk_tunnel_list: list[str],
    start_time: int,
    end_time: int,
    is_source: int = None,
    is_known: int = None,
    protocol: int = None,
    port: int = None,
    top: int = None,
    split_by_ne: bool = None,
    last_hour: bool = None,
) -> dict:
    """Get aggregate ports stats data filter by query parameters.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats2/aggregate/ports

    :param ne_pk_tunnel_list: List of dictionaries of appliance nePk
        values and optional tunnel id's,
        e.g. ``[{"nePk":"77.NE", "tunnelId":"tunnel_8"}, ...]`` \n
        * keyword **ids** (`str`): Network Primary Key (nePk) of
          appliance, e.g. ``3.NE`` \n
        * keyword **tunnelId** (`str`): tunnel id, e.g. ``Tunnel_12``,
          mandatory field but can be blank string "" \n
    :type ne_pk_tunnel_list: list[str]
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param is_source: 0 to specifiy port as source port, 1 to specifiy
        port as destination port, defaults to None
    :type is_source: int, optional
    :param is_known: 1 to specify if port is assigned to an application,
        0 if not, defaults to None
    :type is_known: int, optional
    :param protocol: Integer value representing protocol used by port,
        defaults to None
    :type protocol: int, optional
    :param port: Integer value of port number, defaults to None
    :type port: int, optional
    :param top: Number of rows to return from query, defaults to None
    :type top: int, optional
    :param split_by_ne: ``True`` to split aggregate stats by appliance,
        if ``True``, there will be an extra level of key inside each
        stats object indicating what appliance the inner stats object
        belongs to, defaults to None
    :type split_by_ne: bool, optional
    :param last_hour: If ``True``, fetch data one hour behind from last
        hour if no data within last hour range, defaults to None
    :type last_hour: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = "/stats/aggregate/ports?startTime={}&endTime={}".format(
        start_time,
        end_time,
    )

    if is_source is not None:
        path = path + "&isSource={}".format(is_source)
    if is_known is not None:
        path = path + "&isKnown={}".format(is_known)
    if protocol is not None:
        path = path + "&protocol={}".format(protocol)
    if port is not None:
        path = path + "&port={}".format(port)
    if top is not None:
        path = path + "&top={}".format(top)
    if split_by_ne is not None:
        path = path + "&splitByNe={}".format(split_by_ne)
    if last_hour is not None:
        path = path + "&lastHour={}".format(last_hour)

    data = ne_pk_tunnel_list

    return self._post(path, data=data)


def get_aggregate_stats_mos_ne_pk_tunnels(
    self,
    ne_pk_tunnel_list: list[str],
    start_time: int,
    end_time: int,
    granularity: str,
    top: int = None,
    overlay: str = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate Mean Opinion Score stats data

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats2/aggregate/mos

    :param ne_pk_tunnel_list: List of dictionaries of appliance nePk
        values and optional tunnel id's,
        e.g. ``[{"nePk":"77.NE", "tunnelId":"tunnel_8"}, ...]`` \n
        * keyword **ids** (`str`): Network Primary Key (nePk) of
          appliance, e.g. ``3.NE`` \n
        * keyword **tunnelId** (`str`): tunnel id, e.g. ``Tunnel_12``,
          mandatory field but can be blank string "" \n
    :type ne_pk_tunnel_list: list[str]
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
    :param top: Number of rows to return from query, defaults to None
    :type top: int, optional
    :param overlay: When set to ``all``,return all bonded tunnels; when
        set to ``0``,return all physical tunnels; when not used, return
        all bonded and physical tunnels; otherwise,return bonded tunnels
        associated with the specified overlay id, defaults to None
    :type overlay: str, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats2/aggregate/mos?"
        + "startTime={}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if top is not None:
        path = path + "&top={}".format(top)
    if overlay is not None:
        path = path + "&overlay={}".format(overlay)
    if group_by_ne is not None:
        path = path + "&groupByNe={}".format(group_by_ne)

    data = ne_pk_tunnel_list

    return self._post(path, data=data)


def get_aggregate_stats_application2_ne_pk_tunnels(
    self,
    ne_pk_tunnel_list: list[str],
    start_time: int,
    end_time: int,
    application: str = None,
    top: int = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate application2 stats data filter by query parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats2/aggregate/application2

    :param ne_pk_tunnel_list: List of dictionaries of appliance nePk
        values and optional tunnel id's,
        e.g. ``[{"nePk":"77.NE", "tunnelId":"tunnel_8"}, ...]`` \n
        * keyword **ids** (`str`): Network Primary Key (nePk) of
          appliance, e.g. ``3.NE`` \n
        * keyword **tunnelId** (`str`): tunnel id, e.g. ``Tunnel_12``,
          mandatory field but can be blank string "" \n
    :type ne_pk_tunnel_list: list[str]
    :param start_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the starting time boundary of data time range
    :type start_time: int
    :param end_time: Long(Signed 64 bits) value of seconds since EPOCH
        time indicating the ending time boundary of data time range
    :type end_time: int
    :param application: Filter for data belonging to appliaction with
        matching name, defaults to None
    :type application: str, optional
    :param top: Return top x applications by throughput. e.g., if
        top=10 is provided, retrieve top 10 applications by throughput,
        defaults to None
    :type top: int, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = "/stats2/aggregate/application2?startTime={}&endTime={}".format(
        start_time, end_time
    )

    if application is not None:
        path = path + "&application={}".format(application)
    if top is not None:
        path = path + "&top={}".format(top)
    if group_by_ne is not None:
        path = path + "&groupByNe={}".format(group_by_ne)

    data = ne_pk_tunnel_list

    return self._post(path, data=data)


def get_aggregate_stats_application_ne_pk_tunnels(
    self,
    ne_pk_tunnel_list: list[str],
    start_time: int,
    end_time: int,
    granularity: str,
    application: str = None,
    traffic_type: str = None,
    ip: bool = None,
    metric: str = None,
    top: int = None,
    group_by_ne: bool = None,
) -> dict:
    """Get aggregate application stats data filter by query parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats2/aggregate/application

    :param ne_pk_tunnel_list: List of dictionaries of appliance nePk
        values and optional tunnel id's,
        e.g. ``[{"nePk":"77.NE", "tunnelId":"tunnel_8"}, ...]`` \n
        * keyword **ids** (`str`): Network Primary Key (nePk) of
          appliance, e.g. ``3.NE`` \n
        * keyword **tunnelId** (`str`): tunnel id, e.g. ``Tunnel_12``,
          mandatory field but can be blank string "" \n
    :type ne_pk_tunnel_list: list[str]
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
    :param application: Filter for data belonging to appliaction with
        matching name, defaults to None
    :type application: str, optional
    :param traffic_type: Filter for data for given traffic type,
        accepted values are ``optimized_traffic``,
        ``pass_through_shaped``, ``pass_through_unshaped``, and
        ``all_traffic``, defaults to None
    :type traffic_type: str, optional
    :param ip: ``True`` to use IP address as key to sort results or
        ``False`` or ``None`` for default sorting by appliance ID,
        defaults to None
    :type ip: bool, optional
    :param metric: Sort stats by the provided metric, can also be used
        with the param 'top' to limit number of items received,
        e.g. ``throughput``, defaults to None
    :type metric: str, optional
    :param top: This parameter should be provided together with param
        ``metric`` to indicate top x items of a metric. e.g. if
        ``metric`` is set to ``throughput`` and ``top`` is ``10``,
        retrieves top 10 tunnels by throughput, defaults to None
    :type top: int, optional
    :param group_by_ne:	Group aggregate stats by appliance. Set to
        ``True`` for an extra level of key inside each tunnel stats
        object indicating what appliance the inner stats object belongs
        to. When not specified, behaves as ``True``, defaults to None
    :type group_by_ne: bool, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats2/aggregate/application?"
        + "startTime={}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if application is not None:
        path = path + "&application={}".format(application)
    if traffic_type is not None:
        path = path + "&trafficType={}".format(traffic_type)
    if ip is not None:
        path = path + "&ip={}".format(ip)
    if metric is not None:
        path = path + "&metric={}".format(metric)
    if top is not None:
        path = path + "&top={}".format(top)
    if group_by_ne is not None:
        path = path + "&groupByNe={}".format(group_by_ne)

    data = ne_pk_tunnel_list

    return self._post(path, data=data)


def get_aggregate_stats_overlay_bandwidth_ne_pk_tunnels(
    self,
    ne_pk_tunnel_list: list[str],
    start_time: int,
    end_time: int,
    granularity: str,
) -> dict:
    """Get aggregate overlay bandwidth stats data filter by query
    parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats2/aggregate/overlays/bandwidth

    :param ne_pk_tunnel_list: List of dictionaries of appliance nePk
        values and optional tunnel id's,
        e.g. ``[{"nePk":"77.NE", "tunnelId":"tunnel_8"}, ...]`` \n
        * keyword **ids** (`str`): Network Primary Key (nePk) of
          appliance, e.g. ``3.NE`` \n
        * keyword **tunnelId** (`str`): tunnel id, e.g. ``Tunnel_12``,
          mandatory field but can be blank string "" \n
    :type ne_pk_tunnel_list: list[str]
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
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats2/aggregate/overlays/bandwidth?"
        + "startTime={}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    data = ne_pk_tunnel_list

    return self._post(path, data=data)


def get_aggregate_stats_interface_overlay_transport_ne_pk_tunnels(
    self,
    ne_pk_tunnel_list: list[str],
    start_time: int,
    end_time: int,
    granularity: str,
    interface_name: str = None,
    overlay: str = None,
) -> dict:
    """Get aggregate interface overlay transport stats data filter by
    query parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats2/aggregate/interfaceOverlay

    :param ne_pk_tunnel_list: List of dictionaries of appliance nePk
        values and optional tunnel id's,
        e.g. ``[{"nePk":"77.NE", "tunnelId":"tunnel_8"}, ...]`` \n
        * keyword **ids** (`str`): Network Primary Key (nePk) of
          appliance, e.g. ``3.NE`` \n
        * keyword **tunnelId** (`str`): tunnel id, e.g. ``Tunnel_12``,
          mandatory field but can be blank string "" \n
    :type ne_pk_tunnel_list: list[str]
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
    :param interface_name: Filter data by interface name,
        defaults to None
    :type interface_name: str, optional
    :param overlay: When set to ``all``,return all bonded tunnels; when
        set to ``0``,return all physical tunnels; when not used, return
        all bonded and physical tunnels; otherwise,return bonded tunnels
        associated with the specified overlay id, defaults to None
    :type overlay: str, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats2/aggregate/interfaceOverlay?"
        + "startTime={}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if interface_name is not None:
        path = path + "&interfaceName={}".format(interface_name)
    if overlay is not None:
        path = path + "&overlay={}".format(overlay)

    data = ne_pk_tunnel_list

    return self._post(path, data=data)


def get_aggregate_stats_shaper_ne_pk_list(
    self,
    ne_pk_tunnel_list: list[str],
    start_time: int,
    end_time: int,
    granularity: str,
    direction: int,
    top: int = None,
) -> dict:
    """Get aggregate interface overlay transport stats data filter by
    query parameters

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - aggregateStats
          - POST
          - /stats2/aggregate/shaper

    :param ne_pk_tunnel_list: List of dictionaries of appliance nePk
        values and optional tunnel id's,
        e.g. ``[{"nePk":"77.NE", "tunnelId":"tunnel_8"}, ...]`` \n
        * keyword **ids** (`str`): Network Primary Key (nePk) of
          appliance, e.g. ``3.NE`` \n
        * keyword **tunnelId** (`str`): tunnel id, e.g. ``Tunnel_12``,
          mandatory field but can be blank string "" \n
    :type ne_pk_tunnel_list: list[str]
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
    :param direction: 0 for Outbound, 1 for Inbound
    :type direction: int
    :param top: Number of rows to return from query, defaults to None
    :type top: int, optional
    :return: Returns dictionary of aggregate stats filtered by query
        parameters
    :rtype: dict
    """
    path = (
        "/stats2/aggregate/shaper?"
        + "startTime={}&endTime={}&granularity={}".format(
            start_time, end_time, granularity
        )
    )

    if direction is not None:
        path = path + "&direction={}".format(direction)
    if top is not None:
        path = path + "&top={}".format(top)

    data = ne_pk_tunnel_list

    return self._post(path, data=data)
