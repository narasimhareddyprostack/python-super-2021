class Employee:
    a=100
    def m1(self):
        Employee.b=200
    @classmethod
    def m2(cls):
        cls.c=300
        Employee.d=400
    @staticmethod
    def m3():
        Employee.e=500
e1=Employee()
e1.m1()
e1.m2()
e1.m3()
print(e1.__dict__)
print(Employee.__dict__)