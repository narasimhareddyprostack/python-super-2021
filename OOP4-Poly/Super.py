class Parent:
    def __init__(self):
        print("parent class constructor")
    def m1(self):
        print("Parent class Instance Method")
    @classmethod
    def m2(cls):
        print("Parent class - class method")
    @staticmethod
    def m3():
        print("Parent class - static method")
        

class Child(Parent):
    def __init__(self):
        pass
        '''
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
        '''
        
    def display(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
        
    @classmethod
    def info(cls):
        #super().__init__()  # we cant access parent class constructor
        #super().m1()   # instance method
        #super().m2()  # class method
        #super().m3()  # static method
        
    #@staticmethod
    #def show():
        #super().__init__()
        #super().m1()
        #super().m2()
        #super().m3()
     

c =Child()
#c.display()
#c.info()  # class method
c.show()
