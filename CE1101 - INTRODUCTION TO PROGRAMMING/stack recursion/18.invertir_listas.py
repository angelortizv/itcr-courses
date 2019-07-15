"""Angelo Ortiz Vega"""
#Entrada: Una Lista de numeros.
#Salida: Lista con orden invertido.
#Restricciones: La entrada debe ser  tipo lista diferente de vacio.

def invertir(lista):
    if isinstance(lista, list) and (lista != []):
        return invertir_aux(lista)
    else:
        return -1

def invertir_aux(lista):
    if (lista == []):
        return []
    else:
        #return [lista[-1]] + invertir_aux(lista[:-1])
        #return invertir_aux(lista[1:]) + [lista[0]]
        return lista[-1:] + invertir_aux(lista[:-1])

print(invertir([1,2,3,4,5]))
print(invertir([5,4,3,2,1]))
print(invertir([4,8,9,3,11]))