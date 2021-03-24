from numpy import matrix, diag, copy, matmul
import numpy as np
import math
import numpy.linalg as la

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printbl(str):
    print(f'{bcolors.OKBLUE}{str}{bcolors.ENDC}')

def printh(str):
    print(f'{bcolors.HEADER}{str}{bcolors.ENDC}')

def printg(str):
    print(f'{bcolors.OKGREEN}{str}{bcolors.ENDC}')

def get_max(M): #get position of absolute max value above main diagonal
    m = 0.0
    res = (0, 0)
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if i < j and abs(M[i,j]) > m:
                m = abs(M[i, j])
                res = (i, j)
    return res

def f(i, j, M):
    if M[i, i] != M[j, j]:
        return 0.5 * math.atan((2*M[i, j]) / (M[i, i] - M[j, j]))
    else:
        return math.pi / 4

def c(i, j, M):
    return math.cos(f(i, j, M))

def s(i, j, M):
    return math.sin(f(i, j, M))

def t(M):
    res = 0.0
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            res += M[i, j] ** 2

    for i in range(M.shape[0]):
        res -= M[i, i] ** 2
    return res

def trans(v): # translates vector (v^T)
    v_1 = np.copy(v)
    return v_1.reshape((-1, 1))

def power(M, eps = 1e-8):
    eig = []
    Mc = np.copy(M)
    lamb = 0
    for i in range(4):
        x = np.array([1, 1, 1, 1])
        while True:
            x_1 = np.dot(Mc, x)
            x_norm = la.norm(x_1)
            x_1 = x_1/x_norm
            if(abs(lamb - x_norm) <= eps): # If precision is reached,
                break                      # it returns eigenvalue
            else:
                lamb = x_norm
                x = x_1
        eig.append(lamb)

        # Matrix Deflaction
        v = x_1/la.norm(x_1)
        R = v * trans(v)
        R = eig[i]*R
        Mc = Mc - R

    return (eig, Mc)
