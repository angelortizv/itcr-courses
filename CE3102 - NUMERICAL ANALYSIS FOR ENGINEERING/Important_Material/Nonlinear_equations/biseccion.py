
import sympy as sp
import numpy as np
#import matplotlib.pyplot as plt

def biseccion(f, a, b, tol, iterMax):
    x = sp.Symbol('x') #se define la variable simbolica
    f1 = sp.sympify(f) #se pasa la función ingresada a una simbólica
    er = [] #se define el vector de los errores para graficar posteriormente
    k = 0 #se inicializa las iteraciones en cero
    if f1.subs(x, a)*f1.subs(x, b) < 0: #se verifica el teorema de Bolzano
        while k < iterMax:
            k += 1
            xk = (a+b)/2 #se calcula el valor siguiente de la aproximación
            if f1.subs(x, a)*f1.subs(x, xk) < 0: #se verifica el teorema de Bolzano
                #se cumple en el primer intervalo
                b = xk #se actualiza el límite superiror
            else:
                a = xk #se actualiza el limite inferior
            error = abs(f1.subs(x, xk)) #se calcula el error
            er.append(sp.N(error)) #se agrega el error al vector de errores
            if error < tol: #se verifica si el error cumpla con
                break

        #fig, graf = plt.subplots() #se crea la gráfica
        #ejeX = np.arange(1, k+1, 1) #se crea el eje X (son las iteraciones)
        #graf.plot(ejeX, er) #se grafican los datos
        #plt.show() #se muestra la gráfica

        return [xk, error] #se retorna la aproximación y el error
    else:
        xk = "NA"
        k = "NA"
        error = "NA"
        print("El intervalo seleccionado no cumple las condiciones del" 
        + "teorema de Bolzano")
        return [xk, error]



f = 'exp(x) - x -2'  #se define la función a utilizar.
a = -6 #se define el límite inferior del rango [a, b]
b = -4 #se define el límete superior del rango [a, b]
tol = 10**-5 #se define la tolerancia máxima
iterMax = 1000 #se definen las iteracioens máximas antes de detenerse
 
y = biseccion(f, a, b, tol, iterMax) #se llama a la función con sus parámetros y 
                                        #se guarda en una variable
print(y) #se muestra el resultado
