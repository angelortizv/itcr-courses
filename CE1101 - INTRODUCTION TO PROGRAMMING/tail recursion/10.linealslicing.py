""""Angelo Ortiz Vega"""
# Entrada: Numero y Lista.
# Restricciones: El Numero debe ser Entero y Lista debe ser de tipo list.
# Salidas: Bool, True = Numero esta en la lista. False: en caso contrario.

def busqueda(num, lista):
   if isinstance(num, int) and (lista, list):
      return busqueda_aux(num, lista)
   else:
      return -1

def busqueda_aux(num, lista):
   if (lista == []):
      return False
   elif (lista[0] == num):
      return True
   else:
      return busqueda_aux(num, lista[1:])
