from typing import List, Optional

from .bot import Bot
from .comments import Comment
from .core import HttpClient
from .loop_manager import Looper
from .server import Server
from .user import User


class Client:
    def __init__(self, token: str, api_version: int = 1, fork_name: str = "discord"):
        self.http: HttpClient = HttpClient(
            f"https://api.bettercord.xyz/v{api_version}", token)
        self.fork_name = fork_name

    async def get_bot_info(self, bot_id: int) -> Optional[Bot]:
        response = await self.http.get(f"/bots/{bot_id}")
        if response is not None:
            res = await response.json()
            if response.status == 200:
                return Bot(res)
            raise Exception(res["error"])

    async def get_bot_comments(self, bot_id: int) -> Optional[List[Comment]]:
        response = await self.http.get(f"/bots/{bot_id}/comments")
        if response is not None:
            res = await response.json()
            if response.status == 200:
                return list(map(Comment, res["reviews"]))
            raise Exception(res["error"])

    async def post_stats(self, server_count: int, shard_count: int = 1) -> Optional[bool]:
        response = await self.http.post("/bots/stats", headers={
            "serverCount": str(server_count),
            "shardCount": str(shard_count)
        })
        if response is not None:
            res = await response.json()
            if response.status == 200:
                return True
            raise Exception(res["error"])

    async def get_user(self, user_id: int) -> Optional[User]:
        response = await self.http.get(f"/profile/{user_id}")
        if response is not None:
            res = await response.json()
            if response.status == 200:
                return User(res)
            raise Exception(res["error"])

    async def check_vote(self, user_id: int) -> Optional[bool]:
        response = await self.http.get(f"/bots/check/{user_id}")
        if response is not None:
            res = await response.json()
            return bool(res["voted"])

    async def get_server_info(self, server_id: int) -> Optional[Server]:
        response = await self.http.get(f"/server/{server_id}")
        if response is not None:
            res = await response.json()
            if response.status == 200:
                return Server(res)
            raise Exception(res["error"])

    def run(self, bot):
        Looper(bot, self.http, self.fork_name).create_loop()
