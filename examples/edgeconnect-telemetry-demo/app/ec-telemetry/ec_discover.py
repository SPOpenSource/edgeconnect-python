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

import json
import logging
import os
import time
from logging.handlers import RotatingFileHandler

import redis
from influxdb_client import InfluxDBClient
from rq import Queue
from rq.registry import FailedJobRegistry, ScheduledJobRegistry

from pyedgeconnect import Orchestrator

# Define Redis instance and Queue to connect to
r = redis.Redis(host="redis", port=6379)
q = Queue("ectelem", connection=r, failure_ttl=3600, result_ttl=0)

# Setup log settings for messages and errors
log_max_bytes = int(os.getenv("LOG_MAX_BYTES"))
log_max_backups = int(os.getenv("LOG_MAX_BACKUPS"))
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
# Set logging severity level from environment variable
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

# Map environment variables
db_url = os.getenv("DB_URL")
db_token = os.getenv("DB_TOKEN")
db_org = os.getenv("DB_ORG")
db_bucket = os.getenv("DB_BUCKET")
orch_url = os.getenv("ORCH_URL")
orch_api_key = os.getenv("ORCH_API_KEY")

# On first run, empty previous task queues
# Empty Failed Queue
failed_registry = FailedJobRegistry(queue=q)
for job_id in failed_registry.get_job_ids():
    failed_registry.remove(job_id, delete_job=True)
# Empty Main Queue
main_registry = ScheduledJobRegistry(queue=q)
for job_id in main_registry.get_job_ids():
    main_registry.remove(job_id, delete_job=True)

# Run loop on telemetry collection queueing for appliances
while True:

    # Start log
    logger.critical("*** --- *** --- EC TELEMETRY NEW QUEUE STARTING --- *** --- ***")

    # Instantiate Orchestrator for discovering appliances
    orch = Orchestrator(
        orch_url,
        api_key=orch_api_key,
        verify_ssl=False,
    )

    logger.debug(f"CONFIGURED ORCH: {orch_url}")
    logger.debug(f"CONFIGURED DB: {db_url}")

    # Check reachability to Orchestrator, raise exception/log if unable
    orch_confirm_auth = orch.get_orchestrator_hello()
    # Check reachability to InfluxDB, raise exception/log if unable
    db_test_client = InfluxDBClient(
        url=db_url,
        token=db_token,
        org=db_org,
    )
    db_health = db_test_client.health()

    # Validate response checks for Orchestrator and InfluxDB
    if (
        orch_confirm_auth != "There was an internal server error."
        and orch_confirm_auth is not False
    ):
        logger.debug("ORCH REACHABLE")
        if db_health.status == "pass":
            logger.debug("DB REACHABLE")
            ready_to_retrieve = True
        else:
            logger.critical("DB UNREACHABLE -- NO DATA RETRIEVED/PROCESSED")
            logger.error(db_health)
            ready_to_retrieve = False

    else:
        logger.critical(
            "ORCH AUTH FAILED OR UNREACHABLE -- NO DATA RETRIEVED/PROCESSED"
        )
        ready_to_retrieve = False

    # Delete tes connection to InfluxDB
    db_test_client.__del__()

    # If Orchestrator and InfluxDB are reachable,
    # begin telemetry collection
    if ready_to_retrieve:

        # Get appliances and determine reachability
        logger.debug(f"Retrieving appliance data from Orchestrator")
        appliances = orch.get_appliances()
        appliance_state_time = int(time.time())

        # Get interface labels from Orchestrator and map the interface
        # labels into a flat dictionary
        logger.debug(f"Retrieving interface label data from Orchestrator")
        orch_int_labels = orch.get_all_interface_labels()
        interface_labels = {}
        for label in orch_int_labels["wan"]:
            interface_labels[label] = orch_int_labels["wan"][label]["name"]
        for label in orch_int_labels["lan"]:
            interface_labels[label] = orch_int_labels["lan"][label]["name"]

        # Get overlay ids from Orchestrator and map the overlay ids into
        # a flat dictionary
        logger.debug(f"Retrieving overlay data from Orchestrator")
        overlays = orch.get_all_overlays_config()
        overlay_ids = {}
        for overlay in overlays:
            overlay_ids[str(overlay["id"])] = overlay["name"]

        # Get appliance licensing information from Orchestrator
        logger.debug(f"Retrieving appliance licensing data from Orchestrator")
        licensing = orch.get_portal_licensed_appliances()

        # Limit appliances to submit to job queue if any are specified
        # in the limit_appliances.json file
        limit_filename = "/app/ec-telemetry/limit_appliances.json"
        with open(limit_filename) as limit_file:
            appliance_subset = json.load(limit_file)["appliance_subset"]

        # Create flat list of all appliance hostnames in Orchestrator
        # to reverse check against appliances listed in
        # limit_appliances.json file to log error if appliance
        # referenced that does not exist
        all_appliance_hostnames = []
        for appliance in appliances:
            all_appliance_hostnames.append(appliance["hostName"])

        appliance_set = []
        # If appliances are listed in the limit file, filter only
        # appliances with matching hostnames to job queue.
        if len(appliance_subset) > 0:
            for appliance in appliances:
                if appliance["hostName"] in appliance_subset:
                    appliance_set.append(appliance)
            for appliance in appliance_subset:
                if appliance not in all_appliance_hostnames:
                    logger.error(
                        f"No appliance with hostname {appliance} found in Orchestrator, please update limit_appliances.json contents"
                    )
        # If no appliances are listed in the limit file, add the first
        # four currently reachable appliancesto the queue and add their
        # hostnames to the limit file
        else:
            num_random_appliances = 4
            logger.warning("No appliances listed in limit_appliances.json file")
            random_appliances = []
            while len(appliance_set) < num_random_appliances:
                for appliance in appliances:
                    if len(appliance_set) == num_random_appliances:
                        break
                    elif appliance["state"] == 1:
                        appliance_set.append(appliance)
                        logger.critical(
                            f"adding {appliance['hostName']} to process list"
                        )
                        logger.critical(
                            f"Total appliances to be collected: {len(appliance_set)}"
                        )
                        random_appliances.append(appliance["hostName"])

                if (
                    len(appliance_set) > 0
                    and len(appliance_set) < num_random_appliances
                ):
                    logger.critical(
                        f"{len(appliance_set)} appliances were currently reachable from Orchestrator"
                    )
                    break
                elif len(appliance_set) == 0:
                    logger.critical(
                        f"No appliances were currently reachable from Orchestrator"
                    )
                    break

            if len(appliance_set) != 0:
                new_appliance_subset = {}
                new_appliance_subset["appliance_subset"] = random_appliances
                with open(limit_filename, "w") as limit_file:
                    json.dump(new_appliance_subset, limit_file)
                logger.warning(
                    f"Proceeding collection for these reachable appliances {random_appliances}"
                )
                logger.warning(
                    "Please update limit_appliances.json to change which appliances telemetry is collected from"
                )

        if len(appliance_set) > 0:
            # Append licensing information into appliance list
            for appliance in appliance_set:
                for license_item in licensing:
                    if license_item["applianceId"] == appliance["id"]:
                        appliance["license_display"] = license_item["licenses"]["fx"][
                            "tier"
                        ]["display"]
                        appliance["license_bw"] = license_item["licenses"]["fx"][
                            "tier"
                        ]["bandwidth"]

            # Append interface mapping and overlay mapping to appliance list
            # before submitting appliances to job queue
            for appliance in appliance_set:
                appliance["interface_labels_map"] = interface_labels
                appliance["overlay_id_map"] = overlay_ids
                appliance["time_retrieved"] = appliance_state_time

            logger.info(f"SENDING APPLIANCES TO QUEUE: {len(appliance_set)}")

            # Queue each appliance object for workers to process
            for appliance in appliance_set:
                task = q.enqueue(
                    "ec_telemetry.ec_data_gather",
                    appliance,
                )
        else:
            logger.critical(
                "No appliances added to collection queue, waiting 60 sec until next attempt"
            )
        # If appliances have been queued, wait 60 seconds until next run
        time.sleep(60)

    # If not ready to retrieve (Orchestrator or Influxdb fail
    # reachability check), try again in 3 seconds
    else:
        time.sleep(3)
