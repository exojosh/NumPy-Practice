# -*- coding: utf-8 -*-
"""
Created on Fri May 21 10:45:56 2021
Josh Limon
Student ID: 804-984-257

Homework 7 Problem 5b and c (System of Differential Equations)
"""

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

Ns = np.outer(np.linspace(0, 5, 50), np.ones(50)) #Creates a 50x50 matrix with rows that are equally (0.1 is the distance between values of rows)
Nf = Ns.copy().T
z = ((Ns*Nf)**2)/(np.exp(Nf+Ns))

fig = plt.figure(figsize=(14,9))
plot = plt.axes(projection = '3d')
fig2 = plt.figure(figsize=(14,9))
cont = fig2.add_subplot(111)

plot.plot_surface(Nf, Ns, z)
plt.contourf(Ns, Nf, z)

plt.show()