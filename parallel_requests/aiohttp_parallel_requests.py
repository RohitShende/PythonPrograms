import asyncio
import aiohttp





async def get_principal_name(session, url, token):
    async with session.get(url, headers=token) as resp:
        if resp.status_code == 200:
            principal_info = await resp.json()
            principal_name = principal_info['displayName']
            # print(f"Principal Name for principal id = {principal_id}  retrieved as : {principal_name}")
            return principal_name
        # print(f"GET call for principal name failed for principal id = {principal_id} with status code : {resp.status_code}, and response as {resp.text}")
        return None


async def main():
    async with aiohttp.ClientSession(trust_env=True) as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.ensure_future(get_principal_name(session, url, graph_token)))

        principal_names = await asyncio.gather(*tasks)
        print(principal_names)


if __name__ == '__main__':
    asyncio.run(main())
