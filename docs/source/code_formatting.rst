=========================
Code Formatting
=========================


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

