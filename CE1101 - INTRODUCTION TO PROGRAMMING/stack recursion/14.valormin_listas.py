""""Angelo Ortiz Vega"""
#Entradas: Lista
#Salidas: El valor minimo de la lista
#Restricciones: La entrada debe ser de tipo lista

def minimo(lista):
    if isinstance(lista, list) and (lista != []):
        return minimo_aux(lista)
    else:
        return "Error: El valor ingresado no es una lista"

def minimo_aux(lista):
    if (lista[1:] == []):
   #if len(lista == 1):
        return lista[0]
    elif (lista[0] <= lista[1]):
        return minimo_aux([lista[0]] + lista[2:])
    else:
        return minimo_aux(lista[1:])

print(minimo([5,4,3,6,12,243,4]))

