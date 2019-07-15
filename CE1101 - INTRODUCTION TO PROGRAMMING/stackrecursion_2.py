#FIBONACCI FUNCTION
def fihonacci(num):
    if isinstance(num, int) and (num > 0):
        return fibonacci_aux(num)
    else:
        return -1

def fibonacci_aux(num):
    print(num, end=",")
    if (num <= 2):
        return num
    else:
        return fibonacci_aux(num - 1) + fibonacci_aux(num - 2)

#SUMMARY OF NUMBER
def summary(num):
    if isinstance(num, int) and (num > 0):
        print("La sumatoria del Numero y sus anteriores es: ", summary_aux(num))
    else:
        return -1

def summary_aux(num):
    #print(num, end="+")
    if (num == 0):
        #print(num, end="=")
        return 0
    else:
        return num + summary_aux(num - 1)

#DETERMINES IF A NUMBER IS PRIME
def validate_primes(num):
    if isinstance(num, int) and (num > 1):
        return validate_primes_aux(num)
    elif (num == 0) or (num == 1):
        return "Numero Especial"
    else:
        return -1

def validate_primes_aux(num):
    if (num > 0):
        return "Numero Primo"
    else:
        return ((num / validate_primes_aux(num - 1)) == 0)
    elif():

#SUM OF PAIRS, IMPAIRS
def sum (list1):
    if isinstance (list1, list):
        print("Suma Pares: ", sum_pairs_aux(list1))
        print("Suma Impares: ", sum_impairs_aux(list1))
        print("Suma Total: ", sum_total_aux(list1))
    else:
        return "Error: el valor ingresado no es una lista"

def sum_pairs_aux(list1):
    if (list1 == [ ]):
        return 0
    elif (lista[0] %2 == 0):
        return list1[0] + sum_pairs_aux(list1[1:])
    else:
        return  sum_pairs_aux(list1[1:])
    
def sum_impairs_aux(list1):
    if (list1 == [ ]):
        return 0
    elif (list1[0] %2 == 1):
        return list1[0] + sum_impairs_aux(list1[1:])
    else:
        return  sum_impairs_aux(list1[1:])

    
def sum_total_aux(list1):
    if (list1 == [ ]):
        return 0
    else:
        return list1[0] + sum_total_aux(list1[1:])

#DETERMINES MIN IN A LIST
def minimum(list1):
    if isinstance(list1, list) and (list1 != []):
        return minimum_aux(list1)
    else:
        return "Error: El valor ingresado no es una lista"

def minimum_aux(list1):
    if (list1[1:] == []):
   #if len(lista == 1):
        return list1[0]
    elif (list1[0] <= list1[1]):
        return minimum_aux([list1[0]] + list1[2:])
    else:
        return minimum_aux(list1[1:])

#DETERMINES MAX IN A LIST
def maximum(list1):
    if isinstance(list1, list) and (list1 != []):
        return maximum_aux(list1)
    else:
        return -1

def maximum_aux(list1):
    if (list1[1:] == [ ]):
        return list1[0]
    elif (list1[0] >= list1[1]):
        return maximum_aux([list1[0]] + list1[2:])
    else:
        return maximo_aux(lista[1:])

#SUM OF THE ROOT OF EACH ELEMENT
import math as m

def sum_root(list1):
    if isinstance(list1, list) and (list1 != [ ]):
        return sum_root_aux(list1)
    else:
        return "Error: El valor ingresado no es una lista"


def sum_root_aux(list1):
    if (list1 == []):
        return 0
    else:
        return m.sqrt(list1[0]) + sum_root_aux(list1[1:])

#REVERSE A LIST
def reverse(list1):
    if isinstance(list1, list) and (list1 != []):
        return reverse_aux(list1)
    else:
        return -1

def reverse_aux(list1):
    if (list1 == []):
        return []
    else:
        #return [lista[-1]] + invertir_aux(lista[:-1])
        #return invertir_aux(lista[1:]) + [lista[0]]
        return list1[-1:] + reverse_aux(list1[:-1])


