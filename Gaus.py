# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 17:16:54 2024

@author: Ana
"""
import numpy as np
A = np.array ([[2,3,4,5], [6,15,19,23], [8,42,60,70], [12,60,1,17]])
B = np.array ([5, 30, 98, 144])

def Gauss (A, B):
  A = A.astype(float)
  B = B.astype(float)
  n = A.shape[0]
  AB = np.c_[A, B]
  x = np.zeros(n)
  for k in range (n-1):
    for i in range (k+1, n):
      l = AB[i, k]/AB[k, k]
      AB[i,:] -= l*AB[k,:]
    for i in range (n-1, -1, -1):
      s = 0
      for j in range (i+1, n):
        s += AB[i, j] * x[j]
      x[i] = (AB[i, n] - s) / AB[i, i]
  return x 
x = Gauss(A, B)
print('\n El vector solución del sistema, x=', x)




    
      
  
  

  
    
  
  

  


