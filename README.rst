.. image:: https://readthedocs.org/projects/aiomojang/badge/?version=master 
   :alt: Documentation Status 
.. image:: https://img.shields.io/pypi/v/aiomojang?color=red&label=aiomojang 
   :alt: PyPI 
.. image:: https://img.shields.io/github/release-date/capslock321/aiomojang  
   :alt: GitHub Release Date 
.. image:: https://img.shields.io/github/license/capslock321/aiomojang 
   :alt: GitHub

Overview
===============================
.. role:: raw-html(raw)
    :format: html
    
Aiomojang is a asynchronous implementation of Mojang's API, designed to be simple to use and easy understanding.
:raw-html:`<br />`
It makes use of the await and async keywords introduced in Python 3.5 **(PEP 492)**.

Installation
===============================
The best way to install this is to user pip to install this repository.

Windows:
------------------

**Stable Release:**

.. code-block:: bash
    
    pip install -U aiomojang
    
**Latest Release:**

.. code-block:: bash
    
    python -3 pip install -U git+https://github.com/capslock321/aiomojang.git
    
Unix:
------------------

**Stable Release:**

.. code-block:: bash
    
    pip3 install -U aiomojang

**Latest Release:**

.. code-block:: bash
    
    pip3 install -U git+https://github.com/capslock321/aiomojang.git
    
    
Basic Code Usage:
===============================

**Documentation can be found at:** https://aiomojang.readthedocs.io/en/latest/

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
        
Issues:
================================
If you have any issues with this wrapper, please open a issue on this repository.

Contribution
================================
If you wish to contribute, please open a Pull Request on this repository.

Licence
================================
This project is licensed under the **MIT License**.
