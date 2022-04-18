import numpy as np
from sympy import Symbol
import math
from matplotlib import pyplot as plt


def relajacion(matriz, vector_independiente, valor_inicial, tol, iterMax):
    """
    Funcion que implementa el metodo iterativo de relajacion
    :param matriz_a: Matriz cuadrada sim´etrica definida positiva
    :param vector_independiente: Vector columna
    :param tol: Tolerancia al fallo que debe tener el resultado
    :param iterMax: Iteraciones maximas
    :return: Vector resultado
    """
    n = len(matriz)  # Numero de filas
    m = len(matriz[0])  # Numero de columnas
    iter = 0  # Numero de iteraciones

    # Verificar si es cuadrada
    if (n != m):
        raise ValueError('La matriz debe ser cuadrada')

    # Verifica que A sea igual a At
    if (np.array_equal(matriz, np.transpose(matriz)) != True):
        raise ValueError('La matriz A no es igual a la matriz At')

    # Verificar si b es del largo de la matriz
    if (len(b) != m):
        raise ValueError('La matriz debe ser cuadrada')

    if teorema_2(matriz,n) == False:#Comprueba las submatrices sean invertibles
        raise ValueError('La matriz no cumple el teorema 2, sus determinantes no son cero')

    

    # Calcular la matriz D
    d = cal_matriz_d(matriz, n)

    # Calcular la matriz L
    l = cal_matriz_l(matriz, n)

    # Calcular matriz U
    u = cal_matriz_u(matriz, n)

    # Calcular N
    matriz_n = -(l + u)

    # Calcular M-1
    m_inver = np.linalg.inv(d)

    # Calcular valor M-1*N
    matriz_a = np.dot(m_inver, matriz_n)

    # Calcular radio espectral
    p = radio_espectral(matriz_a)

    # Calcular el valor de w optimo
    w = 2 / (1 + math.sqrt(1 - p ** 2))

    # Calcula d+wl
    temp_1 = d + np.dot(w, l)

    # Calcula w*b
    temp_3 = np.dot(w, vector_independiente)

    # Calculo de C
    C = hacia_Adelante(temp_1, temp_3, n)
    
    D = []
    A = []

    while (iter <= iterMax):


        temp_2 = np.dot((np.dot((1 - w), d) - np.dot(w, u)), valor_inicial)

        T = hacia_Adelante(temp_1, temp_2, n)  # Se calcula T
        X = T + C # Se calcula el valor de X+1 

        # Se calcula el error
        x_actual = 0 
        x_anterior = 0
        for i in range(0, n):
            x_actual += (X[i][0])**2
            x_anterior += (valor_inicial[i][0])**2
        error = (math.sqrt(x_actual)-math.sqrt(x_anterior))/math.sqrt(x_actual)

        # Se agregan los valores de error e iteracion 
        D.append(iter)
        A.append(error)

        # Se actualiza el valor de X
        valor_inicial = X

        # Se comprueba si el error es menor a la tolerancia
        if (error < tol):
            break

        iter += 1

    #Grafico de error por iteracion
    plt.plot(np.array(D), np.array(A))
    plt.title("Gráfico")
    plt.legend(["Error"])
    plt.show() 

    print(valor_inicial, error)
    return [valor_inicial, error]


# Parametros de entrada
# matriz_a matriz  cuadrada, #n largo de la matriz
# Salida
# Matriz D
# Calculo de la matriz D
def cal_matriz_d(matriz_a, n):
    d = np.zeros_like(matriz_a)
    for i in range(0, n):
        d[i][i] = matriz_a[i][i]
    return d


# Parametros de entrada
# matriz_a matriz  cuadrada, #n largo de la matriz
# Salida
# Matriz L
# Calculo de la matriz L
def cal_matriz_l(matriz_a, n):
    d = np.zeros_like(matriz_a)
    for i in range(0, n):
        for j in range(0, i):
            d[i][j] = matriz_a[i][j]
    return d


# Parametros de entrada
# matriz_a matriz  cuadrada, #n largo de la matriz
# Salida
# Matriz U
# Calculo de la matriz U
def cal_matriz_u(matriz_a, n):
    u = np.zeros_like(matriz_a)
    for i in range(0, n):
        for j in range(i + 1, n):
            u[i][j] = matriz_a[i][j]
    return u


# Parametros de entrada
# matriz_a matriz  cuadrada, matriz cuadrada D
# Salida
# Matriz N
# Calculo de la matriz N
def cal_matriz_n(matriz_a, matriz_d):
    matriz_n = -(matriz_a - matriz_d)
    return matriz_n


# Parametros de entrada
# matriz_a matriz  cuadrada
# Salida
# Valor del radio espectral
# Calculo del valor máximo del radio espectral
def radio_espectral(matriz_a):
    valores, vectores = np.linalg.eig(matriz_a)
    mayor = 0
    for i in range(len(valores)):
        if (mayor < abs(valores[i])):
            mayor = valores[i]
    return mayor


#Parametros de entrada
#A matriz  triangular inferior, #b nueva matriz de valores independientes, #n largo de la matriz
#Salida
#soluciones matriz de soluciones "x#"
#Sustitucion hacia adelante
def hacia_Adelante(A, b, n):
    soluciones = np.zeros((n, 1))#Matriz de soluciones
    soluciones[0] = b[0] / A[0, 0]#Primera solucion
    i = 1

    while (i < n):#Mueve las filas
        sumatoria = 0
        for j in range(0, i):#Mueve columnas
            sumatoria = sumatoria + (A[i, j] * soluciones[j])#Sumatoria necesaria

        x = (b[i] - sumatoria) / A[i, i]#Calcular el valor de la solucion "x"
        soluciones[i] = x#Agrega la solucion a la matriz de soluciones
        i = i + 1
    return soluciones

#Parametros de entrada
#A matriz  cuadrada, #n largo de la matriz
#Salida
#Valor booleado que identifica si se cumple o no el teorema 2
#Evaluacion del Teorema de LU
def teorema_2(A, n):#Comprueba que las submatrices tiene determinante diferente de 0
    A = np.matrix(A, float)
    Valor = True#Booleano que sirve para identificar si se cumplio o no el teorema
    for k in range(0, n):
        if np.linalg.det(A[0:k, 0:k]) == 0:
            Valor = False#Se detiene si una submatriz no cumple el teorema 2
            break
    return Valor#True se cumple, #False se incumple

# Valores iniciales
if __name__ == '__main__':
    a = [[4, 3, 0], [3, 4, -1], [0, -1, 4]]
    b = [[7], [7], [-1]]
    relajacion(a, b, [[0], [0], [0]], 10**(-10), 5)
