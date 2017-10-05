from aiohttp import web


async def post_assortment(request):
    return web.Response(text='This is where we\'ll set picks')


async def get_assortment(request):
    return web.Response(text='This is where we\'ll get picks')
