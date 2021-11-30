class Employee:
    def __init__(self,a,b):
        self.emp_id =a
        self.emp_name = b
    
    def getEmployeeDetails(self):
        print(self.emp_name)
        
e = Employee(101, "Rahul Gandhi")
e.getEmployeeDetails()