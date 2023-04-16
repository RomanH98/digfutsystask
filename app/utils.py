import asyncio
import time
import aiohttp


async def get_groups(friend, session, token):
    url = 'https://api.vk.com/method/groups.get'
    parametres = {
        'access_token': token,
        'v': '5.131', 'user_id': friend, 'extended': 1}
    async with session.get(url=url, params=parametres) as response:
        data_json = await response.json()
        if 'error' in data_json:
            '''some logic for says that user have private groups or was deleted'''
            pass
        else:
            result = data_json['response']
            groups = {i['id']: i['name'] for i in result['items']}
            return groups


async def main(friends, token):
    results = {}
    async with aiohttp.ClientSession() as session:
        for i in range(0, len(friends), 3):
            tasks = [asyncio.ensure_future(get_groups(friends[i], session, token))]

            if i + 1 < len(friends):
                tasks.append(asyncio.ensure_future(
                    get_groups(friends[i + 1], session, token)
                ))
                if i + 2 < len(friends):
                    tasks.append(asyncio.ensure_future(
                        get_groups(friends[i + 2], session, token)
                    ))
            result = await asyncio.gather(*tasks)
            for i in result:
                if i:
                    results.update(i)
            time.sleep(1)
    return results