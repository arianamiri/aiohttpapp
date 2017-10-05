from aiohttp import web

from concierge.routes import setup_routes

app = web.Application()
setup_routes(app)

if __name__ == '__main__':
    web.run_app(app, port=5858)
