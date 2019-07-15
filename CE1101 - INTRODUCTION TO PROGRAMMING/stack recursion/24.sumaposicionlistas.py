"""Angelo Ortiz Vega"""
#Entrada: Una lista de numeros longitud n.
#Salida: Suma de los elementos en la lista.
#Restricciones: La entrada debe ser de tipo lista.

def suma(lista):
    if isinstance(lista, list):
        return suma_aux(lista, 1)
    else:
        return "Error: El objeto ingresado no es una lista."

def suma_aux(lista, contador):
    if (lista == []):
        return 0
    elif isinstance(lista[0], list):
        return suma_aux(lista[0] + lista[1:], contador)
    else:
        return (lista[0] ** contador) + suma_aux(lista[1:], contador + 1)

"""Si le pasamos (0) como parametro:
    return (lista[0]** (contador + 1)) + suma_aux(lista[1:], contador + 1)"""
