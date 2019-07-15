""""Angelo Ortiz Vega"""
# Entrada: Matriz[lista de listas]
# Restricciones: Matriz debe ser de tipo list.
# Salidas: Suma de los elementos dentro de la matriz, promedio de la suma.

def suma_matriz(matriz):
    if isinstance(matriz, list) and (matriz != [ ]):
        return matriz_aux(matriz, len(matriz), len(matriz[0]), 0, 0, 0, 0)
    else:
        return "Error, La matriz no es una lista."

def matriz_aux(matriz, num_filas, num_columnas, fila, columna, suma, contador):
    if (fila == num_filas):
        return suma, suma//contador
    elif columna == num_columnas:
        return matriz_aux(matriz, num_filas, num_columnas, fila + 1, 0, suma, contador )
    else:
        return matriz_aux(matriz, num_filas, num_columnas, fila, columna + 1, suma + (matriz[fila][columna]), contador + 1)
