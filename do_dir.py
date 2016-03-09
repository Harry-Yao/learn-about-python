# -*- coding: utf-8 -*-

from datetime import datetime
import os

pwd = os.path.abspath('.')
key = input('Please inter what you want to search:\n')
for f in os.walk(pwd+key):
    print(f)