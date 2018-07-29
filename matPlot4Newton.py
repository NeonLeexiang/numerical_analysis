"""
    12.25.2017 Monday
    created by neonleexiang
    matPlot4NewtonMethod
"""


import matplotlib.pyplot as plt


def plot4Newton(list4x, out4x):
    list4y = []
    for i in list4x:
        list4y.append(abs(i - out4x))
    plt.title("distance of x and x*")
    plt.xlabel("x")
    plt.ylabel("x - x*")
    plt.xlim(xmin=int(min(list4x)-1), xmax=int(max(list4x)+1))
    plt.ylim(ymin=int(min(list4y)-1), ymax=int(max(list4y)+1))
    return plt.plot(list4x, list4y, 'ro')

