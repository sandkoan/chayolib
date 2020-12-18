from math import sqrt
import ctypes

def quadratic(a, b, c):
    d = (b ** 2) - (4 * a * c)
    sol1 = (-b - sqrt(d)) / (2 * a)
    sol2 = (-b + sqrt(d)) / (2 * a)
    return (sol1, sol2)

# import os
# # print(quadratic(1, 7, -4))
# temp = os.path.dirname(os.path.realpath(__file__))
# total = os.path.join(temp, "program.so")
# print(total)
# lib = ctypes.cdll.LoadLibrary(total)
# print(dir(lib))
# strchr = lib.quadratic
# strchr.restype = ctypes.c_double
# strchr = lib.quadratic(ctypes.c_double(5), ctypes.c_double(10), ctypes.c_double(15))
# print(strchr)

from ctypes import cdll
import ctypes as c
lib = cdll.LoadLibrary("./program.so")
print(lib.__dict__)
strchr = lib.temp
strchr.restype = c.c_int
strchr = lib.temp(1, 7, -4)


print(strchr)