#!/usr/bin/python3
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from sympy.abc import u, t
from functions import *

import os
os.environ['QT_LOGGING_RULES'] = "qt5ct.debug=false"   #suppress qt5ct debugging

F = ((2 * sym.sqrt(u)) / t) - 1
a = 0.5
b = 2
U0 = 15
N = 2000
h = (b-a)/N
U = [U0]
T = np.linspace(a, b, N)

printh('Eulers method')

for i in range(N-1):
    U.append(float(U[i] + h * F.subs([(t, T[i]), (u, U[i])])))

N = N*2
T = np.linspace(a, b, N)
Y = [U0]
h = (b-a)/N

for i in range(N-1):
    Y.append(float(Y[i] + h * F.subs([(t, T[i]), (u, Y[i])])))

e = max([abs(U[i] - Y[i*2]) for i in range(len(U))])
print(f'Result: {U[-1]}')
print(f'Error: {e}')

plt.plot(np.linspace(a, b, int(N / 2)), U)
plt.savefig('Euler.png', dpi = 200)
printLink('Euler.png')

N = 2000
h = (b-a)/N
T = np.array([a + k * h for k in range(N)])
X = [U0]

printh('Cauchy–Euler method')

for i in range(N-1):
    X.append(float(X[i] + (h/2)*(F.subs([(t, T[i]), (u, X[i])]) +
    F.subs([(t, T[i]), (u, X[i] + h * F.subs([(t, T[i]), (u, X[i])]))]))))

print(f'Result: {X[-1]}')
plt.clf()
plt.plot(np.linspace(a, b, N), X)
plt.savefig('Cauchy-Euler.png', dpi = 200)
printLink('Cauchy-Euler.png')

printh('Runge Kutta Fourth Order (RK4) Method')

W, yn = rk4(a, U0, b, N)
print(f'Result: {yn}')

plt.clf()
plt.plot(np.linspace(a, b, N), W)
plt.savefig('RK4.png', dpi = 200)
printLink('RK4.png')

plt.clf()
plt.plot(np.linspace(a, b, N), abs(X - W))
plt.savefig('Difference CE RK4.png', dpi = 200)
printLink('Difference CE RK4.png')

plt.clf()
plt.plot(np.linspace(a, b, N), abs(X - np.array(U)))
plt.savefig('Difference E CE.png', dpi = 200)
printLink('Difference E CE.png')
