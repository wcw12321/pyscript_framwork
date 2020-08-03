#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 13:27
# @Author  : mark.wang
# @Site    :
# @File    : settings.py
# @Software: PyCharm
import os
os.environ.setdefault('API_TOKEN', '121')
os.environ.setdefault('API', 'h123')

API_TOKEN = os.environ.get("API_TOKEN")
API = os.environ.get("API")
