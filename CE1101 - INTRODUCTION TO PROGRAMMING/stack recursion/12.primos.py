""""Angelo Ortiz Vega"""
#Entradas: Numero Entero
#Salidas: Primo, Compuesto o Especial
#Restricciones:

def validar(num):
    if isinstance(num, int) and (num > 1):
        return primos(num)
    elif (num == 0) or (num == 1):
        return "Numero Especial"
    else:
        return -1

def primos(num):
    if (num > 0):
        return "Numero Primo"
    else:
        return ((num / primos(num - 1)) == 0)
    elif():


print(validar(7))