# MIT License
# (C) Copyright 2022 Hewlett Packard Enterprise Development LP.
#
# advancedProperties : Orchestrator advance properties


def get_orchestrator_advanced_properties(
    self,
) -> dict:
    """Get Orchestrator advanced properties

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - advancedProperties
          - GET
          - /gms/advancedProperties

    :return: Returns dictionary of Orchestrator advanced properties \n
        * keyword **ParallelStatsTasks** (`int`): Default value is
          ``20``
        * keyword **jettyMinThreads** (`int`): Default value is ``10``
        * keyword **ParallelOrchestrationTasks** (`int`): Default value
          is ``50``
        * keyword **restRequestTimeout** (`int`): Default value is
          ``60``
        * keyword **excludedTableNames** (`str`): Default value is
          ``dailyapp,dailydrc,dailydrops,dailydscp,dailyflow,dailyinterface,dailyjitter,dailymemory,dailynxtraffic,dailyshaper,dailytrafficclass,dailytunneltraffic,hourlyapp,hourlydns,hourlydrc,hourlydrops,hourlydscp,hourlyflow,hourlyflowapp,hourlyflowapp2,hourlyinterface,hourlyjitter,hourlylatency,hourlyloss,hourlynxtraffic,hourlyport,hourlyshaper,hourlytoptalkers,hourlytrafficclass,hourlytunneltraffic,minuteapp,minutedrc,minutedrops,minutedscp,minuteflow,minuteinterface,minutejitter,minutenxtraffic,minuteshaper,minutetrafficclass,minutetunneltraffic,neconfig2,hourlyBehavioral,minuteinterfaceoverlay,hourlyinterfaceoverlay,dailyinterfaceoverlay,restrequesttimestats,minutemos,hourlymos,dailymos,minuteboost,hourlyboost,dailyboost,minutesecuritypolicy,hourlysecuritypolicy,dailysecuritypolicy``
        * keyword **sslExcludeCiphers** (`str`): Default value is
          ``.*NULL.*,.*RC4.*,.*MD5.*,.*DES.*,.*DSS.*``
        * keyword **ContentSecurityPolicyHeaderEnabled** (`bool`):
          Default value is ``true``
        * keyword **excludeTables** (`bool`): Default value is ``false``
        * keyword **jettyAcceptQueueSize** (`int`): Default value is
          ``1000``
        * keyword **bridgeCacheExpireTime** (`int`): Default value is
          ``120``
        * keyword **sslIncludeProtocols** (`str`): Default value is
          ``TLSv1.2``
        * keyword **dbPoolMaxConnectionLifeTime** (`int`): Default value
          is ``300000``
        * keyword **dbPoolIdleTimeout** (`int`): Default value is
          ``120000``
        * keyword **sslIncludeCiphers** (`str`): Default value is
          ``TLS_DHE_RSA.*,TLS_ECDHE.*``
        * keyword **sslExcludeProtocols** (`str`): Default value is
          ``SSL,SSLv3,SSLv2,SSLv2Hello,TLSv1,TLSv1.1``
        * keyword **modifyTunnelBatchSize** (`int`): Default value is
          ``500``
        * keyword **dbPoolValidationTimeout** (`int`): Default value is
          ``3000``
        * keyword **mgmtInterface** (`str`): Default value is ``eth0``
        * keyword **dbPoolMinimumIdleConnections** (`int`): Default
          value is ``10``
        * keyword **emailImagesMaxSize** (`int`): Default value is
          ``10``
        * keyword **newSoftwareReleasesNotification** (`bool`): Default
          value is ``true``
        * keyword **dbPoolConnectionTimeout** (`int`): Default value is
          ``30000``
        * keyword **ParallelActionTasks** (`int`): Default value is
          ``50``
        * keyword **threadPoolSize** (`int`): Default value is ``1000``
        * keyword **dbPoolLeakDetectionThreshold** (`int`): Default
          value is ``300000``
        * keyword **denyApplianceOnDelete** (`bool`): Default value is
          ``true``
        * keyword **failedLoginAttemptThreshold** (`int`): Default value
          is ``5``
        * keyword **ParallelReachabilityTasks** (`int`): Default value
          is ``20``
        * keyword **restRequestStatsCollection** (`bool`): Default value
          is ``true``
        * keyword **jettyMaxThreads** (`int`): Default value is ``128``
        * keyword **jettyIdleTimeout** (`int`): Default value is
          ``60000``
        * keyword **dbPoolMaxConnections** (`int`): Default value is
          ``1000``
        * keyword **MultipleOrchestratorsForOneZscalerAccount** (`bool`):
          Default value is ``false``
        * keyword **bondedTunnelReorderWaitTime** (`int`): Default value
          is ``100``
        * keyword **fileOpsChunkSize** (`int`): Default value is result
          of 1024 * 1024, ``1048576``
        * keyword **oauthRefreshTokenRefreshTime** (`int`): time
          interval in minutes to periodically check whether refresh
          token is still valid for OAuth sessions, default is ``5``
    :rtype: dict
    """  # noqa E501
    return self._get("/gms/advancedProperties")


def update_orchestrator_advanced_properties(
    self,
    parallel_stats_tasks: int,
    jetty_min_threads: int,
    parallel_orchestration_tasks: int,
    rest_request_timeout: int,
    excluded_table_names: str,
    ssl_exclude_ciphers: str,
    content_security_policy_header_enabled: bool,
    exclude_tables: bool,
    jetty_accept_queue_size: int,
    bridge_cache_expire_time: int,
    ssl_include_protocols: str,
    db_pool_max_connection_lifetime: int,
    db_pool_idle_timeout: int,
    ssl_include_ciphers: str,
    ssl_exclude_protocols: str,
    modify_tunnel_batch_size: int,
    db_pool_validation_timeout: int,
    mgmt_interface: str,
    db_pool_minimum_idle_connections: int,
    email_images_max_size: int,
    new_software_releases_notification: bool,
    db_pool_connection_timeout: int,
    parallel_action_tasks: int,
    thread_pool_size: int,
    db_pool_leak_detection_threshold: int,
    deny_appliance_on_delete: bool,
    failed_login_attempt_threshold: int,
    parallel_reachability_tasks: int,
    rest_request_stats_collection: bool,
    jetty_max_threads: int,
    jetty_idle_timeout: int,
    db_pool_max_connections: int,
    multiple_orchestrators_one_zscaler: bool,
    bonded_tunnel_reorder_wait_time: int,
    file_ops_chunk_size: int,
    oauth_refresh_token_refresh_time: int,
) -> bool:
    """Update Orchestrator advanced properties

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - advancedProperties
          - PUT
          - /gms/advancedProperties

    .. warning::

        All parameters must be updated, as such, for updating a single
        paramter, it is advised to retrieve current values from
        :func:`~pyedgeconnect.Orchestrator.get_orchestrator_advanced_properties`
        to make sure other unitended changes are not made.

    :param parallel_stats_tasks: Number of parallel stats tasks
    :type parallel_stats_tasks: int
    :param jetty_min_threads: Minimum number of jetty threads
    :type jetty_min_threads: int
    :param parallel_orchestration_tasks: Number of parallel
        orchestration tasks
    :type parallel_orchestration_tasks: int
    :param rest_request_timeout: Timeout in seconds for REST requests
    :type rest_request_timeout: int
    :param excluded_table_names: Tables to exclude
    :type excluded_table_names: str
    :param ssl_exclude_ciphers: SSL ciphers to exclude
    :type ssl_exclude_ciphers: str
    :param content_security_policy_header_enabled: Enable content
        security policy header
    :type content_security_policy_header_enabled: bool
    :param exclude_tables: Exclude the named tables in
        ``excluded_table_names``
    :type exclude_tables: bool
    :param jetty_accept_queue_size: Queue size for Jetty
    :type jetty_accept_queue_size: int
    :param bridge_cache_expire_time: Bridge cache expire time
    :type bridge_cache_expire_time: int
    :param ssl_include_protocols: SSL protocols to include
    :type ssl_include_protocols: str
    :param db_pool_max_connection_lifetime: Database pool max
        connection lifetime
    :type db_pool_max_connection_lifetime: int
    :param db_pool_idle_timeout: Database pool idle timeout value
    :type db_pool_idle_timeout: int
    :param ssl_include_ciphers: SSL ciphers to inlucde
    :type ssl_include_ciphers: str
    :param ssl_exclude_protocols: SSL protocols to exclude
    :type ssl_exclude_protocols: str
    :param modify_tunnel_batch_size: Batch size of tunnel modify actions
    :type modify_tunnel_batch_size: int
    :param db_pool_validation_timeout: Database pool validation timeout
        value
    :type db_pool_validation_timeout: int
    :param mgmt_interface: Orchestrator host management interface
    :type mgmt_interface: str
    :param db_pool_minimum_idle_connections: Database pool minimum idle
        connections
    :type db_pool_minimum_idle_connections: int
    :param email_images_max_size: Email image attachment maximum size
    :type email_images_max_size: int
    :param new_software_releases_notification: Notify messages on new
        software releases
    :type new_software_releases_notification: bool
    :param db_pool_connection_timeout: Database pool connection timeout
        value
    :type db_pool_connection_timeout: int
    :param parallel_action_tasks: Number of parallel action tasks
    :type parallel_action_tasks: int
    :param thread_pool_size: Thread pool size
    :type thread_pool_size: int
    :param db_pool_leak_detection_threshold: Database pool leak
        detection
    :type db_pool_leak_detection_threshold: int
    :param deny_appliance_on_delete: Deny appliance when deleted from
        Orchestrator
    :type deny_appliance_on_delete: bool
    :param failed_login_attempt_threshold: Number of failed login
        attempts before locking user
    :type failed_login_attempt_threshold: int
    :param parallel_reachability_tasks: Number of parallel reachability
        tasks
    :type parallel_reachability_tasks: int
    :param rest_request_stats_collection: Enable REST request stats
        collection
    :type rest_request_stats_collection: bool
    :param jetty_max_threads: Maximum of jetty threads
    :type jetty_max_threads: int
    :param jetty_idle_timeout: Jetty idle timeout value
    :type jetty_idle_timeout: int
    :param db_pool_max_connections: Database pool maximum connections
    :type db_pool_max_connections: int
    :param multiple_orchestrators_one_zscaler: ``True`` if multiple
        Orchestrators are leveraging one Z-Scaler account
    :type multiple_orchestrators_one_zscaler: bool
    :param bonded_tunnel_reorder_wait_time: Wait time for bonded tunnel
        reorder action
    :type bonded_tunnel_reorder_wait_time: int
    :param file_ops_chunk_size: File operations chunk size
    :type file_ops_chunk_size: int
    :param oauth_refresh_token_refresh_time: OAuth refresh-token refresh
        time
    :type oauth_refresh_token_refresh_time: int
    :return: Returns True/False based on successful call
    :rtype: bool
    """  # noqa E501
    data = {
        "ParallelStatsTasks": parallel_stats_tasks,
        "jettyMinThreads": jetty_min_threads,
        "ParallelOrchestrationTasks": parallel_orchestration_tasks,
        "restRequestTimeout": rest_request_timeout,
        "excludedTableNames": excluded_table_names,
        "sslExcludeCiphers": ssl_exclude_ciphers,
        "ContentSecurityPolicyHeaderEnabled": content_security_policy_header_enabled,  # noqa E501
        "excludeTables": exclude_tables,
        "jettyAcceptQueueSize": jetty_accept_queue_size,
        "bridgeCacheExpireTime": bridge_cache_expire_time,
        "sslIncludeProtocols": ssl_include_protocols,
        "dbPoolMaxConnectionLifeTime": db_pool_max_connection_lifetime,
        "dbPoolIdleTimeout": db_pool_idle_timeout,
        "sslIncludeCiphers": ssl_include_ciphers,
        "sslExcludeProtocols": ssl_exclude_protocols,
        "modifyTunnelBatchSize": modify_tunnel_batch_size,
        "dbPoolValidationTimeout": db_pool_validation_timeout,
        "mgmtInterface": mgmt_interface,
        "dbPoolMinimumIdleConnections": db_pool_minimum_idle_connections,
        "emailImagesMaxSize": email_images_max_size,
        "newSoftwareReleasesNotification": new_software_releases_notification,
        "dbPoolConnectionTimeout": db_pool_connection_timeout,
        "ParallelActionTasks": parallel_action_tasks,
        "threadPoolSize": thread_pool_size,
        "dbPoolLeakDetectionThreshold": db_pool_leak_detection_threshold,
        "denyApplianceOnDelete": deny_appliance_on_delete,
        "failedLoginAttemptThreshold": failed_login_attempt_threshold,
        "ParallelReachabilityTasks": parallel_reachability_tasks,
        "restRequestStatsCollection": rest_request_stats_collection,
        "jettyMaxThreads": jetty_max_threads,
        "jettyIdleTimeout": jetty_idle_timeout,
        "dbPoolMaxConnections": db_pool_max_connections,
        "MultipleOrchestratorsForOneZscalerAccount": multiple_orchestrators_one_zscaler,
        "bondedTunnelReorderWaitTime": bonded_tunnel_reorder_wait_time,
        "fileOpsChunkSize": file_ops_chunk_size,
        "oauthRefreshTokenRefreshTime": oauth_refresh_token_refresh_time,
    }

    return self._put(
        "/gms/advancedProperties",
        data=data,
        expected_status=[204],
        return_type="bool",
    )


def get_orchestrator_advanced_properties_metadata(
    self,
) -> dict:
    """Get Orchestrator advanced properties metadata and default values

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - advancedProperties
          - GET
          - /gms/advancedProperties/metadata

    :return: Returns dictionary of Orchestrator advanced properties with
        respective default values, if a restart is required, and
        optional custom value if currently set \n
        * keyword **<adv_property_name>** (`dict`): Dictionary for each
          advanced property information \n
            * keyword **defaultValue** (`str`/`int`/`bool`): The default
              value of the related property, type varies based on
              property
            * keyword **isRestartRequired** (`bool`): ``True`` if
              property change would require a restart, ``False`` if no
              restart required
            * keyword **customValue** (`str`/`int`/`bool`, optional):
              This key will only be present if the current value set
              on Orchestrator is different from the default value
    :rtype: dict
    """
    return self._get("/gms/advancedProperties/metadata")
