# -*- coding: utf-8 -*-

"""
MIT License

Copyright (c) 2021 capslock321

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from aiomojang.exceptions import BadRequestException, ApiException
import aiohttp
import asyncio
import datetime
import json
import base64
from typing import Optional


class Players:
    """
    Gets information on a list of users.
    """

    @staticmethod
    async def _send_payload(*queries):
        """
          Sends a request to Mojang's API.

          If more than 10 names are provided, only the first ten will be sent.
          Returns:
              dict: The json that is returned from Mojang.
        """
        async with aiohttp.ClientSession() as session:
            payload = list(queries[:10])[0]
            async with session.post(f'https://api.mojang.com/profiles/minecraft', json = payload) as resp:
                return await resp.json()

    async def get_names(self, *queries) -> list:
        """
          Returns a list of names obtained using Mojang's API.
          Returns:
              list: The names obtained.
        """
        payload = await self._send_payload(queries)
        names = []
        for item in payload:
            try:
                if 'error' in payload:
                    raise ApiException(f"{payload['errorMessage']}")
                names.append(item['name'])
            except KeyError:
                raise BadRequestException(payload['errorMessage'])
        return names

    async def get_uuids(self, *queries) -> list:
        """
          Returns a list of uuids obtained using Mojang's API.
          Returns:
              list: The uuids obtained.
        """
        payload = await self._send_payload(queries)
        uuids = []
        for item in payload:
            try:
                if 'error' in payload:
                    raise ApiException(f"{payload['errorMessage']}")
                uuids.append(item['id'])
            except KeyError:
                raise BadRequestException(payload['errorMessage'])
        return uuids


class Player:
    """
    Gets information on a user's profile.

    Attributes:
        profile(str): The user's profile you want to search up, eg. User("SomeRandomPerson")
        at(int): The person who had the name at the given timestamp. Defaults to 0

    """

    def __init__(self, profiles: str, at: Optional[int] = 0):
        self.profiles = profiles
        self.at = at

    @staticmethod
    async def _get_player_id(player):
        """
          Gets the uuid with a name
          Returns:
              str: The uuid.
        """
        async with aiohttp.ClientSession() as session:
            payload = [
                player
            ]
            async with session.post(f'https://api.mojang.com/profiles/minecraft', json=payload) as resp:
                data = await resp.json()
                return data[0]['id']

    @staticmethod
    async def _process_uuid(uuid):
        """
          Removes - from the given statement, allowing input of uuids with - in them.
          Returns:
              str: The processed uuid.
        """
        uuid = uuid.strip('-')  # remove - from the uuid if there is any
        return uuid.replace('-', '')

    async def _create_connection(self, base):
        """
          Creates a connection with Mojang's API.
          Returns:
              dict: The json that is returned from Mojang.
        """
        # used to create a connection using aiohttp
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.mojang.com/{await self._process_uuid(base)}') as resp:
                if resp.status == 204:
                    return None
                return await resp.json()

    @property
    async def name(self) -> str:
        """
          Gets the name for the user.
          Returns:
              str: Returns the name of the user.
          Raises:
              BadRequestError: If no user with these parameters can be found.
        """
        connection = await self._create_connection(f'user/profile/{self.profiles}/names')
        try:
            if 'error' in connection:
                raise ApiException(f"{connection['errorMessage']}")
            return connection[len(connection) - 1]['name']
        except KeyError:
            raise BadRequestException(connection['errorMessage'])

    @property
    async def uuid(self) -> str:
        """
           Gets the uuid for the user.
           Returns:
               str: Returns the uuid of the user.
           Raises:
              BadRequestError: If no user with these parameters can be found.
        """
        connection = await self._create_connection(f'/users/profiles/minecraft/{self.profiles}?at={self.at}')
        try:
            if 'error' in connection:
                raise ApiException(f"{connection['errorMessage']}")
            return connection['id']
        except KeyError:
            raise BadRequestException(connection['errorMessage'])

    async def get_history(self, num: Optional[int] = None) -> dict:
        """
           Gets the name history for the user.
           Returns:
               dict: Returns the name history for the given user at the given timestamp.
        """
        connection = await self._create_connection(f'user/profile/{await self.uuid}/names')
        if 'error' in connection:
            raise ApiException(f"{connection['errorMessage']}")
        if num is None:
            return connection
        return connection[num]

    @property
    async def is_legacy(self) -> bool:
        """
           Returns if the account is legacy.
           Returns:
               bool: Returns True if the account is legacy.
        """
        connection = await self._create_connection(f'/users/profiles/minecraft/{self.profiles}?at={self.at}')
        if 'error' in connection:
            raise ApiException(f"{connection['errorMessage']}")
        if 'legacy' in connection:
            return True
        return False

    @property
    async def is_demo(self) -> bool:
        """
           Returns if the account is a demo account (unpaid).
           Returns:
               bool: Returns True if the account is a demo account (unpaid).
        """
        connection = await self._create_connection(f'/users/profiles/minecraft/{self.profiles}?at={self.at}')
        if 'error' in connection:
            raise ApiException(f"{connection['errorMessage']}")
        if 'demo' in connection:
            return True
        return False

    async def _get_render_information(self, query, unsigned):
        """
          Creates a connection with Mojang's API.
          Attributes:
              query: The player to process
              unsigned: The mode in which to access the information.
          Returns:
              dict: The json that is returned from Mojang.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get('https://sessionserver.mojang.com/session/minecraft/profile/'
                                   f'{await self._process_uuid(query)}?unsigned={unsigned}') as resp:
                return await resp.json()

    async def get_raw_data(self, unsigned: bool = True):
        """
          Returns raw json for a skin or a cape
          Attributes:
              unsigned: Defaults to True, the mod in which to access the information in.
          Returns:
              dict: The raw data.
        """
        try:
            data = await self._get_render_information(self.profiles, unsigned)
            skin = base64.b64decode(data['properties'][0]['value'])
        except KeyError:
            gp = await self._get_player_id(self.profiles)  # converts name to uuid
            data = await self._get_render_information(gp, unsigned)
            skin = base64.b64decode(data['properties'][0]['value'])
        return json.loads(skin.decode('ascii'))

    async def get_skin(self, unsigned: Optional[bool] = False):
        """
        Get's the current skin that the player has on.
        Attributes:
              unsigned: Defaults to True, the mod in which to access the information in.
        Returns:
            str: The link to their skin.
        """
        data = await self.get_raw_data(unsigned)
        return data['textures']['SKIN']['url']

    async def get_cape(self, unsigned: Optional[bool] = False):
        """
        Get's the current cape that the player has on.
        Attributes:
              unsigned: Defaults to True, the mod in which to access the information in.
        Returns:
            str: The link to their cape.
        """
        data = self.get_raw_data(unsigned)
        return data

    async def signature(self, unsigned: Optional[bool] = False):
        """
          Returns the requester's base64 signature.

          Will only work if unsigned is False.
          Returns:
              str: The base64 signature.
        """
        gp = await self._get_player_id(self.profiles)  # converts name to uuid
        data = await self._get_render_information(gp, unsigned)
        return data['properties'][0]['signature']

    async def timestamp(self, unsigned: Optional[bool] = False):
        """
              Returns the formatted timestamp in which the data has been requested at.
              Returns:
                  str: The formatted timestamp.
        """
        info = await self.get_raw_data(unsigned)
        return datetime.datetime.utcfromtimestamp(info['timestamp'] / 1e3).strftime('%Y-%m-%d %H:%M:%S')
