"""Angelo Ortiz Vega"""
#Entrada: Una Lista de numeros.
#Salida: Lista que contiene solo numeros primos.
#Restricciones: La entrada debe ser ded tipo lista.

def validar(lista):
    if isinstance(lista, list):
        return recorrer(lista) 
    else:
        return "Error: La entrada no es de tipo lista."

#Recorre la lista, añade si es primo
def recorrer(lista):
    if (lista == []):
        return []
    elif primos_aux(lista[0], 2):
        return [lista[0]] + recorrer(lista[1:])
    else:
        return recorrer(lista[1:])

#Determina si un numero es Primo, True: Numero Primo v False: Numero No Primo
def primos_aux(num, contador):
    if (num == 0 or num == 1 or num == 2 or num == 3):
        return True
    elif(contador == num):
        return True
    elif (num % contador == 0):
        return False
    else:
        return primos_aux(num, contador+1)
    
print(validar([1,2,3,4,7,9,97,43]))