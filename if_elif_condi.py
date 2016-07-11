#!/usr/bin/python3

import random

for integer in range(1,20):
	number_1 = random.randint(1,7)
	number_2 = random.randint(1,7)

	if number_1 > number_2:
		print ("{0} bigger then {1}".format(number_1,number_2))
	elif number_1 < number_2:
		print ("{0} small then {1}".format(number_1,number_2))
