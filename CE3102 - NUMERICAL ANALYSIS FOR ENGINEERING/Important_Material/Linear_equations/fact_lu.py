import numpy
import numpy as np


#Parametros de entrada
#A matriz nxn, #b matriz de valores independientes
#Salida
#x matriz  de las soluciones
def fact_lu(A, b):
    n = A.shape[0]#Obtiene el numero de filas de A
    m = A.shape[1]#Obtiene el numero de columnas de A
    t = b.shape[0]#Obtiene el numero de filas de b
    o = b.shape[1]#Obtiene el numero de columnas de B
    if n != m:#Comprueba que la matriz sea cuadrada
        raise ValueError("La matriz no es cuadrada")
    if t != n or o!=1:#Comprueba que las matriz b sea las dimensiones adecuadas
        raise ValueError("La matriz b no tiene las dimensiones correctas")
    if teorema_2_lu(A,n) == False:#Comprueba las submatrices sean invertibles
        raise ValueError("La matriz no cumple el teorema 2 de Fact LU")

    M = matriz_inf_lu(A, n)#Obtiene la matriz de inferior y superior en version LU

    y = hacia_Adelante(M[1], b, n)#Resuelve Ly=b
    x = hacia_Atras(M[0], y, n)#Resuleve Ux=y
    return x

#Parametros de entrada
#A matriz  cuadrada, #n largo de la matriz
#Salida
#Valor booleado que identifica si se cumple o no el teorema 2
#Evaluacion del Teorema de LU
def teorema_2_lu(A, n):#Comprueba que las submatrices tiene determinante diferente de 0
    Valor = True#Booleano que sirve para identificar si se cumplio o no el teorema
    for k in range(0, n):
        if np.linalg.det(A[0:k, 0:k]) == 0:
            Valor = False#Se detiene si una submatriz no cumple el teorema 2
            break
    return Valor#True se cumple, #False se incumple


#Parametros de entrada
#A matriz cuadrada, #n largo de la matriz
#Salida
#U matriz Triangular superior LU, #L Matriz Triangular inferior LU
#Matrices inferior y superior version Factorizacion de LU
def matriz_inf_lu(A,n):
    U=A
    L=np.zeros((n,n))

    for k in range(0,n-1):#Columnas
        for i in range(k+1,n):#Filas
            Mik=U[i,k]/U[k,k]
            L[i,k]=Mik#Agrega a la matriz los valores ocupuesto a los "Multiplicadores" de la matriz
            for j in range(k,n):#Ciclo para agregar los nuevos valores de la matriz U
                U[i,j]=U[i,j]-Mik*U[k,j]
                if i==j:
                    L[i,j]=1
    L[0,0]=1
    return U,L


#Parametros de entrada
#A matriz  triangular superior, #b nueva matriz de valores independientes, #n largo de la matriz
#Salida
#soluciones matriz de soluciones "x#"
#Sustitucion hacia atras
def hacia_Atras(A, b, n):
    soluciones = np.zeros((n, 1))
    i = n - 1;

    while (i >= 0):
        sumatoria = 0
        for j in range(i + 1, n):
            sumatoria = sumatoria + (A[i, j] * soluciones[j])

        x = (1 / A[i, i]) * (b[i] - sumatoria)
        soluciones[i] = x
        i = i - 1
    return soluciones


#Parametros de entrada
#A matriz  triangular inferior, #b nueva matriz de valores independientes, #n largo de la matriz
#Salida
#soluciones matriz de soluciones "x#"
#Sustitucion hacia adelante
def hacia_Adelante(A, b, n):
    soluciones = np.zeros((n, 1))#Matriz de soluciones
    soluciones[0] = b[0] / A[0, 0]#Primera solucion
    i = 1;

    while (i < n):#Mueve las filas
        sumatoria = 0
        for j in range(0, i):#Mueve columnas
            sumatoria = sumatoria + (A[i, j] * soluciones[j])#Sumatoria necesaria

        x = (b[i] - sumatoria) / A[i, i]#Calcular el valor de la solucion "x"
        soluciones[i] = x#Agrega la solucion a la matriz de soluciones
        i = i + 1
    return soluciones



if __name__ == '__main__':
    #Ejemplos de ingresos de datos
    A = np.matrix('4 -2 1; 20 -7 12;-8 13 17', float)
    A2 = np.matrix('25 15 -5 -10;15 10 1 -7;-5 1 21 4;-10 -7 4 18',float)

    b = numpy.matrix('11;70;17')
    b2 = np.matrix('-25;-19;-21;-5')
    print("Ejemplo 1 tiene como resultado:")
    print(fact_lu(A, b))
    print("Ejemplo 2 tiene como resultado:")
    print(fact_lu(A2, b2))
