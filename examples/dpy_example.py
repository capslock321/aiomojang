import discord
import aiomojang
from discord.ext import commands

# This is a example cog using aiomojang.

class Main(commands.Bot):

    def __init__(self):
        super(Main, self).__init__(command_prefix="!", case_insensitive = True)

        self.add_cog(Example(self))

    async def on_ready(self):
        print(f'Logged in as: {self.bot.user.name}')

class Example(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is ready")

    @commands.command()  # Get information on a player.
    async def mojang(self, ctx, player: str):
        profile = aiomojang.Player(player)
        try:
            embed = discord.Embed(title="Information on: ", color=discord.Colour.green())
            embed.add_field(name="Player's name: ", value=player)  # Because doing profile.name will raise an error.
            embed.add_field(name="Player's uuid: ", value=await profile.uuid, inline=False)
            embed.set_image(url = await profile.get_skin())
            await ctx.send(embed=embed)
        except aiomojang.exceptions.ApiException:
            return await ctx.send(f"No user with the name {player} was found.")
        
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

bot = Main()
bot.run("TOKEN")
