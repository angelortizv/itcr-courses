"""Angelo Ortiz Vega"""
# Entrada: Numero.
# Restricciones: El numero a la entrada debe ser de tipo entero.
# Salida: El largo del numero.

def largo(num):
    if isinstance(num, int):
        return largo_aux(num, 0)
    else:
        return -1

def largo_aux(num, resultado):
    if (num == 0):
        return resultado
    else:
        return largo_aux(num//10, resultado + 1)


