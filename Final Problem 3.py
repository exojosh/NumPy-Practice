# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 16:27:39 2021

@author: Josh Limon
C/O 2021, 804-984-257

Math 142 Final Coding for Problem 3
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def dX(x,y):
    dx = 2*x - x*y - x**2;
    dy = 3*y - 2*x*y - y**2;
    return [dx,dy]

def dX1(x,y):
    dx = 2*x - x*y - x**2;
    return dx

def dX2(x,y):
    dy = 3*y - 2*x*y - y**2;
    return dy


xaxis, yaxis = np.meshgrid(np.linspace(-5.0, 5.0, 100), np.linspace(-5.0, 5.0, 100))
derX, derY = dX(xaxis, yaxis);

plt.streamplot(xaxis, yaxis, derX, derY, color='r', density=1.0)
plt.axis('square')
plt.axis([-5,5,-5,5])

t = np.linspace(0,8,100);
x0 = dX(-2.0, 4.0)
ys1 = odeint(dX1, x0[0], t);
ys2 = odeint(dX2, x0[1], t);
plt.plot(ys1[:],ys2[:], 'b')
            

plt.show()