import numpy as np
import math

def s(n, x):
    return sum(x ** n)

def b(n, x, y):
    return sum(abs(y * (x ** n)))

def createA(n, x):
    list = []
    for i in range(n+1):
        l = []
        for j in range(n+1):
            l.append(s(j+i, x))
        list.append(l)
    return np.array(list)

def createB(n, x, y):
    list = []
    for i in range(n+1):
        list.append([b(i, x, y)])
    return np.array(list)

def approx(n, x, y, X):
    a = np.linalg.solve(createA(n, x), createB(n, x, y))
    res = 0.0
    for i in range(n+1):
        res += a[i] * (X ** i)
    return res

def abserror(n, x, y):
    aprx = np.array([approx(n, x, y, X) for X in x])
    return max([abs(y[i] - aprx[i])[0] for i in range(len(y))])

def rmserror(n, x, y):
        aprx = np.array([approx(n, x, y, X) for X in x])
        return math.sqrt(sum([abs(y[i] - aprx[i])[0] for i in range(len(y))]))/len(aprx)

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
