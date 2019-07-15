"""Angelo Ortiz Vega"""
#Entrada: Una lista.
#Salida: Determinar si posee al menos un cero Arroja True o False.
#Restricciones: La entrada debe ser de tipo lista.

def compara(lista):
    if isinstance(lista, list):
        cero = lambda digito : digito  == 0
        return compara_aux(lista, cero)
    else:
        return -1

def compara_aux(lista, condicion):
    if (lista == []):
        return False
    elif condicion(lista[0]):
        return True
    else:
        return compara_aux(lista[1:], condicion)
