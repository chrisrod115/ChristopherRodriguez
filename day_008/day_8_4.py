#Write your code below this line ๐
from pyparsing import Or
from sympy import numer


def prime_checker(number):
    if (number == 2):
        print("prime number")
    elif (number % 3 == 0) or (number % 2 == 0):
        print("not prime number")
    else:
        print("prime number")


#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)



