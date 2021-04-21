#!/usr/bin/python3
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from sympy.abc import u, t
from functions import *

F = ((2 * sym.sqrt(u)) / t) - 1
#F = u**2 /(t+1)
#X0 = 0.5
a = 0.5
b = 2
U0 = 15
N = 5000
h = (b-a)/N
U = [U0]
T = np.array([a + k * h for k in range(N)])
i = 0
for i in range(N-1):
    U.append(float(U[i] + h * F.subs([(t, T[i]), (u, U[i])])))

print((U[-1] - U[-2])/3)

plt.plot(U)
plt.savefig('plot1.png')

N = 200
h = (b-a)/N
T = np.array([a + k * h for k in range(N)])
X = [U0]
for i in range(N-1):
    X.append(float(X[i] + (h/2)*(F.subs([(t, T[i]), (u, X[i])]) + F.subs([(t, T[i]), (u, X[i] + h * F.subs([(t, T[i]), (u, X[i])]))]))))

plt.clf()
plt.plot(X)
plt.savefig('plot2.png')

rk4(a, U0, b, 100)
