=======================
Installation
=======================

Python Version
---------------

.. note::

    Requires Python 3.9.0+ (due to PEP585 type-hinting e.g.
    ``def my_func(var1 = list[str]``)

Once Python 3.9 is installed on the system, it's recommended to use a
virtual environment to install the package to.

In the directory you'd like to write your project/script, setup a python
virtual environment specifically with python3.9 and activate it. This
is important if you have other versions of python installed on your
system.

.. code:: bash

    :~$ python3.9 -m venv my_new_project
    :~$ source my_new_project/bin/activate
    (my_new_project) :~$ python3 --version
    Python 3.9.0+

Now you can install the package and run your python code

.. code:: bash

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
    pyedgeconnect         0.13.0a1.dev1+g45fd843.d20210428
    urllib3               1.26.4

Install from PyPI
-------------------

.. code:: bash

    $ pip install pyedgeconnect


Install from GitHub
-------------------

To install the most recent version of pyedgeconnect, open an
interactive shell and run:

.. note::

    These commands assume you're within a Python 3.9 venv, or Python 3.9
    is the exclusive Python version installed in regard to referencing
    the use of ``pip``.

    If that is not the case, you can specifically append
    ``python3.9 -m`` ahead of the ``pip install ...``

.. code:: python

    pip install git+https://github.com/SPOpenSource/edgeconnect-python

To install a specific branch use the @branch syntax

.. code:: python

    pip install git+https://github.com/SPOpenSource/edgeconnect-python@<branch_name>

For editing the code and general testing you can specify the [dev]
extras which will include ["black", "flake8", "flake8-rst-docstrings",
"isort", "sphinx", "sphinx_rtd_theme"]

To install from the remote repo with the [dev] extras option use the
following syntax:

.. code::

    pip install  -e git+https://github.com/SPOpenSource/edgeconnect-python#egg=pyedgeconnect[dev]


