# MIT License
# (C) Copyright 2021 Hewlett Packard Enterprise Development LP.

import logging
import os
import sys
import traceback

import requests
from urllib3.exceptions import InsecureRequestWarning


class HttpCommon:
    """Class to leverage common HTTP functions and handling responses"""

    # BASE HTTP REQUESTS

    def _req_post(
        self,
        url: str,
        data,
    ) -> requests.Response:
        """Assemble and send Requests request for HTTP POST method

        :param url: Full URL to use in HTTP request
        :type url: str
        :param data: Data to pass in request body
        :type data: str, list, dict
        :return: Requests Response object
        :rtype: requests.Response
        """
        apiSrcStr = self.apiSrcId if ("?" not in url) else self.apiSrcId2
        return self.session.post(
            self.url_prefix + url + apiSrcStr,
            json=data,
            verify=self.verify,
            timeout=120,
            headers=self.headers,
        )

    def _req_get(
        self,
        url: str,
    ) -> requests.Response:
        """Assemble and send Requests request for HTTP GET method

        :param url: Full URL to use in HTTP request
        :type url: str
        :return: Requests Response object
        :rtype: requests.Response
        """
        apiSrcStr = self.apiSrcId if ("?" not in url) else self.apiSrcId2
        return self.session.get(
            self.url_prefix + url + apiSrcStr,
            verify=self.verify,
            timeout=120,
            headers=self.headers,
        )

    def _req_delete(
        self,
        url: str,
    ) -> requests.Response:
        """Assemble and send Requests request for HTTP DELETE method

        :param url: Full URL to use in HTTP request
        :type url: str
        :return: Requests Response object
        :rtype: requests.Response
        """
        apiSrcStr = self.apiSrcId if ("?" not in url) else self.apiSrcId2
        return self.session.delete(
            self.url_prefix + url + apiSrcStr,
            verify=self.verify,
            timeout=120,
            headers=self.headers,
        )

    def _req_put(
        self,
        url: str,
        data,
    ) -> requests.Response:
        """Assemble and send Requests request for HTTP PUT method

        :param url: Full URL to use in HTTP request
        :type url: str
        :param data: Data to pass in request body
        :type data: str, list, dict
        :return: Requests Response object
        :rtype: requests.Response
        """
        apiSrcStr = self.apiSrcId if ("?" not in url) else self.apiSrcId2
        return self.session.put(
            self.url_prefix + url + apiSrcStr,
            json=data,
            verify=self.verify,
            timeout=120,
            headers=self.headers,
        )

    # HTTP RESPONSE HANDLER

    def _handle_response(
        self,
        api_path: str,
        response: requests.models.Response,
        expected_status: list,
        return_type: str,
    ):
        """Handle response from API call

        :param api_path: API path that was used for API call
            (not including url_prefix)
        :type api_path: str
        :param response: Requests response object to obtain status code
        :type response: requests.Response
        :param expected_status: List of expected HTTP status codes of
            response, e.g. [200] or [200,204]
        :type expected_status: list
        :param return_type: Option for data to return back to original
            function, e.g. "json" "text" "bool" "full_response"
        :type return_type: str
        :return: Requests Response object
        :rtype: requests.Response
        """
        if response.status_code not in expected_status:
            self.logger.error(
                "{} {} | Received HTTP {} | Response text: {}".format(
                    response.request,
                    api_path,
                    response.status_code,
                    response.text,
                )
            )
            # return formatted data for the source method
            # for JSON data, return a dictionary with the details of
            # the response
            if return_type == "json":
                return {
                    "request": response.request,
                    "api_path": api_path,
                    "status_code": response.status_code,
                    "text": response.text,
                }
            elif return_type == "text":
                return response.text
            elif return_type == "bool":
                return False
            elif return_type == "full_response":
                return response

        # If Orchestrator set with log_success == True, include response
        # text in log messages. Default behavior is to omit response
        # text from log messages for successful API calls.
        if self.log_success:
            self.logger.info(
                "{} {} | Received HTTP {} | Response text: {}".format(
                    response.request,
                    api_path,
                    response.status_code,
                    response.text,
                )
            )
        else:
            # Log successful call, omit response text in case sensitive
            # data in response text
            self.logger.info(
                (
                    "{} {} | Received: HTTP {} ".format(
                        response.request, api_path, response.status_code
                    )
                    + "| Response text omitted to avoid logging sensitive data"
                )
            )

        # return formatted data for the source method
        if return_type == "json":
            return response.json()
        elif return_type == "text":
            return response.text
        elif return_type == "bool":
            return True
        elif return_type == "full_response":
            return response

    # HTTP REQUESTS CALLED BY METHODS

    def _post(
        self,
        api_path: str,
        data="",
        expected_status: list = [200],
        return_type: str = "json",
    ):
        """Setup HTTP POST request and send results to _handle_response
        method. Catches Exceptions and logs to log file

        :param api_path: API path to append to url_prefix
        :type api_path: str
        :param data: Data to pass in request body, defaults to ""
        :type data: str, list, dict, optional
        :param expected_status: List of expected HTTP status codes of
            response, defaults to [200]
        :type expected_status: list, optional
        :param return_type: Filter for data to include in response to
            function call, accepted values are "json" "text" "bool"
            "full_response", defaults to "json"
        :type return_type: str, optional
        :return: Returns False on exceptions, otherwise passes return
            through _handle_response method for processing Requests
            response
        :rtype: bool, _handle_response method
        """
        if return_type not in ["json", "text", "bool", "full_response"]:
            self.logger.error(
                "Called POST {} with unknown return type '{}'".format(
                    api_path, return_type
                )
            )
        try:
            response = self._req_post(api_path, data)
            return self._handle_response(
                api_path, response, expected_status, return_type
            )

        except Exception as ex:
            self.logger.error(
                "Exception {} when calling POST {}. Traceback: {}".format(
                    type(ex), api_path, traceback.format_exc()
                )
            )
            return False

        self.logger.error(
            "Reached end without returning for POST "
            + "{}, return_type '{}'".format(api_path, return_type)
        )
        return False

    def _get(
        self,
        api_path: str,
        expected_status: list = [200],
        return_type: str = "json",
    ):
        """Setup HTTP GET request and send results to _handle_response
        method. Catches Exceptions and logs to log file

        :param api_path: API path to append to url_prefix
        :type api_path: str
        :param expected_status: List of expected HTTP status codes of
            response, defaults to [200]
        :type expected_status: list, optional
        :param return_type: Filter for data to include in response to
            function call, accepted values are "json" "text" "bool"
            "full_response", defaults to "json"
        :type return_type: str, optional
        :return: Returns False on exceptions, otherwise passes return
            through _handle_response method for processing Requests
            response
        :rtype: bool, _handle_response method
        """
        if return_type not in ["json", "text", "bool", "full_response"]:
            self.logger.error(
                "Called GET {} with unknown return type '{}'".format(
                    api_path, return_type
                )
            )
        try:
            response = self._req_get(api_path)
            return self._handle_response(
                api_path, response, expected_status, return_type
            )

        except Exception as ex:
            self.logger.error(
                "Exception {} when calling GET {}. Traceback: {}".format(
                    type(ex), api_path, traceback.format_exc()
                )
            )
            return False

        self.logger.error(
            "Reached end without returning for GET "
            + "{}, return_type '{}'".format(api_path, return_type)
        )
        return False

    def _delete(
        self,
        api_path: str,
        expected_status: list = [200],
        return_type: str = "json",
    ):
        """Setup HTTP DELETE request and send results to
        _handle_response method. Catches Exceptions and logs to log file

        :param api_path: API path to append to url_prefix
        :type api_path: str
        :param expected_status: List of expected HTTP status codes of
            response, defaults to [200]
        :type expected_status: list, optional
        :param return_type: Filter for data to include in response to
            function call, accepted values are "json" "text" "bool"
            "full_response", defaults to "json"
        :type return_type: str, optional
        :return: Returns False on exceptions, otherwise passes return
            through _handle_response method for processing Requests
            response
        :rtype: bool, _handle_response method
        """
        if return_type not in ["json", "text", "bool", "full_response"]:
            self.logger.error(
                "Called DELETE {} with unknown return type '{}'".format(
                    api_path, return_type
                )
            )
        try:
            response = self._req_delete(api_path)
            return self._handle_response(
                api_path, response, expected_status, return_type
            )

        except Exception as ex:
            self.logger.error(
                "Exception {} when calling DELETE {}. Traceback: {}".format(
                    type(ex), api_path, traceback.format_exc()
                )
            )
            return False

        self.logger.error(
            "Reached end without returning for DELETE "
            + "{}, return_type '{}'".format(api_path, return_type)
        )
        return False

    def _put(
        self,
        api_path: str,
        data="",
        expected_status: list = [200],
        return_type: str = "json",
    ):
        """Setup HTTP PUT request and send results to _handle_response
        method. Catches Exceptions and logs to log file

        :param api_path: API path to append to url_prefix
        :type api_path: str
        :param data: Data to pass in request body, defaults to ""
        :type data: str, list, dict, optional
        :param expected_status: List of expected HTTP status codes of
            response, defaults to [200]
        :type expected_status: list, optional
        :param return_type: Filter for data to include in response to
            function call, accepted values are "json" "text" "bool"
            "full_response", defaults to "json"
        :type return_type: str, optional
        :return: Returns False on exceptions, otherwise passes return
            through _handle_response method for processing Requests
            response
        :rtype: bool, _handle_response method
        """
        if return_type not in ["json", "text", "bool", "full_response"]:
            self.logger.error(
                "Called PUT {} with unknown return type '{}'".format(
                    api_path, return_type
                )
            )
        try:
            response = self._req_put(api_path, data)
            return self._handle_response(
                api_path, response, expected_status, return_type
            )

        except Exception as ex:
            self.logger.error(
                "Exception {} when calling PUT {}. Traceback: {}".format(
                    type(ex), api_path, traceback.format_exc()
                )
            )
            return False

        self.logger.error(
            "Reached end without returning for PUT "
            + "{}, return_type '{}'".format(api_path, return_type)
        )
        return False


# Aruba Orchestrator
class Orchestrator(HttpCommon):
    """Orchestrator setup and imports related methods for making API
    calls to Orchestrator. Child class of :class:`HttpCommon`
    """

    def __init__(
        self,
        url: str,
        api_key: str = "",
        auth_mode: str = "local",
        log_file: bool = False,
        log_console: bool = False,
        log_success: bool = False,
        verify_ssl: bool = True,
    ):
        """Setup Orchestrator instance

        .. warning::
            If ``log_file`` and ``log_success`` are set to ``True``
            response text from successful API calls will be logged to
            the local log file. Some responses can include sensitive
            data that you may not wish to retain in the log files.

        :param url: IP address or URL to Orchestrator server
        :type url: str
        :param api_key: API Key for non-user-based authentication
        :type api_key: str, optional
        :param auth_mode: Reference what form of user-based
            authentication is in use, accepts ``local``, ``radius``, and
            ``tacacs``, defaults to "local"
        :type auth_mode: str, optional
        :param log_file: Enable logging messages to local log file,
            defaults to False
        :type log_file: bool, optional
        :param log_console: Enable logging messages to stdout,
            defaults to False
        :type log_console: bool, optional
        :param log_success: Enable logging response text of successful
            API calls in log messages. Will print a warning to the user
            if set to ``True`` while ``log_file`` is also ``True`` to
            raise awareness that sensitive data may be stored in the log
            file.
        :type log_success: bool, optional
        :param verify_ssl: Set to ``False`` to ignore certificate
            warnings within requests, defaults to ``True``
        :type verify_ssl: bool, optional
        :raises ValueError: If Orchestrator auth_mode specified not in
            supported_auth_modes
        """
        supported_auth_modes = ["local", "radius", "tacacs"]
        if auth_mode not in supported_auth_modes:
            raise ValueError(
                "Orchestrator auth_mode must be one of %r."
                % supported_auth_modes
            )

        self.url_prefix = "https://" + url + "/gms/rest"
        self.session = requests.Session()
        if api_key != "":
            self.headers = {"X-Auth-Token": api_key}
        else:
            self.headers = {}
        # for API calls w/ just source as query param
        self.apiSrcId = "?source=menu_rest_apis_id"
        # for API calls w/ multiple query params
        self.apiSrcId2 = "&source=menu_rest_apis_id"
        # remote authentication modes supported via this helper module
        self.supportedAuthModes = supported_auth_modes
        # change authMode to the desired auth mode before
        # invoking login() function
        self.authMode = auth_mode
        self.authenticated = False

        # disable certificate warning messages / errors
        self.verify = verify_ssl
        if verify_ssl is False:
            requests.packages.urllib3.disable_warnings(
                category=InsecureRequestWarning
            )

        # Allow logging successful response text/data if log_success
        # is set to True, warn user if logging to local file is also
        # enabled
        self.log_success = log_success
        if self.log_success and log_file:
            print(
                """
                NOTE: Logging Response text from successful API calls
                has been enabled. Some responses can include sensitive
                data that you may not wish to retain in the log files.
            """
            )

        # Setup general log settings for messages and errors
        self.logger = logging.getLogger("orchestrator")
        self.formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        self.logger.setLevel(logging.INFO)

        # Setup logging file if log_file set to True
        if log_file:
            local_log_directory = "logging/"
            if not os.path.exists(local_log_directory):
                os.makedirs(local_log_directory)
            self.file_handler = logging.FileHandler(
                "{}sp_orch.log".format(local_log_directory)
            )
            self.file_handler.setFormatter(self.formatter)
            self.file_handler.setLevel(logging.INFO)
            self.logger.addHandler(self.file_handler)

        # Setup logging to console if log_console set to True
        if log_console:
            self.console_handler = logging.StreamHandler(sys.stdout)
            self.console_handler.setFormatter(self.formatter)
            self.console_handler.setLevel(logging.DEBUG)
            self.logger.setLevel(logging.DEBUG)
            self.logger.addHandler(self.console_handler)

    # Imported methods
    from .orch._acls import get_appliance_acls
    from .orch._action_log import (
        cancel_audit_log_task,
        get_audit_log,
        get_audit_log_task_status,
    )
    from .orch._active_sessions import get_active_sessions_orchestrator
    from .orch._admin_distance import get_appliance_admin_distance
    from .orch._aggregate_stats import (
        get_aggregate_stats_active_flows,
        get_aggregate_stats_appliances,
        get_aggregate_stats_appliances_ne_pk_list,
        get_aggregate_stats_appliances_single_appliance,
        get_aggregate_stats_application2_ne_pk_tunnels,
        get_aggregate_stats_application_ne_pk_tunnels,
        get_aggregate_stats_applications,
        get_aggregate_stats_applications_ne_pk_list,
        get_aggregate_stats_applications_single_appliance,
        get_aggregate_stats_boost_ne_pk_list,
        get_aggregate_stats_boost_single_appliance,
        get_aggregate_stats_dns_ne_pk_list,
        get_aggregate_stats_dns_ne_pk_tunnels,
        get_aggregate_stats_dns_single_appliance,
        get_aggregate_stats_drc,
        get_aggregate_stats_drc_ne_pk_list,
        get_aggregate_stats_drc_single_appliance,
        get_aggregate_stats_dscp,
        get_aggregate_stats_dscp_ne_pk_list,
        get_aggregate_stats_dscp_single_appliance,
        get_aggregate_stats_flows,
        get_aggregate_stats_flows_ne_pk_list,
        get_aggregate_stats_flows_single_appliance,
        get_aggregate_stats_interface,
        get_aggregate_stats_interface_ne_pk_list,
        get_aggregate_stats_interface_overlay_transport_ne_pk_list,
        get_aggregate_stats_interface_overlay_transport_ne_pk_tunnels,
        get_aggregate_stats_jitter,
        get_aggregate_stats_jitter_ne_pk_list,
        get_aggregate_stats_jitter_single_appliance,
        get_aggregate_stats_mos_ne_pk_list,
        get_aggregate_stats_mos_ne_pk_tunnels,
        get_aggregate_stats_mos_single_appliance,
        get_aggregate_stats_overlay_bandwidth_ne_pk_tunnels,
        get_aggregate_stats_ports,
        get_aggregate_stats_ports_ne_pk_list,
        get_aggregate_stats_ports_ne_pk_tunnels,
        get_aggregate_stats_ports_single_appliance,
        get_aggregate_stats_security_policy_ne_pk_list,
        get_aggregate_stats_security_policy_single_appliance,
        get_aggregate_stats_shaper_ne_pk_list,
        get_aggregate_stats_top_talkers,
        get_aggregate_stats_top_talkers_ne_pk_list,
        get_aggregate_stats_top_talkers_ne_pk_tunnels,
        get_aggregate_stats_top_talkers_single_appliance,
        get_aggregate_stats_top_talkers_split_single_appliance,
        get_aggregate_stats_traffic_behavior,
        get_aggregate_stats_traffic_behavior_ne_pk_list,
        get_aggregate_stats_traffic_behavior_single_appliance,
        get_aggregate_stats_traffic_class,
        get_aggregate_stats_traffic_class_ne_pk_list,
        get_aggregate_stats_traffic_class_single_appliance,
        get_aggregate_stats_tunnels,
        get_aggregate_stats_tunnels_ne_pk_list,
        get_aggregate_stats_tunnels_ne_pk_tunnels,
        get_aggregate_stats_tunnels_single_appliance,
    )
    from .orch._alarm import (
        acknolwedge_alarms_from_appliance,
        acknowledge_alarms_from_orchestrator,
        add_note_to_appliance_alarm,
        clear_alarms_from_appliance,
        clear_alarms_from_orchestrator,
        delete_alarm_email_delay,
        delete_all_customized_alarm_severity,
        delete_customized_alarm_severity_for_type,
        delete_supressed_alarms,
        get_alarm_count_all_appliances,
        get_alarm_count_from_appliance,
        get_alarm_count_orchestrator_and_appliances,
        get_alarm_count_orchestrator_or_appliances,
        get_alarm_descriptions,
        get_alarm_email_delay,
        get_alarm_notification_status,
        get_alarms_from_appliances,
        get_alarms_from_orchestrator,
        get_customized_alarm_severity,
        get_customized_alarm_severity_for_type,
        get_supressed_alarms,
        set_alarm_email_delay,
        set_alarm_notification_status,
        set_customized_alarm_severity,
        set_supressed_alarms,
        update_alarm_email_delay,
        update_customized_alarm_severity,
    )
    from .orch._api_key import (
        add_api_key,
        delete_api_key,
        get_api_key,
        get_api_keys,
        update_api_key,
    )
    from .orch._appliance import (
        add_and_approve_discovered_appliances,
        add_discovered_appliances,
        appliance_get_api,
        appliance_post_api,
        change_appliance_credentials,
        change_appliance_group,
        default_appliance_stats_config,
        delete_appliance,
        delete_appliance_for_rediscovery,
        deny_appliance,
        get_all_approved,
        get_all_denied_appliances,
        get_all_discovered,
        get_appliance_dns_cache_config,
        get_appliance_extra_info,
        get_appliance_info,
        get_appliance_stats_config,
        get_appliances,
        get_appliances_queued_for_deletion,
        modify_appliance,
        modify_appliance_stats_config,
        update_discovered_appliances,
    )
    from .orch._appliance_backup import (
        backup_appliance_config,
        delete_appliance_backup,
        get_appliance_backup_history,
        restore_appliance_from_backup,
    )
    from .orch._appliance_crash_history import appliance_crash_history
    from .orch._appliance_preconfig import (
        apply_preconfig_to_existing,
        approve_and_apply_preconfig,
        create_preconfig,
        delete_preconfig,
        find_matching_preconfig,
        get_all_preconfig,
        get_apply_preconfig_status,
        get_default_preconfig,
        get_preconfig,
        modify_preconfig,
        validate_preconfig,
    )
    from .orch._appliance_reboot_history import get_appliance_reboot_history
    from .orch._appliances_software_versions import (
        get_appliance_software_version,
    )
    from .orch._application_definition import (
        delete_user_defined_app_address_map,
        delete_user_defined_app_dns_classification,
        delete_user_defined_app_port_protocol,
        get_application_modification_times,
        get_user_defined_app_address_map,
        get_user_defined_app_dns_classification,
        get_user_defined_app_groups,
        get_user_defined_app_port_protocol,
        post_user_defined_app_address_map,
        update_user_defined_app_dns_classification,
        update_user_defined_app_groups,
        update_user_defined_app_port_protocol,
    )
    from .orch._authentication import get_appliance_auth_information
    from .orch._avc_mode import get_avc_mode
    from .orch._banners import get_appliance_login_banners
    from .orch._bgp import (
        get_appliance_bgp_config,
        get_appliance_bgp_config_all_vrfs,
        get_appliance_bgp_neighbors,
        get_appliance_bgp_neighbors_all_vrfs,
        get_appliance_bgp_state,
        get_appliance_bgp_state_all_vrfs,
    )
    from .orch._bonded_tunnels_configuration import (
        get_bonded_tunnel_details,
        get_bonded_tunnel_details_for_appliance,
        get_bonded_tunnel_details_for_appliance_tunnel,
        get_bonded_tunnels_for_physical_tunnel,
        get_bonded_tunnels_state,
    )
    from .orch._broadcast_cli import broadcast_cli
    from .orch._built_in_policies import get_built_in_policies
    from .orch._custom_appliance_tags import get_custom_appliance_tags
    from .orch._custom_certs import (
        check_custom_certs_appliances_to_portal,
        check_custom_certs_orchestrator_to_portal,
        delete_custom_cert,
        get_custom_certs,
        get_custom_certs_enabled,
        set_custom_certs_enabled,
        update_custom_certs,
        verify_custom_cert,
    )
    from .orch._db_partition import delete_db_partition, get_db_partition
    from .orch._debug_files import (
        cancel_debug_file_download,
        delete_debug_file_from_appliance,
        delete_debug_file_from_orchestrator,
        generate_appliance_sysdump,
        get_debug_file_proxy_settings,
        get_debug_files_from_appliance,
        set_debug_file_proxy_settings,
        upload_appliance_debug_files_to_orchestrator,
        upload_appliance_debug_files_to_support,
    )
    from .orch._discovery import (
        get_appliance_discovery_emails,
        set_appliance_discovery_emails,
    )
    from .orch._disks import get_appliance_disk_information
    from .orch._dns import get_appliance_dns
    from .orch._dns_proxy import get_dns_proxy
    from .orch._exception import (
        create_tunnel_exceptions,
        delete_all_tunnel_exceptions,
        delete_single_tunnel_exception,
        delete_tunnel_exceptions_list,
        get_tunnel_exceptions,
        update_single_tunnel_exception,
        update_tunnel_exceptions,
    )
    from .orch._flow import (
        get_appliance_flow_bandwidth_stats,
        get_appliance_flow_details,
        get_appliance_flow_details_verbose,
        get_appliance_flows,
        reclassify_flows,
        reset_flows,
    )
    from .orch._gms_backup import (
        add_or_update_orchestrator_backup_config,
        create_orchestrator_blueprint_template,
        get_orchestrator_backup_config,
        test_orchestrator_backup_config,
    )
    from .orch._gms_notification import (
        delete_gms_notification,
        get_gms_notification,
        update_gms_notification,
    )
    from .orch._gms_server import (
        get_orchestrator_hello,
        get_orchestrator_server_brief,
        get_orchestrator_server_info,
        get_orchestrator_server_os,
        get_orchestrator_server_ping,
        get_orchestrator_server_versions,
    )
    from .orch._gms_smtp import (
        delete_gms_smtp_settings,
        delete_unverified_email_addresses,
        get_gms_smtp_settings,
        get_unverified_email_addresses,
        send_verification_email,
        set_gms_smtp_settings,
        test_gms_smtp_settings,
        verify_email_address,
    )
    from .orch._gms_stats_collection import (
        get_gms_stats_collection,
        get_gms_stats_collection_defaults,
        update_gms_stats_collection,
    )
    from .orch._group import (
        add_gms_group,
        delete_gms_group,
        get_all_appliance_locations,
        get_appliance_location,
        get_gms_group,
        get_gms_groups,
        get_root_gms_group,
        update_appliance_location_grnodepk,
        update_appliance_location_nepk,
        update_gms_group,
    )
    from .orch._ha_groups import get_ha_groups, modify_ha_groups
    from .orch._hostname import get_orchestrator_hostname
    from .orch._idle_time import clear_idle_time, increment_idle_time
    from .orch._ikeless import (
        get_ipsec_udp_key_config,
        get_ipsec_udp_key_history,
        get_ipsec_udp_key_status,
        update_ipsec_udp_key_config,
    )
    from .orch._inbound_shaper import get_appliance_inbound_shaper
    from .orch._interface_labels import (
        get_all_interface_labels,
        get_interface_labels_by_type,
        push_interface_labels_to_appliance,
        update_interface_labels,
    )
    from .orch._interface_state import get_appliance_interface_state
    from .orch._internal_subnets import (
        get_internal_subnets,
        update_internal_subnets,
    )
    from .orch._ip_allow_list import (
        get_ip_allow_list,
        get_ip_allow_list_drops,
        update_ip_allow_list,
    )
    from .orch._license import (
        change_appliance_license,
        delete_appliance_license_token,
        get_nx_licensed_appliances,
        get_portal_licensed_appliances,
        get_portal_licensed_summary,
        get_vx_licensed_appliances,
        grant_appliance_base_license,
        revoke_appliance_base_license,
    )
    from .orch._link_integrity import get_link_integrity_test_result
    from .orch._location import get_location_coordinates_from_address
    from .orch._logging import get_appliance_syslog_config
    from .orch._login import login, logout, send_mfa
    from .orch._loopback import get_loopback_interfaes
    from .orch._maintenance_mode import (
        get_maintenance_mode_appliances,
        update_maintenance_mode_appliances,
    )
    from .orch._mgmt_services import get_mgmt_services
    from .orch._multicast import (
        get_appliance_multicast_config,
        get_appliance_multicast_enabled,
        get_appliance_multicast_interfaces,
        get_appliance_multicast_neighbors,
        get_appliance_multicast_routes,
    )
    from .orch._nat import (
        get_appliance_nat_config,
        get_appliance_nat_maps,
        get_appliance_nat_pools,
    )
    from .orch._nat_policy import (
        get_nat_policy,
        get_nat_policy_dynamic,
        get_nat_policy_inbound_outbound,
    )
    from .orch._net_flow import get_net_flow_configuration
    from .orch._network_memory import erase_appliance_network_memory
    from .orch._optimization_policy import get_optimization_policy
    from .orch._ospf import (
        get_appliance_ospf_config,
        get_appliance_ospf_interfaces_config,
        get_appliance_ospf_interfaces_state,
        get_appliance_ospf_neighbors_state,
        get_appliance_ospf_state,
    )
    from .orch._overlays import (
        configure_new_overlay,
        configure_regionalized_overlay,
        delete_overlay,
        get_all_overlays_config,
        get_all_overlays_config_keyed,
        get_appliance_overlays_association,
        get_max_overlays,
        get_overlay_config,
        get_overlay_config_for_region,
        get_overlays_priorities,
        modify_overlay_config,
        modify_overlay_config_for_region,
        modify_regionalized_overlay,
        set_overlays_priorities,
    )
    from .orch._pause_orchestration import (
        get_pause_orchestration,
        set_pause_orchestration,
    )
    from .orch._peer_priority import get_peer_priority_configuration
    from .orch._port_forwarding import get_appliance_port_fowarding
    from .orch._qos_policy import get_qos_policy
    from .orch._rbac_assignment import (
        delete_rbac_user_assignment,
        get_rbac_assignments,
        get_rbac_user_assignment,
        update_rbac_assignment,
    )
    from .orch._rbac_role import (
        delete_rbac_role,
        get_all_rbac_roles,
        get_rbac_role,
        get_rbac_role_assigned,
        update_rbac_role,
    )
    from .orch._reachability import (
        get_reachability_status_appliance,
        get_reachability_status_orchestrator,
    )
    from .orch._realtime_stats import get_realtime_stats
    from .orch._regions import (
        create_region,
        delete_region,
        get_all_regions,
        get_region,
        get_region_appliance_association,
        get_region_appliance_association_by_nepk,
        get_region_appliance_association_by_region_id,
        set_region_appliance_association,
        update_region_appliance_association,
        update_region_name,
    )
    from .orch._rest_api_config import get_rest_api_config, set_rest_api_config
    from .orch._rest_request_time_stats import (
        get_appliance_rest_stats,
        get_appliance_rest_stats_by_method,
    )
    from .orch._route_policy import get_route_policy
    from .orch._save_changes import (
        save_changes_ne_pk_list,
        save_changes_single_appliance,
    )
    from .orch._security_maps import get_appliance_security_maps
    from .orch._security_settings import (
        get_security_settings,
        set_security_settings,
    )
    from .orch._services import (
        get_gms_internet_policy_services,
        get_gms_third_party_services,
        update_gms_internet_policy_services,
    )
    from .orch._shaper import get_appliance_shaper
    from .orch._shell import get_shell_access_setting, set_shell_access_setting
    from .orch._sp_portal import (
        assign_account_license_ecsp,
        create_case_with_portal,
        delete_old_account_key,
        geo_locate_multiple_ips,
        geo_locate_single_ip,
        get_account_key_change_count,
        get_account_key_change_status,
        get_account_license_ecsp_status,
        get_account_license_feature,
        get_account_license_type,
        get_all_saas_apps,
        get_app_definition_data,
        get_app_definition_total,
        get_app_groups,
        get_app_groups_hash,
        get_appliance_orch_portal_status,
        get_cloud_portal_broadcast_message,
        get_compound_classification,
        get_compound_classification_hash,
        get_count_of_saas_apps,
        get_dns_classification,
        get_dns_classification_hash,
        get_flow_classification,
        get_flow_classification_hash,
        get_ip_protocol_numbers,
        get_orchestrator_to_cloud_portal_status,
        get_port_protocol_classification,
        get_port_protocol_classification_hash,
        get_portal_registration_config,
        get_portal_registration_status,
        get_portal_services_status,
        get_portal_top_sites,
        get_saas_classification,
        get_saas_classification_hash,
        get_service_id_to_country_mapping,
        get_service_id_to_service_mapping,
        get_tcp_udp_port_data,
        get_traffic_behavior,
        get_traffic_behavior_hash,
        get_update_time_for_app_definitions,
        request_new_account_key,
        search_app_definition_data,
        unassign_account_license_ecsp,
        update_portal_registration_config,
        update_portal_registration_status,
    )
    from .orch._stats_retention import (
        get_all_nonstats_retention,
        get_all_stats_collection,
        get_all_stats_retention,
        update_nonstats_retention,
        update_stats_collection,
        update_stats_retention,
    )
    from .orch._tca import get_appliance_tca, get_appliance_tunnel_tca
    from .orch._tcpdump import (
        tcpdump_run,
        tcpdump_status_all,
        tcpdump_status_appliance,
    )
    from .orch._template import (
        associate_template_group_to_appliance,
        create_template_group,
        delete_template_group,
        get_all_template_groups,
        get_appliance_applied_template_goups,
        get_appliance_template_groups_association,
        get_appliance_template_history,
        get_selected_templates_in_template_group,
        get_template_group,
        get_template_group_association_all_appliances,
        get_template_groups_priorities,
        post_template_group,
        select_templates_for_template_group,
        set_template_groups_priorities,
    )
    from .orch._third_party_tunnels_configuration import (
        get_passthrough_tunnel_details,
        get_passthrough_tunnel_details_for_appliance,
        get_passthrough_tunnel_details_for_appliance_tunnel,
        get_passthrough_tunnels_state,
    )
    from .orch._timeseries_stats import (
        get_timeseries_stats_appliance_process_state,
        get_timeseries_stats_appliances,
        get_timeseries_stats_appliances_single_appliance,
        get_timeseries_stats_application,
        get_timeseries_stats_application_ne_pk_list,
        get_timeseries_stats_application_single_appliance,
        get_timeseries_stats_boost_single_appliance,
        get_timeseries_stats_drc,
        get_timeseries_stats_drc_ne_pk_list,
        get_timeseries_stats_drc_single_appliance,
        get_timeseries_stats_dscp,
        get_timeseries_stats_dscp_ne_pk_list,
        get_timeseries_stats_dscp_single_appliance,
        get_timeseries_stats_flow,
        get_timeseries_stats_flow_ne_pk_list,
        get_timeseries_stats_flow_single_appliance,
        get_timeseries_stats_interface_overlay_single_appliance,
        get_timeseries_stats_interface_single_appliance,
        get_timeseries_stats_internal_drops_single_appliance,
        get_timeseries_stats_jitter_single_appliance,
        get_timeseries_stats_mos_single_appliance,
        get_timeseries_stats_orchestrator_memory,
        get_timeseries_stats_security_policy_single_appliance,
        get_timeseries_stats_shaper,
        get_timeseries_stats_shaper_ne_pk_list,
        get_timeseries_stats_traffic_class,
        get_timeseries_stats_traffic_class_ne_pk_list,
        get_timeseries_stats_traffic_class_single_appliance,
        get_timeseries_stats_tunnel_single_appliance,
    )
    from .orch._tunnels_configuration import (
        get_appliance_tunnel_ids,
        get_batch_appliance_tunnels_config,
        get_batch_appliance_tunnels_state,
        get_physical_tunnel_details,
        get_physical_tunnel_details_for_appliance,
        get_physical_tunnel_details_for_appliance_tunnel,
        get_total_tunnel_count,
        get_tunnel_count_for_appliances,
        get_tunnel_traceroute,
        get_tunnels_between_appliances,
        get_tunnels_between_appliances_config_data,
        initiate_tunnel_traceroute,
    )
    from .orch._ui_usage_stats import add_ui_usage_count
    from .orch._user import (
        change_user_password,
        create_or_update_user,
        delete_user,
        get_all_users,
        get_new_two_factor_key,
        get_user,
        reset_user_password,
        user_forgot_password,
    )
    from .orch._vrf import (
        add_routing_segmentation_segment,
        delete_routing_segmentation_maps_from_source_segment,
        delete_routing_segmentation_segment_by_id,
        get_routing_segmentation_enable_status,
        get_routing_segmentation_list_of_security_maps,
        get_routing_segmentation_maps,
        get_routing_segmentation_maps_from_source_segment,
        get_routing_segmentation_security_policy,
        get_routing_segmentation_segment_by_id,
        get_routing_segmentation_segments,
        get_routing_segmentation_snat_maps,
        update_routing_segmentation_enable_status,
        update_routing_segmentation_maps_from_source_segment,
        update_routing_segmentation_security_policy,
        update_routing_segmentation_segment_by_id,
        update_routing_segmentation_snat_maps,
    )
    from .orch._vrf_dnat_maps import get_dnat_maps
    from .orch._vrf_snat_maps import get_snat_maps
    from .orch._vrrp import get_vrrp_interfaes
    from .orch._vti import get_vti_interfaes
    from .orch._vxoa_hostname import update_appliance_hostname
    from .orch._wan_next_hop_health import get_wan_next_hop_health_config
    from .orch._wccp import (
        get_wccp_service_group_settings,
        get_wccp_state,
        get_wccp_system_settings,
    )
    from .orch._zones import (
        get_zone_next_id,
        get_zones,
        get_zones_end_to_end_state,
        get_zones_vrf_mapping,
        set_zone_next_id,
        update_zones,
        update_zones_end_to_end_state,
    )


# Aruba Edge Connect
class EdgeConnect(HttpCommon):
    """Edge Connect setup and imports related methods for making API
    calls to Edge Connect appliances. Child class of :class:`HttpCommon`
    """

    def __init__(
        self,
        url: str,
        log_file: bool = False,
        log_console: bool = False,
        log_success: bool = False,
        verify_ssl: bool = True,
    ):
        """Setup Edge Connect instance

        .. warning::
            If ``log_file`` and ``log_success`` are set to ``True``
            response text from successful API calls will be logged to
            the local log file. Some responses can include sensitive
            data that you may not wish to retain in the log files.

        :param url: IP address or URL to Edge Connect appliance
        :type url: str
        :param api_key: API Key for non-user-based authentication
        :type api_key: str, optional
        :param auth_mode: Reference what form of user-based
            authentication is in use, accepts ``local``, ``radius``, and
            ``tacacs``, defaults to "local"
        :type auth_mode: str, optional
        :param log_file: Enable logging messages to local log file,
            defaults to False
        :type log_file: bool, optional
        :param log_console: Enable logging messages to stdout,
            defaults to False
        :type log_console: bool, optional
        :param log_success: Enable logging response text of successful
            API calls in log messages. Will print a warning to the user
            if set to ``True`` while ``log_file`` is also ``True`` to
            raise awareness that sensitive data may be stored in the log
            file.
        :type log_success: bool, optional
        :param verify_ssl: Set to ``False`` to ignore certificate
            warnings within requests, defaults to ``True``
        :type verify_ssl: bool, optional
        """
        self.url_prefix = "https://" + url + ":443/rest/json"
        self.session = requests.Session()
        self.headers = {}
        # for API calls w/ just source as query param
        self.apiSrcId = "?source=menu_rest_apis_id"
        # for API calls w/ multiple query params
        self.apiSrcId2 = "&source=menu_rest_apis_id"

        # disable certificate warning messages / errors
        self.verify = verify_ssl
        if verify_ssl is False:
            requests.packages.urllib3.disable_warnings(
                category=InsecureRequestWarning
            )

        # Allow logging successful response text/data if log_success
        # is set to True, warn user if logging to local file is also
        # enabled
        self.log_success = log_success
        if self.log_success and log_file:
            print(
                """
                NOTE: Logging Response text from successful API calls
                has been enabled. Some responses can include sensitive
                data that you may not wish to retain in the log files.
            """
            )

        # Setup general log settings for messages and errors
        self.logger = logging.getLogger("edgeconnect")
        self.formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        self.logger.setLevel(logging.INFO)

        # Setup logging file if log_file set to True
        if log_file:
            local_log_directory = "logging/"
            if not os.path.exists(local_log_directory):
                os.makedirs(local_log_directory)
            self.file_handler = logging.FileHandler(
                "{}sp_ecos.log".format(local_log_directory)
            )
            self.file_handler.setFormatter(self.formatter)
            self.file_handler.setLevel(logging.INFO)
            self.logger.addHandler(self.file_handler)

        # Setup logging to console if log_console set to True
        if log_console:
            self.console_handler = logging.StreamHandler(sys.stdout)
            self.console_handler.setFormatter(self.formatter)
            self.console_handler.setLevel(logging.DEBUG)
            self.logger.setLevel(logging.DEBUG)
            self.logger.addHandler(self.console_handler)

    # Imported methods
    from .ecos._gms import assign_orchestrator, get_orchestrator
    from .ecos._interfaces import get_appliance_interfaces
    from .ecos._license import is_reboot_required
    from .ecos._login import login, logout
    from .ecos._network_interfaces import (
        get_appliance_network_interfaces,
        modify_network_interfaces,
    )
    from .ecos._reboot import request_reboot
    from .ecos._save_changes import save_changes
    from .ecos._sp_portal import register_sp_portal, register_sp_portal_status
