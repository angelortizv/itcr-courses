""""Angelo Ortiz Vega"""
#Algoritmo para Ordenamiento de Listas.
# Entrada:Lista.
# Restricciones: Lista debe ser de tipo list.
# Salidas: Lista con Orden Ascendente.

def ordenar(lista):
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
   
