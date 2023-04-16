import asyncio
from flask import redirect
from vk_api import VkApi, ApiError, Captcha
from vk_api.vk_api import VkApiMethod
from .utils import main


class VkWorker():
    def __init__(self, phone: str, password: str):
        self.login = phone
        self.password = password
        self.token = None

    def _session(self) -> VkApiMethod:
        """Get a session via vk_api for
        sending requests to vk and set token"""
        vk_session = VkApi(self.login, self.password)
        vk_session.auth()
        self.token = vk_session.token['access_token']
        session = vk_session.get_api()
        return session

    def _get_friend_list(self) -> list:
        """Method return a list of friend of current user.
        It needs for get a friend's groups """
        session = self._session()
        friends = session.friends.get()['items']
        return friends

    async def _get_friend_groups(self) -> dict:
        """Method async because sync method too slow, but
        we have a vk api rule 5 request per second. It's a try
        to be a faster. Return a dict of friend's groups"""
        token = ''
        friends = self._get_friend_list()
        friends_groups = await main(friends, self.token)
        return friends_groups

    def get_user_groups(self) -> dict:
        """Method return a dict {group id: group name} of
        current user"""
        session = self._session()
        groups = {group['id']: group['name'] for group in session.groups.get(extended=1)['items']}
        return groups

    async def get_user_friends_groups(self) -> dict:
        """Method collect users group and friends group"""
        friends_groups = await self._get_friend_groups()
        groups = self.get_user_groups()
        groups.update(friends_groups)
        return groups

    #
    @staticmethod
    def captcha_handle(phone:str, password:str) -> dict or str:
        """Method use for handling captcha error, return
        dict with sid of captcha and url for captcha"""
        try:
            handler = VkApi(phone, password)
            handler.auth()
            return 'Captcha dont needed'
        except Captcha as error:
            url = error.get_url()
            sid = error.sid
            return {'url': url, 'sid': sid}

    @staticmethod
    def captcha_solver(user_and_captcha_data: dict, *args, **kwargs) -> str:
        """Method use for solving the captcha. Takes dict of data with
        sid,phone,pass,key of captcha. Return success string."""
        sid = user_and_captcha_data['sid'][0]
        phone = user_and_captcha_data['phone']
        password = user_and_captcha_data['password']
        key = user_and_captcha_data['key']
        solver = VkApi(phone, password)
        try:
            solver.auth()
            return 'Captcha dont needed'
        except Captcha as error:
            error.sid = sid
            error.try_again(key)
            return 'Captcha solved'
