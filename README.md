# Aruba Edge Connect Python SDK


This package is a python wrapper for leveraging the API for Aruba
Orchestrator and Edge Connect SDWAN systems.

API's are documented via Swagger directly on Orchestrator and
Edge Connect web interfaces under "Support > Rest API"

Many, but not all API functions have been implemented yet. Development
is underway to continue to add further functions.

As of 0.14.0+ 64% of non-deprecated Swagger functions are covered.


## Install


### Python Version

> **Note:** Requires Python 3.9.0+ (due to PEP585 type-hinting e.g. ``def my_func(var1 = list[str]``)

Once Python 3.9 is installed on the system, it's recommended to use a
virtual environment to install the package to.

In the directory you'd like to write your project/script, setup a python
virtual environment specifically with python3.9 and activate it. This
is important if you have other versions of python installed on your
system.

```bash

    :~$ python3.9 -m venv my_new_project
    :~$ source my_new_project/bin/activate
    (my_new_project) :~$ python3 --version
    Python 3.9.0+
```

Now you can install the package and run your python code

```bash

    (my_new_project) :~$ pip install git+https://github.com/SPOpenSource/edgeconnect-python
    ...
    (my_new_project) :~$ pip list
    Package               Version
    --------------------- --------------------------------
    certifi               2020.12.5
    chardet               4.0.0
    idna                  2.10
    pip                   20.0.2
    pkg-resources         0.0.0
    requests              2.25.1
    setuptools            44.0.0
    pyedgeconnect         0.13.0a2.dev1+g45fd843.d20210428
    urllib3               1.26.4
```

### Install from PyPI

```bash
    $ pip install pyedgeconnect
```

### Install from GitHub

To install the most recent version of pyedgeconnect, open an
interactive shell and run:

> **Note:** These commands assume you're within a Python 3.9 venv, or Python 3.9 is the exclusive Python version installed in regard to referencing the use of ``pip``. If that is not the case, you can specifically append ``python3.9 -m`` ahead of the ``pip install ...``

```bash
    $ pip install git+https://github.com/SPOpenSource/edgeconnect-python
```

To install a specific branch use the @branch syntax

```bash
    $ pip install git+https://github.com/SPOpenSource/edgeconnect-python@<branch_name>
```

### Install dev options

For editing the code and general testing you can specify the ``[dev]``
extras which will include ["black", "flake8", "flake8-rst-docstrings",
"isort", "sphinx", "sphinx_rtd_theme"]

To install from the remote repo with the ``[dev]`` extras option use the
following syntax:

```bash
    $ pip install pyedgeconnect[dev]
    or
    $ pip install  -e git+https://github.com/SPOpenSource/edgeconnect-python#egg=pyedgeconnect[dev]
```

## Docs

[![Documentation Status](https://readthedocs.org/projects/pyedgeconnect/badge/?version=latest)](https://pyedgeconnect.readthedocs.io/en/latest/?badge=latest)

Docs are viewable on [Read the Docs](https://pyedgeconnect.readthedocs.io)

To build the documentation locally, clone the repository, install with ``[dev]`` option
to include sphinx and related packages, then in the docs directory run ``make html``

```bash
    $ git clone https://github.com/SPOpenSource/edgeconnect-python.git
    $ cd pyedgeconnect
    $ pip install .[dev]
    $ cd docs
    $ make html
```

## Usage

### Orchestrator Class

Import the Orchestrator class to your script.

```python
    from pyedgeconnect import Orchestrator
```

To initialize an Orchestrator you must pass the url of the Orchestrator
(IP or FQDN).

> **Note:** If you're connecting to an Orchestrator without a valid certificate you'll want to set the ``verify_ssl`` paramter to ``False`` when instantiating Orchestrator to ignore certificate warnings/errors.

```python
    orch_url = '10.1.1.100'
    orch_url = 'orchestrator.example.com'
    orch = Orchestrator(orch_url, verify_ssl=False)
```

Now you can call the login function to connect to Orchestrator with a
username and password:

```python
    orch_user = 'admin'
    orch_pw = 'change_me'
    orch.login(orch_user, orch_pw)
    orch.logout()
```

Another option is to pass an API Key on init to make authenticated calls
without having to call login/logout functions

```python
    orch_url = 'orchestrator.example.com'
    orch = Orchestrator(orch_url, api_key='xxx')
```

### Edge Connect Class

```python
    from pyedgeconnect import EdgeConnect
```

To initialize an Edge Connect you must pass the url of the Edge Connect
(IP or FQDN).

> **Note:** If you're connecting to an Edge Connect without a valid certificate you'll want to set the ``verify_ssl`` paramter to ``False`` when instantiating EdgeConnect to ignore certificate warnings/errors.

```python
    ecos_url = '10.2.30.50'
    ecos_url = 'edgeconnect.example.com'
    ec = EdgeConnect(ecos_url, verify_ssl=False)
```

Now you can call the login function to connect to Edge Connect with a
username and password:

```python
    ecos_user = 'admin'
    ecos_pw = 'admin'
    ec.login(ecos_user, ecos_pw)
    ec.logout()
```

## Logging

By default, Orchestrator and EdgeConnect classes will not log calls
and/or errors to file or console. When instantiating Orchestrator
or EdgeConnect classes follow the below settings to enable logging
options:

* Logging to a local file: set the ``log_file`` parameter to
``True``. This will create ./logging/sp_orch.log or
./logging/sp_ecos.log relative to where python is launched for calls
that are performed.

* Logging to the console: set the ``log_console`` parameter to
``True``

By default, successful API calls (e.g. returning HTTP 200/204 etc.) will
not log response text to avoid logging sensitive data. To include
response text in log messages, set the ``log_success`` parameter to
``True``.

> **Warning:** If ``log_file`` and ``log_success`` are set to ``True`` response text from successful API calls will be logged to the local log file. Some responses can include sensitive data that you may not wish to retain in the log files.

```python
    orch_url = 'orchestrator.example.com'
    orch = Orchestrator(orch_url, log_file=True, log_console=True)
    # or
    ecos_url = '10.2.30.50'
    ec = EdgeConnect(ecos_url, log_success=True)
```

## Example Code

In the [Examples](/examples) directory you can find scripts leveraging
the Orchestrator class demonstrating some uses

* [create_user.py](/examples/create_user.py)
    * creates a new read-only user on Orchestrator and returns the
      configured details
* [print_appliance_info.py](/examples/print_appliance_info.py)
    * retrieves all appliances, retrieves detailed attributes of the
      appliances, and prints details in a table format
* [run_packet_capture.py](/examples/run_packet_capture.py)
    * runs a tcpdump packet capture on a specified appliance, once
      completed, uploads to Orchestrator for user retrieval


## This is an alpha product

This package is still very new. This is made explicit by the "Alpha"
trove classifier, as well as by the "a" in the version number. **Until
the package becomes stable, you should expect some formatting and/or
syntax to change in the future**.

## License

MIT

## Contributing to pyedgeconnect

Adding more modules and API functions are prioritized as needed for use.
There is not currently support for reviewing external PR's as maintenance
is best effort by the authors.

Open an [issue](issues)
to track any/all suggestions/fixes/additions.
Please don't file an issue to ask a question.

As this code is in early stages there are larger changes that may be
discussed in regards to overall structure, error handling, logging, etc.
Suggestions for these topics can be raised via issue or contacting the
authors.

See contribution details at [Contributing](CONTRIBUTING.md)

## Release Notes

Release notes are located in ``docs/source/release-notes`` directory [here](docs/source/release-notes)


## Authors

Authored by Zach Camara, email at <zachary.camara@hpe.com>
