#BINARYSEARCH
def binary(num, lista):
   if isinstance(num, int) and  (lista, list):
      return binary_aux(num, lista, len(lista)//2)
   else:
      return -1

def binary_aux(num, lista, half):
   if (lista == []):
      return False
   elif (num == lista[half]):
      return True
   elif (num > lista[half]):
      return binary_aux(num, lista[(half+1):], half//2)
   elif (num < lista[half]):
      return binary_aux(num, lista[:(half+1)], half//2)

#SORT LIST
def sort(lista):
   if isinstance(lista, list) and (lista != []):
      return recorrido_aux(lista, 0, 0)
   else:
      return -1

def recorrido_aux(lista, indice, recorrido):
   if (recorrido == len(lista)-1):
      return lista
   elif (indice == len(lista)-1):
      return recorrido_aux(lista, 0, recorrido + 1)
   elif (lista[indice] > lista[indice + 1]):
         lista[indice], lista[indice + 1] = lista[indice + 1], lista[indice]
   return recorrido_aux(lista, indice + 1, recorrido)

#SUM ELEMENTS IN MATRIZ
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

#SUM DIAGONALS IN MATRIZ
def diagonal(matriz):
   if isinstance(matriz, list) and (len(matriz) == len(matriz[0])):
      return diagonal_aux(matriz, len(matriz), len(matriz[0]), 0, 0, 0)
   else:
      return -1

def diagonal_aux(matriz, numf, numc, fila, columna, suma):
   if (fila == numf):
      return suma
   else:
      return diagonal_aux(matriz, numf, numc, fila + 1, columna + 1, suma + matriz[fila][columna])

#SUM ANTIDIAGONALS IN MATRIZ
def antidiagonal(matriz):
   if isinstance(matriz, list) and (len(matriz) == len(matriz[0])):
      return antidiagonal_aux(matriz, len(matriz), 0, 0)
   else:
      return -1

def antidiagonal_aux(matriz, largo, fila, suma):
   if (fila == largo):
      return suma
   else:
      return antidiagonal_aux(matriz, largo, fila + 1, suma + matriz[fila][-(fila + 1)])


#DETERMINES TRANSPUESTA OF A MATRIZ
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

#MATRIX PRODUCT
def productoMatrices(matrizA,matrizB):
    return producto(matrizA,matrizB,0,0,0,0,[])

def producto(matrizA,matrizB,indice1,indice2,indice3,operacion,nuevaMatriz):
    if len(matrizA) == indice1:
        return nuevaMatriz

    elif len(matrizB) == indice2 and len(matrizB[0])-1 == indice3:
        return producto(matrizA,matrizB,indice1+1,0,0,0,nuevaMatriz + [[operacion]])

    elif len(matrizB) == indice2:
        return producto(matrizA,matrizB,indice1,0,indice3+1,0,nuevaMatriz + [[operacion]])

    else:
        return producto(matrizA,matrizB,indice1,indice2+1,indice3,
                        operacion + calculo(matrizA,matrizB,indice1,indice2,indice3,operacion),
                        nuevaMatriz)

def calculo(matrizA,matrizB,indice1,indice2,indice3,operacion):
    return matrizA[indice1][indice2]*matrizB[indice2][indice3]


#FILL WITH ASTERISCOS
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


