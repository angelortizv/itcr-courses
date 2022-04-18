import sympy as sp 
import numpy as np
import matplotlib.pyplot as plt
import math

# Se definen las entradas que en este caso
# tol = es la entrada correspondiente a la tolerancia que tendra el sistema
# f = es la funcion definida en un string
# x0 = es el valor inicial en 0
# iterMax = la cantidad de iteraciones máxima que el sistema realizara 
# La salida esperada de este sistema 
# xk = El punto donde f(xk) = 0 
# e = El valor del error
# Ademas de la funcion ploteada de la cantidad de iteración y el valor de error
def muller(f,x0,x1,x2,iterMax,tol):
    x3 = 0 # valor de la tercera solución del sistema
    error = 0 # Variable para el del error
    er = [] # Lista donde se almacenaran lel calculo de los errores
    k = 0 # variable para el valor de las iteraciones
    x = sp.Symbol('x') # Define del texto x a simbólico
    f1 = sp.sympify(f) # Método Symbol que convierte el texto a simbólico
    print('iniciando while')
    while iterMax > k: # El sistema se ejecuta hasta que cumpla con su maxima iteración
        c = sp.N(f1.subs(x,x2)) # Calculo de la variable c con el calculo de la funcion en x3
        b =  ((x0-x2)**2*(sp.N(f1.subs(x,x1)) - sp.N(f1.subs(x,x2))) - (x1-x2)**2*(sp.N(f1.subs(x,x0)) - sp.N(f1.subs(x,x2)))) / ((x0-x1)*(x0-x2)*(x1-x2)) # Calcula y almacena el valor de b
        a = ( (x1-x2)*(sp.N(f1.subs(x,x0)) - sp.N(f1.subs(x,x2))) - (x0-x2)*(sp.N(f1.subs(x,x1)) - sp.N(f1.subs(x,x2)))) / ((x0-x1)*(x0-x2)*(x1-x2)) # Calcula y almacena el valor de a
        print(a,b,c)

        E = b + np.sign(b)*math.sqrt(b**2 - 4*a*c) # Calculo de la raíz con factor positivo
        EN = b - np.sign(b)*math.sqrt(b**2 - 4*a*c) # Calculo de la raíz con factor negativo
        if abs(EN)> abs(E): # Calculo de si la raíz negativa es mayor a la positiva y cambiarla
            E = EN
        x3 = x2 - 2*c/E # Calculo de un tercer punto que se aproxima a x2
        f3 = sp.N(f1.subs(x,x3)) # Evaluar la funcion en ese punto
        x0 = x1 # Recalculo de x0
        x1 = x2 # Recalculo de x1
        x2 = x3 # Recalculo de x2
        if(abs(sp.N(f1.subs(x,x3))) < tol): #Calculo de error y parada en caso de que sea menor a la tolerancia permitida
            break
        else:
            error = abs(sp.N(f1.subs(x,x3))) # Calculo del error 
            print(error)
            er.append(error) #Agregar a la lista del errores
            k=k+1
        
    plt.rcParams.update({'font.size':14})
    ejex = np.arange(1, k+1)
    print(ejex)
    print(er)
    plt.plot(ejex,er, marker='o',color='red')
    plt.xlabel('Iteraciones ($k$)')
    plt.ylabel('$|f(x_k)|$')
    plt.title('Metodo de Muller Iteraciones vrs Error)')
    plt.show()
    return x3 # return de la solución mas cercana

f = 'sin(x) -x/2'
x0 = 2
x1 = 2.2
x2 = 1.8
tol = 10^-6
iterMax = 4

y = muller(f,x0,x1,x2,iterMax,tol)
print(y)
