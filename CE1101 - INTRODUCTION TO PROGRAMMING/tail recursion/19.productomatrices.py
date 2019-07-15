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
