""""Angelo Ortiz Vega"""
#Entradas: Lista
#Salidas: El valor maximo de la lista
#Restricciones: La entrada debe ser de tipo lista

def maximo(lista):
    if isinstance(lista, list) and (lista != []):
        return maximo_aux(lista)
    else:
        return -1

def maximo_aux(lista):
    if (lista[1:] == [ ]):
        return lista[0]
    elif (lista[0] >= lista[1]):
        return maximo_aux([lista[0]] + lista[2:])
    else:
        return maximo_aux(lista[1:])

print(maximo([1,245,26,3,4,5,75,100,150,200,243,244]))
