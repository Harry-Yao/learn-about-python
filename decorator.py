# -*- coding:utf-8 -*-

import functools
'''
def log(func1):
    @functools.wraps(func1)
    def wrapper(*args, **kw):
        print('begin call')
        f = func1(*args, **kw)
        print('end call')
        return f
    return wrapper

@log
def func1():
    print("running")

func1()
'''
def log(text):
    if isinstance(text,str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator
    else:
        func = text
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s():' % (func.__name__))
            return func(*args, **kw)
        return wrapper

@log
def func():
    pass

func()

@log("hehe")
def fun2():
    pass
fun2()