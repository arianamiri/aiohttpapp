from aiohttp import web

from concierge.managers import PicksManager


async def post_picks(request):
    """
    create picks for the user
    payload:
    {
        stlyistId: <int>,
        customerId: <int>,
        products: [
            <int>,
            <int>,
            ...
        ]
    }
    """
    post_data = await request.json()

    stylist_id = post_data.get('stylistID')
    customer_id = post_data.get('memberID')
    products = post_data.get('styles')

    PicksManager.create_picks(stylist_id, customer_id, *products)
    data = {
        'url': request.app.router['get_customer_picks'].url_for(
            customer_id=customer_id
        ).path
    }

    return web.json_response(data)


async def get_picks(request):
    host_name = socket.gethostname()
    text = '{}: This is where we\'ll get picks'.format(host_name)
    return web.Response(text=text)
