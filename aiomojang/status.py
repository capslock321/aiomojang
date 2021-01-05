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
import asyncio


class Status:

    def __init__(self):
        pass

    """Get information on the status of Mojang services."""

    @staticmethod
    async def _create_connection():
        async with aiohttp.ClientSession() as session:
            async with session.get('https://status.mojang.com/check') as resp:
                return await resp.json()

    async def raw(self) -> list:
        data = await self._create_connection()  # nothing really much to do in here
        return data

    @property
    async def session(self) -> str:
        """
          Gets the status of session.minecraft.net.
          Returns:
              str: The status of session.minecraft.net.
        """
        data = await self.raw()
        for x in data:
            try:
                return x['session.minecraft.net']
            except KeyError:
                continue

    @property
    async def account(self) -> str:
        """
          Gets the status of account.mojang.com.
          Returns:
              str: The status of account.mojang.com.
        """
        data = await self.raw()
        for x in data:
            try:
                return x['account.mojang.com']
            except KeyError:
                continue

    @property
    async def auth(self) -> str:
        """
          Gets the status of authserver.mojang.com.
          Returns:
              str: The status of authserver.mojang.com.
        """
        data = await self.raw()
        for x in data:
            try:
                return x['authserver.mojang.com']
            except KeyError:
                continue

    @property
    async def sessionserver(self) -> str:
        """
          Gets the status of sessionserver.mojang.com.
          Returns:
              str: The status of sessionserver.mojang.com.
        """
        data = await self.raw()
        for x in data:
            try:
                return x['sessionserver.mojang.com']
            except KeyError:
                continue

    @property
    async def api(self) -> str:
        """
          Gets the status of api.mojang.com.
          Returns:
              str: The status of api.mojang.com.
        """
        data = await self.raw()
        for x in data:
            try:
                return x['api.mojang.com']
            except KeyError:
                continue

    @property
    async def textures(self) -> str:
        """
          Gets the status of textures.minecraft.net.
          Returns:
              str: The status of textures.minecraft.net.
        """
        data = await self.raw()
        for x in data:
            try:
                return x['textures.minecraft.net']
            except KeyError:
                continue

    @property
    async def mojang(self) -> str:
        """
          Gets the status of mojang.com.
          Returns:
              str: The status of mojang.com.
        """
        data = await self.raw()
        for x in data:
            try:
                return x['mojang.com']
            except KeyError:
                continue

    @property
    async def minecraft(self) -> str:
        """
          Gets the status of minecraft.net.
          Returns:
              str: The status of minecraft.net.
        """
        data = await self.raw()
        for x in data:
            try:
                return x['minecraft.net']
            except KeyError:
                continue

