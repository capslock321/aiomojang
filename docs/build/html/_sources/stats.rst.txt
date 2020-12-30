Statistics Documentation
=====================================
This focuses on getting Mojang statistics.

**Basic Example:**

.. code-block:: python

   import aiomojang
   import asyncio

   async def get_mojang_statistics():
       # You can get Mojang statistics with aiomojang.Statistics()
       stats = aiomojang.Statistics()
       # Using any function under aiomojang.Statistics() requires a payload
       # The payload can be of the following:
       #    item_sold_minecraft
       #    prepaid_card_redeemed_minecraft
       #    item_sold_cobalt
       #    item_sold_scrolls
       #    prepaid_card_redeemed_cobalt
       #    item_sold_dungeons
       return await stats.get_sale_velocity("item_sold_minecraft")  # Returns a float.

   asyncio.run(get_mojang_statistics())  # Running the function

.. toctree::
   :maxdepth: 2
   :caption: Home

.. autoclass:: aiomojang.misc.Statistics
    :members:
