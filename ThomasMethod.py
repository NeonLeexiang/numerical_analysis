"""
    12.20.2017 Wednesday
    created by neonleexiang
    Thomas Method
"""
from __future__ import division  # change the '/' into maths method
import numpy


def thomasMethod(a, d):  # a = matrix A,d = matrix D
    u = []
    v = []
    x = []
    u.append(d[0]/a[0][0])  # u[0]
    v.append(a[0][1]/a[0][0])  # v[0]
    trA = numpy.linalg.matrix_rank(a) - 1  # begin i,j = 2 ~ n-1
    for i in range(1, trA):
        u.append((d[i] - a[i][i-1]*u[i-1])/(a[i][i]-a[i][i-1]*v[i-1]))
        v.append(a[i][i+1]/(a[i][i]-a[i][i-1]*v[i-1]))
    u.append((d[trA]-a[trA][trA-1]*u[trA-1])/(a[trA][trA]-a[trA][trA-1]*v[trA-1]))  # u[n]
    x.append(u[trA])  # x[n]
    for i in range(trA-1, -1, -1):
        x.append(u[i] - v[i]*x[trA-i-1])  # x[n],x[n-1],x[n-2]...
    return x[::-1], u, v
