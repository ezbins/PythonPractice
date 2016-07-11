#!/usr/bin/python3.4

def total(a=5,*numbers,**phonebook):
     print('a is',a, end='\n')

     for single_item in numbers:
          print("single_item is {0}".format(single_item), end='\n')

     for first_part, second_part in phonebook.items():
          print(first_part,second_part)


total(10,1,2,3,Jack=1123,John=2231,Inge=1560)