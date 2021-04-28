import numpy as np

import math
#function to be solved
#F = ((2 * sym.sqrt(u)) / t) - 1
def f(x,y):
    return ((2 * math.sqrt(y)) / x) - 1

# RK-4 method
def rk4(x0,y0,xn,n):
    '''Runge Kutta Fourth Order (RK4) Method'''
    # Calculating step size
    h = (xn-x0)/n

    #print('\n--------SOLUTION--------')
    #print('-------------------------')
    #print('x0\ty0\tyn')
    #print('-------------------------')
    res = np.full(n, 0.0)
    for i in range(n):
        k1 = h * (f(x0, y0))
        k2 = h * (f((x0+h/2), (y0+k1/2)))
        k3 = h * (f((x0+h/2), (y0+k2/2)))
        k4 = h * (f((x0+h), (y0+k3)))
        k = (k1+2*k2+2*k3+k4)/6
        yn = y0 + k
        res[i] = yn
        #print('%.4f\t%.4f\t%.4f'% (x0,y0,yn) )
        #print('-------------------------')
        y0 = yn
        x0 = x0+h

    #print('At x=%.4f, y=%.4f' %(xn,yn))
    return (res, yn)

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
