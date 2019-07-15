"""Suma de Digitos de un numero"""        
#Entrada: Un numero entero
#Salida: Suma de los digitos
#Restricciones: Numero Entero Positivo mayor a cero

def suma(num):
    if isinstance(num, int) and (num > 0):
        return suma_aux(abs(num))
    else:
        return -1

def suma_aux(num):
    if(num == 0):
        return 0
    else:
        return num%10 + suma_aux(num//10)
