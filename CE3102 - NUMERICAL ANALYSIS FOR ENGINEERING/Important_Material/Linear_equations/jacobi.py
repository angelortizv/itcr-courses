import numpy as np
"""
Determina si una matriz es dominantes
A: Matriz cuadrada
retorna un booleano
"""
def domin_matri(A):
    n = len(A)
    for f in range(0,n): # iteracion en la matriz
        d = A[f,f] # valor del diagonal
        f1 = A[f,:] # vector con los valores de las filas
        if abs(d) > abs(f1).sum(): # Verificacion de que el valor de la diagonal es el mayor de la final
            return False
    return True
"""
Esta funcion se encarga de calcular el xk apartir del sistema de jacobi y error estimado de la funcion
A: matriz
b: vector de valores independientes
xo: valor incial de xk
tol: tolerancia del sistema al error
iterMax: Numero de iteraxiones maximas permitidas
Retorna el valor de xk y el error estimado
"""     
def jacobi(A,b,xo,tol,iterMax):
    [n,m] = A.shape
    if(n != m): # Verifica que la matriz sea cuadrada
        raise ValueError('La matriz no es cuadrada')
    t = len(b)
    o = len(b[0])
    if(t !=n and o!=1): # verifica que el vector y la matriz sean de las mismas dimensiones
        raise ValueError('La matriz de valores independientes no cumple con las dimensiones de la matriz A')
    if(domin_matri(A) != True):
        raise ValueError('La matriz no es dominante')
    d = np.diag(A) # determina la diagonal de A
    D_inv = np.diag(1./d) # determina el inverso de la diagonal
    LpU = A - np.diag(d) # Realiza el calculo de A - el inverso de la diagonal
    z = D_inv * b.transpose() # Caclulo de D-1*bt
    xk = xo
    error = 0
    for k in range(1,iterMax):
        xk = (-D_inv*LpU*xk) +z # calculo de xk segun jacobi
        error = np.linalg.norm(A*xk -b) # Caculo del error
        if(error<tol):
            break

    return [xk,error]


A = np.matrix('10 1 -1 5;0 -7 1 1; 1 2 5 0;4 4 1 10')
b = np.matrix('1 1 1 1')
iterMax = 150
tol = 1^-15
x0 = np.zeros((4,1))
print(jacobi(A,b,x0,tol,iterMax))
