#COUNTDOWN
def countdown(value):
    print(value)
    if (vale > 0):
        countdown (value - 1)
    elif (value <= 0):
        return 0

def countdown2(value):
    print(value, end = " ")
    if (value <= 0):
        return 0
    else:
        countdown2(value - 1)

#SUM BETWEEN TWO DIGITS
def summ(num):
    if isinstance(num, int) and (num > 0):
        return sum_aux(abs(num))
    else:
        return -1

def sum_aux(num):
    if(num == 0):
        return 0
    else:
        return num%10 + sum_aux(num//10)

#CALCULATE THE LENGHT OF A NUMBER
def lengthcalc(num):
    if isinstance(num, int) and (num > 0):
        return lengthcalc_aux(abs(num))
    else:
        return -1

def lengthcalc_aux(num):
    if(num == 0):
        return 0
    else:
        return 1 + lengthcalc_aux(num//10)

#DETERMINE AMOUNT OF PAIR NUMBERS
def pairs(num):
    if isinstance(num, int) and (num > 0):
        return pairs_aux(num)
    else:
        return -1

def  pairs_aux(num):
    if (num == 0):
        return 0
    elif ((num%10)%2 == 0):
        return 1 + pairs_aux(num//10)
    else:
        return pairs_aux(num//10)

#DETERMINE AMOUNT OF IMPAIRS NUMBERS
def impairs(num):
    if isinstance(num, int) and (num > 0):
        return impairs_aux(num)
    else:
        return -1

def  impairs_aux(num):
    if (num == 0):
        return 0
    elif ((num%10)%2 == 1):
        return 1 + impairs_aux(num//10)
    else:
        return impairs_aux(num//10)

#CREATE A NEW NUMBER WITH PAIRS AND IMPAIRS NUMBERS
def new_num(num):
    if isinstance(num, int) and (num > 0):
        return [new_pairs(abs(num), 0), new_impairs(num, 0)]
    else:
        return -1

def new_pairs(num, pot):
    if (num == 0):
        return 0
    elif ((num%10)%2 == 0):
        return ((num % 10)*(10 ** pot) + new_pairs(num//10, pot + 1))
    else:
        return new_pairs(num//10, pot)

def new_impairs(num, potencia):
    if (num == 0):
        return 0
    elif ((num%10)%2 == 1):
        return ((num % 10)*(10 ** pot) + new_impairs(num//10, pot + 1))
    else:
        return new_impairs(num//10, pot)

#FACTORIAL OF A NUMBER
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

#DETERMINE AMOUNT OF NUMBERS BETWEEN TWO NUMBERS
def between_in(num):
    if isinstance(num, int) and (num > 0):
        return between_in_aux(num)
    else:
        return -1

def between_in_aux(num):
    if (num == 0):
        return True
    elif (num%10 <= 4) and (num%10 >= 0):
        return between_in_aux(num//10)
    else:
        return False





