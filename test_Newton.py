"""
    12.22.2017 Friday
    created by neonleexiang
    test Newton Method
"""


import Newton
import matPlot4Newton
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 1


df = Newton.divf(f)


# newtonMethod
print Newton.NewtonMethod(f, df, 10, 0.0000001)
output = Newton.NewtonMethod(f, df, 10, 0.000001)
fp = open("newtonMethod", 'w+')
fp.writelines('x*'+'='+str(output[0])+'\n')
fp.writelines('xlist'+"="+str(output[1])+'\n')
fp.close()
out4x = output[0]
list4x = output[1]
plot1 = matPlot4Newton.plot4Newton(list4x, out4x)
plt.title("newtonMethod")
plt.savefig('newtonMethod.png')


# newtonMethod1
print Newton.NewtonMethod1(f, df, 10, 0.0000001)
output = Newton.NewtonMethod1(f, df, 10, 0.0000001)
fp = open("newtonMethod1", 'w+')
fp.writelines('x*'+'='+str(output[0])+'\n')
fp.writelines('xlist'+"="+str(output[1])+'\n')
fp.close()
out4x = output[0]
list4x = output[1]
plot2 = matPlot4Newton.plot4Newton(list4x, out4x)
plt.title("newtonMethod1")
plt.savefig('newtonMethod1.png')


# newtonMethod2
print Newton.NewtonMethod2(f, df, 10, 0.0000001)
output = Newton.NewtonMethod2(f, df, 10, 0.0000001)
fp = open("newtonMethod2", 'w+')
fp.writelines('x*'+'='+str(output[0])+'\n')
fp.writelines('xlist'+"="+str(output[1])+'\n')
fp.close()
out4x = output[0]
list4x = output[1]
plot3 = matPlot4Newton.plot4Newton(list4x, out4x)
plt.title("newtonMethod2")
plt.savefig('newtonMethod2.png')


# newtonMethod1_1
print Newton.NewtonMethod1(f, df, 8, 0.0000001)
output = Newton.NewtonMethod1(f, df, 8, 0.0000001)
fp = open("newtonMethod1_1", 'w+')
fp.writelines('x*'+'='+str(output[0])+'\n')
fp.writelines('xlist'+"="+str(output[1])+'\n')
fp.close()
out4x = output[0]
list4x = output[1]
plot2_1 = matPlot4Newton.plot4Newton(list4x, out4x)
plt.title("newtonMethod1_1")
plt.savefig('newtonMethod1_1.png')


# newtonMethod1_2
print Newton.NewtonMethod1(f, df, 2, 0.0000001)
output = Newton.NewtonMethod1(f, df, 2, 0.0000001)
fp = open("newtonMethod1_2", 'w+')
fp.writelines('x*'+'='+str(output[0])+'\n')
fp.writelines('xlist'+"="+str(output[1])+'\n')
fp.close()
out4x = output[0]
list4x = output[1]
plot2_2 = matPlot4Newton.plot4Newton(list4x, out4x)
plt.title("newtonMethod1_2")
plt.savefig('newtonMethod1_2.png')


# newtonMethod1_3
print Newton.NewtonMethod1(f, df, 5, 0.0000001)
output = Newton.NewtonMethod1(f, df, 5, 0.0000001)
fp = open("newtonMethod1_3", 'w+')
fp.writelines('x*'+'='+str(output[0])+'\n')
fp.writelines('xlist'+"="+str(output[1])+'\n')
fp.close()
out4x = output[0]
list4x = output[1]
plot2_3 = matPlot4Newton.plot4Newton(list4x, out4x)
plt.title("newtonMethod1_3")
plt.savefig('newtonMethod1_3.png')
