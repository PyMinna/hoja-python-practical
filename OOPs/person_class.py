class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello..", self.name)
        print("Your age =", self.age)

p = person("Alice",22)
p2 = person("Rahul",25)

p.greet()
p2.greet()