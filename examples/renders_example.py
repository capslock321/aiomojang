import aiomojang
import asyncio

async def get_user_skins():
    # If you want a user's cape, you can run aiomojang.Cape() instead.
    skin = aiomojang.Skin("Hypermnesia")
    # This may be confusing, but by passing in a user's name, you are getting their skin.
    # You can get a skins url using skin.url()
    # If you only need the last part of the link, you can do skin.id()
    return await skin.url

asyncio.run(get_user_skins())  # Running the function
