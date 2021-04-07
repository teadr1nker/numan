#!/usr/bin/python3

import sympy as sp
import numpy as np
from functions import *
from sympy.abc import x
import matplotlib.pyplot as plt
import math

f = x ** 4 - sp.sqrt(x + 1) - 3
a = 0.5
b = 2.5
j = 137
T = []
for r in range(j):
    T.append(a + ((b-a)/j)*r)

n = np.array([5, 10, 15, 20, 25])#, 30, 40, 50, 60])
#print(f'T: {T}')
N = n[0]
X = []
for i in range(N):
    X.append(a + ((b-a)*i)/N)
##1
#L = sp.Sum(f.subs(x, X[k]) * sp.Product((t-X[i])/(X[k] - X[i]), (i, 0, N)), (k, 0, N))
def L(t, Xl):
    res = 0.0
    for k in range(len(Xl)):
        mul = f.subs(x, Xl[k])
        for i in range(len(Xl)):
            if Xl[k] - Xl[i] != 0:
                mul *= (t - Xl[i]) / (Xl[k] - Xl[i])
        res += mul
    return res

La = []
for t in T:
    La.append(L(t, X))

#p1 = sp.plot(f, show=False)
#p1.save('plot11.png')
printh('equidistant nodes')

F = []
for t in T:
    F.append(f.subs(x, t))

plt.plot(T, F)
plt.savefig('plot11.png')
#printLink('plot11.png')

#plt.clf()
plt.plot(T, La, '.')
plt.savefig('L_f.png', dpi = 200)
printLink('L_f.png')
D = []
for e, l in enumerate(La):
    D.append(l - f.subs(x, T[e]))

plt.clf()
plt.plot(T, D)
plt.savefig('differenceL.png')
printLink('differenceL.png')

printh('error')
error = []
for ns in n:
    Xe = []
    for i in range(ns):
        Xe.append(a + ((b-a)*i)/ns)
    print(f'N = {ns}', end = '\r')

    err = []
    for t in T:
        err.append(abs(f.subs(x, t) - L(t, Xe)))

    error.append(max(err))
print(error)


##2
#V = []
#for r in range(N):
#    V.append(math.cos(math.pi * ((1+2*r)/(2*(N+1)))))

Z=[]
for r in range(N):
    Z.append((a+b)/2 + ((b-a)/2)*(math.cos(math.pi * ((1+2*r)/(2*(N+1))))))

def LCH(t, Zl):
    res = 0.0
    for k in range(N):
        mul = f.subs(x, Zl[k])
        for i in range(N):
            if Zl[k] - Zl[i] != 0:
                mul *= (t - Zl[i]) / (Zl[k] - Zl[i])
        res += mul
    return res

La = []
for t in T:
    La.append(LCH(t, Z))
printh('Chebyshev nodes')
plt.clf()
plt.plot(T, F)
plt.plot(T ,La, '.')
plt.savefig('LCH_F.png', dpi=200)
printLink('LCH_F.png')
D = []
for e, l in enumerate(La):
    D.append(l - f.subs(x, T[e]))

plt.clf()
plt.plot(T, D)
plt.savefig('differenceLCH.png')
printLink('differenceLCH.png')
printh('error')
errorch = []
for ns in n:

    Ve = []
    for r in range(ns):
        Ve.append(math.cos(math.pi * ((1+2*r)/(2*(ns+1)))))

    Ze=[]
    for ve in Ve:
        Ze.append((a+b)/2 + ((b-a)/2)*ve)

    print(f'N = {ns}', end = '\r')

    err = []
    for t in T:
        err.append(abs(f.subs(x, t) - LCH(t, Ze)))

    errorch.append(max(err))
print(errorch)
printh('error comparison')
plt.clf()
plt.plot(n, error)
plt.plot(n, errorch)
plt.savefig('error.png')
printLink('error.png')


##3
printh('Builtin interpolation')
N = n[0]
Xx = []
for r in range(N):
    Xx.append(a + ((b - a) *r)/N)

yy = []
for xx in Xx:
    yy.append(f.subs(x, xx))

LS = np.interp(
np.array(T, dtype='float64'),
np.array(Xx, dtype='float64'),
np.array(yy, dtype='float64'))

#print(LS)
plt.clf()
plt.plot(T, LS)
plt.plot(Xx, yy, 'o')
plt.savefig('interpolation.png')
printLink('interpolation.png')

printh('error')
errorint = []
for ns in n:
    print(f'N = {ns}', end = '\r')
    Xx = []
    for r in range(ns):
        Xx.append(a + ((b - a) *r)/N)

    yy = []
    for xx in Xx:
        yy.append(f.subs(x, xx))

    LS = np.interp(
    np.array(T, dtype='float64'),
    np.array(Xx, dtype='float64'),
    np.array(yy, dtype='float64'))

    err = []
    for i, t in enumerate(T):
        err.append(abs(f.subs(x, t) - LS[i]))
    errorint.append(max(err))
print(errorint)        
