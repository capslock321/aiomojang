Overview
===============================
Aiomojang is a asynchronous implementation of Mojang's API.


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
        return await aiomojang.User("7e2ad381193e40e2adfe8df266134d8c").name
        # Output: Hypermnesia


    # you can get a user's uuid by providing his name
    async def get_uuid():
        # getting a user's uuid
        return await aiomojang.User("Hypermnesia").uuid
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
