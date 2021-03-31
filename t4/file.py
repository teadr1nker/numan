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

n = np.array([5, 10, 15, 20, 25, 30, 40, 50, 60])
#print(f'T: {T}')
N = n[0]
X = []
for i in range(N):
    X.append(a + ((b-a)*i)/N)

#L = sp.Sum(f.subs(x, X[k]) * sp.Product((t-X[i])/(X[k] - X[i]), (i, 0, N)), (k, 0, N))
def L(t):
    res = 0.0
    for k in range(N):
        mul = f.subs(x, X[k])
        for i in range(N):
            if X[k] - X[i] != 0:
                mul *= (t - X[i]) / (X[k] - X[i])
        res += mul
    return res

La = []
for i in range(j):
    La.append(L(T[i]))

p1 = sp.plot(f, show=False)
p1.save('plot1.png')

plt.clf()
plt.plot(La)
plt.savefig('plot2.png')


V = []
for r in range(N):
    V.append(math.cos(math.pi * ((1+2*r)/(2*(N+1)))))

Z=[]
for i in range(len(V)):
    Z.append((a+b)/2 + ((b-a)/2)*V[i])

def LCH(t):
    res = 0.0
    for k in range(N):
        mul = f.subs(x, Z[k])
        for i in range(N):
            if Z[k] - Z[i] != 0:
                mul *= (t - Z[i]) / (Z[k] - X[i])
        res += mul
    return res


La = []
for i in range(j):
    La.append(LCH(T[i]))

plt.clf()
plt.plot(La)
plt.savefig('plot3.png')
