#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import os

L = 0.1
n = 10
T0 = 0
T1s = 40
T2s = 20
dx = L / n
alpha = 0.0001
t_final = 60
dt = 0.5

T = np.ones(n) * T0
x = np.linspace(dx/2, L - dx/2, n)
dTdt = np.empty(n)

counter = 0
t = np.arange(0, t_final, dt)
for j in range(1, len(t)):
    plt.clf()
    for i in range(1, n - 1):
        dTdt[i] = alpha*(-(T[i] - T[i-1])/dx**2 + (T[i+1] - T[i])/dx**2)
    dTdt[0] = alpha*(-(T[0] - T1s)/dx**2 + (T[0] - T[1])/dx**2)
    dTdt[-1] = alpha*(-(T[-1] - T[-2])/dx**2 + (T2s - T[-1])/dx**2)
    T = T + dTdt * dt
    plt.plot(x, T)
    plt.xlabel('Dist')
    plt.ylabel('Temp')
    plt.legend(['t=%.000f 10x' % t[j]])
    plt.savefig('tmp_%04d.png' % counter)
    print(f'Temp: {t[j]}', end='\r')
    counter += 1

os.system('rm video.mp4')
os.system('ffmpeg -r 30 -i tmp_%04d.png -c:v libx264 -vf fps=30 -pix_fmt yuv420p video.mp4')
os.system('rm tmp_*.png')
