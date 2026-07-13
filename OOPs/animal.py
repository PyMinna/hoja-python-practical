class Animal:
    def __init__(self):
        self.name = "I am lion"
        self._height = 34
        self.__weight = 45

    def details(self):
        print("name :",self.name)
        print("height :",self._height)

    def get_weight(self):
        return self.__weight

lion = Animal()
cat = Animal()

print(lion.name)
print(lion._height)
print(lion.get_weight())