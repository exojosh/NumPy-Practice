# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 21:26:35 2021

Code by Josh Limon
Student ID: 804-984-257

Homework 2 Problem 5 (Euler algorithm Practice)
"""
import math
import numpy as np
import matplotlib.pyplot as plt


x1_0 = -0.2; #We initialize the value to the value at t=0
N = 150;
t = np.linspace(0, 5, N);
deltat = t[1] -t[0];
f1 = np.zeros([N]);
f1[0] = x1_0;

for i in range(1, N):
    x1 =  2.71828**(t[i-1] + (4*(f1[i-1]))); ##This fucntion gets some weird results around i = 14 prob cuz imaginary component
    f1[i] = f1[i-1] + deltat*x1;
    print(t[i])
    
plt.plot(t, f1)
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend(['x(t)'])
plt.show()

x2_01 = 2
x2_02 = 3
#I didn't finish because I don't know how to set up as a system of linear ordinary differential equations with numpy right now.