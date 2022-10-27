.. upload_security_policy:


.. important::

    The following example is more complex code than the general examples,
    generating data and interacting with Orchestrator. Using and
    modifying these examples requires a greater understanding of python
    functions, handling variables, and conforming source data to your
    own environment.

    Updating the security policy of an EdgeConnect, especially with
    automation, should be treated with caution as a bad firewall policy
    could allow unwanted traffic or block unintended production traffic.
    This code example is not meant to check the intent of any rules,
    simply show how policy can be uploaded in an automated fashion.

.. note::

    The code referenced in this document and all published examples
    with pyedgeconnect are available from the GitHub repository within the
    `examples <https://github.com/SPOpenSource/edgeconnect-python/tree/main/examples>`_
    folder. Each example script contains logic to authenticate to the
    Orchestrator as documented in the authentication example.

    Clone the repository and download the examples with:

    .. code:: bash

        $ git clone https://github.com/SPOpenSource/edgeconnect-python.git

Upload EdgeConnect Security Policy
************************************

This example uses a CSV file as source data to generate a security
policy for EdgeConnect. The security policy can be uploaded to a net-new
Template Group to later be applied to multiple appliances or pushed
directly to a single appliance.

The client running the script communicates with Orchestrator, and
Orchestrator in turn passes the data to the Edge Connect appliance if
pushing policy directly to an appliance.

EdgeConnect Firewall Zone Behavior
==================================

Prior to Orchestrator 9+, Zone firewall rules are required for the
source Zone to the assigned Zone of the overlay the traffic will match
into as well as rules for egressing the overlay Zone to the final
destination Zone.

For example:

Traffic is sourced from a LAN-side Zone of "Users", crossing into
the Overlays, all of which have a zone of "Fabric", and finally when
reaching the far-end, egressing to a zone of "Protected."

For a rule to allow ``192.0.2.0/24`` from ``Users`` to ``198.51.100.0/24`` in
``Protected`` there would be two rules required:

    .. list-table::
        :header-rows: 1

        * - From Zone
          - To Zone
          - Source IP
          - Dest IP
        * - Users
          - Fabric
          - 192.0.2.0/24
          - 198.51.100.0/24
        * - Fabric
          - Protected
          - 192.0.2.0/24
          - 198.51.100.0/24

For Orchestrator 9+, on the Firewall Zone Secuirty Policies page
(``Configuration -> Overlays & Security -> Security -> Firewall Zone Security Policies``)
there is a toggle for ``New Firewall Zoning``. When enabled, this allows
rules to account for end-to-end behavior and no longer requires zones
for the overlays. For the same use case there would be a single rule:

    .. list-table::
        :header-rows: 1

        * - From Zone
          - To Zone
          - Source IP
          - Dest IP
        * - Users
          - Protected
          - 192.0.2.0/24
          - 198.51.100.0/24


Python Script & Orchestrator API calls
======================================

The script will first check in with Orchestrator to pull information
to correlate object id's to the friendly names used in the source data
such as appliance hostname, zone names, and overlay names.

.. note::

    Zones referenced in the policy must already exist in Orchestrator.
    While there are pyedgeconnect functions to create Zones, this
    example does not create previously undefined Zones from the ruleset
    in Orchestrator.

    The example data included in the file ``security_policy.csv`` must
    be updated accordingly for your environment referencing appropriate
    security zones, rule priorites, merge settings and/or default
    logging levels where applicable.

    IP Ranges used in sample rules follow RFC 5735 as example ranges

For each rule specified, add match criteria to the ruleset with the
specified priority and within the appropriate zone pair.

Once the ruleset is complete, the security map will be installed to the
specified new Template Group or appliance directly per the runtime
arguments.

.. note::

    To reference all possible match criteria fields, get existing
    security policy from an EdgeConnect to see the corresponding JSON.
    This can be proxied through Orchestrator with
    :func:`pyedgeconnect.Orchestrator.appliance_get_api` while
    specifying the nePk of the appliance to the endpoint
    ``/securityMaps``, or connecting directly to the appliance with
    :func:`pyedgeconnect.EdgeConnect.get_appliance_security_policy_map`


Runtime arguments
^^^^^^^^^^^^^^^^^

The python script has multiple runtime arguments defined. The primary
required argument is ``-c`` or ``--csv`` to specify the CSV file to be
read as source data for generating the security policy.

The destination of the rules will depend on one of the two following
options:

* Use ``-a`` or ``--appliance`` to specify the appliance hostname to
  apply the policy to directly
* Use ``-tg`` or ``--templategroup`` to specify the name of a new
  Template Group to be created with the security policy selected

Running the script and pushing rules to an appliance named MY-APPLIANCE-01:

.. code-block:: bash

    python upload_security_policy.py -c security_policy.csv -a MY-APPLIANCE-01

Additional availble runtime arguments are as follows:

- ``-dll`` or ``--denyloglevel``
    - Type: Integer
    - Desc: Specify the Log Level for deny all log events
    - Example values: ``0`` for none or ``8`` for debug
    - Default value: ``2``
- ``-m`` or ``--merge``
    - Type: Boolean
    - Desc: Merge rules with existing rules on appliance, will overwrite
      rules with same priority value in a zone pair. Including the
      ``-m`` will translate to ``True``, no option will default to
      ``False``
    - Default value: ``False``
- ``-o`` or ``--orch``
    - Type: String
    - Desc: Specify the Orchestrator IP or FQDN
    - Example values: ``192.0.2.100`` or ``orchestrator.<company>.com``
    - Default value: ``None``

Running the script and pushing rules to a Template Group named
Group-Sec-Policy set to merge and default log level of 3:

.. code-block:: bash

    python upload_security_policy.py -c security_policy.csv -tg Group-Sec-Policy -m -dll 3


CSV File / Source Data for Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this example the source data for generating a security ruleset is a
CSV file. The variables referenced in the match criteria of the python
correspond to the headers in the CSV file.

.. important::

    The included CSV file has headers for all possible match criteria
    as of Orchestrator 9.1. As new match criteria is introduced it may
    be necessary to add columns in the CSV and if-statements in the
    python to add appropriate criteria for new options. Similarly,
    columsn for paramters that are unused in the rules are not necessary
    to be present in the CSV file.

    In the opposite direction, features such as Address or Service
    groups were only introduced in Orchestrator 9.1, and would not apply
    to policy for a pre-9.1 environment.

.. note::

    * EdgeConnect 8.x only supports ~600 rules
    * This script only supports a maximum of 1000 rules
    * Rule priorities for appliance ruleset should be in the range of 25000+
    * Rule priorities for template group policies should be between 1000-9999

Below is a reference for the values currently supported for the CSV file.

The columns ``rule_priority``, ``action``, ``src_zone``, and
``dst_zone`` are required, other headers are optional.

* ``rule_priority``: The priority of the rule in the zone pair
* ``action``: Allow or deny matching traffic, e.g. ``allow`` or ``deny``
* ``src_zone``: Source Firewall Zone, e.g. ``Corp``
* ``dst_zone``: Destination Firewall Zone, e.g. ``Public``
* ``acl``: Name of ACL to match
* ``src_ip``: Source IP Address to match, e.g. ``192.0.2.0/24``
* ``dst_ip``: Destination IP Address to match, e.g. ``8.8.8.8/32``
* ``either_ip``: Source or Destination IP Address to match
* ``src_addrgrp_groups``: Source Address Group
* ``dst_addrgrp_groups``: Destination Address Group
* ``either_addrgrp_groups``: Source or Destination Address Group
* ``protocol``: Protocol to match, e.g. ``ip``, ``icmp``
* ``src_port``: Source IP Port to match, e.g. ``162``
* ``dst_port``: Destination IP Port to match, e.g. ``443``
* ``vlan``: Interface to match on, e.g. ``lan0``, ``lan0.10``
* ``application``: Application name to match (built-in or user-defined)
* ``app_group``: Application group name to match (built-in or user-defined)
* ``dscp``: DSCP marking to match, e.g. ``af11``
* ``src_dns``: Source DNS to match
* ``dst_dns``: Destination DNS to match, e.g. ``*google.com``
* ``either_dns``: Source or Destination DNS to match
* ``src_geo``: Source geo to match, e.g. ``Brazil``
* ``dst_geo``: Destination geo to match, e.g. ``United States``
* ``either_geo``: Source or Destination geo to match
* ``src_service``: Source Address Map name to match
* ``dst_service``: Destination Address Map name to match
* ``either_service``: Source or Destination Address Map name to match
* ``tbehavior``: Identified traffic behavior, e.g. ``Idle``, ``Voice``,
  ``Video_Conferencing``
* ``overlay``: Overlay name to match
* ``internet``: ``Fabric`` or ``Internet``
* ``logging``: Enable logging for rule with ``enable``, defaults to
  ``disable``
* ``logging_priority``: Loggig priority level for rule. Defaults to ``0``

Logging levels translate as follows:

    .. list-table::
        :header-rows: 1

        * - Numeric Level
          - Log Level
        * - 0
          - None
        * - 1
          - Emergency
        * - 2
          - Alert
        * - 3
          - Critical
        * - 4
          - Error
        * - 5
          - Warning
        * - 6
          - Notice
        * - 7
          - Info
        * - 8
          - Debug

Orchestrator API calls
^^^^^^^^^^^^^^^^^^^^^^^^^^

The API calls to Orchestrator (outside of authentication) used in this
example are:

* :func:`pyedgeconnect.Orchestrator.get_appliances`
   * Retrieves all appliances to correlate provided appliance name to
     appliance id for pushing security rules to appliance
* :func:`pyedgeconnect.Orchestrator.get_all_overlays_config`
   * Retrieves all overlays to correlate overlay names in policy source
     data to overlay ids
* :func:`pyedgeconnect.Orchestrator.get_all_template_groups`
   * Retrieves all template groups to make sure new template group name
     is unique, will otherwise exit
* :func:`pyedgeconnect.Orchestrator.get_zones`
   * Retrieves all zones to correlate zone names in policy source data
     to zone ids
* :func:`pyedgeconnect.Orchestrator.create_template_group`
   * Creates new template group in Orchestrator
* :func:`pyedgeconnect.Orchestrator.select_templates_for_template_group`
   * Selects active templates in template group, in this case, security
     policy
* :func:`pyedgeconnect.Orchestrator.appliance_post_api`
   * Sends a POST to appliance ECOS API endpoint, in this case to
     ``/securityMaps`` to push security policy directly to appliance
     through an Orchestrator API endpoint as passthrough.