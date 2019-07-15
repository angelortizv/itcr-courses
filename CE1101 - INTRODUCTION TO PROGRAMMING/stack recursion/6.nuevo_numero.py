""""Angelo Ortiz Vega"""
#Entradas: Numero Entero
#Salidas:   Nuevo Numero con los Numeros Pares, y Numeros Impares
#Restricciones: El Numero debe de ser Entero

def nuevo_numero(num):
    if isinstance(num, int) and (num > 0):
        return [nuevo_pares(abs(num), 0), nuevo_impares(num, 0)]
    else:
        return -1

def nuevo_pares(num, potencia):
    if (num == 0):
        return 0
    elif ((num%10)%2 == 0):
        return ((num % 10)*(10 ** potencia) + nuevo_pares(num//10, potencia + 1))
    else:
        return nuevo_pares(num//10, potencia)

def nuevo_impares(num, potencia):
    if (num == 0):
        return 0
    elif ((num%10)%2 == 1):
        return ((num % 10)*(10 ** potencia) + nuevo_impares(num//10, potencia + 1))
    else:
        return nuevo_impares(num//10, potencia)

print(nuevo_numero(123456))