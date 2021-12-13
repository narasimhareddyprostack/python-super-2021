class Employee:
    def display(self):
        print("No - argument")
        
    def display(self,a):
        print("one argument")
        
    def display(self,a,b):
        print("Two argument")
        
e = Employee()
e.display(10,20)
        