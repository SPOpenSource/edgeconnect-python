=======================
Installation
=======================

Python Version
---------------

.. note::

    Requires Python 3.7+

Once Python 3.7+ is installed on the system, it's recommended to use a
virtual environment to install the package to.

In the directory you'd like to write your project/script, setup a python
virtual environment with the desired python version and activate it. This
is important if you have other versions of python installed on your
system.

.. code:: bash

    :~$ python3.9 -m venv my_new_project
    :~$ source my_new_project/bin/activate
    (my_new_project) :~$ python3 --version
    Python 3.9.13

Now you are ready to install the package and run your python code.

.. note::

    Going forward, these commands assume you're within a Python 3.7+ venv, or Python 3.7+
    is the exclusive Python version installed in regard to referencing
    the use of ``pip``.

    If that is not the case, you can specifically append
    ``python3.x -m`` ahead of the ``pip install ...``

Install from PyPI
-------------------

.. code:: bash

    $ pip install pyedgeconnect
    ...
    $ pip list
    Package                       Version
    ----------------------------- --------------------------------
    ...                           ...
    pyedgeconnect                 x.y.z
    ...                           ...

Install from GitHub
-------------------

To install the most recent version of pyedgeconnect, open an
interactive shell and run:

.. code:: bash

    $ pip install git+https://github.com/SPOpenSource/edgeconnect-python
    ...
    $ pip list
    Package                       Version
    ----------------------------- --------------------------------
    ...                           ...
    pyedgeconnect                 x.y.z
    ...                           ...

To install a specific branch use the @branch syntax

.. code:: bash

    $ pip install git+https://github.com/SPOpenSource/edgeconnect-python@<branch_name>
    # Install the Development branch
    $ pip install git+https://github.com/SPOpenSource/edgeconnect-python@Development

Build Documentation Locally
---------------------------

To build the documentation locally, clone the repository, install with ``[dev]`` option
to include sphinx and related packages, then in the docs directory run ``make html``

.. code:: bash

    $ git clone https://github.com/SPOpenSource/edgeconnect-python.git
    $ cd edgeconnect-python
    $ pip install .[dev]
    $ cd docs
    $ make html