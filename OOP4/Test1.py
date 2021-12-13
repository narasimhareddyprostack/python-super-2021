class A:
  def display(self):
        print("A - Display")
class B:
     def display(self):
        print("B - Display")
class C(B,A):
   pass
c = C()
c.display()
print(C.mro())