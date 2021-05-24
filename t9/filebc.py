#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
#from functions import *
import os

def p(X):
    return np.log(3.5 + X)

def f(tt, X):
    return X - 0.5*tt*(X**2)

def u0(X):
    return X**2 + 1

def T1(tt):
    return 1

def T2(tt):
    return 2 - tt

#L = 0.1
L = 2
n = 10
T0 = 0
#T1s = 40
#T2s = 20
dx = L / n
#alpha = 0.0001
t_final = 1
dt = 0.01

T = np.ones(n) * T0
x = np.linspace(dx/2, L - dx/2, n)
dTdt = np.empty(n)

counter = 0
t = np.arange(0, t_final, dt)
for j in range(1, len(t)):
    plt.clf()
    for i in range(1, n - 1):
        #dTdt[i] = p*(-(T[i] - T[i-1])/dx**2 + (T[i+1] - T[i])/dx**2)
        dTdt[i] = p(x[i])*x[i]*(-(T[i] - T[i-1])/dx**2 + (T[i+1] - T[i])/dx**2) #+ f(j, i)
    #dTdt[0] = alpha*(-(T[0] - T1s)/dx**2 + (T[0] - T[1])/dx**2)
    #dTdt[-1] = alpha*(-(T[-1] - T[-2])/dx**2 + (T2s - T[-1])/dx**2)
    dTdt[0] = p(x[0])*x[0]*(-(T[0] - T1(t[j]))/dx**2 + (T[1] - T[1])/dx**2) #+ f(j, 0)
    dTdt[-1] = p(x[-1])*x[-1]*(-(T[0] - T[-2])/dx**2 + (T[1] - T2(t[j]))/dx**2) #+ f(j, n-1)
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
