import bettercord
from discord.ext import commands


bot = commands.Bot(command_prefix=".")
client = bettercord.Client("BETTERCORD_TOKEN")

client.run(bot)

bot.run("DISCORD_TOKEN")
