class Vehicle:
    def start():
        print("Vehicle starting....")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

c = Car
c.start()

c = Bike
c.start()