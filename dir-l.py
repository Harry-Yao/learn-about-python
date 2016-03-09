#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
import os
import datetime

def timeFormat(otime):
    return datetime.datetime.utcfromtimestamp(otime).strftime("%Y-%m-%d")

for i in os.listdir('.'):
    if os.path.isfile(i):
        print([x for x in os.stat(i)])
'''
from datetime import datetime
import os

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))
