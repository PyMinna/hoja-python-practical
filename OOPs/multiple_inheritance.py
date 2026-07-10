class Mother:
    def cook():
        print("Cooking....")

class Father:
    def drive():
        print("Driving....")

class child(Mother,Father):
    pass

c = child
c.cook()
c.drive()