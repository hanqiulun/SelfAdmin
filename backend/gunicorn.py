# -*- coding: utf-8 -*-
'''
------------------------------------------------------------
File Name: gunicorn.py
Description : 
Project: backend
Last Modified: Monday, 18th March 2019 3:30:36 pm
-------------------------------------------------------------
'''

import multiprocessing
bind = '127.0.0.1:8000'
backlog = 512 
timeout = 30 
worker_class = 'aiohttp.GunicornWebWorker'

workers = multiprocessing.cpu_count() * 2 + 1 
