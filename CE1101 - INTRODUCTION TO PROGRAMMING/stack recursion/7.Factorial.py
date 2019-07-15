""""Angelo Ortiz Vega"""
#Entradas: Numero Entero
#Salidas: El Favtorial de un Numero Entero
#Restricciones: El Numero debe de ser Entero

def factorial(num):
    if isinstance(num, int) and (num > 0):
        return factorial_aux(num)
    else:
        return -1

def factorial_aux(num):
    if (num == 0):
        return 0
    else:
        return num * (num-1)

print(factorial(5))