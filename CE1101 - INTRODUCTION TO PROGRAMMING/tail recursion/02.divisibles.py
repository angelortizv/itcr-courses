""""Angelo Ortiz Vega"""
# Entrada: Numero.
# Restricciones: El numero a la entrada debe ser de tipo entero.
# Salidas: Elimina los digitos divisibles entre tres, dos, uno.

def divisibles(num):
    if isinstance(num, int):
        return divisibles3_aux(num, 0, 0), divisibles2_aux(num, 0, 0)
    else:
        return -1

def divisibles3_aux(num, resultado, potencia):
    if(num == 0):
        return resultado
    elif((num%10)%3 == 0):
        return divisibles3_aux(num//10, resultado, potencia)
    else:
        return divisibles3_aux(num//10, (num%10 * 10**potencia) + resultado, potencia + 1)

def divisibles2_aux(num, resultado, potencia):
    if(num == 0):
        return resultado
    elif((num%10)%2 == 0):
        return divisibles2_aux(num//10, resultado, potencia)
    else:
        return divisibles2_aux(num//10, (num%10 * 10**potencia) + resultado, potencia + 1)


