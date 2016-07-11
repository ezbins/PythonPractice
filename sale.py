#!/usr/bin/env python3
from collections import namedtuple

# "import collections" statment,writing collections.namedtuple
#Sale=collections.namedtuple("Sale","productid customerid date quantity price")
Sale=namedtuple("Sale","productid customerid date quantity price")

sales=[]
sales.append(Sale(432, 921, "2008-09-14",3, 7.99))
sales.append(Sale(531, 920, "2010-05-14",1, 14.22))

total=0
for sale in sales:
     total+=sale.quantity*sale.price

print("Total price is {total}".format(**locals()) ,end='\n')
