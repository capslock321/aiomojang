User Documentation
=====================================
This section of this wrapper focuses on player names, uuids and name history.
This section has 2 classes, Users and Players.

**Basic Example:**

.. code-block:: python

    import aiomojang
    import asyncio


    async def get_user_history():
     user = aiomojang.Player("Example")  # You can get a users information by passing it into the class.
     # you can get a user's uuid using: aiomojang.Player("Name").uuid
     # you can get a user's name using: aiomojang.Player("Name").name
     # However, you CANNOT run .uuid with a uuid and CANNOT run .name with a name.
     return await user.get_history()  # you can get the user's name history with get_history()


    asyncio.run(get_user_history())  # Running the function


Player
------------------
This focuses on individual players, and will take only one name.

.. toctree::

.. autoclass:: aiomojang.user.Player
    :members:

Users
------------------

This class focuses on getting information on multiple users.
As such, it can take multiple users in the constructor and returns a list of the requested information.

.. autoclass:: aiomojang.user.Users
    :members:
