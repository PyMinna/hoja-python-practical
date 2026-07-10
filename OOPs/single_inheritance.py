class Animal:
    def eat():
        print("Eating...")

class Dog(Animal):
    def bark():
        print("Barking...")

a = Dog
a.eat()
a.bark()