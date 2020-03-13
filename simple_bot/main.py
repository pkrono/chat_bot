#!/usr/bin/env python3

from aiohttp import web
from aiohttp.web import Request, Response, json_response
from botbuilder.core.integration import aiohttp_error_middleware
from views import messages

from config import Config

conf = Config()



APP = web.Application(middlewares=[aiohttp_error_middleware])

#app = web.Application()
APP.router.add_post("/api/messages", messages)
#messages(APP)

if __name__ == "__main__":
    try:
        web.run_app(APP, host=conf.HOST, port=conf.PORT)
    except Exception as err:
        raise err
