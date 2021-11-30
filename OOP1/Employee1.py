class Employee:
    """ Test Employee class """
    def __init__(self):
        print("Constructor Executing")
        
    def getEmployee(self):
        print("getEmployee method()/function")
    

e = Employee()
e.getEmployee()
e1= Employee()
print(type(e))
print(type(e1))