class car:

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def start(self):
        print(self.brand,self.model, "is starting...")

car1 = car("BMW","XS")
car2 = car("Tesla","Model S")

car1.start()
car2.start()