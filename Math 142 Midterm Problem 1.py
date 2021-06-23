# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 19:35:21 2021

Code by Josh Limon
Student ID: 804-984-257

Midterm Problem 1
"""


import numpy as np
import matplotlib.pyplot as plt
import math

thearray = np.array([[0,1,0,0],[0,0,1,0],[0,0,0,1],[-24,-50,-35,-10]])
initial = np.array([1,-1,0.5,-0.3])
eigenvalues, eigenvectors = np.linalg.eig(thearray)
constants = np.linalg.solve(eigenvectors, initial)
x1solution = np.dot(  constants, eigenvectors[0,:]) #Checks initial condition x1 is valid for constants solution

print(eigenvalues)
print(eigenvectors)
print('\n\n')
print(constants)

c1=constants[0]
c2=constants[1]
c3=constants[2]
c4=constants[3]

x11=eigenvectors[0,0]
x12=eigenvectors[0,1]
x13=eigenvectors[0,2]
x14=eigenvectors[0,3]

x21=eigenvectors[1,0]
x22=eigenvectors[1,1]
x23=eigenvectors[1,2]
x24=eigenvectors[1,3]
print(c1)

def x(t):
    ans = np.exp(-4*t) + c2*x12*np.exp(-3*t) + c3*x13*np.exp(-2*t) + c4*x14*np.exp(-1*t)
    return ans


def dxdt(t):
    return c1*x21*np.exp(-4*t) + c2*x22*np.exp(-3*t) + c3*x23*np.exp(-2*t) + c4*x24*np.exp(-1*t)

t = np.linspace(0,10, 1001)

plt.plot(t, x(t), 'r', label = 'x(t)')
plt.plot(t, dxdt(t), 'b', label = 'dx/dt(t)')
plt.legend(loc='best')
plt.title("Problem 1")
plt.xlabel('t')
plt.grid()
plt.show()