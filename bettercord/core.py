from typing import Dict, Union

import aiohttp

class HttpClient:
    def __init__(self, base_url: str, authorization_token: str):
        self.base_url: str = base_url
        self.token: str = authorization_token

    async def get(self, path: str, headers: Dict[str, Union[str, int]] = {}):
        url = self.base_url + path
        headers["Authorization"] = self.token

        try:
            async with aiohttp.ClientSession() as session:
                return (await session.get(url, headers=headers))
        except Exception as err:
            print((
                f"[ BETTERCORD.PY ] An error occurred during exception of the GET request: {err}\n"
                "More information about this request:\n"
                f"URL: {url}\nHeaders: {headers}"))

        return None

    async def post(self, path: str, headers: Dict[str, Union[str, int]] = {}):
        url = self.base_url + path
        headers["Authorization"] = self.token

        try:
            async with aiohttp.ClientSession() as session:
                return (await session.post(url, headers=headers))
        except Exception as err:
            print((
                f"[ BETTERCORD.PY ] An error occurred during exception of the POST request: {err}\n"
                "More information about this request:\n"
                f"URL: {url}\nHeaders: {headers}"))
