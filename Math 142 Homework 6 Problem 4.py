# -*- coding: utf-8 -*-
"""
Created on Fri May 14 11:58:54 2021
Josh Limon
Student ID: 804-984-257

Homework 6 Problem 4c (System of Differential Equations)
"""

import numpy as np
import matplotlib.pyplot as plt
import math


def fun1(x, t):
    return (math.cos(x))**2;
    
def fun2(x, t): 
    return x**2 + x - 3;
    
t = np.linspace(-6, 30, 181)
y0 = 1
from scipy.integrate import odeint
sol = odeint(fun2, y0, t)
"""
for i in range (1, 121):
    sol[i] = fun1(t[i], y0)
    """


print(sol)

plt.plot(t, sol, 'r', label = 'x(t)')
plt.legend(loc='best')
plt.title("x^2 + x -3, x0 = 1")
plt.xlabel('t')
plt.grid()
plt.show()