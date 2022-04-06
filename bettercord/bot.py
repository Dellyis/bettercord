from typing import ClassVar, List, Optional, Tuple


class Bot:
    """
    Attributes
    ----------
    name: :class:`str`
        The bot's username.
    id: :class:`int`
        The bot's ID.
    discriminator: :class:`int`
        The bot's discriminator. This is given when the username has conflicts.
    avatar: :class:`str`
        The channel's avatar url.
    prefix: :class:`str`
        The bot's prefix.
    owner: :class:`str`
        The bot owner's username.
    owner_id: :class:`int`
        The bot owner's id.
    coowners: :class:`list[int]`
        The bot coowners' ids.
    github: :class:`str`
        The bot's github.
    support: :class:`str`
        The bot's support server.
    website: :class:`str`
        The bot's website.
    tags: :class:`list[str]`
        The bot's tags.
    short_descriprion: :class:`str`
        The bot's short description.
    long_descriprion: :class:`str`
        The bot's long description.
    banner: class:`str`
        The bot's card banner.
    votes: :class:`int`
        The count of votes the bot has.
    certificate: :class:`bool`
        Bot certificate.
    """

    __slots__: Tuple[str, ...] = ("name", "id", "discriminator", "avatar", "prefix", "owner", 
                                  "coowners", "github", "support", "website", "tags", 
                                  "short_descriprion", "long_descriprion", "banner", "votes", 
                                  "certificate", "raw_data")

    __repr_info__: ClassVar[Tuple[str, ...]] = ("name", "id", "discriminator", "prefix", "owner", 
                                                "coowners", "tags", "votes", "certificate")

    def __repr__(self) -> str:
        attrs = " ".join(f"{key}={getattr(self, key)!r}" for key in self.__repr_info__)
        return f"<{self.__class__.__name__} {attrs}>"


    def __init__(self, raw_data: dict):
        self.name: str = raw_data["username"]
        self.id: int = int(raw_data["botID"])
        self.discriminator: int = int(raw_data["discrim"])
        self.avatar: str = raw_data["avatar"]
        self.prefix: str = raw_data["prefix"]
        self.owner: str = raw_data["owner"]
        self.owner_id: int = int(raw_data["ownerID"])
        self.coowners: List[int] = list(map(int, raw_data["coowners"]))
        self.github: Optional[str] = raw_data.get("github")
        self.support: Optional[str] = raw_data.get("support")
        self.website: Optional[str] = raw_data.get("website")
        self.tags: List[str] = raw_data.get("tags", [])
        self.short_descriprion: str = raw_data["shortDesc"]
        self.long_descriprion: str = raw_data["longDesc"]
        self.banner: Optional[str] = raw_data.get("background")
        self.votes: int = raw_data["votes"]
        self.certificate: bool = raw_data["certificate"] == "Certified"
        self.raw_data: dict = raw_data
