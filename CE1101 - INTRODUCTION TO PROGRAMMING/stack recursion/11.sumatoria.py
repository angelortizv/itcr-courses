""""Angelo Ortiz Vega"""
#Entradas: Numero Entero
#Salidas: Sumatoria del Numero
#Restricciones: El Numero debe de ser Entero mayor a 1

#Ejemplo de Corrida: 5: 1+2+3+4+5 = 15


def sumatoria(num):
    if isinstance(num, int) and (num > 0):
        print("La sumatoria del Numero y sus anteriores es: ", sumatoria_aux(num))
    else:
        return -1

def sumatoria_aux(num):
    #print(num, end="+")
    if (num == 0):
        #print(num, end="=")
        return 0
    else:
        return num + sumatoria_aux(num - 1)






