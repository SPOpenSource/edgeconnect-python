.. generate_preconfig:


.. important::

    The following example is more complex code than the general examples,
    generating data and interacting with Orchestrator. Using and
    modifying these examples requires a greater understanding of python
    functions, handling variables, and additional tools such as Jinja.


.. note::

    The code referenced in this document and all published examples
    with pyedgeconnect are available from the GitHub repository within the
    `examples <https://github.com/SPOpenSource/edgeconnect-python/tree/main/examples>`_
    folder. Each example script contains logic to authenticate to the
    Orchestrator as documented in the authentication example.

    Clone the repository and download the examples with:

    .. code:: bash

        $ git clone https://github.com/SPOpenSource/edgeconnect-python.git

Generate EdgeConnect Preconfig
********************************

This example uses a Jinja template to generate the YAML text for an
EdgeConnect preconfig. The YAML preconfig allows for an appliance to be
partially or fully deployed in a Zero Touch Provisioning (ZTP) model
where the appliance configuration is staged on Orchestrator prior to the
appliance being approved into the SDWAN environment.

Before running the code, make sure that the Python package ``jinja2`` is
installed in your environment in addition to ``pyedgeconnect``.

These are referenced in the ``requirements.txt`` file in the preconfig
example directory

.. code-block:: python

    pip install -r requirements.txt
    # OR
    pip install pyedgeconnect
    pip install jinja2


EdgeConnect YAML Jinja Template
===============================

The first component of this automation example is the Jinja template
modeled after the preconfig YAML documented on Orchestrator.

.. note::

    To reference all possible preconfig fields, values, and definitions
    in Orchestrator, navigate to the Preconfigure Appliances tab:
    ``Configuration->Overlays & Security->Discovery->Preconfiguration``

    Click the ``New`` button and you will be presented with a heavily
    commented preconfiguration file with all possible fields for reference.

The included Jinja template for this example has inline comments explaining
the logic around the subjective variable names, including default value
behavior, setting calculated variables, and operating with conditional
logic to write certain text or values.

With this flexibility, this can be extended to create a minimal input
process to create full configurations to ZTP EdgeConnect appliances.
The example uses a CSV file as a data source for the configuration,
allowing many appliances to be generated from one source. The same logic
could be applied to fetch source data from a Configuration
Management Database (CMDB) where the information may already exist and
maintain a "Single source of truth."

.. note::

    The included Jinja template has only a few of the many sections that
    can be specified in the preconfig and it is up to the individual user
    or Organization to determine what sections are important/necessary
    to build a functional EdgeConnect configuration for their environment.

    For more documentation and information on Jinja templating visit the
    Pallets Project site: https://jinja.palletsprojects.com/


Below is a side-by-side view comparing a Jinja template
and the resulting YAML text that would render assuming only four
variables defined:

.. code-block:: python

    w1_max_out = 100000 # WAN Interface 1 max outbound bandwidth
    w2_max_out = 25000 # WAN Interface 2 max outbound bandwidth
    w1_max_in = 100000 # WAN Interface 1 max inbound bandwidth
    w2_max_in = 300000 # WAN Interface 2 max inbound bandwidth

    # Unused variable definitions
    mode: str # Deployment mode
    shape_in: bool # Shape inbound traffic
    out_max: int # Maximum outbound bandwidth


+---------------------------------------------------------------------------------------+-----------------------------------------+
| Jinja Template                                                                        | Rendered YAML                           |
+---------------------------------------------------------------------------------------+-----------------------------------------+
| .. code-block:: python                                                                | .. code-block::                         |
|    :caption: ec_preconfig_template.jinja2                                             |    :caption: preconfig.yml              |
|                                                                                       |                                         |
|    {% set wan1_outbound = data['w1_max_out'] | default(0,true) | int %}               |                                         |
|    {% set wan2_outbound = data['w2_max_out'] | default(0,true) | int %}               |                                         |
|    {% set wan_total_outbound = wan1_outbound + wan2_outbound %}                       |                                         |
|    {% set wan1_inbound = data['w1_max_in'] | default(0,true) | int %}                 |                                         |
|    {% set wan2_inbound = data['w2_max_in'] | default(0,true) | int %}                 |                                         |
|    {% set wan_total_inbound = wan1_inbound + wan2_inbound %}                          |                                         |
|                                                                                       |                                         |
|    deploymentInfo:                                                                    |    deploymentInfo:                      |
|      deploymentMode: {{ data['mode'] | default("inline-router",true) }}               |        deploymentMode: inline-router    |
|      totalOutboundBandwidth: {{ wan_total_outbound }}                                 |        totalOutboundBandwidth: 125000   |
|      totalInboundBandwidth: {{ wan_total_inbound }}                                   |        totalInboundBandwidth: 400000    |
|      shapeInboundTraffic: {{ data['shape_in'] | default("true",true) }}               |        shapeInboundTraffic: true        |
|      passThroughShapedTraffic:                                                        |        passThroughShapedTraffic:        |
|        outboundMaxBandwidth: {{ data['out_max'] | default(wan_total_outbound,true) }} |            outboundMaxBandwidth: 125000 |
+---------------------------------------------------------------------------------------+-----------------------------------------+


As Jinja is a Python-based templating language, conditional operators can be used
to determine sections of the template based on certain values

An example below would be writing a different value for localMetric based on the
hostname of an appliance. This same logic could be applied to determining
what Template Groups to apply based on the region of the appliance etc.

.. code-block:: python

  {% if data['hostname'][-3:] == "-01" %}
    localMetric: 50
  {% elif data['hostname'][-3:] == "-02" %}
    localMetric: 60
  {% endif %}


Python Script & Orchestrator API calls
======================================

The second component of this automation example is the Python script
that will read the source CSV file, render each row of data through
the Jinja template, validate the resulting Preconfig YAML on Orchestrator,
and optionally upload the Preconfig to Orchestrator.


Runtime arguments
^^^^^^^^^^^^^^^^^

The python script has multiple runtime arguments defined. The one
required argument is ``-c`` or ``--csv`` to specify the CSV file to be
read as source data for generating the Preconfig YAML.

Running the script with only this argument would appear as:

.. code-block:: bash

    python preconfig.py -c new_preconfigs.csv

Additional availble runtime arguments are as follows:

- ``-o`` or ``--orch``
    - Type: String
    - Desc: Specify the Orchestrator IP or FQDN
    - Example values: ``192.0.2.100`` or ``orchestrator.<company>.com``
    - Default value: ``None``
- ``-u`` or ``--upload``
    - Type: Boolean
    - Desc: Upload the rendered YAML preconfig to Orchestrator.
      Including the ``-u`` will translate to ``True``, no option will
      default to ``False``
    - Default value: ``False``
- ``-aa`` or ``--autoapply``
    - Type: Boolean
    - Desc: Auto-apply the YAML preconfig on Orchestrator to a
      discovered appliance. Including the ``-aa`` will translate to
      ``True``, no option will default to ``False``
    - Default value: ``False``
- ``-j`` or ``--jinja``
    - Type: String
    - Desc: Specify another jinja template to use
    - Example values: ``dc_template.jinja2`` or ``branch2.jinja2``
    - Default value: ``ec_preconfig_template.jinja2``


Running the script and uploading valid preconfigs to Orchestrator:

.. code-block:: bash

    python preconfig.py -c new_preconfigs.csv -u True


CSV File / Source Data for Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this example the source data for generating a preconfig from the
Jinja template is a CSV file. The variables referenced in the Jinja
template correspond to the headers in the CSV file. If additional
variables are added to the Jinja template, make sure to add appropriate
columns in the CSV file.

.. important::

    The included CSV file has headers for all variables referenced in
    the included Jinja template, however, due to default values and/or
    other conditional logic, it may not be necessary to have columns
    for every variable to generate a valid preconfig.

Only a few example values are included in the CSV file in the
repository as a starting point as valid values will vary from each
Orchestrator environment, and many variables have default values that
will be included via the Jinja template.

Always reference the Orchestrator page ``Preconfigure Appliances`` with
the built-in ``new`` preconfig to see acceptable values for specific
preconfig options.

Orchestrator API calls
^^^^^^^^^^^^^^^^^^^^^^^^^^

The two API calls to Orchestrator (outside of authentication) are
:func:`pyedgeconnect.Orchestrator.validate_preconfig` and
:func:`pyedgeconnect.Orchestrator.create_preconfig`.

The ``validate_preconfig`` function sends the preconfig YAML text to
Orchestrator and will either return a success (HTTP 200 OK) or if
contents of the preconfig are invalid, an error message indicating
what content is invalid (e.g. reference a Template Group that doesn't
exist on Orchestrator)

If ``validate_preconfig`` returns a 200 OK, then the same preconfig data
will be sent via the ``create_preconfig`` function to save the preconfig
on Orchestrator



Removing Preconfigs
^^^^^^^^^^^^^^^^^^^^^

If valid preconfigs are posted to Orchestrator that you wish to remove,
the Python script ``remove-preconfig.py`` functions similarly to the
``preconfig.py`` referencing the same CSV file and will remove preconfigs
with matching preconfig names

.. note::

    Both scripts use the ``hostname`` column value to name the preconfigs

To remove the preconfigs generated, the same runtime argument is used of
``-c`` or ``--csv`` to reference the CSV file

.. code-block:: bash

    python remove-preconfig.py -c new_preconfigs.csv

This will retrieve all configured preconfigs on Orchestrator, find
all preconfigs with a matching name as those in the CSV file, then
prompt the user to confirm that those preconfigs should be removed from
Orchestrator.