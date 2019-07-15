""""Angelo Ortiz Vega"""
# Entrada: Numero Entero.
# Restricciones: Debe ser Entero mayor a Cero.
# Salidas: Lista con los que no son Divisibles y los que son divisibles.

def divisibles(num):
   if isinstance(num, int) and (num > 0):
      return [divisibles_aux(num, 0, 0), divisibles_aux2(num, 0, 0)]
   else:
      return -1

#Elimina Numeros Divisibles entre tres.
def divisibles_aux(num, resultado, exponente):
   if (num == 0):
      return resultado
   elif (((num%10)%3) == 0) and ((num%10) != 0):
      return divisibles_aux(num//10, resultado, exponente)
   else:
      return divisibles_aux(num//10,  (num%10)*(10**(exponente)) + resultado, exponente + 1)

#Concatena los Numeros Divisibles entre tres.
def divisibles_aux2(num, resultado, exponente):
   if (num == 0):
      return resultado
   elif (((num%10)%3) == 0):
      return divisibles_aux2(num//10,  (num%10)*(10**(exponente)) + resultado, exponente + 1)
   else:
      return divisibles_aux2(num//10, resultado, exponente)
