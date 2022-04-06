from typing import ClassVar, Optional, Tuple


class User:
    """
    Attributes
    ----------
    id: :class:`int`
        The user's id.
    biogryphy: :class:`Optional[str]`
        The user's biography.
    website: :class:`Optional[str]`
        The user's website.
    github: :class:`Optional[str]`
        The user's github.
    twitter: :class:`Optional[str]`
        The user's twitter.
    instagram: :class:`Optional[str]`
        The user's instagram.
    """

    __slots__: Tuple[str, ...] = ("id", "biogryphy", "website", "github", "twitter", "instagram", "raw_data")

    __repr_info__: ClassVar[Tuple[str, ...]] = ("id", "biogryphy", "website", "github", "twitter", "instagram",)

    def __repr__(self) -> str:
        attrs = " ".join(f"{key}={getattr(self, key)!r}" for key in self.__repr_info__)
        return f"<{self.__class__.__name__} {attrs}>"

    def __init__(self, raw_data: dict):
        self.id: int = int(raw_data["id"])
        self.biography: Optional[str] = raw_data.get("biogryphy")
        self.website: Optional[str] = raw_data.get("website")
        self.github: Optional[str] = raw_data.get("github")
        self.twitter: Optional[str] = raw_data.get("twitter")
        self.instagram: Optional[str] = raw_data.get("instagram")
        self.raw_data: dict = raw_data
