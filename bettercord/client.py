from typing import List, Optional

from .bot import Bot
from .comment import Comment
from .core import HttpClient
from .errors import *
from .loop_manager import Looper
from .server import Server
from .user import User


class Client:
    def __init__(self, token: str, api_version: int = 1, fork_name: str = "discord"):
        super().__init__()
        self.http: HttpClient = HttpClient(
            f"https://api.bettercord.xyz/v{api_version}", token)
        self.fork_name = fork_name

    async def get_bot_info(self, id: int) -> Optional[Bot]:
        """Returns a bot info with the given ID.

        Parameters
        ----------
        id: :class:`int`
            The ID to search for.

        Returns
        -------
        Optional[:class:`~bettercord.Bot`]
            The bot info or ``None`` if not found.
        """
        response = await self.http.get(f"/bots/{id}")
        if response is not None:
            res = await response.json()
            if response.status == 200:
                return Bot(res)
            raise BotNotFound(id, res["error"])

    async def get_bot_comments(self, id: int) -> Optional[List[Comment]]:
        """Returns a bot comments info with the given ID.

        Parameters
        ----------
        id: :class:`int`
            The ID to search for.

        Returns
        -------
        Optional[:class:`~List[bettercord.Comment]`]
            The list of comments or ``None`` if not found.
        """
        response = await self.http.get(f"/bots/{id}/comments")
        if response is not None:
            res = await response.json()
            if response.status == 200:
                return list(map(Comment, res["reviews"]))
            raise NotFound(res["error"])

    async def post_stats(self, server_count: int, shard_count: Optional[int] = None) -> Optional[bool]:
        """Returns a status of post stats.

        Parameters
        ----------
        server_count: :class:`int`
            The server count to post for.
        server_count: Optional[:class:`int`]
            The shard count to post for.

        Returns
        -------
        Optional[:class:`~bool`]
            The status or ``None`` if bad request.
        """
        response = await self.http.post("/bots/stats", headers={
            "serverCount": str(server_count),
            "shardCount": str(shard_count) or 1
        })
        if response is not None:
            res = await response.json()
            if response.status == 200:
                return True
            raise PostStatsDenied(res["error"])

    async def get_user_info(self, id: int) -> Optional[User]:
        """Returns a user info with the given ID.

        Parameters
        ----------
        id: :class:`int`
            The ID to search for.

        Returns
        -------
        Optional[:class:`~bettercord.User`]
            The user info or ``None`` if not found.
        """
        response = await self.http.get(f"/profile/{id}")
        if response is not None:
            res = await response.json()
            if response.status == 200:
                return User(res)
            raise UserNotFound(id, res["error"])

    async def check_bot_vote(self, id: int) -> Optional[bool]:
        """Returns a bot vote status with the given user ID.

        Parameters
        ----------
        id: :class:`int`
            The user ID to check for.

        Returns
        -------
        Optional[:class:`~bool`]
            The status or ``None`` if user not found.
        """
        response = await self.http.get(f"/bots/check/{id}")
        if response is not None:
            res = await response.json()
            if response.status == 200:
                return bool(res["voted"])
            raise CheckVoteForbidden(res["error"])

    async def get_server_info(self, id: int) -> Optional[Server]:
        """Returns a server info with the given ID.

        Parameters
        ----------
        id: :class:`int`
            The ID to search for.

        Returns
        -------
        Optional[:class:`~disnake.Server`]
            The server info or ``None`` if not found.
        """
        response = await self.http.get(f"/server/{id}")
        if response is not None:
            res = await response.json()
            if response.status == 200:
                return Server(res)
            raise ServerNotFound(id, res["error"])

    async def check_server_vote(self, server_id: int, user_id: int) -> Optional[bool]:
        """Returns a user vote status for server with the given server and user IDs.

        Parameters
        ----------
        server_id: :class:`int`
            The server ID to check for.
        user_id: :class:`int`
            The user ID to check for.

        Returns
        -------
        Optional[:class:`~bool`]
            The status or ``None`` if server or user not found.
        """
        response = await self.http.get(f"/server/{server_id}/{user_id}")
        if response is not None:
            res = await response.json()
            if response.status == 200:
                return bool(res["voted"])
            raise BadRequest(res["error"])

    def run(self, bot) -> None:
        """Starting task for auto posting stats every 10 minutes.

        Parameters
        ----------
        id: Union[:class:`Bot`, :class:`AutoShardedBot`]
            The discord bot client.
        """
        bot.bettercord_client = self
        Looper(bot, self.http, self.fork_name).create_loop()
