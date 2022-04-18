from mpmath.functions.functions import re
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

f = 'exp(x) + x-2'  # se define la función a utilizar.
x0 = 5  # se define el límite inferior del rango [a, b]
tolerancia = 10 ** -5  # se define la tolerancia máxima
iterMax = 500  # se definen las iteracioens máximas antes de detenerse

def NewtonRaphson(f, x0 , tolerancia , iterMax):
    x = sp.Symbol('x') # Asi se define la varible simbolica
    f_simbolica = sp.sympify(f) # Se define de la funcion funcion
    f_derivda = f_simbolica.diff(x) # Se calcula la primera deriva

    f_derivda = sp.lambdify(x , f_derivda) # f_derivada se convierte en una funcion evaluable
    f_eval = sp.lambdify(x , f_simbolica) # La funcion inicial se pasa a a una funcion evaluable
    er = []  # se define el vector de los errores para graficar posteriormente
    xk = x0  # Se define el primer valor o el valor inicial de x0
    error = tolerancia + 1  # se define un valor inicial para el error
    k = 0  # se inicializa las iteraciones en cero
    while k < iterMax:
        k += 1  # Se suma el valor de la iteracion
        if(f_derivda(xk) == 0):
            print('Funcion contiene punto critico')
            return 0
        xk = xk - f_eval(xk) / f_derivda(xk)  # se calcula una nueva interacion
        error = abs(f_eval(xk))  # se calcula el error
        er.append(sp.N(error))  # se agrega el error al vector de error
        if(error < tolerancia):
            break
    fig, graf = plt.subplots()  # se crea la gráfica
    ejeX = np.arange(0, k, 1)  # se crea el eje X (son las iteraciones)
    graf.plot(ejeX, er)  # se grafican los datos
    plt.title('Metodo de Newton')
    plt.show()  # se muestra la gráfica
    return [xk, error, k]  # se retorna la aproximación y el error


funcion1 = NewtonRaphson(f, x0, tolerancia , iterMax)
print("Aproximación: ", funcion1[0], " Error: ", funcion1[1], " Iteraciones: ", funcion1[2] - 1)