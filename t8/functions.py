import numpy as np

def tridiagonal(p, q, f, N, a, b, m1, m2):
    h = (b - a) / N
    X = np.linspace(a, b, N)
    B = np.full(N, 1)
    A = np.array([1 - p(x) * h for x in X])
    C = np.array([2 - p(x) * h + q(x) * (h**2) for x in X])
    G = np.array([-f(x) for x in X])
    alpha = [0]
    beta = [m1]
    for i in range(N-1):
        alpha.append(B[i+1]/(C[i+1] - A[i+1] * alpha[i]))
        beta.append(((h**2)*G[i+1] + A[i+1]*beta[i]) / (C[i+1] - A[i+1]*alpha[i]))

    Y = [m2]
    for i in range(N-1):
        Y.append(alpha[N-1-i]* Y[i] + beta[N-1-i])
    Y[-1] = m1

    return np.flip(np.array(Y))

################################################################################
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
#                                                                              #
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
    os.system(f'echo \'\e]8;;file://{os.path.abspath(str)}\aOpen {str}\e]8;;\a\'')
