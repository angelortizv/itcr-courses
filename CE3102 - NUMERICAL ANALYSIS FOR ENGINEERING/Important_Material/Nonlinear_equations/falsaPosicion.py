import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


f = 'log(x) - exp(-x) - cos(x)'  # se define la función a utilizar.
a = 1  # se define el límite inferior del rango [a, b]
b = 2 # se define el límite superior del rang0 [a, b]
K = 0 # Valor inicial de la iteraciones
tolerancia = 10 ** -5  # se define la tolerancia máxima
iterMax = 500  # se definen las iteracioens máximas antes de detenerse


def falsaPosicion(f, a , b,  tolerancia , iterMax):
    x = sp.Symbol('x') # Asi se define la varible simbolica
    f_simbolica = sp.sympify(f) # Se define de la funcion funcion
    f_eval = sp.lambdify(x , f_simbolica) # La funcion inicial se pasa a a una funcion evaluable
    er = []  # se define el vector de los errores para graficar posteriormente
    xk = a  # Se define el primer valor o el valor inicial de
    xk_1 = b
    k = 0 
    if( f_eval(a) * f_eval(b) < 0): # Se verficia el teorema de bolzano
        n = f(xk_1) * (xk_1 - xk)#numerador formula de la secante
        d = f(xk_1) - f(xk) #denominador de la formula de la secante
        xk = xk_1
        xk_1 = xk_1 - n/d
        while(k < iterMax):
            k = k + 1
            if(abs(d) > tolerancia):
                if(f_eval(a)*f_eval(b) < 0):
                    b = xk_1
                    n = f(xk_1) * (xk_1 - a) #numerador formula de la secante
                    d = f(xk_1) - f(a) #denominador de la formula de la secante
                    xk = xk_1  #se actualiza el valor de la iteración anterior
                    xk_1 = xk_1 - n/d #se calcula el nuevo valor de la aproximación
                    error = abs((xk_1 - xk)/xk_1) #se calcula el error
                    er.append(sp.N(error))  # se agrega el error al vector de error
                    if(error < tolerancia): # se verifica que el error cumpla con la tolerancia
                        break
            elif(f_eval(a) * f_eval(b) < 0):
                a = xk_1  # Se cumple el segundo intervalo
                n = f(xk_1) * (xk_1 - b); #numerador formula de la secante
                d = f(xk_1) - f(b); #denominador de la formula de la secante
                xk = xk_1; # se actualiza el valor de la iteración anterior
                xk_1 = xk_1 - n/d; # se calcula el nuevo valor de la aproximación
                error = abs((xk_1 - xk)/xk_1); # se calcula el error
                er.append(sp.N(error))  # se agrega el error al vector de error
                if(error < tolerancia): # se verifica que el error cumpla con la tolerancia
                    break
            else: 
                break
    else:
        print("La funcion no es valida no cumple con los parametros vistos en clase")
        return 0
    fig, graf = plt.subplots()  # se crea la gráfica
    ejeX = np.arange(0, k, 1)  # se crea el eje X (son las iteraciones)
    graf.plot(ejeX, er)  # se grafican los datos
    plt.title('Metodo de Punto Fijo')
    plt.show()  # se muestra la gráfica
    return [xk, error, k]  # se retorna la aproximación y el error

funcion1 = falsaPosicion(f, a , b, tolerancia, iterMax)
print("Aproximación: ", funcion1[0], " Error: ", funcion1[1], " Iteraciones: ", funcion1[2] - 1)

def falsaPosicionExamen(f, a, b, tol, iterMax):
    x = sp.Symbol('x')
    f1 = sp.sympify(f)
    print(f1)
    er = []
    k = 0
    xk = a
    xk_1 = b

    if f1.subs(x, a)*f1.subs(x, b) < 0: #se verifica el teorema de Bolzano
        n = sp.N(f1.subs(x, xk_1)) * (xk_1 - xk)
        d = sp.N(f1.subs(x, xk_1)) - sp.N(f1.subs(x, xk))
        xk = xk_1
        xk_1 = xk_1 - n/d #se usa la formula de la secante

        while k < iterMax:
            k += 1
            if abs(d) > tol:
                if f1.subs(x, a)*f1.subs(x, xk_1) < 0: #se verifica el teorema de Bolzano
                    #se cumple en el primer intervalo
                    b = xk_1
                    n = sp.N(f1.subs(x, xk_1)) * (xk_1 - a)
                    d = sp.N(f1.subs(x, xk_1)) - sp.N(f1.subs(x, a))
                    xk = xk_1
                    xk_1 = xk_1 - n/d #se usa la formula de la secante
                    
                    error = abs((xk_1 - xk)/xk_1)
                    er.append(sp.N(error))
                elif f1.subs(x, b)*f1.subs(x, xk_1) < 0:
                    a = xk_1
                    n = sp.N(f1.subs(x, xk_1)) * (xk_1 - b)
                    d = sp.N(f1.subs(x, xk_1)) - sp.N(f1.subs(x, b))
                    xk = xk_1
                    xk_1 = xk_1 - n/d #se usa la formula de la secante
                    
                    error = abs((xk_1 - xk)/xk_1)
                    er.append(sp.N(error))
                else:
                    break
            if error < tol:
                break

        fig, graf = plt.subplots()
        ejeX = np.arange(1, k+1, 1)
        graf.plot(ejeX, er)
        plt.show()

        return [xk_1, k, error]
    else:
        xk = "NA"
        k = "NA"
        error = "NA"
        print("El intervalo seleccionado no cumple las condiciones del teorema de Bolzano")
        return [xk, k, error]

f = 'log(x)- exp(-x) - cos(x)'
a = 1
b = 2
tol = 10**-5
iterMax = 1000

y = falsaPosicionExamen(f, a, b, tol, iterMax)
print(y)
