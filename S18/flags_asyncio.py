# BEGIN FLAGS_ASYNCIO
import asyncio

import aiohttp  # <1>

from PythonTest.S17.flags import save_flag, show, main, BASE_URL  # <2>

  # <3>
async def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    async with aiohttp.ClientSession() as session:  # <4>
        resp = await session.get(url)
        if resp.status == 200:
            image = await resp.read()  # <5>
            return image


async def download_one(cc):  # <6>
    image = await get_flag(cc)  # <7>
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    #loop = asyncio.get_event_loop()
    #loop.run_in_executor(None, save_flag, image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    loop = asyncio.get_event_loop()  # <8>
    to_do = [download_one(cc) for cc in sorted(cc_list)]  # <9>
    wait_coro = asyncio.wait(to_do)  # <10>
    res, _ = loop.run_until_complete(wait_coro)  # <11>
    loop.close()  # <12>

    return len(res)


if __name__ == '__main__':
    main(download_many)
# END FLAGS_ASYNCIO