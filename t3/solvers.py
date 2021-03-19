from numpy import matrix, diag, copy, matmul
import numpy as np
import math
import numpy.linalg as la

def solve_with_rotation(m):
    print('a')

def f(i, j, A):
    if A[i, i] != A[j, j]:
        return 0.5 * math.atan((2*A[i, j]) / (A[i, i] - A[j, j]))
    else:
        return math.Pi / 4

def c(i, j, A):
    return math.cos(f(i, j, A))

def s(i, j, A):
    return math.cos(i, j, A)


def power(A, N=50):
    y = [matrix([[1],[1],[1],[1]])]

    for i in range(N):
        y1 = A*(y[i])
        y.append(y1)

    yn = y[len(y)-1]
    print('Power method:\n', yn / yn[yn.shape[0]-1])

    lmb1 = y[N][0] / y[N-1][0]
    print('lmb1: ', lmb1)
    #print('ooo\n', A*yn - yn*lmb1)
