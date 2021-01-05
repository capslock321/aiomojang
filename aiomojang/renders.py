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

import aiohttp
import base64
import json
import re
import asyncio
import datetime
from typing import Optional


class Render:
    """
        Gets information on a skin or cape.

        Attributes:
            player(str): The user's profile you want to search up.
            unsigned(bool): If the request is unsigned.

    """

    def __init__(self, player, unsigned: Optional[bool] = True):
        self.player = player
        self.unsigned = unsigned

    @staticmethod
    async def _process_uuid(uuid):
        uuid = uuid.strip('-')  # remove - from the uuid if there is any
        return uuid.replace('-', '')

    @staticmethod
    async def _get_player_id(player):
        async with aiohttp.ClientSession() as session:
            payload = [
                player
            ]
            async with session.post(f'https://api.mojang.com/profiles/minecraft', json = payload) as resp:
                data = await resp.json()
                return data[0]['id']

    async def _create_connection(self, query):
        """
          Creates a connection with Mojang's API.
          Returns:
              dict: The json that is returned from Mojang.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get('https://sessionserver.mojang.com/session/minecraft/profile/'
                                   f'{await self._process_uuid(query)}?unsigned={str(self.unsigned).lower()}') as resp:
                return await resp.json()

    async def raw(self):
        """
          Returns raw json for a skin or a cape
          Returns:
              dict: The raw data.
        """
        try:
            data = await self._create_connection(self.player)
            skin = base64.b64decode(data['properties'][0]['value'])
        except KeyError:
            gp = await self._get_player_id(self.player)  # converts name to uuid
            data = await self._create_connection(gp)
            skin = base64.b64decode(data['properties'][0]['value'])
        return json.loads(skin.decode('ascii'))

    async def timestamp(self):
        """
              Returns the formatted timestamp in which the data has been requested at.
              Returns:
                  str: The formatted timestamp.
        """
        info = await self.raw()
        return datetime.datetime.utcfromtimestamp(info['timestamp'] / 1e3).strftime('%Y-%m-%d %H:%M:%S')

    async def profile_id(self):
        """
          Returns the profile's uuid for the user being requested.
          Returns:
              str: The players uuid.
        """
        info = await self.raw()
        return info['profileId']

    async def profile_name(self):
        """
          Returns the profile's name for the user being requested.
          Returns:
              str: The players name.
        """
        info = await self.raw()
        return info['profileName']

    async def signature(self):
        """
          Returns the requester's base64 signature.

          Will only work if unsigned is False.
          Returns:
              str: The base64 signature.
        """
        data = await self._create_connection()
        return data['properties'][0]['signature']


class Skin(Render):

    def __init__(self, player, unsigned: Optional[bool] = True):
        super().__init__(player, unsigned)

    @property
    async def model(self):
        try:
            info = await self.raw()
            return info['textures']['SKIN']['metadata']['model']
        except KeyError:
            return "classic"

    @property
    async def id(self):
        """
          Returns the skin render id.

          Returns:
              str: The id for the skin.
        """
        info = await self.raw()
        return info['textures']['SKIN']['url'][38:]

    async def url(self):
        """
          Returns the skin render url.

          Returns:
              str: The url for the skin.
        """
        info = await self.raw()
        return info['textures']['SKIN']['url']


class Cape(Render):

    def __init__(self, player, unsigned: Optional[bool] = True):
        super().__init__(player, unsigned)

    @property
    async def id(self):
        """
              Returns the cape render id.

              Returns:
                  str: The id for the cape.
        """
        info = await self.raw()
        return info['textures']['CAPE']['url'][38:]

    async def url(self):
        """
          Returns the cape render url.

          Returns:
              str: The render url for the cape.
        """
        info = await self.raw()
        return info['textures']['CAPE']['url']




