#!/usr/bin/python3

from numpy import matrix, diag, linalg
from solvers import solve_with_rotation, power

D = matrix([[1.342, 0.432, -0.599, 0.202],
            [0.432, 1.342, 0.256, -0.599],
            [-0.599, 0.256, 1.342, 0.532],
            [0.202, -0.599, 0.532, 1.342]])

C = diag([0.05, 0.03, 0.02, 0.04])

A = D + 19*C
print('Initial matrix:\n', A)
print('Eigenvalues: ', linalg.eigvals(A))

solve_with_rotation(A)
y = (power(A))
print(y[len(y)-1])
