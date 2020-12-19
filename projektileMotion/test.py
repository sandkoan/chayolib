from ctypes import *

lib = CDLL("projektileMotion/program.dll", winmode=0)
strchr = lib.quadratic
strchr.restype = c_double
a = c_double(3)
b = c_double(5)
c = c_double(-6)
print(strchr(a, b, c))
