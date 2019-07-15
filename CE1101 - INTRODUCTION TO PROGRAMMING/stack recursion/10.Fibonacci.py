""""Angelo Ortiz Vega"""
#Entradas: Numero Entero
#Salidas: Sucesion de Fibonacci del Presente Numero
#Restricciones: El Numero debe de ser Entero

import time

def fihonacci(num):
    if isinstance(num, int) and (num > 0):
        return fibonacci_aux(num)
    else:
        return -1

def fibonacci_aux(num):
    print(num, end=",")
    #time.sleep(2)
    if (num <= 2):
        return num
    else:
        return fibonacci_aux(num - 1) + fibonacci_aux(num - 2)

print(fibonacci_aux(6))