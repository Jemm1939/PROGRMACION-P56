# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:13:10 2020

@author: POINT
"""


import numpy as np
matrix=np.array([[1,2,3,4,5],[5,6,8,9,10]],dtype=np.int64)
print(matrix)
print("\n")
print("la matriz tiene: ",matrix.ndim, " dimensiones")
print("\n")
print("el tipo de datos de la matriz es: ",matrix.dtype)
print("\n")
print("el tamaño de la matriz es: ",matrix.size)
print("\n")
print("la forma de la mtriz es: ",matrix.shape)