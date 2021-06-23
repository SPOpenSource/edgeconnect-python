=========================
 SDK Logic and Formatting
=========================

Package File Hierarchy
----------------------

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

Logical Function Flow
---------------------

.. code::

                ┌─Class:Orchestrator┐    ┌────────────Class:HttpCommon───────────────┐
                ┌───────────────────┐    ┌──────────────────┐    ┌───────────────────┐
                │                   │    │     _get()       │    │    _req_get()     │
    USER        │     EXAMPLE       ├─1──►     _post()      ├─2──►    _req_post()    │
    INPUT   ─►  │     FUNCTION      │    │     _put()       │    │    _req_put()     │
                │                   ◄─6──┼─┐   _delete() ┌──◄──3─┤    _req_delete()  │
                └───────────────────┘    └─▲─────────────┼──┘    └───────────────────┘
                                           │             │
                                           │             4
                                           5             │
                                           │   ┌─────────▼────────────┐
                                           │   │                      │
                                           └───┤  _handle_response()  │
                                               │                      │
                                               └──────────────────────┘



This class is the base class for processing HTTP requests from front-end
functions and handling responses back to the user.

The logic is the same for HTTP `GET`, `POST`, `PUT`, and `DELETE`. The
below example walks through processing a `GET`.

1. A function from
:class:`~pyedgeconnect.Orchestrator` or
:class:`~pyedgeconnect.EdgeConnect` makes a call to
:meth:`pyedgeconnect.HttpCommon._get` with the short path
(portion of the path that is unique to the function) and other optional
parameters such as ``expected_status`` or ``return_type`` if applicable.

2. The :meth:`pyedgeconnect.HttpCommon._get` function will check
that the requested ``return_type`` parameter is valid, then pass the
``api_path`` to :meth:`pyedgeconnect:HttpCommon:_req_get`. This
function appends the short path to the url prefix for the instance of
:class:`~pyedgeconnect.Orchestrator` or
:class:`~pyedgeconnect.EdgeConnect` and returns a response.

3. The response is returned back to
:meth:`pyedgeconnect.HttpCommon._get` and then along with the
short path, expected HTTP statuses, and data return type are passed to
:meth:`pyedgeconnect.HttpCommon._handle_response`.

4. The :meth:`pyedgeconnect.HttpCommon._handle_response`
will first check if the HTTP response code is within the expected
status. If the expected status code is outside of the expected
values it will be logged as an error. Default expected status is
``200``, though some functions are overridden to include an empty
``204`` as valid, among others.

The return value of the function will vary based on the expected
``return_type`` parameter. If ``return_type`` was ``json`` a dictionary
or list will be returned with the response values, ``text`` will return
response text, ``bool`` will return ``True`` or ``False``, and
``full_response`` will return the full requests.Request object.

When logging an error, the HTTP method and path used, the HTTP status
code, and response text will be written to the error log.

With an error and ``return_type`` of ``json``, a dictionary is returned
with the keys ``request`` for HTTP request method, ``api_path`` for the
API endpoint, ``status_code`` for HTTP response code, and ``text`` for
the response text.

Below is a snippet of this logic from
:meth:`pyedgeconnect.HttpCommon._handle_response` when handling
an unexpected status and treating it as an error.

.. code-block:: python

    if response.status_code not in expected_status:
        self.logger.error(...)

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

5. The return is passed back to the originating
:meth:`pyedgeconnect.HttpCommon._get`

6. The return is passed back to the originating function called by the
user


Code Formatting
---------------

Flake8 is run on the codebase according to parameters in the .flake8
file following PEP8 conventions where possible.

Naming Conventions
^^^^^^^^^^^^^^^^^^

* Classes are named in CamelCase, e.g. HttpCommon, Orchestrator,
  EdgeConnect
* Functions are variables are named in snake_case, e.g. get_appliances()
* Private functions begin with ``_`` e.g. ``_get()`` or ``_req_post()``

Docstrings and comments
^^^^^^^^^^^^^^^^^^^^^^^
* Docstrings follow Sphinx/reStructured Text Formatting
    * Short initial description
    * Reference to where to find this function in Swagger UI
    * Longer description, notes, examples if applicable
    * parameter and return descriptions and types
* All functions have docstrings outlining parameters and returns
* Code in a function begins the line immediately following the docstring

**Example:**

.. code::

    """<Short description here>

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - <swagger section> -> e.g. login
          - <method> -> e.g. GET
          - <endpoint> -> e.g. /logout

    <longer description>

    .. note::

        an optional note

    .. warning::

        an optional warning

    :param <param name>: <param description>
    :type <param name>: <param type>
    :return: <return description>
    :rtype: <return type>
    """
    <code begins here>

Maximum Line Length
^^^^^^^^^^^^^^^^^^^
* All comments and docstrings have a maximum line length of 72
  characters
* All functional code has a maximum line length of 79 characters
* In the rare case when a string or docstring can't be wrapped over
  multiple lines (e.g. specifying a long API endpoint in docstring)
  use ``# noqa:`` at the end of the docstring with ``E501``
  for extending past 79 and ``W505`` for extending past 72, or just
  ``W505`` if past 72 but within 79.

**Example:**

.. code::

    """docstring

    .. list-table::
        :header-rows: 1

        * - Swagger Section
          - Method
          - Endpoint
        * - login
          - GET
          - /long_endpoint/path/{that_cannot}/be/wrapped/over_multiple_lines
    ...
    """ # noqa: W505


Type Hinting (PEP585)
^^^^^^^^^^^^^^^^^^^^^
* All parameters for functions have type hinting following PEP585
  (Python 3.9+) formatting with generic types.

  .. code::

    def my_func(my_var: str) -> dict:
    ...
    # or
    def my_func(my_var: list[int]) -> list:
    ...

