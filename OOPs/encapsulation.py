class Demo:
    def __init__(self):
        self.public_var = "I'm PUBLIC"
        self._protected_var = "I'm PROTECTED"
        self.__private_var = "I'm PRIVATE"
        
    def show(self):
        print(self.public_var)
        print(self._protected_var)

    def get_private(self):
        return self.__private_var

o = Demo()
print(o.public_var)
print(o._protected_var)
print(o.get_private())