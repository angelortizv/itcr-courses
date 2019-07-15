""""Angelo Ortiz Vega"""
# Entrada: Lista.
# Restricciones: La entrada debe ser de tipo lista.
# Salidas: Lista con el numero mayor y el numero menor.

def principal(lista):
   if isinstance (lista, list) and (lista != []):
      print("El numero mayor de la lista es: ",mayores(lista, lista[0]))
      print("El numero menor de la lista es: ",menores(lista, lista[0]))
   else:
      return "Error, El valor ingresado no es una lista"

def mayores(lista, resultado):
   if (lista == []):
      return resultado
   elif (lista[0] > resultado):
      return mayores(lista[1:], lista[0])
   else:
      return mayores(lista[1:], resultado)
   
def menores(lista, resultado):
   if (lista == []):
      return resultado
   elif (lista[0] < resultado):
      return menores(lista[1:], lista[0])
   else:
      return menores(lista[1:], resultado)
