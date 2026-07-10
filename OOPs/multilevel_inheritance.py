class GrandParent:
    def feature_grandparent():
        print("Grandparent Feature")

class Parent(GrandParent):
    def feature_parent():
        print("Parent Feature")

class child(Parent):
    def feature_child():
        print("Child Feature")

c = child
c.feature_grandparent()
c.feature_parent()
c.feature_child()