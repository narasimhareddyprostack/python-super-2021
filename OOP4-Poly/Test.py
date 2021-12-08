class Parent:
    def __init__(self):
        print("Parent class - Constructor")
        print(id(self))
       

class Child(Parent):
    def __init__(self):
        print("child Class - Contrcutor")
        super().__init__()
        print(id(self))
        
c = Child()
print(id(c))



    

