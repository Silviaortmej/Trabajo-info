# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 17:16:54 2024

@author: Ana
"""
"""Resolución de un sistema de ecuaciones lineales mediante el método de eliminación de Gauss. (Se asume que la matriz de coeficientes es invertible)
En este programa se asume también que nunca se va a producir la división entre 0. """
import numpy as np
A = np.array ([[2,3,4,5], [6,15,19,23], [8,42,60,70], [12,60,1,17]])
B = np.array ([5, 30, 98, 144])

#Definimos la función Gauss.
def Gauss (A, B):
  #Nos aseguramos de que la matriz de coeficientes y la columna de términos independientes sean del tipo float. 
  A = A.astype(float)
  B = B.astype(float)
  #Dimensión del sistema (el número de filas).
  n = A.shape[0]
  #Concatenamos A y B para hacer la matriz ampliada.
  AB = np.c_[A, B]
  #Creamos un vector donde se van a ir almacenando las soluciones del sistema. 
  x = np.zeros(n)
  #TRIANGULACIÓN
  for k in range (n-1): #Para cada elemento de la diagonal menos el último.
    for i in range (k+1, n): #Filas por debajo de la diagonal.
      l = AB[i, k]/AB[k, k]
      AB[i,:] -= l*AB[k,:]
      
    #SUSTITUCIÓN
    for i in range (n-1, -1, -1):
      s = 0
      for j in range (i+1, n): #J es cada elemento de la fila.
        s += AB[i, j] * x[j]
      x[i] = (AB[i, n] - s) / AB[i, i] #Operación.
  return x 
x = Gauss(A, B)
print('\n El vector solución del sistema, x=', x)





    
      
  
  

  
    
  
  

  


