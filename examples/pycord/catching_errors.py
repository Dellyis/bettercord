import bettercord
from discord.ext import commands


bot = commands.Bot(command_prefix='.')
client = bettercord.Client("BETTERCORD_TOKEN", fork_name="disnake")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error.original, bettercord.BotNotFound):
        await ctx.send("Bot not found")
    elif isinstance(error.original, bettercord.PostStatsDenied):
        await ctx.send("Post stats denied")
    elif isinstance(error.original, bettercord.UserNotFound):
        await ctx.send("User not found")
    elif isinstance(error.original, bettercord.CheckVoteForbidden):
        await ctx.send("Check vote forbidden")
    elif isinstance(error.original, bettercord.ServerNotFound):
        await ctx.send("Server not found")


bot.run("DISCORD_TOKEN")
