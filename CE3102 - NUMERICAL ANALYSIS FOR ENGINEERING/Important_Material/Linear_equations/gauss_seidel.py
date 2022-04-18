import numpy as np

def domin_matri(A):
    n = len(A)
    for f in range(0,n):
        d = A[f,f]
        f1 = A[f,:]
        if abs(d) > abs(f1).sum():
            return False
    return True
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
A: matriz nxm
n: tamaño de filas de la matriz
Esta funcion se encarga de obtener las matrices L,U,D
"""
def matrices_Jacobi(A):
    n = len(A)
    L = np.zeros((n,n))
    U = np.zeros((n,n))
    D = np.zeros((n,n))
    for i in range(0,n):
        for j in range(0,n):
            if j==i:
                D[i,j] = A[i,j]
            elif i <j:
                U[i,j] = A[i,j]
            elif i > j:
                L[i,j] = A[i,j]
    return [L,U,D]
            
"""
Funcion de gauss_seidel para el calculo de ecuaciones no lineales
A: Matriz A
b: vector de valores independientes
xo: el valor de x inicial
tol: Tolerancia permitida para el error
iterMax: Numero de iteracciones maxima
"""       
def gauss_seidel(A,b,xo,tol,iterMax):
    [n,m] = A.shape
    if(n != m):
        raise ValueError('La matriz no es cuadrada')
    t = len(b)
    o = len(b[0])
    if(t !=n and o!=1):
        raise ValueError('La matriz de valores independientes no cumple con las dimensiones de la matriz A')
    if(domin_matri(A) != True):
        raise ValueError('La matriz no es dominante')
    [L, U, D] = matrices_Jacobi(A)
    x = np.zeros((n,1))
    x1 = xo
    error = []
    H = (L+D)
    c = paso_adelante(H,b)
    for i in range(0,iterMax):
        d = -U*x[0:n,i]
        z = paso_adelante(H,d)
        x1 = z+c
        x = np.hstack((x,x1))
        print('printt')
        print(A*x1-b)
        e_norma2 = np.linalg.norm(A*x1-b)
        error.append(e_norma2)
        if e_norma2 <= tol:
            break
    return error,iterMax,x
        
A = np.matrix('5 1 1;1 5 1; 1 1 5')
b = np.matrix('7;7;7')
x0 = 0
iter = 100
tol = 10**-3
print(gauss_seidel(A,b,x0,tol,iter))
