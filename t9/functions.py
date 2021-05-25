import matplotlib.pyplot as plt
import numpy as np

def slideshow(arr, x, t, L, te):
    for i, a in enumerate(arr):
        plt.clf()
        plt.plot(x, a)
        #plt.xlim((0, L))
        plt.ylim((0, 5))
        plt.xlabel('Dist')
        plt.ylabel('Temp')
        plt.title(f'Heat equation Time: {round(t[i], 5)}')
        plt.savefig('tmp_%04d.png' % i)
        print(f'Time: {t[i]}', end='\r')
        #print(a)
    printg('Ready                                            ')
    os.system('rm video.mp4')
    os.system('ffmpeg -hide_banner -loglevel error -r 15 -i tmp_%04d.png -c:v \
    libx264 -vf fps=30 -pix_fmt yuv420p video.mp4')
    os.system('rm tmp_*.png')
    printLink('video.mp4')

def solve(L, n, te, dt, p, f, u0, T1, T2):
    dx = L / n
    m = int(te / dt)
    x = np.linspace(0, L, n)
    t = np.arange(0, te, dt)

    Y = np.zeros((m, n))
    Y[0] = [u0(X) for X in x]
    Y[:,0] = [T1(T) for T in t]
    Y[:,-1] = [T2(T) for T in t]
    for j in range(0, m-1):
        for i in range(1, n-1):
            Y[j+1,i] = Y[j,i]+p(x[i])*(dt/(dx**2))*(Y[j,i+1]-2*Y[j,i]+Y[j, i-1])\
            +f(t[j], x[i])*dt

    return (Y, t, x)

def solveTurb(L, n, te, dt, p, f, u0, T1, T2):
    dx = L / n
    m = int(np.trunc(te / dt))
    x = np.linspace(0, L, n)
    t = np.arange(dt, te, dt)
    Y = np.zeros((m, n))
    Y[:,0] = [T1(T) for T in t]
    Y[:,-1] = [T2(T) for T in t]
    Y[0] = [u0(X) for X in x]
    for j in range(0, m-1):
        for i in range(1, n-1):
            Y[j+1,i] = Y[j, i]+p(x[i])*(dt/dx**2)*(Y[j,i+1]-2*Y[j,i]+Y[j, i-1])\
            +f(t[j], x[i])*dt

    return (Y, t, x)

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

def printbl(s):
    print(f'{bcolors.OKBLUE}{s}{bcolors.ENDC}')

def printh(s):
    print(f'{bcolors.HEADER}{s}{bcolors.ENDC}')

def printg(s):
    print(f'{bcolors.OKGREEN}{s}{bcolors.ENDC}')

def printbo(s):
    print(f'{bcolors.BOLD}{s}{bcolors.ENDC}')

import os
def printLink(s):
    os.system(f'echo \'\e]8;;file://{os.path.abspath(s)}\aOpen {s}\e]8;;\a\'')
