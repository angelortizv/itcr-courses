import numpy
import numpy as np

#Parametros de entrada
#A matriz nxn, #b matriz de valores independientes
#Salida
#x matriz  de las soluciones
#Metodo de thomas
def thomas(A, b):
    n = A.shape[0]  # Obtiene el numero de filas de A
    m = A.shape[1]  # Obtiene el numero de columnas de A
    t = b.shape[0]  # Obtiene el numero de filas de b
    o = b.shape[1]  # Obtiene el numero de columnas de B

    if (n != m):#Comprueba que la matriz sea cuadrada
        raise ValueError("La matriz no es cuadrada")
    if t!=n or o!=1:#Comprueba que las matriz b sea las dimensiones adecuadas
        raise ValueError("La matriz b no tiene las dimensiones correctas")

    M=obtiene_verifica_matriz(A,n)#Metodo para comprobar si la matriz es tridiagonal o lanza error si no lo es
    x=thomas_aux(M[0],M[1],M[2],b,n)#Llama a la funcion auxiliar para resolver el problema
    return x
#Parametros de entrada
#A matriz nxn, #n largo de la matriz
#Salida
#a Matriz de los valores de la diagonal,#b Matriz con los valores encima de la diagonal,#c Matriz con los valores debajo de la diagonal
#Metodo de thomas
def obtiene_verifica_matriz(A,n):
    a = np.zeros((n, 1))#Matriz lleno de zeros nx1
    b = np.zeros((n, 1))
    c = np.zeros((n, 1))

    for i in range(0,n):#Mueve filas
        for j in range(0,n):#Mueve columnas
            if j == i:#Diagonal
                a[i] = A[i,j]#Guarda valor en la matriz
            elif (i+1) == j:
                b[i] = A[i,j]
            elif (i-1) == j:
                c[i] = A[i,j]
            else:
                if A[i,j] != 0:
                    raise ValueError("Esta matriz no es tridiagonal")
    return a,b,c


#Parametros de entrada
#a Matriz de los valores de la diagonal,#b Matriz con los valores encima de la diagonal,#c Matriz con los valores debajo de la diagonal
#Salida
#sol matriz de soluciones
#Metodo de auxiliar de thomas, realiza el algoritmo para resolver el sistema
def thomas_aux(a,b,c,d,n):
    r=np.zeros((n, 1))#Matriz lleno de zeros nx1
    t= np.zeros((n, 1))
    sol= np.zeros((n, 1))
    r[0]=b[0]/a[0]#Primer coeficiente

    for i in range(1,n-1):
        if(a[i]-r[i-1]*c[i])==0:#Comprueba que el divisor no sea 0
            raise ValueError("No se puede dividir entre 0")
        else:
            r[i]=b[i]/(a[i]-r[i-1]*c[i])#Calcula los nuevos coeficientes
    t[0]=d[0]/a[0]#Se realiza el primera barrido/susticion(similar hacia adelante)
    for j in range(1,n):
        if (a[j]-r[j-1]*c[j])==0:#Comprueba que el divisor no sea 0
            raise ValueError("No se puede dividir entre 0")
        else:
            t[j]=(d[j]-t[j-1]*c[j])/(a[j]-r[j-1]*c[j])#Completa el barrido/susticion(similar hacia adelante)

    sol[n-1]=t[n-1]#Calcula la ultima solucion
    k=n-2
    while k>=0:
        sol[k]=t[k]-r[k]*sol[k+1]#Calcula las demas soluciones
        k=k-1
    return sol


if __name__ == '__main__':
    #Ejemplo de como se ingresan los datos
    A=np.matrix('5 1 0 0;1 5 1 0;0 1 5 1;0 0 1 5',float)
    b=np.matrix('-12;-14;-14;-12',float)
    print("Solucion x de ejemplo:")
    print(thomas(A, b))
