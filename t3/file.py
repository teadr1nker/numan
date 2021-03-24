#!/usr/bin/python3

from numpy import array, diag, linalg, identity, matmul, around
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
printg(f'Eigenvalues:\n{linalg.eigvals(A)}')
print('Eingvectors:\n', linalg.eig(A)[1])

#rotation method
N = 16 #Iterations
printall = False #print all Iterations
V = identity(A.shape[0])
U = identity(A.shape[0])
Ar = A
printbl('Rotation method')
for n in range(N):
    U = identity(Ar.shape[0])
    i, j = get_max(Ar)
    U[i, i] = c(i, j, Ar)
    U[j, j] = c(i, j, Ar)
    U[i, j] = -s(i, j, Ar)
    U[j, i] = s(i, j, Ar)
    Ar = matmul(matmul(U.T, Ar), U)
    V = matmul(V, U)
    #print(f'V\n{V}')
    if(n == N-1 or printall):
        printh(f'Iteration #{n+1}')
        print(f'i = {i} j = {j}\nt = {round(t(Ar), 9)}\n'+
        f'A:\n{around(Ar, 4)}')
        printg(f'A Diagonal: {Ar.diagonal()}')

#power method
printbl('Power method')
eig, prs = power(A)
printg(f'Eigenvalues: {around(eig, 8)}')
print(f'\nDeflaction:\n{prs}')
