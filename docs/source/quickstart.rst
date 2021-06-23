===========================
Quickstart
===========================


To start using pyedgeconnect, import the appropriate Class
into your script:

.. code:: python

    from pyedgeconnect import Orchestrator
    # or
    from pyedgeconnect import EdgeConnect

To initialize an Orchestrator you must pass the url of the Orchestrator
(IP or FQDN).

.. note::

   If you're connecting to an Orchestrator without a valid certificate
   you'll want to set the ``verify_ssl`` paramter to ``False`` when
   instantiating Orchestrator to ignore certificate warnings/errors.

.. code:: python

   orch = Orchestrator('10.1.1.100')
   # or
   orch = Orchestrator('orchestrator.example.com', verify_ssl=False)

   ec = EdgeConnect('10.2.30.50')
   # or
   ec = EdgeConnect('edgeconnect.example.com', verify_ssl=False)

You can then connect to the instance with the `login` method:

.. code:: python

   orch.login("username", "password")
   orch.logout()
   # or
   ec.login("username", "password")
   ec.logout()

For Orchestrator 9.x+ you can alternatively use API Keys to authenticate
calls to Orchestrator:

.. code:: python

   orch_url = 'orchestrator.example.com'
   orch = Orchestrator(orch_url, api_key='abcdefghijklmnopqrstuvwxyz123')

.. note::

   This is also beneficial because you can dedicate keys to different
   apps/uses as well as setting read-only vs. read-write permissions,
   expiration dates, and won't increment logged-in user count.