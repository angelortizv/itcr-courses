"""Angelo Ortiz Vega"""
#Entrada: Un numero.
#Salida: Los numeros pares y los numeros impares.
#Restricciones: El numero debe ser de tipo entero.

def compara(num):
    if isinstance(num, int):
        pares = lambda digito : digito % 2 == 0
        impares = lambda digito : digito % 2 == 1
        return compara_aux(num, pares), compara_aux(num, impares)
    else:
        return -1

def compara_aux(num, condicion):
    if (num == 0):
        return 0
    elif condicion(num % 10):
        return 1 + compara_aux(num//10, condicion)
    else:
        return compara_aux(num//10, condicion)
