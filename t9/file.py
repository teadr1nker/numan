#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from functions import *
#import os

def p(X):
    return np.log(3.5 + X)

def f(tt, X):
    return X - 0.5*tt*(X**2)

def u0(X):
    return X**2 + 1

def T1(tt):
    return 1

def T2(tt):
    return 2 - tt

printh('Differential method')
L = 2
n = 50
te = 1
dt = 0.01

Y1, t, x = solve(L, n, te, dt, p, f, u0, T1, T2)
plt.clf()
plt.plot(x, Y1[int(n/2)])
plt.plot(x, Y1[-1])
plt.plot(x, Y1[0])
plt.legend(['/2','-1','0'])
plt.title('Heat equation')
plt.savefig('HE.png')
printLink('HE.png')

printh('Error')

Y2, _, x2 = solve(L, n * 2, te, dt / 2, p, f, u0, T1, T2)
plt.clf()
plt.plot(x2, Y2[n])
plt.plot(x2, Y2[-1])
plt.plot(x2, Y2[0])
plt.legend(['/2','-1','0'])
plt.title('Heat equation (2n, dt/2)')
plt.savefig('HE2.png')
printLink('HE2.png')
error = 0.0
m = int(te/(dt/2))
for i in range(n):
    err = abs(Y1[-1, i] - Y2[-1, i*2])
    if err > error:
        error = err

print(error/3)


#print(error/3)
printh('Turbulence')
Y3, _, x3 = solveTurb(L, n, te, 0.0152, p, f, u0, T1, T2)
plt.clf()
plt.plot(x3, Y3[int(n/2)])
plt.plot(x3, Y3[-1])
plt.legend(['middle','last'])
plt.savefig('turbulence.png')
printLink('turbulence.png')


ans = input('Create video? y/n ')
if ans == 'y':
    slideshow(Y1, x, t, L, te)
