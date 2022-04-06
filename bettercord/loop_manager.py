from typing import Optional

from .core import HttpClient


class Global:
    fork_name: str = ""
    http: Optional[HttpClient] = None


class Looper:
    def __init__(self, bot, http_client: HttpClient, fork_name: str = "discord") -> None:
        self.bot = bot
        Global.fork_name = fork_name
        Global.http = http_client
    
    def create_loop(self):
        self.bot.load_extension(".extension", package="bettercord")
