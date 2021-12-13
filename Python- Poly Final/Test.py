class User:
    def display(self):
        print("User - display()")
class Employee:
    def display(self):
        print("Employee - display()")
class PE:
   def display(self):
        print("PE - display()")
class CE:
   def display(self):
        print("CE - display()")

l1 = [User(), Employee(),PE(),CE()]


def getCall(obj):
    obj.display()
    
for x in l1:
    getCall(x)
    

    

    
    
