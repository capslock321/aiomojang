import discord
import aiomojang
from discord.ext import commands

# This is a example cog using aiomojang.

bot = commands.Bot(command_prefix = "!", case_insensitive = True)


class Example(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is ready")

    @commands.command()  # Get information on a player.
    async def mojang(self, ctx, player: str):
        profile = aiomojang.Player(player)
        embed = discord.Embed(title="Information on: ", color=discord.Colour.green())
        embed.add_field(name="Player's name: ", value=player)  # Because doing profile.name will raise an error.
        embed.add_field(name="Player's uuid: ", value=await profile.uuid, inline=False)
        embed.set_image(url=await profile.get_skin())
        await ctx.send(embed=embed)

    @commands.command()  # Name history command
    async def history(self, ctx, player: str):
        profile = aiomojang.Player(player)
        embed = discord.Embed(title=f"{player}'s name history: ", color=discord.Colour.blue())
        i = 1
        for x in await profile.get_history():
            embed.add_field(name = f"Name #{i}: ", value = x['name'])  # Iterate through the names.
            i = i + 1
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Example(bot))
    

setup(bot)  # Due to running the file in the same file as the cog, i run setup here


bot.run("TOKEN")
