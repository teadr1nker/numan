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
printh('Trapezoidal method:')
J = []
for k in K:
    tr = trapezoidal(f, k, a, b)
    J.append(tr)
    print(f'K = {k}: {tr}')
J = np.array(J)

Z = J - I
printbo('Difference:')
for i, z in enumerate(Z):
    print(f'K = {K[i]}: {z}')
printbo('Error J_i - J_i-1:')
R = []
for i in range(len(J)-1):
    e = (J[i+1] - J[i])/3
    R.append(e)
    print(f'{e}')

R = np.array(R)


printbo('Error R_k - 1/R_k:')
for i in range(len(R)-1):
    print(R[i]/R[i+1])

G = gauss5(f, a, b)
printh('Gauss method')
print(f'G = {G}')
printbo(f'Difference of I and G: {abs(I - G)}')
