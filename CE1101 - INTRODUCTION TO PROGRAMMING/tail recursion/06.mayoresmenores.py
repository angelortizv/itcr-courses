""""Angelo Ortiz Vega"""
# Entrada: Lista.
# Restricciones: La entrada debe ser de tipo lista.
# Salidas: Lista con el numero mayor y el numero menor.

def principal(lista):
   if isinstance (lista, list) and (lista != []):
      print("El numero mayor de la lista es: ",mayores(lista, 0, lista[0]))
      print("El numero menor de la lista es: ",menores(lista, 0, lista[0]))
   else:
      return "Error, El valor ingresado no es una lista"

def mayores(lista, indice, resultado):
   if (indice == len(lista)):
      return resultado
   elif (lista[indice] > resultado):
      return mayores(lista, indice + 1, lista[indice])
   else:
      return mayores(lista, indice + 1, resultado)

def menores(lista, indice, resultado):
   if (indice == len(lista)):
      return resultado
   elif (lista[indice] < resultado):
      return menores(lista, indice + 1, lista[indice])
   else:
      return menores(lista, indice + 1, resultado)
