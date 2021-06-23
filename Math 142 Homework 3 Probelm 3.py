# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 15:18:34 2021

Code by Josh Limon
Student ID: 804-984-257

Homework 3 Problem 3 (System of Differential Equations)
"""

import numpy as np
import matplotlib.pyplot as plt
import math

"""
mx''(t) + c x'(t) + k x(t) = 0, 4mk < c^2 so overdamped, m = 1, k = 1, c = 3, x(0)=1, x'(0)=v0
x''(t) + 3x'(t) + x = 0 

We set x'(t) = omega(t)
and get omega'(t) = -3x'(t) -x

our system of first order differential equations

Note: below, y is the vector [x, omega]
"""

def overdamp(y, t):
    x, omega = y
    dydt = [omega, -3*omega - x]
    return dydt

v0 = 5; "<---- Change ME for varying initial velocity"
y0 = [1, -v0]

t = np.linspace(0,10, 101)

from scipy.integrate import odeint
sol = odeint(overdamp, y0, t)

plt.plot(t, sol[:, 0], 'r', label = 'x(t)')
plt.plot(t, sol[:, 1], 'b', label = 'dx/dt(t)')
plt.legend(loc='best')
plt.title("v0 = 5")
plt.xlabel('t')
plt.grid()
plt.show()