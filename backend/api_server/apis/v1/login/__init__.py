# -*- coding: utf-8 -*-
'''
------------------------------------------------------------
File Name: __init__.py
Description : 
Project: login
Last Modified: Monday, 18th March 2019 1:54:53 pm
-------------------------------------------------------------
'''


from aiohttp import web
from aiohttp_cors import (
    CorsViewMixin,
)
from aiohttp.web_response import Response

login = web.RouteTableDef()
d = {
    "admin": {
        "roles": ['admin'],
        "token": 'admin',
        "introduction": '我是超级管理员',
        "avatar": 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
        "name": 'Super Admin'
    },
    "editor": {
        "roles": ['editor'],
        "token": 'editor',
        "introduction": '我是编辑',
        "avatar": 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
        "name": 'Normal Editor'
    }
}


@login.view('/login/login')
class _(
    web.View,
    CorsViewMixin
):
    async def post(self) -> Response:
        a = web.json_response(d["admin"])
        return web.json_response(d["admin"])


@login.view('/login/logout')
class _(
    web.View,
    CorsViewMixin
):
    async def post(self) -> Response:
        return web.json_response(d["admin"])
