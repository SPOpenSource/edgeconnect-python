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
