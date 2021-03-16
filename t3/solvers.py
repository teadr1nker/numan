from numpy import matrix, diag, copy
import numpy as np
import numpy.linalg as la

def solve_with_rotation(m):
    """Solve system with rotation method.
    :param m: numpy matrix
    :return: None
    """
    n = m.shape[0]
    # forward trace
    for i in range(n-1):
        for j in range(i + 1, n):
            c = m[i, i] / (m[i, i]**2 + m[j, i]**2) ** .5
            s = m[j, i] / (m[i, i]**2 + m[j, i]**2) ** .5
            tmp1 = m[i, :] * c + m[j, :] * s
            tmp2 = m[i, :] * -s + m[j, :] * c
            m[i, :] = tmp1
            m[j, :] = tmp2

    # check for non-singularity
    if is_singular(m):
        print('The system has infinite number of answers...')
        return

    # backward trace
    x = matrix([0.0 for i in range(n)]).T
    for k in range(n - 1, -1, -1):
        x[k, 0] = (m[k, -1] - m[k, k:n] * x[k:n, 0]) / m[k, k]

    # Display results
    print(x)


def is_singular(m):
    """Check matrix for nonsingularity.
    :param m: matrix (list of lists)
    :return: True if system is nonsingular
    """
    return any(diag(m) == 0)


def power(A, N=50):
    y = [matrix([[1],[1],[1],[1]])]

    for i in range(N):
        y.append(A*y[i])

    print('Power method:\n', y[len(y)-1])

    lmb1 = y[len(y) - 1][0] / y[len(y) -2][0]
    print('lmb1: ', lmb1)
