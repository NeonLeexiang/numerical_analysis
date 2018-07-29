"""
    12.22.2017 Friday
    created by neonleexiang
    Judgement of Thomas Method
"""


import numpy


def judge_Thomas(Matrix):
    for i in range(numpy.linalg.matrix_rank(Matrix)):
        for j in range(2, numpy.linalg.matrix_rank(Matrix)-i):
            if Matrix[i][i] != 0 and Matrix[i][i+j] == 0 and Matrix[j+i][i] == 0:
                return True
            else:
            	return False