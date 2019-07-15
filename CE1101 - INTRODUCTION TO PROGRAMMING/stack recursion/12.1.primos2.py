""""Angelo Ortiz Vega"""
#Entradas: Numero Entero
#Salidas: Primo, Compuesto o Especial
#Restricciones:

def validar(num):
    if isinstance(num, int) and (num > 1):
        return primos(num, num-1)
    elif (num == 0) or (num == 1):
        return "Especial"
    else:
        return -1

def primos(num, divisor):
    if (divisor == 1):
        return "Primo"
    elif (num%divisor == 0):
        return "Compuesto"
    else:
        return primos(num, divisor-1)

print("El numero es:",validar(7))
print("El numero es:",validar(9))
print("El numero es:",validar(0))
