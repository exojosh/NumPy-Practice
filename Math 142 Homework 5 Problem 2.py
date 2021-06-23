# -*- coding: utf-8 -*-
"""
Created on Fri May  7 15:09:16 2021

Code by Josh Limon
Student ID: 804-984-257

Homework #5 problem #5b
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import odeint

def dz_dt(Z, t, s, m, k):
    x, y = Z[0], Z[1]
    dxdt = y;
    dydt = -(s/m)*(y**3)  - (k/m)*x
    return [dxdt, dydt]

t = np.linspace(0,12, 100)
Z0 = [0, 0]
Zs = odeint(dz_dt, Z0, t, args=(1,2,7))



fig = plt.figure()
fig.set_size_inches(6,6)

initial = np.arange(1.0, 3.0, 0.1)
for r in initial:
    Z0 = [r, 2.0]
    Zs = odeint(dz_dt, Z0, t, args=(1,2,10))
    plt.plot(Zs[:,0], Zs[:,1], "-")
    