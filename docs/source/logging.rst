=======================
Logging & Debugging
=======================

By default, Orchestrator and EdgeConnect classes will not log calls
and/or errors to file or console.

To enable logging to a local file, set the ``log_file`` parameter to
``True`` when instantiating :class:`~pyedgeconnect.Orchestrator`
or :class:`~pyedgeconnect.EdgeConnect`.
This will create ./logging/sp_orch.log or ./logging/sp_ecos.log relative
to where python is launched for calls that are performed.

To enable logging to the console, set the ``log_console`` parameter to
``True`` when instantiating :class:`~pyedgeconnect.Orchestrator`
or :class:`~pyedgeconnect.EdgeConnect`.

By default, successful API calls (e.g. returning HTTP 200/204 etc.) will
not log response text to avoid logging sensitive data. To include
response text in log messages, set the ``log_success`` parameter to
``True``.

.. warning::
    If ``log_file`` and ``log_success`` are set to ``True``
    response text from successful API calls will be logged to
    the local log file. Some responses can include sensitive
    data that you may not wish to retain in the log files.

.. code:: python

    orch_url = 'orchestrator.example.com'
    orch = Orchestrator(orch_url, log_console=True, log_success=True)
    # or
    ecos_url = '10.2.30.50'
    ec = EdgeConnect(ecos_url, log_file=True)