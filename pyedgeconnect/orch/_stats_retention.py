# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# statsRetention : Stats retention


def get_all_stats_retention(self) -> dict:
    """Get all statistics retention configuration

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - statsRetention
          - GET
          - /gms/stats/retention

    :return: Returns dictionary of statistics retention
    :rtype: dict
    """
    return self._get("/gms/stats/retention")


def update_stats_retention(
    self,
    stat_type: str,
    granularity: str = None,
    partition_duration: int = None,
    retention: int = None,
    data: list = None,
) -> bool:
    """Update statistics retention configuration

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - statsRetention
          - PUT
          - /gms/stats/retention/{statType}

    .. note::
        Swagger documentation says the ``granularity``,
        ``partition_duration``, and ``retention`` fields are optional,
        however, can't use ``0`` or ``""`` for any of the parameters per
        the Model Schema example in Swagger.

        The logic is upheld that if any of the parameters are left as
        default of ``None`` the assumption is the ``data`` parameter
        will be used instead. If ``data`` is left to default of ``None``
        the function will raise a ValueError.


    :param stat_type: Statistic type e.g. ``interfacebyoverlay``
    :type stat_type: str
    :param granularity: Data granularity possible values ``MINUTE``,
        ``HOUR`` and ``DAY``, defaults to None
    :type granularity: str, optional
    :param partition_duration: Database partitions duration/size,
        defaults to None
    :type partition_duration: int, optional
    :param retention: Data retention is seconds, defaults to None
    :type retention: int, optional
    :param data: List of dictionaries containing the above variables to
        update multiples, defaults to None
    :type data: list, optional
    :raises ValueError: Either ``granularity``, ``partition_duration``,
        and ``retention`` parameters must be set, or the parameters must
        be contained in the ``data`` parameter.
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    if granularity is None or partition_duration is None or retention is None:
        if data is not None:
            return self._put(
                "/gms/stats/retention/{}".format(stat_type),
                data=data,
                return_type="bool",
            )
        else:
            raise ValueError(
                "Not enough valid parameters were passed to perform function"
            )
    else:
        data = [
            {
                "granularity": granularity,
                "partitionDuration": partition_duration,
                "retention": retention,
            }
        ]
        return self._put(
            "/gms/stats/retention/{}".format(stat_type),
            data=data,
            return_type="bool",
        )


def get_all_nonstats_retention(self) -> dict:
    """Get all non-statistics retention configuration

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - statsRetention
          - GET
          - /gms/stats/nonStatsTable/retention

    :return: Returns dictionary of non-statistics retention
    :rtype: dict
    """
    return self._get("/gms/stats/nonStatsTable/retention")


def update_nonstats_retention(
    self,
    stat_type: str,
    partition_duration: int = None,
    retention: int = None,
) -> bool:
    """Update non-statistics retention configuration

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - statsRetention
          - PUT
          - /gms/stats/nonStatsTable/retention/{statType}

    :param stat_type: Statistic type e.g. ``interfacebyoverlay``
    :type stat_type: str
    :param partition_duration: Database partitions duration/size,
        defaults to None
    :type partition_duration: int, optional
    :param retention: Data retention is seconds, defaults to None
    :type retention: int, optional
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {"partitionDuration": partition_duration, "retention": retention}

    return self._put(
        "/gms/stats/nonStatsTable/retention/{}".format(stat_type),
        data=data,
        return_type="bool",
    )


def get_all_stats_collection(self) -> dict:
    """Get all statistics collection Enable/Disable info

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - statsRetention
          - GET
          - /gms/stats/collection

    :return: Returns dictionary of statistics collection
    :rtype: dict
    """
    return self._get("/gms/stats/collection")


def update_stats_collection(
    self,
    stat_type: str,
    enable: bool,
) -> bool:
    """Update statistics collection Enable/Disable info for named
    statistic

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - statsRetention
          - PUT
          - /gms/stats/collection/{statType}

    :param stat_type: Statistic type e.g. ``interfacebyoverlay``
    :type stat_type: str
    :param enable: ``True`` for Enabled or ``False`` for Disabled
    :type enable: bool
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    data = {}
    data[stat_type] = enable

    return self._put(
        "/gms/stats/collection/{}?isEnabled={}".format(stat_type, enable),
        data=data,
        return_type="bool",
    )
