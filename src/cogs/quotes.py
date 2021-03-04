from discord.ext import commands
from discord import Embed


class QuotesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='say')
    async def say(self, ctx):
        e = Embed(title='Test', description='что то')
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(QuotesCog(bot))
