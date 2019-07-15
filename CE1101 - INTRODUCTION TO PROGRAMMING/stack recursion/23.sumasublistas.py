"""Angelo Ortiz Vega"""
#Entrada: Una lista.
#Salida: Suma de listas y sublistas.
#Restricciones: La entrada debe ser de tipo lista.

def suma(lista):
    if isinstance(lista, list):
        return suma_aux(lista)
    else:
        return "Error: La entrada no es una lista."

def suma_aux(lista):
    if (lista == []):
        return 0
    elif isinstance(lista[0], list):
        return  suma_aux(lista[0]) + suma_aux(lista[1:])
    else:
        return lista[0] + suma_aux(lista[1:])


