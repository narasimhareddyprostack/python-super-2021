class Parent:
    def m1(self):
        print("m1 () - method")
class Child(Parent):
    def m2(self):
        print("m2 () - method")
class GrandChild(Child):
    def m3(self):
        print("m3 () - method")

obj = GrandChild()
obj.m1()
obj.m2()
obj.m3()