class User:
    userid = 1000000
    def __init__(self, a,b):
        self.name = a
        self.age = b
        print("Parent Class - cosntructor")
        
class Employee(User):
    def __init__(self,name,age,eid, sal):
        super().__init__(name,age)
        self.eid =eid
        self.sal =sal
        print("Child Class - cosntructor")
        print(super().userid)
        print(super().name)
    
e = Employee("Rahul Gandhi", 50, 101, 45000)
print(e.__dict__)