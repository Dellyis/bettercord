from typing import Any


class BettercordException(Exception):
    pass


class BadRequest(BettercordException):
    pass


class Forbidden(BettercordException):
    pass


class NotFound(BettercordException):
    pass


class BotNotFound(NotFound):
    def __init__(self, bot_id: int, *args: Any):
        self.bot_id: int = bot_id
        super().__init__(*args)


class PostStatsDenied(BadRequest):
    pass


class UserNotFound(NotFound):
    def __init__(self, user_id: int, *args: Any):
        self.user_id: int = user_id
        super().__init__(*args)


class CheckVoteForbidden(Forbidden):
    pass


class ServerNotFound(NotFound):
    def __init__(self, server_id: int, *args: Any):
        self.server_id: int = server_id
        super().__init__(*args)
