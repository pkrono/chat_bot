from botbuilder.core import (
    BotFrameworkAdapter,
    BotFrameworkAdapterSettings,
    TurnContext,
)

from botbuilder.schema import Activity

from botbuilder.schema import Activity, ActivityTypes
from aiohttp.web import Request, Response, json_response

from bot import *

bot = Bot()

SETTINGS = BotFrameworkAdapterSettings("","")
ADAPTER = BotFrameworkAdapter(SETTINGS)

# Listen for incoming requests on /api/messages
async def messages(req: Request) -> Response:
    # Main bot message handler.
    if "application/json" in req.headers["Content-Type"]:
        body = await req.json()
    else:
        return Response(status=415)

    activity = Activity().deserialize(body)
    auth_header = req.headers["Authorization"] if "Authorization" in req.headers else ""

    try:
        response = await ADAPTER.process_activity(activity, auth_header, bot.on_message)
        if response:
            return json_response(data=response.body, status=response.status)
        return Response(status=201)
    except Exception as err:
        raise err
