# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.
#
# dbPartition : Managing Orchestrator Database Partitions


def get_db_partition(
    self,
    table: str = None,
    partition: str = None,
) -> list:
    """Get Orchestrator database partition details

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - dbPartition
          - GET
          - /dbPartition/info

    :param table: Name of db table, defaults to None
    :type table: str, optional
    :param partition: Name of db partition, defaults to None
    :type partition: str, optional
    :return: Returns list
    :rtype: list
    """
    base_path = "/dbPartition/info"

    if table is None and partition is None:
        return self._get(base_path)
    elif table is not None and partition is None:
        return self._get("{}?table={}".format(base_path, table))
    elif table is None and partition is not None:
        return self._get("{}?partition={}".format(base_path, partition))
    else:
        return self._get(
            "{}?table={}&partition={}".format(base_path, table, partition)
        )


def delete_db_partition(
    self,
    table: str,
    partition: str,
) -> bool:
    """Delete Orchestrator database table partition.

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - dbPartition
          - DELETE
          - /dbPartition/{table}/{partition}

    .. note::
        Default & Current partition cannot be deleted

    :param table: Name of db table
    :type table: str
    :param partition: Name of db partition
    :type partition: str
    :return: Returns True/False based on successful call
    :rtype: bool
    """
    return self._delete(
        "/dbPartition/{}/{}".format(table, partition),
        expected_status=[204],
        return_type="bool",
    )
