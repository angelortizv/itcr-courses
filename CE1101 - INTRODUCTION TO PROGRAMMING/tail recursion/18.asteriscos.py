"""Angelo Ortiz Vega"""
# Entrada: n
# Restricciones: n debe ser entero.
# Salidas: Rellena asteriscos en primera y ultima fila, primera y ultima columna.

def ceros(n):
    if isinstance(n, int) and (n > 0):
        return ceros_aux(n, [], [], 0, 0)
    else:
        return "Error"

def ceros_aux(n, matriz, fila, indiceFila, indiceColumna):
    if (indiceFila == n):
        return matriz
    elif (indiceColumna == n):
        return ceros_aux(n, matriz + [fila], [], indiceFila + 1, 0)
    else:
        return ceros_aux(n, matriz, fila + [0], indiceFila, indiceColumna + 1)


def asteriscos(n):
    if isinstance(n, int) and (n > 0):
        return asteriscos_aux(n, [], [], 0, 0)
    else:
        return "Error"
  
def asteriscos_aux(n, matriz, fila, indiceFila, indiceColumna):
    if (indiceFila == n):
        return matriz
    elif (indiceColumna == n):
        return asteriscos_aux(n, matriz + [fila], [], indiceFila + 1, 0)
    elif (indiceFila == 0) or (indiceFila == (n-1)):
        return asteriscos_aux(n, matriz, fila + ['*'], indiceFila, indiceColumna + 1)
    elif  (indiceColumna == 0) or (indiceColumna == (n-1)):
        return asteriscos_aux(n, matriz, fila + ['*'], indiceFila, indiceColumna + 1)
    else:
        return asteriscos_aux(n, matriz, fila + [0], indiceFila, indiceColumna + 1)
