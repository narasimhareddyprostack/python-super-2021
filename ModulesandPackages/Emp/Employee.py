class Employee:
    def __init__(self,name):
        self.name = name
        print('Constructor')
    
    def getName(self):
        print("Hello,GM", self.name)