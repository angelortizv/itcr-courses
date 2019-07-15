""""Angelo Ortiz Vega"""
# Entrada: Matriz[lista de listas], Elemento.
# Restricciones: Matriz debe ser de tipo list, elemento de ser de tipo int mayor que cero.
# Salidas: Suma el Elemento para cada posicion en matriz.

def suma_matriz(elemento, matriz):
    if isinstance(matriz, list) and (matriz != [ ]) and isinstance(elemento, int):
        return matriz_aux(elemento, matriz, len(matriz), len(matriz[0]), 0, 0, 0)
    else:
        return "Error, La matriz no es una lista."

def matriz_aux(elemento, matriz, num_filas, num_columnas, fila, columna, suma):
    if (fila == num_filas):
        return suma
    elif columna == num_columnas:
        return matriz_aux(elemento, matriz, num_filas, num_columnas, fila + 1, 0, suma)
    else:
        return matriz_aux(elemento, matriz, num_filas, num_columnas, fila, columna + 1, suma + (matriz[fila][columna] + elemento))
