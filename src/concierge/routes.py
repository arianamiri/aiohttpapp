from concierge.views import post_assortment, get_assortment


def setup_routes(app):
    app.router.add_get('/assortments', get_assortment)
    app.router.add_post('/assortments', post_assortment)
