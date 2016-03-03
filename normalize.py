# -*- coding:utf-8 -*-
from functools import reduce
'''
def normalize(name):
    return name.capitalize()

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
    def fn(x, y):
        return x * y
    return reduce(fn,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
'''
def str2float(s):
    str = s.split('.')
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, str[0]))+reduce(fn,map(char2num, str[1]))*10**(s.find('.')-len(s)+1)

print('str2float(\'123.456\') =', str2float('12323.454678'))