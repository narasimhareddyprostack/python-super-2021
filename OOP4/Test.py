class A:
    def display(self):
        print("A - Display")
class B:
     def display(self):
        print("B - Display")
class C(A,B):
    pass

c = C()
c.display()