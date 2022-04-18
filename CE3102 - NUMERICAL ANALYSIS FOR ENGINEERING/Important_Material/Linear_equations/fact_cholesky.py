import sympy as sp
import numpy as np
import math

"""
Resuelve un sistema de ecuaciones por el metodo de la sustitucion hacia atras
:param A Matriz de tamaño nxn. Debe ser triangular superior.
:param b Vector del tamaño n
"""
def paso_atras(A,b):
    [n,m] = A.shape
    s = np.zeros((n,1))
    i = n-1
    while i>-1:
        sum = 0
        for j in range(i+1,n):
            sum = sum + (A.item(i,j)*s.item(j))
        x = (1/ A.item(i,i))*(b.item(i)-sum)
        s.itemset(i,x)
        i = i-1
    return s
"""
Resuelve un sistema de ecuaciones por el metodo de la sustitucion hacia adelante
:param A Matriz de tamaño nxn. Debe ser triangular superior.
:param b Vector del tamaño n
"""
def paso_adelante(A,b):
    [n,m] = A.shape
    s = np.zeros((n,1))
    i = 0
    while i<n:
        sum = 0
        for j in range(0,i):
            sum = sum + (A.item(i,j)*s.item(j))
        x = (1/ A.item(i,i))*(b.item(i)-sum)
        s.itemset(i,x)
        i = i+1
    return s
"""
Determina si la matriz es positiva definida
:param A Matrix de tamaño nxn
:param n tamaño de la matriz
"""
def postiva_definida(A,n):
    for i in range(0,n):
        A_t = A[0:i,0:i]
        result = np.linalg.det(A_t)
        if(result <0):
            return False
    return True
"""
"""
def fact_cholesky(a, B):
    A = np.matrix(a)
    b = np.matrix(B)
    n = len(A)
    m = len(A[0])
    [n,m] =A.shape
    if(n != m):
        raise ValueError('La matriz no es cuadrada')
    t = len(b)
    o = len(b[0])
    if(t !=n and o!=1):
        raise ValueError('La matriz de valores independientes no cumple con las dimensiones de la matriz A')
    A_t = A.transpose()
    if np.allclose(A,A_t) != True:
        raise ValueError('La matriz no es simetrica')
    if(postiva_definida(A,n) != True):
        raise ValueError('La matriz no es simetrica')
    L = np.zeros((n,n))
    for i in range(0,n):
        for j in range(0,i+1):
            sum = 0
            if(j==i):
                for k in range(0,j):
                    sum = sum + pow(L.item(j,k),2)
                L[j,j] = math.sqrt(A.item(j,j)-sum)
            else:
                for k in range(0,j):
                    sum += L.item(i,k)*L.item(j,k)
                L[i,j] = (A.item(i,j) -sum) / L.item(j,j)
                    
    y = paso_adelante(L,b)
    x = paso_atras(L.transpose(),y)
    
    return x

    

#A = '25 15 -5 -10; 15 10 1 -7;-5 1 21 4; -10 -7 4 18'
A = '5 -1 0;-1 2 -1;0 -1 5'
b= '-25; -19; -21'
print(fact_cholesky(A,b))
