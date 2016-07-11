#!/usr/bin/python3
import random

for x in range(1,11):
	throw_1 = random.randint(1,6)
	throw_2 = random.randint(1,6)
	total = throw_1+throw_2
	if total == 7:
		print('Seven Thrown')
	if total == 11:
		print('Eleven Thrown')
	if throw_1 == throw_2:
		print ('Double Thrown')

text = 'abcd'
if text == "abcd":
	print ('text true')

