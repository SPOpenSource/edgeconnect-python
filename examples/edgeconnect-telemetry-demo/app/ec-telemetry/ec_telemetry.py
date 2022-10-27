# THIS DEMO IS NOT MEANT TO BE A PRODUCTION MONITORING SOLUTION

# This example code serves to demonstrate the possibilities in
# retrieving and visualizing telemetry data from Orchestrator and
# EdgeConnect. The demo is simple to run, however, modifying
# and/or incorporating components of this work into your own solution
# requires a greater understanding of Python, Docker, InfluxDB,
# Grafana, and Redis.

# All of these components are not necessarily required for developing
# your own solution as there may be pieces of data you don't need
# to collect, some additional others that you want to add,
# substitude alternative tools for task queuing, database, and
# visualization or alerting needs.

import logging
import os
import shutil
import socket
import sys
import tarfile
import time
from datetime import datetime
from logging.handlers import RotatingFileHandler

from influxdb_client.client.util.multiprocessing_helper import \
    MultiprocessingWriter
from influxdb_client.client.write_api import WriteOptions

from pyedgeconnect import EdgeConnect


def ec_data_gather(
    appliance,
):
    """Collect telemetry data from EdgeConnect appliance and write the
    data to InfluxDB database

    :param appliance: Appliance data object, populated by response from
        :func:`pyedgeconnect.Orchestrator.get_appliances` and augmented
        by :func:`pyedgeconnect.Orchestrator.get_all_interface_labels`,
        :func:`pyedgeconnect.Orchestrator.get_all_overlays_config`, and
        :func:`pyedgeconnect.Orchestrator.get_portal_licensed_appliances`
    :type appliance: dict
    :return: N/A
    :rtype: N/A
    """

    # Timer class to track processing time within a collection task
    class Timer:
        def __init__(self):
            self._start_time = None
            self._elapsed_time = None

        def start(self):
            """Start a new timer"""
            self._start_time = time.perf_counter()

        def current(self):
            """Calculate current running time on timer"""
            current_time = time.perf_counter() - self._start_time
            return f"{current_time:0.4f}"

        def stop(self):
            """Stop the timer, and report the elapsed time"""
            elapsed_time = time.perf_counter() - self._start_time
            self._elapsed_time = f"{elapsed_time:0.4f}"
            self._start_time = None

        def check_minute(self):
            """Log if timer has gone over 60 seconds of processing"""
            # Log critical error if time to collect/process telemetry
            # is over 60 seconds as likely indicative of resource
            # constraints on container e.g. memory leak
            current_time = time.perf_counter() - self._start_time
            if int(current_time) > 60:
                logger.critical(
                    f"{log_prefix} - {current_time}: Process taking over 60 seconds to complete, check container resource utilization or expected latency to reach appliance, certain requests may have timed out"
                )

    def list_tunnel_aliases(tunnels: list) -> list:
        """Format list of dictionaries containing tunnel id's and
        aliases and return all tunnel aliases in flat list

        :param tunnels: Structure of
            [{"id": <tunnel_id>, "alias": <tunnel_alias>}, ...]
        :type tunnels: list
        :return: List of tunnel aliases
        :rtype: list
        """
        # Blank list to populate with tunnel aliases
        alias_list = []
        # If tunnels query was successful, append tunnel aliases to list
        try:
            if tunnels is not False:
                for tunnel in tunnels:
                    alias_list.append(tunnel["alias"])
            else:
                raise NameError("Tunnel data not retrieved, cannot process aliases")
        except Exception as e:
            logger.error(
                f"{log_prefix}{proc_timer.current()}: {e}",
                exc_info=1,
            )
            logger.error(f"tunnels info: {tunnels}")

        return alias_list

    def proc_interface_minute_stats(
        general_ec_tags,
        stat_file,
        interface_labels,
    ) -> list:
        """Process minute stats data for interfaces

        :param general_ec_tags: common metadata to tag data with for
            appliance
        :type general_ec_tags: dict
        :param stat_file: Line text of minute stats for stat type
        :type stat_file: str
        :param interface_labels: Interface label mapping of label names
            and id's
        :type interface_labels: dict
        :return: List of data points to send to InfluxDB
        :rtype: list
        """
        # points object to write to influx
        data_points = []

        for line in stat_file:
            # 63026 - Stats value bug ECOS stats pre 9.1.3.0 & 9.2.2.0
            line = line.replace("18446744073709551615", "0")
            str_stat_list = line.split(",")

            # Identify traffic type
            if str_stat_list[3] == "1":
                traffic_type = "optimized_traffic"
            elif str_stat_list[3] == "2":
                traffic_type = "passthrough_shaped"
            elif str_stat_list[3] == "3":
                traffic_type = "passthrough_unshaped"
            elif str_stat_list[3] == "4":
                traffic_type = "all_traffic"

            # Set values for tags
            tags = general_ec_tags.copy()
            tags["interface_name"] = str_stat_list[1]  # e.g. wan0
            tags["traffic_type"] = traffic_type

            # Set interface label tag, numeric value translated to
            # label name, e.g. 1 may be INET1
            if str_stat_list[2] == "0":
                tags["interface_label"] = "None"
            else:
                tags["interface_label"] = interface_labels[str_stat_list[2]]

            # Assign values to corresponding fields
            fields = {
                "bytes_tx": int(str_stat_list[4]),
                "bytes_rx": int(str_stat_list[5]),
                "packets_tx": int(str_stat_list[6]),
                "packets_rx": int(str_stat_list[7]),
                "overhead_bytes_tx": int(str_stat_list[8]),
                "overhead_bytes_rx": int(str_stat_list[9]),
                "overhead_packets_tx": int(str_stat_list[10]),
                "overhead_packets_rx": int(str_stat_list[11]),
                "firewall_bytes_tx": int(str_stat_list[12]),
                "firewall_bytes_rx": int(str_stat_list[13]),
                "firewall_packets_tx": int(str_stat_list[14]),
                "firewall_packets_rx": int(str_stat_list[15]),
                "max_bandwidth_tx": int(str_stat_list[16]),
                "max_bandwidth_rx": int(str_stat_list[17]),
                # Ignore 18-29
            }

            # Use timestamp from minute data
            timestamp = int(str_stat_list[30])

            # Append formatted data
            data_points.append(
                {
                    "measurement": "interface_stats",
                    "tags": tags,
                    "time": datetime.fromtimestamp(timestamp),
                    "fields": fields,
                }
            )

        return data_points

    def proc_tunnel_minute_stats(
        general_ec_tags,
        stat_file,
        overlay_ids,
    ) -> list:
        """Process minute stats data for tunnels

        :param general_ec_tags: common metadata to tag data with for
            appliance
        :type general_ec_tags: dict
        :param stat_file: Line text of minute stats for stat type
        :type stat_file: str
        :param overlay_ids: Overlay mapping of overlay names
            and id's
        :type overlay_ids: dict
        :return: List of data points to send to InfluxDB
        :rtype: list
        """
        # points object to write to influx
        data_points = []

        for line in stat_file:
            # 63026 - Stats value bug ECOS stats pre 9.1.3.0 & 9.2.2.0
            line = line.replace("18446744073709551615", "0")
            str_stat_list = line.split(",")

            # Mark as SDWAN tunnel if not 0
            if str_stat_list[4] == "0":
                sdwan_tunnel = False
            else:
                sdwan_tunnel = True

            # Set values for tags
            tags = general_ec_tags.copy()
            tags["tunnel_id"] = str_stat_list[1]
            tags["tunnel_alias"] = str_stat_list[2]

            # Set tunnel overlay tag
            if str_stat_list[3] == "0":
                tags["overlay"] = "underlay"
            else:
                tags["overlay"] = overlay_ids[str_stat_list[3]]

            # Assign values to corresponding fields
            fields = {
                "sdwan_tunnel": sdwan_tunnel,
                "bytes_wan_tx": int(str_stat_list[6]),
                "bytes_wan_rx": int(str_stat_list[7]),
                "bytes_lan_tx": int(str_stat_list[8]),
                "bytes_lan_rx": int(str_stat_list[9]),
                "packets_wan_tx": int(str_stat_list[10]),
                "packets_wan_rx": int(str_stat_list[11]),
                "packets_lan_tx": int(str_stat_list[12]),
                "packets_lan_rx": int(str_stat_list[13]),
                "average_latency": int(str_stat_list[14]),  # Milliseconds*100
                "minute_latency": int(
                    str_stat_list[15]
                ),  # Minute latency during the minute Milliseconds*100
                "TCP_flow_count": int(str_stat_list[16]),
                "TCP_Accelerated_flow_count": int(str_stat_list[17]),
                "non-TCP_flow_count": int(str_stat_list[18]),
                "Flows_Created": int(str_stat_list[19]),
                "Flows_Deleted": int(str_stat_list[20]),
                "Lost_Packets_pre-FEC": int(str_stat_list[21]),
                "Lost_Packets_post-FEC": int(str_stat_list[22]),
                "Loss_Pct_pre-FEC": int(
                    str_stat_list[23]
                ),  # Loss Pct * 100 e.g. 0.84% is 84
                "Loss_Pct_post-FEC": int(
                    str_stat_list[24]
                ),  # Loss Pct * 100 e.g. 0.84% is 84
                "Out_of_Order_Packets_pre-POC": int(str_stat_list[25]),
                "Out_of_Order_Packets_post-POC": int(str_stat_list[26]),
                "Out_of_Order_Pct_pre-POC": int(str_stat_list[27]),
                "Out_of_Order_Pct_post-POC": int(str_stat_list[28]),
                "Overhead_wan_rx_packets": int(str_stat_list[29]),
                "Overhead_wan_tx_packets": int(str_stat_list[30]),
                "Overhead_wan_rx_bytes": int(str_stat_list[31]),
                "Overhead_wan_tx_bytes": int(str_stat_list[32]),
                "Overhead_header_wan_rx_bytes": int(str_stat_list[33]),
                "Overhead_header_wan_tx_bytes": int(str_stat_list[34]),
                # Ignore 35, bw utilization percentage - not measured properly
                # Ignore 36-64
                "Post_FEC_MOS_Score_(*100)": int(str_stat_list[65]),
                "Pre_FEC_MOS_Score_(*100)": int(str_stat_list[66]),
                # Ignore 67-68
                "Jitter_(ms)": int(str_stat_list[69]),
                # Ignore 70
            }

            # Use timestamp from minute data
            timestamp = int(str_stat_list[71])
            # Append formatted data
            data_points.append(
                {
                    "measurement": "tunnel_stats",
                    "tags": tags,
                    "time": datetime.fromtimestamp(timestamp),
                    "fields": fields,
                }
            )

        return data_points

    def proc_flow_minute_stats(
        general_ec_tags,
        stat_file,
    ) -> list:
        """Process minute stats data for flows

        :param general_ec_tags: common metadata to tag data with for
            appliance
        :type general_ec_tags: dict
        :param stat_file: Line text of minute stats for stat type
        :type stat_file: str
        :return: List of data points to send to InfluxDB
        :rtype: list
        """
        # points object to write to influx
        data_points = []

        for line in stat_file:
            # 63026 - Stats value bug ECOS stats pre 9.1.3.0 & 9.2.2.0
            line = line.replace("18446744073709551615", "0")
            str_stat_list = line.split(",")

            # Identify flow type
            if str_stat_list[1] == "1":
                flow_type = "TCP Accelerated"
            elif str_stat_list[1] == "2":
                flow_type = "TCP Non-Accelerated"
            elif str_stat_list[1] == "3":
                flow_type = "Non-TCP"

            # Identify traffic type
            if str_stat_list[2] == "1":
                traffic_type = "optimized_traffic"
            elif str_stat_list[2] == "2":
                traffic_type = "passthrough_shaped"
            elif str_stat_list[2] == "3":
                traffic_type = "passthrough_unshaped"
            elif str_stat_list[2] == "4":
                traffic_type = "all_traffic"

            # Set values for tags
            tags = general_ec_tags.copy()
            tags["flow_type"] = flow_type
            tags["traffic_type"] = traffic_type

            fields = {
                "flows_created": int(str_stat_list[3]),
                "flows_deleted": int(str_stat_list[4]),
                "flows_exist": int(str_stat_list[5]),
                # Ignore [6-8]
                "wan_tx_bytes": int(str_stat_list[9]),
                "wan_rx_bytes": int(str_stat_list[10]),
                "lan_tx_bytes": int(str_stat_list[11]),
                "lan_rx_bytes": int(str_stat_list[12]),
                "wan_tx_packets": int(str_stat_list[13]),
                "wan_rx_packets": int(str_stat_list[14]),
                "lan_tx_packets": int(str_stat_list[15]),
                "lan_rx_packets": int(str_stat_list[16]),
                # Ignore [17-24]
            }

            # Use timestamp from minute data
            timestamp = int(str_stat_list[25])
            # Append formatted data
            data_points.append(
                {
                    "measurement": "flow_stats",
                    "tags": tags,
                    "time": datetime.fromtimestamp(timestamp),
                    "fields": fields,
                }
            )

        return data_points

    def proc_boost_minute_stats(
        general_ec_tags,
        stat_file,
    ) -> list:
        """Process minute stats data for boost

        :param general_ec_tags: common metadata to tag data with for
            appliance
        :type general_ec_tags: dict
        :param stat_file: Line text of minute stats for stat type
        :type stat_file: str
        :return: List of data points to send to InfluxDB
        :rtype: list
        """
        # points object to write to influx
        data_points = []

        for line in stat_file:
            # 63026 - Stats value bug ECOS stats pre 9.1.3.0 & 9.2.2.0
            line = line.replace("18446744073709551615", "0")
            str_stat_list = line.split(",")

            # Set values for tags
            tags = general_ec_tags.copy()

            # Assign values to corresponding fields
            fields = {
                "boost_configured_kbps": int(str_stat_list[1]),
                "boost_bytes": int(str_stat_list[2]),
                "seconds_not_boosted_in_minute": int(str_stat_list[3]),
                # Ignore [4]
            }

            # Use timestamp from minute data
            timestamp = int(str_stat_list[5])
            # Append formatted data
            data_points.append(
                {
                    "measurement": "boost_stats",
                    "tags": tags,
                    "time": datetime.fromtimestamp(timestamp),
                    "fields": fields,
                }
            )

        return data_points

    def proc_drops_minute_stats(
        general_ec_tags,
        stat_file,
    ) -> list:
        """Process minute stats data for drops

        :param general_ec_tags: common metadata to tag data with for
            appliance
        :type general_ec_tags: dict
        :param stat_file: Line text of minute stats for stat type
        :type stat_file: str
        :return: List of data points to send to InfluxDB
        :rtype: list
        """
        # points object to write to influx
        data_points = []

        for line in stat_file:
            # 63026 - Stats value bug ECOS stats pre 9.1.3.0 & 9.2.2.0
            line = line.replace("18446744073709551615", "0")
            str_stat_list = line.split(",")

            # Set values for tags
            tags = general_ec_tags.copy()

            drop_reason_code = int(str_stat_list[1])

            # Each number code represents some sort of drops in the
            # system – most of them are normal. Some of them are
            # equivalent to “interface queue drops” on traditional
            # routers. We are interested in these codes:
            # 8 – LAN Rx Queue Full
            # 18 – LAN Tx Queue Full
            # 19 – LAN Tx ZCI Queue Full
            # 31 – Wan Rx Queue Full
            # 53 – Wan Tx ZCI Queue Full

            # Demo code currently aggregates all other drops into single
            # code of "Other"

            if drop_reason_code == 8:
                drop_reason = "LAN Rx Queue Full"
            elif drop_reason_code == 18:
                drop_reason = "LAN Tx Queue Full"
            if drop_reason_code == 19:
                drop_reason = "LAN Tx ZCI Queue Full"
            elif drop_reason_code == 31:
                drop_reason = "WAN Rx Queue Full"
            elif drop_reason_code == 53:
                drop_reason = "WAN Tx ZCI Queue Full"
            else:
                drop_reason = "Other"

            tags["drop_reason"] = drop_reason

            # Assign values to corresponding fields
            fields = {
                "drop_count": int(str_stat_list[2]),
            }

            # Use timestamp from minute data
            timestamp = int(str_stat_list[3])
            # Append formatted data
            data_points.append(
                {
                    "measurement": "drop_stats",
                    "tags": tags,
                    "time": datetime.fromtimestamp(timestamp),
                    "fields": fields,
                }
            )

        return data_points

    def proc_interface_overlay_minute_stats(
        general_ec_tags,
        stat_file,
        interface_labels,
        overlay_map,
    ) -> list:
        """Process minute stats data for overlay

        :param general_ec_tags: common metadata to tag data with for
            appliance
        :type general_ec_tags: dict
        :param stat_file: Line text of minute stats for stat type
        :type stat_file: str
        :param interface_labels: Interface label mapping
        :type interface_labels: dict
        :param overlay_map: Overlay mapping
        :type overlay_map: dict
        :return: List of data points to send to InfluxDB
        :rtype: list
        """
        # points object to write to influx
        data_points = []

        for line in stat_file:
            # 63026 - Stats value bug ECOS stats pre 9.1.3.0 & 9.2.2.0
            line = line.replace("18446744073709551615", "0")
            str_stat_list = line.split(",")

            # Set values for tags
            tags = general_ec_tags.copy()
            tags["interface_name"] = str_stat_list[1]  # e.g. wan0
            tags["tunnel_type"] = int(str_stat_list[4])  # e.g. 0, 1, 2

            # Set interface label tag, numeric value translated to
            # label name, e.g. 1 may be INET1
            if str_stat_list[2] == "0":
                tags["interface_label"] = "None"
            else:
                tags["interface_label"] = interface_labels[str_stat_list[2]]

            # Set overlay label tag, numeric value translated to
            # label name, e.g. 1 may be RealTime
            if str_stat_list[3] == "0":
                tags["overlay"] = "underlay"
            else:
                tags["overlay"] = overlay_map[str_stat_list[3]]

            # Assign values to corresponding fields
            fields = {
                "bytes_tx": int(str_stat_list[5]),
                "bytes_rx": int(str_stat_list[6]),
                "packets_tx": int(str_stat_list[7]),
                "packets_rx": int(str_stat_list[8]),
                "overhead_bytes_tx": int(str_stat_list[9]),
                "overhead_bytes_rx": int(str_stat_list[10]),
                "overhead_packets_tx": int(str_stat_list[11]),
                "overhead_packets_rx": int(str_stat_list[12]),
                "max_bw_tx": int(str_stat_list[13]),
                "max_bw_rx": int(str_stat_list[14]),
                # Ignore 15-22
            }

            # Use timestamp from minute data
            timestamp = int(str_stat_list[23])
            # Append formatted data
            data_points.append(
                {
                    "measurement": "interface_overlay_stats",
                    "tags": tags,
                    "time": datetime.fromtimestamp(timestamp),
                    "fields": fields,
                }
            )

        return data_points

    def proc_memory_stats(
        general_ec_tags,
        ec_memory,
        retrieve_time,
    ) -> list:
        """Process memory stats data from point-in-time retrieval

        :param general_ec_tags: common metadata to tag data with for
            appliance
        :type general_ec_tags: dict
        :param ec_memory: EdgeConnect memory values
        :type ec_memory: dict
        :param retrieve_time: Integer time of values retrieved
        :type retrieve_time: int
        :return: List of data points to send to InfluxDB
        :rtype: list
        """
        # points object to write to influx
        data_points = []

        # Process memory data
        # Set values for tags
        tags = general_ec_tags.copy()

        # Assign values to corresponding fields
        fields = {
            "total_memory": int(ec_memory["total"]),
            "free_memory": int(ec_memory["free"]),
            "buffers": int(ec_memory["buffers"]),
            "cached": int(ec_memory["cached"]),
            "used_memory": int(ec_memory["used"]),
            "swap_total": int(ec_memory["swapTotal"]),
            "swap_free": int(ec_memory["swapFree"]),
            "swap_used": int(ec_memory["swapUsed"]),
        }

        # Use timestamp from when memory data was retrieved
        timestamp = retrieve_time
        # Append formatted data
        data_points.append(
            {
                "measurement": "memory_stats",
                "tags": tags,
                "time": datetime.fromtimestamp(timestamp),
                "fields": fields,
            }
        )

        return data_points

    def proc_cpu_stats(
        general_ec_tags,
        ec_cpu_minute_5sec_interval,
    ) -> list:
        """Process cpu stats data from point-in-time retrieval

        :param general_ec_tags: common metadata to tag data with for
            appliance
        :type general_ec_tags: dict
        :param ec_cpu_minute_5sec_interval: EdgeConnect cpu values
        :type ec_cpu_minute_5sec_interval: dict
        :return: List of data points to send to InfluxDB
        :rtype: list
        """
        # points object to write to influx
        data_points = []

        # Process cpu data
        for cpu_stat in ec_cpu_minute_5sec_interval["data"]:
            cpu_stat_ts = list(cpu_stat.keys())[0]
            for cpu in cpu_stat[cpu_stat_ts]:
                # Set values for tags
                tags = general_ec_tags.copy()
                tags["cpu_number"] = cpu["cpu_number"]

                # Assign values to corresponding fields
                fields = {
                    "cpu_pIdle": float(cpu["pIdle"]),
                    "cpu_pUser": float(cpu["pUser"]),
                    "cpu_pSys": float(cpu["pSys"]),
                    "cpu_pIRQ": float(cpu["pIRQ"]),
                    "cpu_pNice": float(cpu["pNice"]),
                }

                # CPU Timestamp is returned in ms, convert to s for datetime
                timestamp = int(cpu_stat_ts) / 1000
                # Append formatted data
                data_points.append(
                    {
                        "measurement": "cpu_stats",
                        "tags": tags,
                        "time": datetime.fromtimestamp(timestamp),
                        "fields": fields,
                    }
                )

        return data_points

    def proc_route_table_stats(
        general_ec_tags,
        appliance_routes,
        retrieve_time,
    ) -> list:
        """Process memory stats data from point-in-time retrieval

        :param general_ec_tags: common metadata to tag data with for
            appliance
        :type general_ec_tags: dict
        :param appliance_routes: EdgeConnect route table data
        :type appliance_routes: dict
        :param retrieve_time: Integer time of values retrieved
        :type retrieve_time: int
        :return: List of data points to send to InfluxDB
        :rtype: list
        """
        # points object to write to influx
        data_points = []

        # Process alarm data
        # Set values for tags
        tags = general_ec_tags.copy()

        # Calculate route table sizes
        total_route_table_size = appliance_routes["subnets"]["count"]
        total_v4_routes = 0
        total_v6_routes = 0
        for route in appliance_routes["subnets"]["entries"]:
            if route["state"]["version"] == 4:
                total_v4_routes += 1
            elif route["state"]["version"] == 6:
                total_v6_routes += 1
            else:
                pass

        # Assign values to corresponding fields
        fields = {
            "total_routes": total_route_table_size,
            "total_v4_routes": total_v4_routes,
            "total_v6_routes": total_v6_routes,
        }

        # Use timestamp from when route table was retrieved
        timestamp = retrieve_time
        # Append formatted data
        data_points.append(
            {
                "measurement": "route_table_stats",
                "tags": tags,
                "time": datetime.fromtimestamp(timestamp),
                "fields": fields,
            }
        )

        return data_points

    def proc_alarm_stats(
        general_ec_tags,
        ec_alarms,
        retrieve_time,
    ) -> list:
        """Process memory stats data from point-in-time retrieval

        :param general_ec_tags: common metadata to tag data with for
            appliance
        :type general_ec_tags: dict
        :param ec_alarms: EdgeConnect alarm data
        :type ec_alarms: dict
        :param retrieve_time: Integer time of values retrieved
        :type retrieve_time: int
        :return: List of data points to send to InfluxDB
        :rtype: list
        """
        # points object to write to influx
        data_points = []

        # Process alarm data
        # Set values for tags
        tags = general_ec_tags.copy()

        # Assign values to corresponding fields
        fields = {
            "critical_alarms": int(ec_alarms["summary"]["num_critical"]),
            "major_alarms": int(ec_alarms["summary"]["num_major"]),
            "minor_alarms": int(ec_alarms["summary"]["num_minor"]),
            "warning_alarms": int(ec_alarms["summary"]["num_warning"]),
            "cleared_alarms": int(ec_alarms["summary"]["num_cleared"]),
            "outstanding_alarms": int(ec_alarms["summary"]["num_outstanding"]),
            "sw_outstanding_alarms": int(
                ec_alarms["summary"]["num_software_outstanding"]
            ),
            "hw_outstanding_alarms": int(
                ec_alarms["summary"]["num_equipment_outstanding"]
            ),
            "tca_outstanding_alarms": int(ec_alarms["summary"]["num_tca_outstanding"]),
            "traffic_class_outstanding_alarms": int(
                ec_alarms["summary"]["num_traffic_class_outstanding"]
            ),
            "tunnel_outstanding_alarms": int(
                ec_alarms["summary"]["num_tunnel_outstanding"]
            ),
            "raise_ignore_alarms": int(ec_alarms["summary"]["num_raise_ignore"]),
        }

        # Use timestamp from when alarm data was retrieved
        timestamp = retrieve_time
        # Append formatted data
        data_points.append(
            {
                "measurement": "alarm_stats",
                "tags": tags,
                "time": datetime.fromtimestamp(timestamp),
                "fields": fields,
            }
        )

        return data_points

    def proc_tunnel_count_stats(
        general_ec_tags,
        tunnel_summary,
        retrieve_time,
    ) -> list:
        """Process memory stats data from point-in-time retrieval

        :param general_ec_tags: common metadata to tag data with for
            appliance
        :type general_ec_tags: dict
        :param tunnel_summary: EdgeConnect tunnel count data
        :type tunnel_summary: dict
        :param retrieve_time: Integer time of values retrieved
        :type retrieve_time: int
        :return: List of data points to send to InfluxDB
        :rtype: list
        """
        # points object to write to influx
        data_points = []
        # Process tunnel count data
        # Set values for tags
        tags = general_ec_tags.copy()

        # Assign values to corresponding fields
        # Tunnel Summary is preformatted from earlier data retrieval
        # and aggregation
        fields = tunnel_summary.copy()

        # Use timestamp from when tunnel data was retrieved
        timestamp = retrieve_time
        # Append formatted data
        data_points.append(
            {
                "measurement": "tunnel_count_stats",
                "tags": tags,
                "time": datetime.fromtimestamp(timestamp),
                "fields": fields,
            }
        )

        return data_points

    def proc_deployment_info(
        general_ec_tags,
        deployment,
        interface_labels,
        retrieve_time,
    ) -> list:
        """Process memory stats data from point-in-time retrieval

        :param general_ec_tags: common metadata to tag data with for
            appliance
        :type general_ec_tags: dict
        :param deployment: EdgeConnect deployment configuration data
        :type deployment: dict
        :param interface_labels: Interface label mapping of label names
            and id's
        :type interface_labels: dict
        :param retrieve_time: Integer time of values retrieved
        :type retrieve_time: int
        :return: List of data points to send to InfluxDB
        :rtype: list
        """
        # points object to write to influx
        data_points = []

        # Process deployment data
        # Set values for tags
        tags = general_ec_tags.copy()

        # Capture system-level bandwidth
        tags["interface_name"] = "SYSTEM"

        # Assign values to corresponding fields
        fields = {
            "wan_inbound_bw": deployment["sysConfig"]["maxInBW"],
            "wan_outbound_bw": deployment["sysConfig"]["maxBW"],
        }

        # Use timestamp from when deployment data was retrieved
        timestamp = retrieve_time
        # Append formatted data
        data_points.append(
            {
                "measurement": "deployment_info",
                "tags": tags,
                "time": datetime.fromtimestamp(timestamp),
                "fields": fields,
            }
        )

        # Capture all WAN interface configured bandwidth
        for interface in deployment["modeIfs"]:
            # Check for sub-interfaces, if length of 1 no sub-interfaces
            if len(interface["applianceIPs"]) == 1:
                if interface["applianceIPs"][0]["wanSide"] is True:
                    if interface["applianceIPs"][0].get("vlan") is None:
                        wan_int_name = interface["ifName"]
                        wan_int_inbound = interface["applianceIPs"][0]["maxBW"][
                            "inbound"
                        ]
                        wan_int_outbound = interface["applianceIPs"][0]["maxBW"][
                            "outbound"
                        ]
                    else:
                        wan_int_name = f'{interface["ifName"]}.{interface["applianceIPs"][0]["vlan"]}'
                        wan_int_inbound = interface["applianceIPs"][0]["maxBW"][
                            "inbound"
                        ]
                        wan_int_outbound = interface["applianceIPs"][0]["maxBW"][
                            "outbound"
                        ]
                    tags = general_ec_tags.copy()
                    tags["interface_name"] = wan_int_name
                    tags["interface_label"] = interface_labels[
                        interface["applianceIPs"][0]["label"]
                    ]
                    tags["lan/wan"] = "WAN"
                    fields = {
                        "wan_inbound_bw": wan_int_inbound,
                        "wan_outbound_bw": wan_int_outbound,
                    }
                    # Append formatted data
                    data_points.append(
                        {
                            "measurement": "deployment_info",
                            "tags": tags,
                            "time": datetime.fromtimestamp(timestamp),
                            "fields": fields,
                        }
                    )
                else:
                    # LAN Interface
                    pass
            # If sub-interfaces present, iterate through them
            else:
                for sub_interface in interface["applianceIPs"]:
                    if sub_interface["wanSide"] is True:
                        if sub_interface.get("vlan") is None:
                            wan_int_name = interface["ifName"]
                            wan_int_inbound = sub_interface["maxBW"]["inbound"]
                            wan_int_outbound = sub_interface["maxBW"]["outbound"]
                        else:
                            wan_int_name = (
                                f'{interface["ifName"]}.{sub_interface["vlan"]}'
                            )
                            wan_int_inbound = sub_interface["maxBW"]["inbound"]
                            wan_int_outbound = sub_interface["maxBW"]["outbound"]
                        tags = general_ec_tags.copy()
                        tags["interface_name"] = wan_int_name
                        tags["interface_label"] = interface_labels[
                            sub_interface["label"]
                        ]
                        tags["lan/wan"] = "WAN"
                        fields = {
                            "wan_inbound_bw": wan_int_inbound,
                            "wan_outbound_bw": wan_int_outbound,
                        }
                        # Append formatted data
                        data_points.append(
                            {
                                "measurement": "deployment_info",
                                "tags": tags,
                                "time": datetime.fromtimestamp(timestamp),
                                "fields": fields,
                            }
                        )
                    else:
                        # LAN Interface
                        pass

        return data_points

    def proc_disk_stats(
        general_ec_tags,
        ec_disk_usage,
        retrieve_time,
    ) -> list:
        """Process memory stats data from point-in-time retrieval

        :param general_ec_tags: common metadata to tag data with for
            appliance
        :type general_ec_tags: dict
        :param ec_disk_usage: EdgeConnect disk utilization data
        :type ec_disk_usage: dict
        :param retrieve_time: Integer time of values retrieved
        :type retrieve_time: int
        :return: List of data points to send to InfluxDB
        :rtype: list
        """
        # points object to write to influx
        data_points = []

        # Process disk data
        for directory in ec_disk_usage:
            # Set values for tags
            tags = general_ec_tags.copy()
            tags["disk_dir"] = directory

            # Assign values to corresponding fields
            fields = {
                "1k-blocks": int(ec_disk_usage[directory]["1k-blocks"]),
                "used": int(ec_disk_usage[directory]["used"]),
                "available": int(ec_disk_usage[directory]["available"]),
                "used_percent": int(ec_disk_usage[directory]["usedpercent"]),
                "filesystem": ec_disk_usage[directory]["filesystem"],
            }

            # Use timestamp from when disk data was retrieved
            timestamp = retrieve_time
            # Append formatted data
            data_points.append(
                {
                    "measurement": "disk_stats",
                    "tags": tags,
                    "time": datetime.fromtimestamp(timestamp),
                    "fields": fields,
                }
            )

        return data_points

    def proc_system_info_stats(
        general_ec_tags,
        ec_system_info,
        retrieve_time,
    ) -> list:
        """Process memory stats data from point-in-time retrieval

        :param general_ec_tags: common metadata to tag data with for
            appliance
        :type general_ec_tags: dict
        :param ec_system_info: EdgeConnect disk utilization data
        :type ec_system_info: dict
        :param retrieve_time: Integer time of values retrieved
        :type retrieve_time: int
        :return: List of data points to send to InfluxDB
        :rtype: list
        """
        # points object to write to influx
        data_points = []

        # Set values for tags
        tags = general_ec_tags.copy()

        # Process system info data, currently only takes uptime
        # logs it to the existing appliance metatadata measurement
        fields = {
            "uptime": ec_system_info["uptime"],
        }

        # Use timestamp from when system info was retrieved
        timestamp = retrieve_time
        # Append formatted data
        data_points.append(
            {
                "measurement": "appliance_metadata",
                "tags": tags,
                "time": datetime.fromtimestamp(timestamp),
                "fields": fields,
            }
        )

        return data_points

    def proc_realtime_stats(
        general_ec_tags,
        realtime_pps,
        realtime_pps_time,
    ) -> list:
        """Process memory stats data from point-in-time retrieval

        :param general_ec_tags: common metadata to tag data with for
            appliance
        :type general_ec_tags: dict
        :param realtime_pps: EdgeConnect disk utilization data
        :type realtime_pps: dict
        :param realtime_pps_time: Realtime stats timestamp of values
            retrieved, units of microseconds
        :type realtime_pps_time: int
        :return: List of data points to send to InfluxDB
        :rtype: list
        """
        # points object to write to influx
        data_points = []

        # Set values for tags
        tags = general_ec_tags.copy()

        # Process realtime stats data, currently only takes packets
        # per second data
        fields = {
            "pps": realtime_pps,
        }

        # Use timestamp from when system info was retrieved
        # realtime stats uses microseconds, convert to seconds
        # for determining timestamp dividing by 1,000,000
        timestamp = realtime_pps_time / 1000000
        # Append formatted data
        data_points.append(
            {
                "measurement": "realtime",
                "tags": tags,
                "time": datetime.fromtimestamp(timestamp),
                "fields": fields,
            }
        )

        return data_points

    # Map environment variables
    ec_user = os.getenv("EC_USER")
    ec_pw = os.getenv("EC_PW")
    db_url = os.getenv("DB_URL")
    db_token = os.getenv("DB_TOKEN")
    db_org = os.getenv("DB_ORG")
    db_debug = os.getenv("DB_DEBUG")
    db_bucket = os.getenv("DB_BUCKET")
    log_max_bytes = int(os.getenv("LOG_MAX_BYTES"))
    log_max_backups = int(os.getenv("LOG_MAX_BACKUPS"))
    container_hostname = socket.gethostname()

    with MultiprocessingWriter(
        url=db_url,
        token=db_token,
        org=db_org,
        write_options=WriteOptions(batch_size=1000, flush_interval=1000),
        debug=db_debug,
    ) as influx_write_api:

        # Start timing process
        proc_timer = Timer()
        proc_timer.start()

        # Appliance details
        ne_pk = appliance["id"]
        ec_hostname = appliance["hostName"]
        ec_ip = appliance["ip"]

        # Setup log settings for messages and errors
        log_level = os.getenv("LOG_LEVEL")
        logger = logging.getLogger(__name__)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        local_log_directory = "logging/"
        if not os.path.exists(local_log_directory):
            os.makedirs(local_log_directory)
        log_file_handler = RotatingFileHandler(
            f"{local_log_directory}ec-telemetry.log",
            maxBytes=log_max_bytes,
            backupCount=log_max_backups,
        )
        log_file_handler.setFormatter(formatter)
        if log_level == "CRITICAL":
            logger.setLevel(logging.CRTICAL)
        elif log_level == "ERROR":
            logger.setLevel(logging.ERROR)
        elif log_level == "WARNING":
            logger.setLevel(logging.WARNING)
        elif log_level == "INFO":
            logger.setLevel(logging.INFO)
        elif log_level == "DEBUG":
            logger.setLevel(logging.DEBUG)
        elif log_level == None:
            logger.disabled = True
        logger.addHandler(log_file_handler)

        log_prefix = f"cid: {container_hostname} - {ec_hostname} @ {ec_ip} - "

        logger.info(
            f"{log_prefix}{proc_timer.current()}: --------APPLIANCE STARTED--------"
        )
        proc_timer.check_minute()

        # Set tag if appliance is hub or non-hub
        if appliance["networkRole"] == "1":
            network_role = "hub"
        else:
            network_role = "non-hub"

        # Appliance ID & Hostname to tag all data series with
        general_ec_tags = {
            "appliance_id": ne_pk,
            "hostname": ec_hostname,
        }

        appliance_meta_fields = {
            "network_role": network_role,
            "model": appliance["model"],
            "platform": appliance["platform"],
            "software_version": appliance["softwareVersion"],
            "license_display": appliance["license_display"],
            "license_bw": appliance["license_bw"],
            "appliance_state": appliance["state"],
            "appliance_reachability": appliance["reachabilityChannel"],
        }
        # Appliance state to Orchestrator value mapping:
        # 0 - Unknown ( When an appliance is added to Orchestrator, it
        #   is in this state )
        # 1 - Normal ( Appliance is reachable from Orchestrator)
        # 2 - Unreachable ( Appliance is unreachable from Orchestrator )
        # 3 - Unsupported Version ( Orchestrator does not support this
        #   version of the appliance )
        # 4 - Out of Synchronization ( Orchestrator's cache of appliance
        #   configuration/state is out of sync with the
        #   configuration/state on the appliance )
        # 5 - Synchronization in Progress ( Orchestrator is currently
        #   synchronizing appliances's configuration and state )

        # Appliance reachability to Orchestrator value mapping:
        # 0 - Unknown
        # 1 - Orchestrator talks to appliance using HTTP/HTTPS using
        #   user id and password. This is not used for EdgeConnects and
        #   SD-WAN
        # 2 - Appliance connects to Orchestrator using HTTPS Websocket.
        #   Orchestrator uses this permanent connection to
        #   configure/monitor appliance. This is done because Appliance
        #   may be behind a firewall making it hard for Orchestrator to
        #   contact appliance using IP address
        # 4 - Orchestrator sends configuration/monitoring request to
        #   Aruba Cloud Portal which relays those requests to
        #   Appliance. Appliance sends its response to Cloud Portal
        #   which relays it back to Orchestrator

        # Create subdirectory for unpacking and processing appliance
        # minute stat files
        ec_directory = f"stats/temp/{ne_pk}"
        if not os.path.exists(ec_directory):
            os.makedirs(ec_directory)

        appliance_state_time = appliance["time_retrieved"]

        current_stat = "metadata"
        try:
            # Log appliance state/reachability information regardless if
            # appliance is currently reachable from this monitoring script
            tags = general_ec_tags.copy()
            fields = appliance_meta_fields
            timestamp = appliance_state_time
            data_points = [
                {
                    "measurement": "appliance_metadata",
                    "tags": tags,
                    "time": datetime.fromtimestamp(timestamp),
                    "fields": fields,
                }
            ]

            logger.debug(
                f"{log_prefix}{proc_timer.current()}: WRITE APPLIANCE METADATA AND REACHABILITY"
            )
            proc_timer.check_minute()

            # Write appliance metadata and reachability to InfluxDB
            try:
                influx_write_api.write(
                    bucket=db_bucket,
                    record=data_points,
                )
            except Exception as e:
                logger.error(
                    f"{log_prefix}{proc_timer.current()}: Failed sending {current_stat} to InfluxDB, data points and exception below",
                    exc_info=1,
                )
                logger.error(data_points)

        except Exception as e:
            logger.error(
                f"{log_prefix}{proc_timer.current()}: Failed assembling {current_stat} to send to InfluxDB, data points and exception below",
                exc_info=1,
            )
            logger.error(data_points)

        # Check if appliance is reachable before trying to login and
        # perform stats collection
        try:
            logger.debug(f"{log_prefix}{proc_timer.current()}: Ping check")
            proc_timer.check_minute()
            ping_check = os.system(f"ping -c 3 -W 2 {ec_ip}")
            # 0 indicates success
            # 256 indicates unreachable
            # 512 indicates syntax error
            if ping_check == 0:
                pass
            else:
                logger.error(
                    f"{log_prefix}{proc_timer.current()}: FAILED TO PING APPLIANCE - ping response code: {ping_check}"
                )
                # Exit as appliance is unreachable from worker
                # container at this moment and stats cannot be collected
                sys.exit(0)

            # Log into appliance to gather telemetry and metadata mapping
            ec = EdgeConnect(ec_ip, verify_ssl=False)
            login_state = ec.login(ec_user, ec_pw)
            if login_state:
                try:
                    logger.debug(
                        f"{log_prefix}{proc_timer.current()}: GET MINUTE STATS"
                    )
                    proc_timer.check_minute()

                    try:
                        # Gather Minute Stats data from appliance
                        # Determine current minute range of data from appliance
                        # Returns value for 'newest' and 'oldest'
                        ec_min_range = ec.get_appliance_stats_minute_range()
                        # Poll the latest available minute data from appliance
                        newest_minute = int(ec_min_range["newest"])
                        # Set oldest minute to lookback 3 minutes (180 sec)
                        oldest_minute = newest_minute - 180
                        # Set current poll to newest minute data
                        current_poll_minute = newest_minute
                        # Collect appliance minute stats
                        while current_poll_minute > oldest_minute:
                            # Get statistics TGZ from appliance
                            minute_stat = ec.get_appliance_stats_minute_file(
                                f"st2-{current_poll_minute}.tgz",
                            )
                            if type(minute_stat) is bool:
                                logger.error(
                                    f"{log_prefix}{proc_timer.current()}: Retrieve minute stats failed for {datetime.fromtimestamp(current_poll_minute)}",
                                )
                                minute_stats_status = False
                            else:
                                # On success, write TGZ to local file
                                tar_filename = (
                                    f"{ec_directory}/st2-{current_poll_minute}.tgz"
                                )
                                if minute_stat.status_code == 200:
                                    with open(tar_filename, "wb") as stat_file:
                                        for chunk in minute_stat:
                                            stat_file.write(chunk)
                                minute_stats_status = True
                                # Decrement current poll minute
                                current_poll_minute -= 60

                    except Exception as e:
                        logger.error(
                            f"{log_prefix}{proc_timer.current()}: Retrieve minute stats failed",
                            exc_info=1,
                        )
                        minute_stats_status = False

                    logger.debug(
                        f"{log_prefix}{proc_timer.current()}: GET DEPLOYMENT STATS"
                    )
                    proc_timer.check_minute()
                    try:
                        # Get deployment information to understand max interface
                        # and system bandwidths
                        deployment = ec.get_appliance_deployment()
                        deployment_time = int(time.time())
                        deployment_stats_status = True
                        if deployment is False:
                            logger.error(
                                f"{log_prefix}{proc_timer.current()}: Retrieve deployment stats failed"
                            )
                            deployment_stats_status = False

                    except Exception as e:
                        logger.error(
                            f"{log_prefix}{proc_timer.current()}: Retrieve deployment stats failed",
                            exc_info=1,
                        )
                        deployment_stats_status = False

                    logger.debug(
                        f"{log_prefix}{proc_timer.current()}: GET MEMORY STATS"
                    )
                    proc_timer.check_minute()
                    try:
                        # Current memory use (returns current value)
                        ec_memory = ec.get_appliance_memory()
                        ec_memory_time = int(time.time())
                        memory_stats_status = True
                        if ec_memory is False:
                            logger.error(
                                f"{log_prefix}{proc_timer.current()}: Retrieve memory stats failed"
                            )
                            memory_stats_status = False
                    except Exception as e:
                        logger.error(
                            f"{log_prefix}{proc_timer.current()}: Retrieve memory stats failed",
                            exc_info=1,
                        )
                        memory_stats_status = False

                    logger.debug(f"{log_prefix}{proc_timer.current()}: GET CPU STATS")
                    proc_timer.check_minute()
                    try:
                        # Current CPU use (returns 5sec intervals for
                        # whole minute)
                        # If newest_minute wasn't captured from minute
                        # stats, poll for current minute time
                        try:
                            cpu_time = newest_minute * 1000
                        except NameError:
                            cpu_time = int(time.time()) * 1000

                        # Get current CPU utilization
                        ec_cpu_minute_5sec_interval = ec.get_appliance_cpu(0)

                        # If no cpu data retrieved mark as failed
                        # and move on
                        if (
                            ec_cpu_minute_5sec_interval.get("data") is None
                            or ec_cpu_minute_5sec_interval is False
                        ):

                            logger.error(
                                f"{log_prefix}{proc_timer.current()}: Retrieve cpu stats failed",
                            )
                            logger.error(f"CPU values: {ec_cpu_minute_5sec_interval}")
                            cpu_stats_status = False

                        else:
                            cpu_stats_status = True

                    except Exception as e:
                        logger.error(
                            f"{log_prefix}{proc_timer.current()}: Retrieve cpu stats failed",
                            exc_info=1,
                        )
                        cpu_stats_status = False

                    logger.debug(
                        f"{log_prefix}{proc_timer.current()}: GET ROUTE TABLE STATS",
                    )
                    proc_timer.check_minute()
                    try:
                        # Current route table size
                        appliance_routes = ec.get_appliance_subnets()
                        ec_route_time = int(time.time())
                        route_stats_status = True
                        if appliance_routes is False:
                            logger.error(
                                f"{log_prefix}{proc_timer.current()}: Retrieve route stats failed"
                            )
                            route_stats_status = False
                    except Exception as e:
                        logger.error(
                            f"{log_prefix}{proc_timer.current()}: Retrieve route stats failed"
                        )
                        route_stats_status = False

                    logger.debug(f"{log_prefix}{proc_timer.current()}: GET ALARM STATS")
                    proc_timer.check_minute()
                    try:
                        # Get Alarm counts by type (Critical, etc.)
                        ec_alarms = ec.get_appliance_alarms()
                        ec_alarm_time = int(time.time())
                        alarm_stats_status = True
                        if ec_alarms is False:
                            logger.error(
                                f"{log_prefix}{proc_timer.current()}: Retrieve alarm stats failed"
                            )
                            alarm_stats_status = False
                    except Exception as e:
                        logger.error(
                            f"{log_prefix}{proc_timer.current()}: Retrieve alarm stats failed",
                            exc_info=1,
                        )
                        alarm_stats_status = False

                    logger.debug(
                        f"{log_prefix}{proc_timer.current()}: GET TUNNEL COUNTS"
                    )
                    proc_timer.check_minute()

                    try:
                        # Collect all configured tunnel counts
                        total_underlay_sdwan_tunnels = len(
                            ec.get_appliance_all_tunnel_ids()
                        )
                        total_overlay_tunnels = len(
                            ec.get_appliance_all_bonded_tunnel_ids()
                        )
                        total_third_party_tunnels = len(
                            ec.get_appliance_all_3rdparty_tunnel_ids()
                        )
                        # Collect up tunnel counts
                        up_underlay_sdwan_tunnels = len(
                            ec.get_appliance_all_tunnel_ids(state_match="Up")
                        )
                        up_overlay_tunnels = len(
                            ec.get_appliance_all_bonded_tunnel_ids(state_match="Up")
                        )
                        up_third_party_tunnels = len(
                            ec.get_appliance_all_3rdparty_tunnel_ids(state_match="Up")
                        )
                        # Collect down underlay tunnel information
                        down_underlay_sdwan_tunnels = ec.get_appliance_tunnel_aliases(
                            limit=1000,
                            state_match="Down",
                        )

                        # Assemble down underlay tunnel aliases to list
                        down_underlay_sdwan_tunnels_aliases = list_tunnel_aliases(
                            down_underlay_sdwan_tunnels
                        )
                        # Collect down overlay tunnel information
                        down_overlay_tunnels = ec.get_appliance_bonded_tunnel_aliases(
                            limit=1000,
                            state_match="Down",
                        )
                        # Assemble down overlay tunnel aliases to list
                        down_overlay_tunnels_aliases = list_tunnel_aliases(
                            down_overlay_tunnels
                        )
                        # Collect down third party tunnel information
                        down_third_party_tunnels = (
                            ec.get_appliance_3rdparty_tunnel_aliases(
                                limit=1000,
                                state_match="Down",
                            )
                        )
                        # Assemble down thid party tunnel aliases to list
                        down_third_party_tunnels_aliases = list_tunnel_aliases(
                            down_third_party_tunnels
                        )

                        # Combine down tunnels into string for easy storage
                        underlay_down_tunnels = ""
                        overlay_down_tunnels = ""
                        third_party_down_tunnels = ""

                        if len(down_underlay_sdwan_tunnels_aliases) > 0:
                            for tunnel in down_underlay_sdwan_tunnels_aliases:
                                underlay_down_tunnels += f"{tunnel},"
                        if len(down_overlay_tunnels_aliases) > 0:
                            for tunnel in down_overlay_tunnels_aliases:
                                overlay_down_tunnels += f"{tunnel},"
                        if len(down_third_party_tunnels_aliases) > 0:
                            for tunnel in down_third_party_tunnels_aliases:
                                third_party_down_tunnels += f"{tunnel},"

                        tunnel_summary = {
                            "underlay_sdwan_tunnels": total_underlay_sdwan_tunnels,
                            "overlay_sdwan_tunnels": total_overlay_tunnels,
                            "third_party_tunnels": total_third_party_tunnels,
                            "up_underlay_sdwan_tunnels": up_underlay_sdwan_tunnels,
                            "up_overlay_sdwan_tunnels": up_overlay_tunnels,
                            "up_third_party_tunnels": up_third_party_tunnels,
                            "down_underlay_sdwan_tunnels": len(
                                down_underlay_sdwan_tunnels
                            ),
                            "down_overlay_sdwan_tunnels": len(down_overlay_tunnels),
                            "down_third_party_tunnels": len(down_third_party_tunnels),
                            "underlay_down_tunnels": underlay_down_tunnels,
                            "overlay_down_tunnels": overlay_down_tunnels,
                            "third_party_down_tunnels": third_party_down_tunnels,
                        }

                        tunnel_summary_time = int(time.time())
                        tunnel_count_stats_status = True
                    except Exception as e:
                        logger.error(
                            f"{log_prefix}{proc_timer.current()}: Retrieve tunnel count stats failed",
                            exc_info=1,
                        )
                        tunnel_count_stats_status = False

                    logger.debug(f"{log_prefix}{proc_timer.current()}: GET DISK STATS")
                    proc_timer.check_minute()
                    try:
                        # Get disk usage stats
                        ec_disk_usage = ec.get_appliance_disk_usage()
                        ec_disk_usage_time = int(time.time())
                        disk_stats_status = True
                    except Exception as e:
                        logger.error(
                            f"{log_prefix}{proc_timer.current()}: Retrieve disk stats failed",
                            exc_info=1,
                        )
                        disk_stats_status = False

                    logger.debug(f"{log_prefix}{proc_timer.current()}: GET SYSTEM INFO")
                    proc_timer.check_minute()
                    try:
                        # Get system info
                        ec_system_info = ec.get_appliance_system_info()
                        ec_system_info_time = int(time.time())
                        system_info_status = True
                        if ec_system_info is False:
                            logger.error(
                                f"{log_prefix}{proc_timer.current()}: Retrieve system info failed"
                            )
                            system_info_status = False
                    except Exception as e:
                        logger.error(
                            f"{log_prefix}{proc_timer.current()}: Retrieve system info failed",
                            exc_info=1,
                        )
                        system_info_status = False

                    logger.debug(
                        f"{log_prefix}{proc_timer.current()}: GET REALTIME STATS"
                    )
                    proc_timer.check_minute()
                    try:
                        # Get realtime stats packets per second
                        realtime_traffic = ec.get_appliance_realtime_stats(
                            stat_type="trafficType",
                            stat_name="3",
                        )

                        realtime_pps = (
                            realtime_traffic["LRX_PKTS"][0][1]
                            + realtime_traffic["LTX_PKTS"][0][1]
                            + realtime_traffic["WRX_PKTS"][0][1]
                            + realtime_traffic["WTX_PKTS"][0][1]
                        )

                        realtime_pps_time = realtime_traffic["LRX_PKTS"][0][0]

                        pps_status = True
                        if realtime_traffic is False:
                            logger.error(
                                f"{log_prefix}{proc_timer.current()}: Retrieve realtime traffic stats failed"
                            )
                            pps_status = False
                    except Exception as e:
                        logger.error(
                            f"{log_prefix}{proc_timer.current()}: Retrieve realtime traffic stats failed",
                            exc_info=1,
                        )
                        pps_status = False

                    logger.debug(
                        f"{log_prefix}{proc_timer.current()}: LOGGING OUT OF APPLIANCE"
                    )
                    proc_timer.check_minute()
                    try:
                        # Logout from appliance once all telemetry gathered
                        ec.logout()
                    except Exception as e:
                        logger.error(
                            f"{log_prefix}{proc_timer.current()}: ERROR LOGGING OUT OF APPLIANCE",
                            exc_info=1,
                        )

                except Exception as e:
                    ec.logout()
                    logger.error(
                        f"{log_prefix}{proc_timer.current()}: ERROR ENCOUNTED WHEN CONNECTED TO APPLIANCE, LOGGING OUT",
                        exc_info=1,
                    )

                # Process collected stats and write to InfluxDB
                if minute_stats_status is True:
                    # Unpack and remove tar files for minute stats
                    try:
                        logger.debug(
                            f"{log_prefix}{proc_timer.current()}: UNPACK MINUTE STATS",
                        )
                        # Unpack all Minute Stat TGZ files
                        for tgz_file in os.listdir(ec_directory):
                            if tgz_file.endswith(".tgz"):
                                # Uncompress TGZ
                                tfile = f"{ec_directory}/{tgz_file}"
                                tar = tarfile.open(tfile)
                                tar.extractall(ec_directory)
                                # Remove original TGZ
                                os.remove(tfile)
                            else:
                                pass
                    except Exception as e:
                        logger.error(
                            f"{log_prefix}{proc_timer.current()}: Failed unpacking minute stat tgz files",
                            exc_info=1,
                        )

                    # Unpack minute statistics and write to InfluxDB
                    for stats_folder in os.listdir(ec_directory):
                        stat_base_dir = f"{ec_directory}/{stats_folder}"
                        logger.debug(
                            f"{log_prefix}{proc_timer.current()}: PROCESS MINUTE STATS -- stats: {stats_folder}"
                        )
                        proc_timer.check_minute()

                        stats_filenames = [
                            "interface_v2.txt",
                            "tunnel_v2.txt",
                            "flow_v2.txt",
                            "boost_v2.txt",
                            "drops_v2.txt",
                            "interface_overlay_v2.txt",
                        ]

                        for stat_filename in stats_filenames:
                            current_stat = f"minute: {stat_filename}"
                            logger.debug(
                                f"{log_prefix}{proc_timer.current()}: PROCESS {current_stat} from {stats_folder}"
                            )

                            try:
                                # Process stats file
                                # Log error if file not present and list
                                # directory contents
                                if (
                                    os.path.exists(f"{stat_base_dir}/{stat_filename}")
                                    is False
                                ):
                                    logger.error(
                                        f"{log_prefix}{proc_timer.current()}: {stat_filename} not present in {stats_folder}"
                                    )
                                    # Log directory contents if expected
                                    # file is not present
                                    try:
                                        contents = os.listdir(stat_base_dir)
                                        logger.error(
                                            f"{log_prefix}{proc_timer.current()}: directory contents {contents}"
                                        )
                                    except Exception as e:
                                        logger.error(
                                            f"{log_prefix}{proc_timer.current()}: Could not log directory contents",
                                            exc_info=1,
                                        )

                                # Log error if file is present but empty
                                elif (
                                    os.stat(f"{stat_base_dir}/{stat_filename}").st_size
                                    == 0
                                ):
                                    logger.warning(
                                        f"{log_prefix}{proc_timer.current()}: {stat_filename} BLANK in {stats_folder}",
                                    )
                                # Else, process file based on stat type
                                else:
                                    if stat_filename == "interface_v2.txt":
                                        with open(
                                            f"{stat_base_dir}/{stat_filename}",
                                            "r",
                                        ) as stat_file:
                                            data_points = proc_interface_minute_stats(
                                                general_ec_tags,
                                                stat_file,
                                                appliance["interface_labels_map"],
                                            )
                                    elif stat_filename == "tunnel_v2.txt":
                                        with open(
                                            f"{stat_base_dir}/{stat_filename}",
                                            "r",
                                        ) as stat_file:
                                            data_points = proc_tunnel_minute_stats(
                                                general_ec_tags,
                                                stat_file,
                                                appliance["overlay_id_map"],
                                            )
                                    elif stat_filename == "flow_v2.txt":
                                        with open(
                                            f"{stat_base_dir}/{stat_filename}",
                                            "r",
                                        ) as stat_file:
                                            data_points = proc_flow_minute_stats(
                                                general_ec_tags,
                                                stat_file,
                                            )
                                    elif stat_filename == "boost_v2.txt":
                                        with open(
                                            f"{stat_base_dir}/{stat_filename}",
                                            "r",
                                        ) as stat_file:
                                            data_points = proc_boost_minute_stats(
                                                general_ec_tags,
                                                stat_file,
                                            )
                                    elif stat_filename == "drops_v2.txt":
                                        with open(
                                            f"{stat_base_dir}/{stat_filename}",
                                            "r",
                                        ) as stat_file:
                                            data_points = proc_drops_minute_stats(
                                                general_ec_tags,
                                                stat_file,
                                            )
                                    elif stat_filename == "interface_overlay_v2.txt":
                                        with open(
                                            f"{stat_base_dir}/{stat_filename}",
                                            "r",
                                        ) as stat_file:
                                            data_points = (
                                                proc_interface_overlay_minute_stats(
                                                    general_ec_tags,
                                                    stat_file,
                                                    appliance["interface_labels_map"],
                                                    appliance["overlay_id_map"],
                                                )
                                            )
                                    # Logic to process additional
                                    # minute stat files would be here
                                    #
                                    # If files do not match any
                                    # processing logic move on to next
                                    # file or directory
                                    else:
                                        continue

                                    logger.debug(
                                        f"{log_prefix}{proc_timer.current()}: WRITE {current_stat} from {stats_folder}"
                                    )
                                    proc_timer.check_minute()

                                    # Write interface stats to InfluxDB
                                    try:
                                        influx_write_api.write(
                                            bucket=db_bucket,
                                            record=data_points,
                                        )
                                    except Exception as e:
                                        logger.error(
                                            f"{log_prefix}{proc_timer.current()}: Failed sending {current_stat} to InfluxDB, data points and exception below",
                                            exc_info=1,
                                        )
                                        logger.error(data_points)

                            except Exception as e:
                                logger.error(
                                    f"{log_prefix}{proc_timer.current()}: Failed processing {current_stat}",
                                    exc_info=1,
                                )

                else:
                    pass

                # Loop over processing point-in-time stats
                point_in_time_stats = [
                    "deployment_info",
                    "memory",
                    "cpu",
                    "route_table",
                    "alarms",
                    "tunnel_counts",
                    "disk",
                    "system_info",
                    "pps",
                ]
                for pit_stat in point_in_time_stats:
                    current_stat = f"point-in-time: {pit_stat}"
                    logger.debug(
                        f"{log_prefix}{proc_timer.current()}: PROCESS {current_stat}"
                    )
                    proc_timer.check_minute()

                    try:
                        if (
                            pit_stat == "deployment_info"
                            and deployment_stats_status is True
                        ):
                            # Process deployment info
                            data_points = proc_deployment_info(
                                general_ec_tags,
                                deployment,
                                appliance["interface_labels_map"],
                                deployment_time,
                            )
                        elif pit_stat == "memory" and memory_stats_status is True:
                            # Process memory stats
                            data_points = proc_memory_stats(
                                general_ec_tags,
                                ec_memory,
                                ec_memory_time,
                            )
                        elif pit_stat == "cpu" and cpu_stats_status is True:
                            # if ec_cpu_minute_5sec_interval["data"] is not None:
                            # Process cpu stats
                            data_points = proc_cpu_stats(
                                general_ec_tags,
                                ec_cpu_minute_5sec_interval,
                            )
                        elif pit_stat == "route_table" and route_stats_status is True:
                            # Current route table size
                            data_points = proc_route_table_stats(
                                general_ec_tags, appliance_routes, ec_route_time
                            )
                        elif pit_stat == "alarms" and alarm_stats_status is True:
                            # Process alarm stats
                            data_points = proc_alarm_stats(
                                general_ec_tags,
                                ec_alarms,
                                ec_alarm_time,
                            )
                        elif (
                            pit_stat == "tunnel_counts"
                            and tunnel_count_stats_status is True
                        ):
                            # Process tunnel count stats
                            data_points = proc_tunnel_count_stats(
                                general_ec_tags,
                                tunnel_summary,
                                tunnel_summary_time,
                            )
                        elif pit_stat == "disk" and disk_stats_status is True:
                            # Process disk stats
                            data_points = proc_disk_stats(
                                general_ec_tags,
                                ec_disk_usage,
                                ec_disk_usage_time,
                            )
                        elif pit_stat == "system_info" and system_info_status is True:
                            # Process system info
                            data_points = proc_system_info_stats(
                                general_ec_tags,
                                ec_system_info,
                                ec_system_info_time,
                            )
                        elif pit_stat == "pps" and pps_status is True:
                            # Process packets per second
                            data_points = proc_realtime_stats(
                                general_ec_tags,
                                realtime_pps,
                                realtime_pps_time,
                            )

                        stat_processing = True

                    except Exception as e:
                        logger.error(
                            f"{log_prefix}{proc_timer.current()}: Failed processing {current_stat}, data points included in debug and exception follow in debug",
                            exc_info=1,
                        )
                        logger.debug(data_points)
                        stat_processing = False
                        # if stat fails and is cpu, log detailed output
                        # from cpu query response
                        if pit_stat == "cpu":
                            logger.error(ec_cpu_minute_5sec_interval)

                    if stat_processing:
                        try:
                            influx_write_api.write(
                                bucket=db_bucket,
                                record=data_points,
                            )
                        except Exception as e:
                            logger.error(
                                f"{log_prefix}{proc_timer.current()}: Failed sending {current_stat} to InfluxDB, data points and exception below",
                                exc_info=1,
                            )
                            logger.error(data_points)

                # Remove minute stats folders once data is sent to InfluxDB
                for stats_folder in os.listdir(ec_directory):
                    shutil.rmtree(f"{ec_directory}/{stats_folder}")

                logger.info(
                    f"{log_prefix}{proc_timer.current()}: --------APPLIANCE COMPLETED--------"
                )

            else:
                logger.error(f"{log_prefix}{proc_timer.current()}: FAILED TO LOGIN")

        except SystemExit:
            # Only called if script could not ping appliance
            pass
        except Exception as e:
            logger.error(
                f"{log_prefix}{proc_timer.current()}: Exception occured",
                exc_info=1,
            )
        finally:
            proc_timer.stop()
            influx_write_api.terminate()
            return
