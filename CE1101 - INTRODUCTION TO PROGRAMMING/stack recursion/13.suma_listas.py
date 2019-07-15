"""Angelo Ortiz Vega"""
#Entradas: Lista
#Salidas: Suma de Pares, Impares, Total
#Restricciones: La entrada debe ser de tipo lista
def suma (lista):
    if isinstance (lista, list):
        print("Suma Pares: ", suma_pares_aux(lista))
        print("Suma Impares: ", suma_impares_aux(lista))
        print("Suma Total: ", suma_total_aux(lista))
    else:
        return "Error: el valor ingresado no es una lista"

def suma_pares_aux(lista):
    if (lista == [ ]):
        return 0
    elif (lista[0] %2 == 0):
        return lista[0] + suma_pares_aux(lista[1:])
    else:
        return  suma_pares_aux(lista[1:])
    
def suma_impares_aux(lista):
    if (lista == [ ]):
        return 0
    elif (lista[0] %2 == 1):
        return lista[0] + suma_impares_aux(lista[1:])
    else:
        return  suma_impares_aux(lista[1:])

    
def suma_total_aux(lista):
    if (lista == [ ]):
        return 0
    else:
        return lista[0] + suma_total_aux(lista[1:])
    
