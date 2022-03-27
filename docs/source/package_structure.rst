============================
 Package Directory Structure
============================

.. code::

    └── pyedgeconnect
        ├── __init__.py
        ├── ecos
        │   ├── __init__.py
        │   ├── <_ecos_function_group>.py
        │   └── ...
        └── orch
            ├── __init__.py
            ├── <_orch_function_group>.py
            └── ...

In the package directory, the top-level ``__init__.py`` defines the
classes leveraged by the user:
:class:`~pyedgeconnect.Orchestrator` and
:class:`~pyedgeconnect.EdgeConnect`.
These are both child classes of the base class
:class:`~pyedgeconnect.HttpCommon` to inerhit the generic HTTP
calls and handling responses.

:class:`~pyedgeconnect.Orchestrator` and
:class:`~pyedgeconnect.EdgeConnect` import their related
functions from files in the ``orch`` and ``ecos`` subdirectories
respectively. These files are named by the corresponding section in
the Silver Peak Swagger UI. While the Swagger sections are named in
CamelCase the python files are named in snake_case.

For example, functions for Orchestrator API calls in the Swagger section
titled "template" will be found in
`pyedgeconnect/orch/_template.py`. API calls in the Swagger
section "realtimeStats" will be found in
`pyedgeconnect/orch/_realtime_stats.py`