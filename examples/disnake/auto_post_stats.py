import bettercord
from disnake.ext import commands


bot = commands.Bot(command_prefix=".")
client = bettercord.Client("BETTERCORD_TOKEN", fork_name="disnake")

client.run(bot)

bot.run("DISCORD_TOKEN")
