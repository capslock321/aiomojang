Render Documentation
=====================================
This class focuses on player apparel, specifically a player's skins and capes.

This does not include optifine capes.

**Basic Example:**

.. code-block:: python

    import aiomojang
    import asyncio

    async def get_user_skins():
        # If you want a user's cape, you can run aiomojang.Cape() instead.
        skin = aiomojang.Skin("Hypermnesia")
        # This may be confusing, but by passing in a user's name, you are getting their skin.
        # You can get a skins url using skin.url()
        # If you only need the last part of the link, you can do skin.id()
        return await skin.url()

    asyncio.run(get_user_skins())  # Running the function


Render
--------------------
The base class, it handles things other than skins and capes such as:

    * A user's uuid.
    * A user's name
    * Date the information was accessed.
    * The base64 signature if enabled.

.. autoclass:: aiomojang.renders.Render
    :members:

Skin
---------------------
This class focuses on the player's skin.

.. autoclass:: aiomojang.renders.Skin
    :members:

Cape
---------------------
This class focuses on the player's cape.

.. autoclass:: aiomojang.renders.Cape
    :members:
