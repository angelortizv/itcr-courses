""""Angelo Ortiz Vega"""
#Entradas: Numero Entero
#Salidas:   Cantidad de Numeros impapares en un Numero
#Restricciones: El Numero debe de ser Entero

def impares(num):
    if isinstance(num, int) and (num > 0):
        return impares_aux(num)
    else:
        return -1

def  impares_aux(num):
    if (num == 0):
        return 0
    elif ((num%10)%2 == 1):
        return 1 + impares_aux(num//10)
    else:
        return impares_aux(num//10)

print(impares(123456222222))