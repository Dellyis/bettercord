from typing import ClassVar, List, Optional, Tuple


class Server:
    """
    Attributes
    ----------
    id: :class:`int`
        The server's ID.
    icon: :class:`Optional[str]`
        The server's icon.
    name: :class:`str`
        The server's name.
    owner_id: :class:`Optional[str]`
        The server's owner ID.
    short_descriprion: :class:`str`
        The server's short description.
    long_descriprion: :class:`str`
        The server's long description.
    bumps: :class:`int`
        The server's bumps count.
    votes: :class:`int`
        The count of votes the server has.
    tags: :class:`list[str]`
        The server's tags.
    """

    __slots__: Tuple[str, ...] = ("id", "icon", "name", "owner_id", "short_descriprion", 
                                  "long_descriprion", "votes", "bumps", "tags", "raw_data",)

    __repr_info__: ClassVar[Tuple[str, ...]] = ("id", "icon", "name", "owner_id",
                                                "short_descriprion", "long_descriprion",
                                                "votes", "bumps", "tags",)

    def __repr__(self) -> str:
        attrs = " ".join(f"{key}={getattr(self, key)!r}" for key in self.__repr_info__)
        return f"<{self.__class__.__name__} {attrs}>"

    def __init__(self, raw_data: dict):
        self.id: int = int(raw_data["id"])
        self.icon: Optional[str] = raw_data.get("avatar")
        self.name: str = raw_data['name']
        self.owner_id: int = int(raw_data["owner"])
        self.short_descriprion: str = raw_data["shortDesc"]
        self.long_descriprion: str = raw_data["longDesc"]
        self.bumps: int = int(raw_data["bumps"])
        self.votes: int = int(raw_data["votes"])
        self.tags: List[str] = raw_data.get("tags", [])
        self.raw_data: dict = raw_data
