class Employee:
    
    def setName(self,name):
        self.name = name
        
    def getName(self):
        return self.name
        

e1 = Employee()
e1.setName("Rahul Gandhi")
print(e1.getName())
print(e1.__dict__)