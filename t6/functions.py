import numpy as np
import sympy as sym
from sympy.abc import x

def trapezoidal(f, k, a, b):
    N = 2 ** k
    h = (b - a)/ N
    res = 0.0
    for n in range(N):
        res += (h/2) * (f.subs(x, a + n*h) + f.subs(x, a + h + n*h))
    return res

X = np.array([0.04691008, 0.23076534, 0.5, 0.76923466, 0.95308992])
C = np.array([0.11846344, 0.23931433 ,0.28444444 ,0.23931433 , 0.11846344])
M = len(X)

def gauss5(f, a, b):
    res = 0.0
    Z = X * (b-a) + a
    for i in range(M):
        res += C[i] * f.subs(x, Z[i])
    return (b-a) * res

################################################################################
#
#
#
#
#
################################################################################

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

def printbo(str):
    print(f'{bcolors.BOLD}{str}{bcolors.ENDC}')

import os
def printLink(str):
    os.system(f'echo \'\e]8;;file://{os.getcwd()}/{str}\aOpen {str}\e]8;;\a\'')
