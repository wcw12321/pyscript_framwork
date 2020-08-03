#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2020/6/16 16:21
#  @Author  : mark.wang
#  @Site    :
#  @File    : message.py
#  @Software: PyCharm
import time
import uuid
import logging
from python_settings import settings

import graypy as graypy


class logger_handler:

    LOGGER_NAME = 'Logger'

    gsk_logger = ''

    gsk_logger_adapter = ''

    LOG_CONTEXT = ''

    fields = {
        '_timestamp': str(time.strftime("%Y-%m-%d %H:%M:%S")),
        '_uuid': ''.join(str(uuid.uuid4()).split('-')),
        '_version': 1.0,
        '_env': 'master',
        '_zone': 'cn',
    }

    def __init__(self, host='', port=''):
        host = host or settings.GELF_HOST
        port = port or settings.GELF_PORT
        self.gsk_logger = logging.getLogger()
        self.gsk_logger.setLevel(logging.DEBUG)
        udp_handler = graypy.GELFUDPHandler(host, int(port))
        self.gsk_logger.addHandler(udp_handler)
        self.gsk_logger_adapter = logging.LoggerAdapter(logging.getLogger(),
                                                        dict(self.fields))

    def info(self, message):
        self.gsk_logger_adapter.info(message)

    def error(self, message):
        self.gsk_logger_adapter.error(message)



