class Grandfather:
    def feature_grandfather(self):
        print("He is a honest man")

class Father(Grandfather):
    def feature_father(self):
        print("He is hardworking man")

class Child(Father):
    def feature_child(self):
        print("He is very curious")

c = Child()
c.feature_grandfather()
c.feature_father()
c.feature_child()