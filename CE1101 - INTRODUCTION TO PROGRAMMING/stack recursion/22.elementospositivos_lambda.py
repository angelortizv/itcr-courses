"""Angelo Ortiz Vega"""
#Entrada: Una lista.
#Salida: Determinar si todos los elementos de la lista son positivos.
#Restricciones: La entrada debe ser de tipo lista.

def compara(lista):
    if isinstance(lista, list):
        mayor = lambda lista : lista[0] >= 0
        return compara_aux(lista, mayor)
    else:
        return -1

def compara_aux(lista, condicion):
    if (lista == []):
        return True
    elif condicion([lista[0]]):
        return compara_aux(lista[1:], condicion)
    else:
        return False
