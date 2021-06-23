# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 20:52:48 2021

Code by Josh Limon
Student ID: 804-984-257

Homework 2 Problem 4 (Numpy Graphing Practice)
"""
import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-5, 5, 250)


f = 3*(x**3) + 20*x -20
h = 2.71828**(-(x**2))

plt.plot(x, f)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(['f(x)'])
plt.show()

plt.plot(x, h)
plt.xlabel('x')
plt.ylabel('h(x)')
plt.legend(['h(x)'])
plt.show()


t = np.linspace(-4, 4, 200)

x_t = t**2 - 3*t
y_t = t**3 - 9*t

plt.plot(t, x_t)
plt.plot(t, y_t)
plt.xlabel('t')
plt.ylabel('value of function')
plt.legend(['x(t)', 'y(t)'])
plt.show()