""""Angelo Ortiz Vega"""
# Entrada: Lista.
# Restricciones: Debe ser de tipo lista diferente a vacio.
# Salidas: Lista con los que pares.

# Indices: Nueva Lista con los elementos pares de la Lista.
def paresindice(lista):
   if isinstance(lista, list) and (lista != []):
      return pares_aux(lista, [], 0 )
   else:
      return -1

def pares_aux(lista, resultado, indice):
   if indice == len(lista):
      return resultado
   elif lista[indice]%2 == 0:
      return pares_aux(lista, [lista[indice]] + resultado, indice + 1)
   else:
      return pares_aux(lista, resultado, indice + 1)

# Slicing: Nueva Lista con los elementos pares de la Lista.
def paresslicing(lista):
   if isinstance(lista, list) and (lista != []):
      return pares_aux2(lista, [])
   else:
      return -1

def pares_aux2(lista, resultado):
   if (lista == []):
      return resultado
   elif lista[0]%2 == 0:
      return pares_aux2(lista[1:], [lista[0]] + resultado)
   else:
      return pares_aux2(lista[1:], resultado)


