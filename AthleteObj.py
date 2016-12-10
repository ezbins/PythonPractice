#!/usr/bin/env python3
from Athlete import Athlete


# class Athlete:

#     def __init__(self, a_name, a_dob=None, a_times=[]):
#         self.name = a_name
#         self.dob = a_dob
#         self.times = a_times

a1 = Athlete('Sara', '2002-12-17', ['2:23', '1:15', '3:34'])
print(a1.getName())
print(type(a1))
