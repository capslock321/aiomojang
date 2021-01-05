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
from aiomojang.exceptions import RequiredPayload, IncorrectPayload
from typing import Optional


class BlockedServers:

    """Get all blocked Minecraft servers from the API."""

    @classmethod
    async def get_blocked_servers(cls):
        """
          Gets all blocked servers.

          Servers are in SHA1.

          Returns:
              list: Returns a list of all blocked server hashes.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://sessionserver.mojang.com/blockedservers') as resp:
                content = await resp.text()
                return content.splitlines()


class Statistics:

    """Get Mojang statistics given a payload."""

    def __init__(self):
        pass

    @staticmethod
    async def _send_payload(keys: str):
        async with aiohttp.ClientSession() as session:
            payload = {
                "metricKeys": [
                    keys
                ]
            }
            async with session.post(f'https://api.mojang.com/orders/statistics', json = payload) as resp:
                response = await resp.json()
                if response['total'] == 0:
                    raise IncorrectPayload(f"{keys} is not a valid payload.")
                return await resp.json()

    async def get_raw_stats(self, payload: str = None):
        """
          Gets the raw statistics for the specified payload.
          Returns:
              dict: The raw json.
          Raises:
              RequiredPayload: If you are missing the required payload.
        """
        if payload is None:
            raise RequiredPayload("You must provide at least one payload.")
        data = await self._send_payload(payload)
        return data

    async def get_total(self, payload: str = None):
        """
          Gets the total amount of sales for the specified payload.
          Returns:
              int: The total amount of sales.
          Raises:
              RequiredPayload: If you are missing the required payload.
        """
        if payload is None:
            raise RequiredPayload("You must provide at least one payload.")
        data = await self._send_payload(payload)
        return data['total']

    async def get_sales_today(self, payload: str = None):
        """
          Gets the total amount of sales in the past 24 hours.
          Returns:
              int: The total amount of sales in the past 24 hours.
          Raises:
              RequiredPayload: If you are missing the required payload.
        """
        if payload is None:
            raise RequiredPayload("You must provide at least one payload.")
        data = await self._send_payload(payload)
        return data['last24h']

    async def get_sale_velocity(self, payload: str = None):
        """
          Gets the sale velocity of the given payload.
          Returns:
              int: The sale velocity.
          Raises:
              RequiredPayload: If you are missing the required payload.
        """
        if payload is None:
            raise RequiredPayload("You must provide at least one payload.")
        data = await self._send_payload(payload)
        return data['saleVelocityPerSeconds']
