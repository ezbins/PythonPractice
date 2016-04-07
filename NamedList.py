#!/usr/bin/python3


class NamedList(list):

    def __init__(self, a_name):
        list.__init__([])
        self.name = a_name


johnny = NamedList("John Paul Jones")
johnny.append("Bass Player")
johnny.extend(['composer','Arranger',"Musician"])
print(type(johnny))
print(johnny)
print(dir(johnny))

for attr in johnny:
    print(johnny.name+" is a "+attr)