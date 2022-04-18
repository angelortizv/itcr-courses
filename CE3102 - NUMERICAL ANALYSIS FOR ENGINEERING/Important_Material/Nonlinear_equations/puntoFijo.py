from mpmath.functions.functions import re
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

f = 'log(2*x + 1)' #Funcion entrada
x0 = 1.5  #Valor inicial
tol=10**-9 # toleracia de erroer
iterMax=1000  #Maxima interacion

def puntoFijo(f, X0 , tol, iterMax): 
    x = sp.Symbol('x') # Asi se define la varible simbolica
    f_simbolica = sp.sympify(f) # Se define de la funcion funcion
    f_eval = sp.lambdify(x , f_simbolica) # La funcion inicial se pasa a a una funcion evaluable
    er = []  # se define el vector de los errores para graficar posteriormente
    xk = x0  # Se define el primer valor o el valor inicial de x0
    k = 0
    error = tol + 1  # se define un valor inicial para el error
    while k < iterMax:
        k += 1
        xkAux = xk
        xk = f_eval(xk)
        error = abs((xk-xkAux)/xk)  # se calcula el error
        er.append(sp.N(error))  # se agrega el error al vector de error
        if(error < tol):
            break
    fig, graf = plt.subplots()  # se crea la gráfica
    ejeX = np.arange(0, k, 1)  # se crea el eje X (son las iteraciones)
    graf.plot(ejeX, er)  # se grafican los datos
    plt.title('Metodo de Punto Fijo')
    plt.show()  # se muestra la gráfica
    return [xk, error, k]  # se retorna la aproximación y el error


funcion1 = puntoFijo(f, x0 , tol, iterMax)
print("Aproximación: ", funcion1[0], " Error: ", funcion1[1], " Iteraciones: ", funcion1[2] - 1)