class Grandfather:
    def grandfather_feature(self):
        print("Grandfather: Wise and experienced")

class Father(Grandfather):
    def father_feature(self):
        print("Father: Hardworking and caring")

class Aunt(Grandfather):
    def aunt_feature(self):
        print("Aunt: Kind and supportive")

class Child(Father, Aunt):
    def child_feature(self):
        print("Child: Energetic and curious")


c = Child()
c.grandfather_feature()
c.father_feature()
c.aunt_feature()
c.child_feature()