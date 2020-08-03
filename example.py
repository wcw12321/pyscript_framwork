#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  @Time    : 2020/8/3 17:58
#  @Author  : mark.wang
#  @Site    :
#  @File    : example.py
#  @Software: PyCharm
import os
from python_settings import settings

if __name__ == '__main__':
    DEFAULT_SETTING = 'config.settings'
    # Initial setting file
    os.environ.get("SETTINGS_MODULE") or os.environ.setdefault('SETTINGS_MODULE', DEFAULT_SETTING)
    print(settings.API_TOKEN)
