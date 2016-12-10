#!/usr/bin/env python3


class Animal():
    name = 'Justic'
    noise = 'Grunt'

    def getName(self):
        return self.name

    def makeNoise(self):
        return self.noise


class Dog(Animal):
    #name = 'bigDog'
    size = 'medium'

    #def getName(self):
    #    return self.name

    def getSize(self):
        return self.size

animal1 = Animal()
print(animal1.getName())

dog1 = Dog()
print(dog1.getName())
print(dog1.getSize())
