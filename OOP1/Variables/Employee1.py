class Employee:
    a=100  #static variable
    def __init__(self):
        self.b=200  #instance variable
    def m1(self):
        self.c=300  #instance variable
        
e1 = Employee()
e2 = Employee()
e1.m1()
e1.d=400            #instance variable
#print(e1)
print(e1.__dict__)
print(e2.__dict__)
print(Employee.__dict__)