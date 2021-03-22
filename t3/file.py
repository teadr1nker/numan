#!/usr/bin/python3

from numpy import array, diag, linalg, identity, matmul
from solvers import *
import numpy as np
import sys


D = array([[1.342, 0.432, -0.599, 0.202],
            [0.432, 1.342, 0.256, -0.599],
            [-0.599, 0.256, 1.342, 0.532],
            [0.202, -0.599, 0.532, 1.342]])

if len(sys.argv) == 1:
    C = diag([0.05, 0.03, 0.02, 0.04])
    A = D + 19 * C
else:
    A = D

print('Initial matrix:\n', A)
print('Eigenvalues:\n', linalg.eigvals(A))
print('Eingvectors:\n', linalg.eig(A)[1])

#rotation method
N = 2 #Iterations
V = identity(A.shape[0])
U = identity(A.shape[0])
Ar = A
print('Rotation method')
for n in range(N):
    U = identity(Ar.shape[0])
    i, j = get_max(Ar)
    U[i, i] = c(i, j, Ar)
    U[j, j] = c(i, j, Ar)
    U[i, j] = -s(i, j, Ar)
    U[j, i] = s(i, j, Ar)
    #print(U)
    Ar = matmul(matmul(U.T, Ar), U)
    V = matmul(V, U)
    print(f'Iteration #{n+1}\ni = {i} j = {j}\nt = {round(t(Ar), 3)}\nA:\n{Ar}')

#power method
print('Power method')
eig, prs = power(A)
print(f'Eigenvalues:\n{eig}\nPresision:\n{prs}')
