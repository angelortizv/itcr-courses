from mpmath.functions.functions import re
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

f = 'exp(x) + x-2'  # se define la función a utilizar.
x0 = 0  # se define el valor x0
x1 = 1 # se define el valor x1
tolerancia = 10 ** -5  # se define la tolerancia máxima
iterMax = 500  # se definen las iteracioens máximas antes de detenerse

def secante(f, x0 , x1,  tolerancia , iterMax):
    x = sp.Symbol('x') # Asi se define la varible simbolica
    f_simbolica = sp.sympify(f) # Se define de la funcion funcion
    f_eval = sp.lambdify(x , f_simbolica) # La funcion inicial se pasa a a una funcion evaluable
    er = []  # se define el vector de los errores para graficar posteriormente
    xk = x0  # Se define el primer valor o el valor inicial de x0
    xk1 = x1
    error = tolerancia + 1  # se define un valor inicial para el error
    k = 0  # se inicializa las iteraciones en cero
    while error > tolerancia:
        k += 1  # Se suma el valor de la iteracion
        xkAux = xk
        xk = xk - f_eval(xk) * ( (xk - xk1) / ( f_eval(xk)-f_eval(xk1))) # la funcion# se calcula una nueva interacion
        xk1 = xkAux 
        error = abs(f_eval(xk))  # se calcula el error
        er.append(sp.N(error))  # se agrega el error al vector de error
        if(error < tolerancia): # se verifica que el error cumpla con la tolerancia
            break
    fig, graf = plt.subplots()  # se crea la gráfica
    ejeX = np.arange(0, k, 1)  # se crea el eje X (son las iteraciones)
    graf.plot(ejeX, er)  # se grafican los datos
    plt.title('Metodo de la secante')
    plt.show()  # se muestra la gráfica
    return [xk, error, k]  # se retorna la aproximación y el error


funcion1 = secante(f, x0, x1,tolerancia , iterMax)
print("Aproximación: ", funcion1[0], " Error: ", funcion1[1], " Iteraciones: ", funcion1[2] - 1)