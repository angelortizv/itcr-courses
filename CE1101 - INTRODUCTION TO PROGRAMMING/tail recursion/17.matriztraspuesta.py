"""Angelo Ortiz Vega"""
# Entrada: Matriz de n x m.
# Restricciones: La Matriz debe ser de tipo lista.
# Salidas: La Traspuesta de la Matriz

def traspuesta(matriz):
    if isinstance(matriz, list)and (matriz != [ ]):
        return traspuesta_aux(matriz, 0, 0, [ ], [ ])
    else:
        return "Error: El valor ingresado no es de tipo lista."

def traspuesta_aux(matriz, fila, columna, filaMatriz, traspuesta):
    if columna == len(matriz[0]):
        return traspuesta
    elif fila == len(matriz):
        return traspuesta_aux(matriz, 0, columna + 1, [], traspuesta + [filaMatriz])
    else:
        return traspuesta_aux(matriz, fila + 1, columna, filaMatriz + [matriz[fila][columna]], traspuesta)
