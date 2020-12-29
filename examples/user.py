import aiomojang
import asyncio


async def get_user_history():
    user = aiomojang.Player("Example")  # You can get a users information by passing it into the class.
    # you can get a user's uuid using: aiomojang.Player("Name").uuid
    # you can get a user's name using: aiomojang.Player("Name").name
    # However, you CANNOT run .uuid with a uuid and CANNOT run .name with a name.
    return await user.get_history()  # you can get the user's name history with get_history()


asyncio.run(get_user_history())  # Running the function
