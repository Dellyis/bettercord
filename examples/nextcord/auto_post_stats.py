import bettercord
from nextcord.ext import commands


bot = commands.Bot(command_prefix=".")
client = bettercord.Client("BETTERCORD_TOKEN", fork_name="nextcord")

client.run(bot)

bot.run("DISCORD_TOKEN")
