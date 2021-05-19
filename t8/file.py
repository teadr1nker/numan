#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from functions import *
from scipy.integrate import odeint, ode

def p(x):
    return np.log(3.5 + x)
    #return 1 + x ** 2

def q(x):
    return 0.8 * (x ** 2)
    #return 0.5 * x

def f(x):
    return 2.5 * x - x ** 2
    #return np.sqrt(x)

printh('Tridiagonal method')

N = 2000
a = 0
b = 0.5
#b = 2
m1 = 1
m2 = 2
#m1 = -1
#m2 = 1
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

#quit(0)
printh('scipy odeint()')

def F(u, x):
        return (u[1] , -u[1] * p(x) + u[0] * q(x) + f(x))

y0 = [m1, m1]
xs = np.linspace(a, b, N)
us = odeint(F, y0, xs)

plt.clf()
plt.plot(xs, us)
plt.savefig('odeint.png')
printLink('odeint.png')

#r = ode(F)
#print(r)

plt.clf()
plt.plot(xs, abs(us[:,0] - Y1))
plt.savefig('difference.png')
printLink('difference.png')
