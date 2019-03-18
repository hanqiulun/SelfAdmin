# -*- coding: utf-8 -*-
'''
------------------------------------------------------------
File Name: app.py
Description : 
Project: api-server
Last Modified: Monday, 18th March 2019 1:45:25 pm
-------------------------------------------------------------
'''

from typing import (
    NoReturn
)
from importlib import import_module
from inspect import isclass

from aiohttp import web
from aiohttp.web import Application
import aiohttp_cors
from api_server.settings import *


def init_routes(app: Application) ->NoReturn:
    # import all current_api_version dir apis
    module = import_module(f"api_server.apis.{CURRENT_API_VERSION}")
    for i in dir(module):
        if not i.startswith("__"):
            object = getattr(module, i)
            if not isclass(object):
                app.add_routes(object)
    # config api cors
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })
    for route in list(app.router.routes()):
        cors.add(route)


def init_app():
    app = web.Application()
    # config routes
    init_routes(app=app)
    return app
