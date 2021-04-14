#!/usr/bin/python3
import numpy as np
from functions import *
import matplotlib.pyplot as plt

x = np.array([1.2, 1.3, 1.4, 1.6, 1.7, 1.9, 2.1, 2.2, 2.4, 2.6, 2.7])
y = np.array([1.449, 1.993, 2.229, 3.556, 3.793, 3.605, 3.566, 3.423, 3.338,
              3.218, 3.028])

T = np.arange(1.2, 2.7, 0.05)
LS = np.interp(
np.array(T, dtype='float64'),
np.array(x, dtype='float64'),
np.array(y, dtype='float64'))

plt.plot(x, y, 'o')
plt.plot(T, [approx(2, x, y, X) for X in T])
plt.plot(T, [approx(4, x, y, X) for X in T])
plt.plot(T, [approx(8, x, y, X) for X in T])
plt.plot(T, [approx(16, x, y, X) for X in T])
plt.plot(T, LS, '.')
plt.legend(['y', 'a2', 'a4', 'a8', 'a16', 'LS'])
plt.savefig('Comparison.png', dpi = 300)
printLink('Comparison.png')

LS2 = np.interp(
np.array(x, dtype='float64'),
np.array(x, dtype='float64'),
np.array(y, dtype='float64'))

printh('Absolute Error')
print(f'    n = 2: {abserror(2, x, y)}')
print(f'    n = 4: {abserror(4, x, y)}')
print(f'    n = 8: {abserror(8, x, y)}')
print(f'   n = 16: {abserror(16, x, y)}')
print(f'   interp: {max(abs(y - LS2))}')

printh('RMS Error')
print(f'    n = 2: {rmserror(2, x, y)}')
print(f'    n = 4: {rmserror(4, x, y)}')
print(f'    n = 8: {rmserror(8, x, y)}')
print(f'   n = 16: {rmserror(16, x, y)}')
print(f'   interp: {math.sqrt(sum((y - LS2)**2))/len(LS2)}')
