#!/usr/bin/python3

import sympy as sym
import numpy as np
from sympy.abc import x
from functions import *

f = x**4 - sym.sqrt(x+1) - 3
a = -1
b = 2
I = float(sym.integrate(f, (x, a, b)))
print(f'Function f(x) = {f}')
print(f'Limits: a={a} b={b}')
print(f'I = sympy.integrate(f, (x, a, b)) = {I}')

K = np.arange(1, 11, 1)
#print(K)
J = []
for k in K:
    print(f'k = {k}', end = '\r')
    J.append(trapezoidal(f, k, a, b))
J = np.array(J)

printh('Trapezoidal method:')
print(J)
Z = J - I
printbo('Difference:')
print(Z)

R = []
for i in range(len(J)-1):
    R.append(abs(J[i+1] - J[i])/3)
R = np.array(R)

printbo('Error J_i - J_i-1:')
print(R)

Rk = []
for i in range(len(R)-1):
    Rk.append(R[i]/R[i+1])
Rk = np.array(Rk)

printbo('Error R_k-1/R_k:')
print(Rk)

G = gauss5(f, a, b)
printh('Gauss method')
print(f'G = {G}')
printbo(f'Difference of I and G: {abs(I - G)}')
