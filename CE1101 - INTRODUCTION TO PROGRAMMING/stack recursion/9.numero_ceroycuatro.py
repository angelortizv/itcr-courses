""""Angelo Ortiz Vega"""
#Entradas: Numero Entero
#Salidas: Booleano
#Restricciones: El Numero debe de ser Entero
#False: el numero posee mas de 4 digitos, True: el numero posee menos de 4 digitos

def limites(num):
    if isinstance(num, int) and (num > 0):
        return limites_aux(num)
    else:
        return -1

def limites_aux(num):
    if (num == 0):
        return True
    elif (num%10 <= 4) and (num%10 >= 0):
        return limites_aux(num//10)
    else:
        return False

print(limites(12341231231231235))