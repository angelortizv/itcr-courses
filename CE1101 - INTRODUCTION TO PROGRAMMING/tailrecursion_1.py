#LENGTH OF NUMBER
def lengthcalc(num):
    if isinstance(num, int):
        return lengthcalc_aux(num, 0)
    else:
        return -1

def lengthcalc_aux(num, result):
    if (num == 0):
        return result
    else:
        return lengthcalc_aux(num//10, result + 1)


#REMOVE DIVISIBLES 
def divisibles(num):
    if isinstance(num, int):
        return divisibles3_aux(num, 0, 0), divisibles2_aux(num, 0, 0)
    else:
        return -1

def divisibles3_aux(num, result, pot):
    if(num == 0):
        return result
    elif((num%10)%3 == 0):
        return divisibles3_aux(num//10, result, pot)
    else:
        return divisibles3_aux(num//10, (num%10 * 10**pot) + result, pot + 1)

def divisibles2_aux(num, result, pot):
    if(num == 0):
        return result
    elif((num%10)%2 == 0):
        return divisibles2_aux(num//10, result, pot)
    else:
        return divisibles2_aux(num//10, (num%10 * 10**pot) + result, pot + 1)

#LIST WITH DIVISIBLES
def divisibles(num):
   if isinstance(num, int) and (num > 0):
      return [divisibles_aux(num, 0, 0), divisibles_aux2(num, 0, 0)]
   else:
      return -1

def divisibles_aux(num, result, pot):
   if (num == 0):
      return result
   elif (((num%10)%3) == 0) and ((num%10) != 0):
      return divisibles_aux(num//10, result, pot)
   else:
      return divisibles_aux(num//10,  (num%10)*(10**(pot)) + result, pot + 1)

def divisibles_aux2(num, result, pot):
   if (num == 0):
      return result
   elif (((num%10)%3) == 0):
      return divisibles_aux2(num//10,  (num%10)*(10**(pot)) + result, pot + 1)
   else:
      return divisibles_aux2(num//10, result, pot)

#SEARCH NUMBER INSIDE LIST
def search(num, lista):
   if isinstance(num, int) and (lista, list):
      return search_aux(num, lista, 0)
   else:
      return -1

def search_aux(num, lista, indice):
   if (indice == len(lista)):
      return False
   elif (lista[indice] == num):
      return True
   else:
      return search_aux(num, lista, indice + 1)

