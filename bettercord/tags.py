from typing import List


class BotTags:
    def __init__(self, tags: List[str]):
        tags = list(map(str.lower, tags))
        self.moderation: bool = "moderation" in tags
        self.fun: bool = "fun" in tags
        self.minecraft: bool = "minecraft" in tags
        self.economy: bool = "economy" in tags
        self.guard: bool = "guard" in tags
        self.nsfw: bool = "nsfw" in tags
        self.anime: bool = "anime" in tags
        self.invite: bool = "invite" in tags
        self.music: bool = "music" in tags
        self.logging: bool = "logging" in tags
        self.dashboard: bool = "web dashboard" in tags
        self.reddit: bool = "reddit" in tags
        self.youtube: bool = "youtube" in tags
        self.twitch: bool = "twitch" in tags
        self.crypto: bool = "crypto" in tags
        self.leveling: bool = "leveling" in tags
        self.game: bool = "game" in tags
        self.roleplay: bool = "roleplay" in tags
        self.utility: bool = "utility" in tags
        self.turkish: bool = "turkish" in tags
        self.all: List[str] = tags


class ServerTags:
    def __init__(self, tags: List[str]):
        tags = list(map(str.lower, tags))
        self.development: bool = "development" in tags
        self.stream: bool = "stream" in tags
        self.media: bool = "media" in tags
        self.company: bool = "company" in tags
        self.game: bool = "game" in tags
        self.emoji: bool = "emoji" in tags
        self.bot_list: bool = "bot list" in tags
        self.server_list: bool = "server list" in tags
        self.turkish: bool = "turkish" in tags
        self.support: bool = "supprot" in tags
        self.sound: bool = "sound" in tags
        self.chatting: bool = "chatting" in tags
        self.nsfw: bool = "nsfw" in tags
        self.challange: bool = "challange" in tags
        self.protest: bool = "protest" in tags
        self.roleplay: bool = "roleplay" in tags
        self.meme: bool = "meme" in tags
        self.shop: bool = "shop" in tags
        self.technology: bool = "technology" in tags
        self.fun: bool = "fun" in tags
        self.social: bool = "social" in tags
        self.esport: bool = "e-spor" in tags
        self.design: bool = "design" in tags
        self.community: bool = "community" in tags
        self.all: List[str] = tags
