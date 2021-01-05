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
from aiomojang.exceptions import AuthenticationError, SecurityQuestionsRequired
from typing import Optional


class Authorization:
    """
    Gets information on things that requires login.

    Attributes:
        username(str): The user's username.
        password(str): The user's password.
        game(str): The game in which to get.
        ctoken(bool): The client token.
        request_user(bool): If you want additional infromation.

    """

    def __init__(self, username: str, password: str,
                 game: Optional[str] = "Minecraft",
                 ctoken: Optional[str] = None,
                 request_user: Optional[str] = True):
        self.username = username
        self.password = password
        self.ctoken = ctoken
        self.request_user = request_user
        self.game = game

    @staticmethod
    async def _send_payload(query, payload):
        """
          Sends a given payload.
          Returns:
              dict: The request json.
        """
        async with aiohttp.ClientSession() as session:
            async with session.post(f'https://authserver.mojang.com/{query}', json=payload) as resp:
                if resp.status != 200:
                    r = await resp.json()
                    raise AuthenticationError(r['errorMessage'])
                return await resp.json()

    async def login(self):
        """
          Logs in the user.
          Returns:
              dict: The login status.
        """
        auth_payload = {
            "agent": {
                "name": self.game,
                "version": 1
            },
            "user": self.username,
            "password": self.password,
            "clientToken": self.ctoken,
            "requestUser": self.request_user
        }
        data = await self._send_payload("authenticate", auth_payload)
        return data

    async def refresh(self, access_token, get_id, client_id: Optional[str] = None):
        """
          Refreshes the given access token.
          Returns:
              dict: The refresh status.
        """
        refresh_payload = {
            "accessToken": access_token,
            "clientToken": client_id,

            "selectedProfile": {
                "id": get_id,
                "name": self.username
            },
            "requestUser": self.request_user
        }
        data = await self._send_payload("refresh", refresh_payload)
        return data

    async def validate(self, access_token, client_id: Optional[str] = None):
        """
          Validate a token.
          Returns:
              dict: The validation status.
        """
        validate_payload = {
            "accessToken": access_token,
            "clientToken": client_id
        }
        data = await self._send_payload("refresh", validate_payload)
        return data

    async def signout(self, username, password):
        """
          Signs out the user.
          Returns:
              dict: The signout status.
        """
        signout_payload = {
            "username": username,
            "password": password
        }
        data = await self._send_payload("refresh", signout_payload)
        return data

    async def invalidate(self, access_token, client_id: Optional[str] = None):
        """
          Invalidate the provided access token.
          Returns:
              dict: The invalidation status.
        """
        invalidate_payload = {
            "accessToken": access_token,
            "clientToken": client_id
        }
        data = await self._send_payload("refresh", invalidate_payload)
        return data

    @property
    async def access_token(self):
        """
          Get's the access token from the login infromation.
          Returns:
              str: The access token.
        """
        data = await self.login()
        return data['accessToken']

    @property
    async def client_token(self):
        """
          Get's the client token from the login infromation.
          Returns:
              str: The client token.
        """
        data = await self.login()
        return data['clientToken']

    @property
    async def id(self):
        """
          Get's the id of the profile.
          Returns:
              str: The id.
        """
        data = await self.login()
        return data['selectedProfile']['id']

    @property
    async def name(self):
        """
          Get's the name of the account.
          Returns:
              str: The name of the account.
        """
        data = await self.login()
        return data['selectedProfile']['name']

    @property
    async def user_id(self):
        """
          Get's the user id.
          Returns:
              str: The user id.
        """
        data = await self.login()
        return data['selectedProfile']['userId']

    @property
    async def created_at(self):
        """
          Gets the account created at date.
          Returns:
              str: The created at date.
        """
        data = await self.login()
        return data['selectedProfile']['createdAt']

    @property
    async def is_legacy(self):
        """
          Checks to see if the account is legacy.
          Returns:
              str: The status.
        """
        data = await self.login()
        return data['selectedProfile']['legacy']

    @property
    async def is_suspended(self):
        """
          Checks to see if the account is suspended.
          Returns:
              str: The status.
        """
        data = await self.login()
        return data['selectedProfile']['suspended']

    @property
    async def is_paid(self):
        """
          Checks to see if the account is paid.
          Returns:
              str: The status.
        """
        data = await self.login()
        return data['selectedProfile']['paid']

    @property
    async def is_migrated(self):
        """
          Checks the migration status.
          Returns:
              str: The access token.
        """
        data = await self.login()
        return data['selectedProfile']['migrated']

    @property
    async def user_identifier(self):
        """
          Get's the user identifier..
          Returns:
              str: The user identifier.
        """
        data = await self.login()
        return data['user']['id']

    @property
    async def email(self):
        """
          Gets the email registered with the account.
          Returns:
              str: The email.
        """
        data = await self.login()
        return data['user']['email']

    @property
    async def uname(self):
        """
          Get's the username.
          Returns:
              str: The username.
        """
        data = await self.login()
        return data['user']['username']

    @property
    async def ip(self):
        """
          Get's the ip.
          Returns:
              str: The ip.
        """
        data = await self.login()
        return data['user']['registerIp']

    @property
    async def migrated_from(self):
        """
          Get's where the account was migrated from.
          Returns:
              str: The migration location.
        """
        data = await self.login()
        return data['user']['migratedFrom']

    @property
    async def migrated_at(self):
        """
          Get's time time when the account was migrated.
          Returns:
              str: The time.
        """
        data = await self.login()
        return data['user']['migratedAt']

    @property
    async def registered_at(self):
        """
          Get's the time when the account was registered.
          Returns:
              str: The time of registration.
        """
        data = await self.login()
        return data['user']['registeredAt']

    @property
    async def password_changed_at(self):
        """
          Gets the time the password was changed at.
          Returns:
              str: The changed at time.
        """
        data = await self.login()
        return data['user']['passwordChangedAt']

    @property
    async def dob(self):
        """
          Get's the date of birth
          Returns:
              str: The dob.
        """
        data = await self.login()
        return data['user']['dateOfBirth']

    @property
    async def is_email_verified(self):
        """
          Checks if the email is verified.
          Returns:
              str: The status.
        """
        data = await self.login()
        return data['user']['emailVerified']

    @property
    async def is_verified_by_parent(self):
        """
          Checks to see if the account is verified by a parent.
          Returns:
              str: The status.
        """
        data = await self.login()
        return data['user']['verifiedByParent']

    @property
    async def is_blocked(self):
        """
          Checks to see if the thing is blocked.
          Returns:
              str: The blocked status.
        """
        data = await self.login()
        return data['user']['blocked']

    @property
    async def is_secured(self):
        """
          Checks to see if the thing is secured.
          Returns:
              str: The security status.
        """
        data = await self.login()
        return data['user']['secured']

    @property
    async def preferred_language(self):
        """
          Get's the preferred language from the login infromation.
          Returns:
              str: The preferred language token.
        """
        data = await self.login()
        return data['user']['properties'][0]['value']

    @property
    async def twitch_access_token(self):
        """
          Get's the twitch token from the login infromation.
          Returns:
              str: The twitch access token.
        """
        data = await self.login()
        return data['user']['properties'][1]['name']

    @property
    async def twitch_oauth_token(self):
        """
          Get's the access token from the login infromation.
          Returns:
              str: The twitch oauth token.
        """
        data = await self.login()
        return data['user']['properties'][1]['value']


class User(Authorization):

    def __init__(self, username: str, password: str,
                 game: Optional[str] = "Minecraft",
                 ctoken: Optional[str] = None,
                 request_user: Optional[str] = True):
        super().__init__(username, password, game, ctoken, request_user)

    @staticmethod
    async def _check_security_questions(auth_token):
        """
          Makes a request to check if security questions are needed for the account.
          Args:
              auth_token: The Authentication token.
          Returns:
              dict: The raw json.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.mojang.com/user/security/location',
                                   headers = {"Authorization": f"Bearer {auth_token}"}) as resp:
                return await resp.json()

    async def _change_name(self, payload: str, new_name):
        """
          Makes a request to change a player's name.
          Args:
              payload: The auth token.
              new_name: The new name to change to.
          Returns:
              dict: The raw json.
          Raises:
              SecurityQuestionsRequired: If security questions are required.
              AuthenticationError: Any other error.
        """
        async with aiohttp.ClientSession() as session:
            async with session.put(f'https://api.minecraftservices.com/minecraft/profile/name/{new_name}',
                                   headers = {"Authorization": f"Bearer {payload}"}) as resp:
                check = await self._check_security_questions(payload)
                if check['error'] == "ForbiddenOperationException":
                    raise SecurityQuestionsRequired("Security questions are required.")
                if resp.status != 200:
                    r = await resp.json()
                    raise AuthenticationError(r['errorMessage'])
                return await resp.json()

    async def _change_skin(self, payload: str, uuid):
        """
          Makes a request to change a player's name.
          Args:
              payload: The auth token.
              uuid: The uuid of the player..
          Returns:
              dict: The raw json.
          Raises:
              SecurityQuestionsRequired: If security questions are required.
              AuthenticationError: Any other error.
        """
        async with aiohttp.ClientSession() as session:
            async with session.post(f'https://api.mojang.com/user/profile/{uuid}/skin', files = dict(model = payload),
                                   headers = {"Authorization": f"Bearer{payload}"}) as resp:
                check = await self._check_security_questions(payload)
                if check['error'] == "ForbiddenOperationException":
                    raise SecurityQuestionsRequired("Security questions are required.")
                if resp.status != 200:
                    r = await resp.json()
                    raise AuthenticationError(r['errorMessage'])
                return await resp.json()

    async def _upload_skin(self, payload: str, file, var: Optional[str] = "slim"):
        """
          Makes a request to change a player's name.
          Args:
              payload: The auth token.
              file: The file of the new skin.
              var: The model to request.
          Returns:
              dict: The raw json.
          Raises:
              SecurityQuestionsRequired: If security questions are required.
              AuthenticationError: Any other error.
        """
        async with aiohttp.ClientSession() as session:
            async with session.post(f'https://api.minecraftservices.com/minecraft/profile/skins', files=dict(variant=var, file=file),
                                    headers = {"Authorization": f"Bearer{payload}"}) as resp:
                check = await self._check_security_questions(payload)
                if check['error'] == "ForbiddenOperationException":
                    raise SecurityQuestionsRequired("Security questions are required.")
                if resp.status != 200:
                    r = await resp.json()
                    raise AuthenticationError(r['errorMessage'])
                return await resp.json()

    async def _reset_skin(self, payload: str, uuid: str):
        """
          Makes a request to change a player's name.
          Args:
              payload: The auth token.
              uuid: The player's uuid.
          Returns:
              dict: The raw json.
          Raises:
              SecurityQuestionsRequired: If security questions are required.
              AuthenticationError: Any other error.
        """
        async with aiohttp.ClientSession() as session:
            async with session.delete(f'https://api.mojang.com/user/profile/{uuid}/skin',
                                      headers={"Authentication": f"Bearer {payload}"}) as resp:
                check = await self._check_security_questions(payload)
                if check['error'] == "ForbiddenOperationException":
                    raise SecurityQuestionsRequired("Security questions are required.")
                if resp.status != 200:
                    r = await resp.json()
                    raise AuthenticationError(r['errorMessage'])
                return await resp.json()

    async def change_name(self, auth_token, new_name: str):
        """See the respective protected classes."""
        data = await self._change_name(auth_token, new_name)
        return data

    async def change_skin(self, auth_token, uuid: str):
        """See the respective protected classes."""
        data = await self._change_skin(auth_token, uuid)
        return data

    async def upload_skin(self, auth, file, var: str):
        """See the respective protected classes."""
        data = await self._upload_skin(auth, file, var)
        return data

    async def reset_skin(self, auth_token, uuid: str):
        """See the respective protected classes."""
        data = await self._reset_skin(auth_token, uuid)
        return data

    @staticmethod
    async def security_questions(auth_token):
        """Get's a list fo security questions.
           Args:
               auth_token: The access token.
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.mojang.com/user/security/challenges', headers = {"Authorization": f"Bearer {auth_token}"}) as resp:
                return await resp.json()
