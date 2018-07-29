"""
    12.22.2017 Friday
    created by neonleexiang
    test ThomasMethod
"""


import sys
import ThomasMethod
import judgement_Thomas


a = [[2, 0, 0, 0, 0, 0, 0],
     [-1, 2, 0, 0, 0, 0, 0],
     [0, -1, 2, 0, 0, 0, 0],
     [0, 0, -1, 2, -1, 0, 0],
     [0, 0, 0, 0, 2, -1, 0],
     [0, 0, 0, 0, 0, 2, -1],
     [0, 0, 0, 0, 0, 0, 2]]
d = [1, 0, 0, 0, 0, 0, 0]
if judgement_Thomas.judge_Thomas(a):
    print "Matrix a is suitable for ThomasMethod"
else:
    print "Matrix a is unsuitable for ThomasMethod"
    sys.exit()
output = list(ThomasMethod.thomasMethod(a, d))
print "x =", output[0], '\n', "u =", output[1], '\n', "v =", output[2]
fp = open("ThomasMethod", 'w+')
fp.write('x ='+str(output[0])+'\n')
fp.write('u ='+str(output[1])+'\n')
fp.write('v ='+str(output[2]))
fp.close()
