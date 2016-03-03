# -*- coding:utf-8 -*-
import math
'''
n1 = 255
n2 = 1000

print(hex(n1),hex(n2))
'''
def quadratic(a, b, c):
    return (math.sqrt(b**2-4*a*c)-b)/(2*a),-(b+math.sqrt(math.pow(b,2)-4*a*c))/(2*a)

print(quadratic(2, 3, 1)) # => (-0.5, -1.0)
print(quadratic(1, 3, -4)) # => (1.0, -4.0)

