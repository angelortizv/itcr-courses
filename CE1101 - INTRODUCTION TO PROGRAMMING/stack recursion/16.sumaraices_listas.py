""""Angelo Ortiz Vega"""
#Entradas: Lista
#Salidas: Sumatoria de la raiz de cada Elemento
#Restricciones: La entrada debe ser de tipo lista

import math as m

def suma_raices(lista):
    if isinstance(lista, list) and (lista != [ ]):
        return suma_raices_aux(lista)
    else:
        return "Error: El valor ingresado no es una lista"


def suma_raices_aux(lista):
    if (lista == []):
        return 0
    else:
        return m.sqrt(lista[0]) + suma_raices_aux(lista[1:])

print(suma_raices([5,7,8,1,2]))