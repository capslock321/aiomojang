.. image:: https://readthedocs.org/projects/aiomojang/badge/?version=master 
   :target: https://aiomojang.readthedocs.io/en/master/?badge=master
   :alt: Documentation Status 
.. image:: https://img.shields.io/pypi/v/aiomojang?color=red&label=aiomojang 
   :target: https://img.shields.io/pypi/v/aiomojang?color=red&label=aiomojang 
   :alt: PyPI 
.. image:: https://img.shields.io/github/release-date/capslock321/aiomojang  
   :target: https://img.shields.io/github/release-date/capslock321/aiomojang  
   :alt: GitHub Release Date 
.. image:: https://img.shields.io/github/license/capslock321/aiomojang 
   :target: https://img.shields.io/github/license/capslock321/aiomojang 
   :alt: GitHub
.. image:: https://img.shields.io/github/commit-activity/w/capslock321/aiomojang   
   :target: https://img.shields.io/github/commit-activity/w/capslock321/aiomojang   
   :alt: GitHub commit activity

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

**Stable Release:**

.. code-block:: bash
    
    python3 -m pip install -U aiomojang

**Latest Release:**

.. code-block:: bash
   
   python3 -m pip install git+https://github.com/capslock321/aiomojang.git
    
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
If you wish to contribute, please open a pull request on this repository.
:raw-html:`<br />`
If you want to see what I am working on now, check the projects tab on this repository.
:raw-html:`<br />`
I am currently working on: **Auth stuff**

Licence
================================
This project is licensed under the **MIT License**.
