# -*- coding: utf-8 -*-
"""
Created on Fri May 28 12:07:50 2021
Josh Limon
Student ID: 804-984-257

Homework 8 Problem 3 (Gradient Descent via Forward Euler Method))
"""
import numpy as np
import matplotlib.pyplot as plt
import math

from mpl_toolkits import mplot3d
#Forward Euler on 3 different functions
def f1euler(x, h):
    xnext = [x[0] - h*math.cos(2*x[0])*(x[1]**2), x[1] + 2*h*x[1]*(math.sin(x[0])**2)]
    return xnext

def f2euler(x, h):
    xnext = [x[0] + h*(x[1]**2), x[1] + 2*h*x[0]*x[1]]
    return xnext

def f3euler(x, h):
    xnext = [x[0] - h*8*x[0] + h*6*x[1], x[1] + h*6*x[0] - 8*h*x[1]]
    return xnext



x1 = np.outer(np.linspace(-10, 10, 100), np.ones(100)) #Creates a 50x50 matrix with rows that are equally (0.1 is the distance between values of rows)
x2 = x1.copy().T
F1 = (x2**2)*np.sin(x1)**2
F2 = x1*x2**2
F3 = 4*x1**2 - 6*x1*x2 + 4*x2**2

#For generating plots and cantours to visualize functions.
c1 = plt.contourf(x1, x2, F1)
cbar1 = plt.colorbar(c1)
plt.show()

c2 = plt.contourf(x1, x2, F2)
cbar2 = plt.colorbar(c2)
plt.show()

c3 = plt.contourf(x1, x2, F3)
cbar3 = plt.colorbar(c3)
plt.show()

fig = plt.figure(figsize=(14,9))
plot = plt.axes(projection = '3d')
plot.plot_surface(x1, x2, F1)

fig2 = plt.figure(figsize=(14,9))
plot2 = plt.axes(projection = '3d')
plot2.plot_surface(x1, x2, F2)

fig3 = plt.figure(figsize=(14,9))
plot3 = plt.axes(projection = '3d')
plot3.plot_surface(x1, x2, F3)

plt.show()

x0 = [5, 3]; #Random seed
F1final = np.zeros((101, 2))
F2final = np.zeros((101, 2))
F3final = np.zeros((101, 2))
F1final[0] = x0;
F2final[0] = x0;
F3final[0] = x0;
for i in range(0,100):
    F1final[i+1] = f1euler(F1final[i], 0.1); #This function dips to the nearest valley and then stays there
    F2final[i+1] = f2euler(F2final[i], 0.1); #Function diverges towards an infinity
    F3final[i+1] = f3euler(F3final[i], 0.1); 
    
print(F1final, F2final, F3final)