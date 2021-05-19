#!/usr/bin/python3
from gekko import GEKKO
import numpy as np
import matplotlib.pyplot as plt
from functions import *

m = GEKKO(remote=False)
#m.time = np.arange(0,2.01,0.05)
m.time = np.linspace(0, 0.5, 2000)
y = m.Var(1.0)
z = m.Var(2.0)
t = m.Var(0.0)
m.Equation(t.dt()==1.0)
m.Equation(y.dt()==z)
m.Equation(z.dt()+(m.log(3.5 + t))*z-(0.8 * (t ** 2))*y==2.5 *t - t ** 2)
m.options.IMODE = 4; m.options.NODES = 3
m.solve(disp=False)
print(m.time,y.value)
plt.plot(m.time,y.value,'r-',label='y')
#plt.plot(m.time,z.value,'b--',label='z')
plt.legend()
plt.xlabel('Time')
plt.savefig('gekko.png')
printLink('gekko.png')
