""""Angelo Ortiz Vega"""
#Algoritmo de Busqueda Binaria
# Entrada: Numero y Lista.
# Restricciones: El Numero debe ser Entero y Lista debe ser de tipo list.
# Salidas: Bool, True = Numero esta en la lista. False: en caso contrario.

def binaria(num, lista):
   if isinstance(num, int) and  (lista, list):
      return binaria_aux(num, lista, len(lista)//2)
   else:
      return -1

def binaria_aux(num, lista, mitad):
   if (lista == []):
      return False
   elif (num == lista[mitad]):
      return True
   elif (num > lista[mitad]):
      return binaria_aux(num, lista[(mitad+1):], mitad//2)
   elif (num < lista[mitad]):
      return binaria_aux(num, lista[:(mitad+1)], mitad//2)
