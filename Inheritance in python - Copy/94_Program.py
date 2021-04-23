''' Program to create a class pets from a class Animals and further
   create class dog from pets. Add a method bark to class dog.'''
class Animals:
    animalType = "Mammal"

class Pets:
    color = "White"

class Dog:
    @staticmethod
    def bark():
        print("Bow bow!")

d  = Dog()
d.bark()