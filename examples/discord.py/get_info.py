import bettercord
from discord.ext import commands


bot = commands.Bot(command_prefix=".")
client = bettercord.Client("BETTERCORD_TOKEN")


@bot.command()
async def get_bot_info(ctx, bot_id: int):
    info = await client.get_bot_info(bot_id)
    await ctx.send(info)


@bot.command()
async def get_bot_comments(ctx, bot_id: int):
    comments = await client.get_bot_comments(bot_id)
    await ctx.send(comments)


@bot.command()
async def get_user_info(ctx, user_id: int):
    info = await client.get_bot_info(user_id)
    await ctx.send(info)


@bot.command()
async def get_server_info(ctx, server_id: int):
    info = await client.get_bot_info(server_id)
    await ctx.send(info)


bot.run("DISCORD_TOKEN")
