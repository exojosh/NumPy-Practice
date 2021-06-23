# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 01:24:29 2021

Code by Josh Limon
Student ID: 804-984-257

Midterm Problem 2
"""

import numpy as np
import matplotlib.pyplot as plt
import math

"""
We set x(t) = x1(t)
and x'(t) = x2(t)
and get x2'(t) = x1 + x2/6 - 31.9


"""
x0 = 0.5;
v0 = -1;

def equa(x, v):
    x1 = x;
    x2 = v;
    dydt = [0.01*x2, 0.01*(x1 + (x2/6) - 31.9)] #I implement delta T here as 0.01
    return dydt



t = np.linspace(0,10, 1001)
f = np.zeros((1001,2));
ind = np.linspace(1,1000, 1001, dtype=int)   
f[1] = equa(x0, v0);

for i in range(2, 1001):
    f[i] = f[i-1] + equa(f[i-1, 0], f[i-1, 1]);


    
 
plt.plot(t, f[ind, 0], 'r', label = 'x(t)')
plt.legend(loc='best')
plt.title("Problem 2(c)")
plt.xlabel('t')
plt.grid()
plt.show()


"""Part (d)"""

t = np.linspace(0, 101, 1001)
def func(t):
    return 10.633 - 55.5313*np.exp((-1/12)*(np.sqrt(145) - 1)*t) +44.998*np.exp((1/12)*(np.sqrt(145) + 1)*t)



plt.plot(t, func(t), 'r', label = 'x(t)')
plt.legend(loc='best')
plt.title("Problem 2(d)")
plt.xlabel('t')
plt.grid()
plt.show()