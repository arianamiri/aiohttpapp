from concierge.views import post_picks, get_picks


def setup_routes(app):
    app.router.add_get('/picks/{customer_id}', get_picks, name='get_customer_picks')
    app.router.add_post('/picks', post_picks, name='add_picks')
