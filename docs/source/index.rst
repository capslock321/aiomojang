Aiomojang
=====================================

Overview
--------------------------------------

Welcome to Aiomojang's Documentation!

.. note::

   This is a full API wrapper, but anything that requires you to login has not been thoroughly tested due to the difficulty of doing so.
   Use at your own risk.

Aiomojang is a asynchronous wrapper of Mojang's api.

.. warning::

   This module requires Python 3.6 and above due to the use of f-strings in the source code.

It is designed to be simple to use and easy understanding.


Installation
===============================

The best way to install this is to user pip to install this repository.

Windows:
------------------
.. code-block:: bash

    python -3 pip install git+https://github.com/capslock321/aiomojang.git

Unix:
------------------
.. code-block:: bash

    pip3 install git+https://github.com/capslock321/namemc.git


Basic Code Usage:
===============================
.. code-block:: python

    import aiomojang
    import asyncio


    # you can get a user's name by providing his uuid
    async def get_name():
        # getting a user's name
        return await aiomojang.Player("7e2ad381193e40e2adfe8df266134d8c").name
        # Output: Hypermnesia


    # you can get a user's uuid by providing his name
    async def get_uuid():
        # getting a user's uuid
        return await aiomojang.Player("Hypermnesia").uuid
        # Output: 7e2ad381193e40e2adfe8df266134d8c


.. toctree::
   :maxdepth: 2
   :caption: Documenation

   ./user

   ./renders

   ./status

   ./stats

   ./blocked

   ./auth


Miscellaneous
==================

* :ref:`genindex`

* :ref:`modindex`

* :ref:`search`
