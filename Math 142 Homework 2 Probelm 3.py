# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 20:23:14 2021

Code by Josh Limon
Student ID: 804-984-257

Homework 2 Problem 3 (Numpy Linear Algebra Practice)
"""

import numpy as np

A = np.array([[1, 2, -1], [0, 1, 0], [3, -1, -2]])
B = np.array([[1, 2, 3], [1, 1, 2], [0, 1, 2]])
C = np.array([[2, 1, 1], [0, 1, -1], [4, 2, 2]])

D = np.dot(B, C)
D = 4 * D
D = D + A
print("Part i) A + 4BC is: \n", D)
    
Ainv = np.linalg.inv(A)
Binv = np.linalg.inv(B)
#Cinv = np.linalg.inv(C) HAS NO INVERSE SINCE DET = 0

print("\n\nPart iia) The inverse of A is: ", Ainv)
print("\nPart iib) The inverse of B is: ", Binv)
##print("\nPart iic) The inverse of C is: ", Cinv)
print("\nPart iic) C has no inverse!")

Cdet = np.linalg.det(C)
print("\n\nPart iii) The determinant of C is: ", Cdet)

print("\nPart iv) Eigenvalues followed by Eigenvectors of B are given by: ", np.linalg.eig(B))

