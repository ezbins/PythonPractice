#!/usr/bin/python3.4

def print_max(a,b):
     if(a>b):
          print("{a} bigger than {b}".format(**locals()) ,end='\n')
     else:
          print("{b} bigger than {a}".format(**locals()) ,end='\n')


while True:
     number1 = int(input("Enter first number: "))
     number2 = int(input("Enter second number: "))
     if (number1 == 0 or number2 == 0):
          print("some variable keey zero value",end='\n')
          break;
     print_max(number1, number2)
     