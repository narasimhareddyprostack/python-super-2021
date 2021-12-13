class A:
    def display(self):
        print("A - display")
class B(A):
     def display(self):
        print("B - display")
class C(A):
   def display(self):
        print("C - display")
class D(B,C):
   def display(self):
        print("D - display")

d = D()
#d.display()
print(D.mro())
