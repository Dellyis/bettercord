from importlib import import_module

from ..loop_manager import Global


discord = import_module(f"{Global.fork_name}")
commands = import_module(f"{Global.fork_name}.ext.commands")
tasks = import_module(f"{Global.fork_name}.ext.tasks")


class BetterCord(commands.Cog):  # type: ignore
    def __init__(self, bot) -> None:
        self.bot = bot
        self.post_stats.start()

    @tasks.loop(minutes=10)  # type: ignore
    async def post_stats(self):
        await self.bot.wait_until_ready()
        response = await Global.http.post("/bots/stats", headers={
            "serverCount": str(len(self.bot.guilds)),
            "shardCount": str(self.bot.shard_count or 1)
        })
        if response is not None:
            res = await response.json()
            if response.status == 200:
                return True
            raise Exception(res["error"])


def setup(bot):
    bot.add_cog(BetterCord(bot))
