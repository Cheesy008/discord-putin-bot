from discord.ext import commands

from src.constants import DISCORD_TOKEN, PREFIX


initial_extensions = ['cogs.quotes']

bot = commands.Bot(command_prefix=PREFIX)


if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

bot.run(DISCORD_TOKEN, reconnect=True)

