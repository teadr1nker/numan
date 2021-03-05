#!/usr/bin/python3

from sympy import Matrix, diag
N=10

def mysum(M1, M2):
    s = M1.shape[1]
    res = 0
    for z in range(s):
        res += M1[z] * M2[z]
    return res

def mtrxavg(M3):
    s = M3.shape[0]
    res = 0
    for z in range(s):
        res+=abs(M3[z])
    return res/s


D = Matrix([[1.342, 0.432, -0.599, 0.202],[0.202, 1.342, 0.432, -0.599],
[-0.599, 0.202, 1.342, 0.432],[0.432, -0.599, 0.202, 1.342]])
C = diag(0.02, 0.02, 0.02, 0.02)
b = Matrix([[1.941], [-0.230], [-1.941], [0.230]])

A = D + 19*C
print('A:\n',A)

root, params = A.gauss_jordan_solve(b)
print('Solution 1:\n', root)

X = [b]
rows = b.shape[0]

for k in range(N):
    x = X[k]
    M = []
    for i in range(rows):
        _x = x[i,0]
        x1 = _x - (1/A[i,i])*(mysum(A.row(i), x) - b[i,0])
        M.append([x1])
    X.append(Matrix(M))

print('Solution 2:\n',X[len(X)-1])

R = []
for l in range(len(X)):
    R.append(mtrxavg(root - X[l]))

import matplotlib.pyplot as plt
plt.plot(R)
plt.savefig('plot1.png')

D = diag(A[0,0], A[1,1], A[2,2], A[3,3])
print(D-0.5*A)
