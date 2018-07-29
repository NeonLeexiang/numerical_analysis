"""
    12.20.2017 Wednesday
    created by neonleexiang
    Newton Method
"""
from __future__ import division


def divf(f):  # derivative
    dx = 0.000000001
    return lambda x: (f(x+dx) - f(x))/dx


def NewtonMethod(f, df, x, e):  # ordinary NewtonMethod
    xlist = []
    while abs(f(x) > e):
        x = x - f(x)/df(x)
        xlist.append(x)
    else:
        return x, xlist


def NewtonMethod1(f, df, x, e):  # x0 NewtonMethod
    xlist = []
    x0 = x
    while abs(f(x) > e):
        x = x - f(x)/df(x0)
        xlist.append(x)
    else:
        return x, xlist


def NewtonMethod2(f, df, x, e):  # x2n-1,x2n NewtonMethod
    xlist = []
    xlist.append(x)
    while abs(f(x) > e):
        x2 = x - f(x)/df(x)
        x = x2 - f(x2)/df(x)
        xlist.append(x2)
        xlist.append(x)
    return x, xlist
