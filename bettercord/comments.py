from datetime import datetime
from typing import ClassVar, Optional, Tuple


class Comment:
    """
    Attributes
    ----------
    author_id: :class:`int`
        The comment's author id.
    rate: :class:`int`
        The comment's stars count. From 1 up to 5.
    content: :class:`str`
        The comment's content.
    date: :class:`datetime`
        The comment's posting time.
    edited: :class:`bool`
        The flag indicates whether the comment has been changed.
    reply: :class:`Optional[str]`
        The reply bot's owner.
    """

    __slots__: Tuple[str, ...] = ("author_id", "rate", "content", "date", "edited", "reply", "raw_data")

    __repr_info__: ClassVar[Tuple[str, ...]] = ("author_id", "rate", "content", "date", "edited", "reply")

    def __repr__(self) -> str:
        attrs = " ".join(f"{key}={getattr(self, key)!r}" for key in self.__repr_info__)
        return f"<{self.__class__.__name__} {attrs}>"

    def __init__(self, raw_data: dict):
        self.author_id: int = int(raw_data["author"])
        self.rate: int = int(raw_data["star_rate"])
        self.content: str = raw_data["message"] if not bool(raw_data.get("edit")) else raw_data["edit"]
        self.date: datetime = datetime.utcfromtimestamp(raw_data["date"] / 1000)
        self.edited: bool = bool(raw_data.get("edit"))
        self.reply: Optional[str] = raw_data.get("reply")
        self.raw_data: dict = raw_data
