import socket
from aiohttp import web


async def post_assortment(request):
    host_name = socket.gethostname()
    text = '{}: This is where we\'ll set picks'.format(host_name)
    return web.Response(text=text)


async def get_assortment(request):
    host_name = socket.gethostname()
    text = '{}: This is where we\'ll get picks'.format(host_name)
    return web.Response(text=text)
