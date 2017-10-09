import asyncio

from aiohttp import ClientSession, TCPConnector


async def get_products_by_pks(*pks):
    async with ClientSession() as session:
        calls = [_make_product_request(session, pk) for pk in pks]
        return await asyncio.gather(*calls)


async def _make_product_request(http_client, pk):
    url = 'https://bear.ruelala.com/api/v3/products/{pk}'.format(pk=pk)
    async with http_client.get(url) as response:
        return await response.json()
