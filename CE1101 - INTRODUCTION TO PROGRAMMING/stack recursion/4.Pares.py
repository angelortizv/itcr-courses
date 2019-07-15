""""Angelo Ortiz Vega"""
#Entradas: Numero Entero
#Salidas:   Cantidad de Numeros pares en un Numero
#Restricciones: El Numero debe de ser Entero

def pares(num):
    if isinstance(num, int) and (num > 0):
        return pares_aux(num)
    else:
        return -1

def  pares_aux(num):
    if (num == 0):
        return 0
    elif ((num%10)%2 == 0):
        return 1 + pares_aux(num//10)
    else:
        return pares_aux(num//10)

print(pares(123456222222))