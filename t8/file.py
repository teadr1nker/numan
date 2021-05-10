#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from functions import *
from scipy.integrate import odeint

def p(x):
    return np.log(3.5 + x)
    #return 1 + x**2

def q(x):
    return 0.8 * (x ** 2)
    #return 0.5 * x

def f(x):
    return 2.5 * x - x ** 2
    #return -math.sqrt(x)

printh('Tridiagonal method')

N = 1000
a = 0
b = 0.5
#b = 2
#m1 = -1
#m2 = 1
m1 = 1
m2 = 2
Y1 = tridiagonal(p, q, f, N, a, b, m1, m2)

plt.plot(np.linspace(a, b, N), Y1)
plt.savefig('tridiagonal.png')
printLink('tridiagonal.png')

Y2 = tridiagonal(p, q, f, N*2, a, b, m1, m2)
error = [abs(Y1[i] - Y2[i*2]) for i in range(N)]
print(f'Error: {max(error)}')
plt.clf()
plt.plot(error)
plt.savefig('error.png')
printLink('error.png')

printh('scipy odeint()')

N = int(N/2)

def ode(u, x):
    return (u[2], u[1], -u[2] - u[1] * p(x) - u[0] * q(x) + f(x))

y0 = [m1, m2, 0]
xs = np.linspace(a, b, N)
us = odeint(ode, y0, xs)

plt.clf()
plt.plot(xs, us[:,0])
plt.savefig('odeint.png')
printLink('odeint.png')
