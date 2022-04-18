import sympy as sp
import numpy as np

def trian_sup(A,b,n):
    M = np.hstack((A,b))
    for k in range(0,n-1):
        for i in range(k+1,n):
            Mik = M.item(i,k)/M.item(k,k)
            for j in range(k,n+1):
                d = M.item(i,j) - Mik*M.item(k,j)
                M.itemset((i,j),d)
    b = M[:,[n]]
    A = M[:,0:n]
    return [A, b]

"""
Resuelve un sistema de ecuaciones por el metodo de la sustitucion hacia atras
:param A Matriz de tamaño nxn. Debe ser triangular superior.
:param b Vector del tamaño n
"""
def paso_atras(A,b,n):
    s = np.zeros((n,1))
    i = n-1
    while i>-1:
        sum = 0
        for j in range(i+1,n):
            sum = sum + (A.item(i,j)*s.item(j))
        x = (1/ A.item(i,i))*(b.item(i)-sum)
        s.itemset(i,x)
        i = i-1
    return [s]

def gaussiana(A, b):
    A = np.matrix(A)
    b = np.matrix(b)
    print('hello')
    n = len(A)
    m = len(A[0])
    [n,m] =A.shape
    if(n != m):
        raise ValueError('La matriz no es cuadrada')
    t = len(b)
    o = len(b[0])
    if(t !=n and o!=1):
        raise ValueError('La matriz de valores independientes no cumple con las dimensiones de la matriz A')
    [A,b] = trian_sup(A,b,n)
    if(np.linalg.det(A) != 0):
        x = paso_atras(A,b,n)
        return x
    else:
        raise ValueError('La matriz no es invertible')






#A= np.matrix('3 3 1; 1 2 1; 3 2 2'); #Matriz 4x4
#A= np.matrix('2 1 2; 3 4 2; 4 4 2'); #Matriz 4x4
#A= np.matrix('2 1 2; 1 2 1; 1 1 2'); #Matriz 4x4
A= np.matrix('6 5 6;4 3 4;8 6 8'); #Matriz 4x4
b= np.matrix('70; 26; -30');
n =4
print(gaussiana(A,b))

#[a,B] = trian_sup(A,b,n)
#print(a)
#print(B)
#[s] = paso_atras(a,B,n)
#print(s)
np.matrix('3.0 -4.0 1.0;0.0 2.333 0.66;0.0 0.0 -5.714')
