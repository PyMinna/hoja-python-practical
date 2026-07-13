class Car:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def start(self):
        print(self.name,"Starts....,its brand is..", self.brand)
    

    def stop(self):
        print(self.name,"Stops....")

BMW = Car("M4","BMW")
BMW.start()
BMW.stop()
s2 = Car("Alto","Maruti")
s2.start()
s2.stop()