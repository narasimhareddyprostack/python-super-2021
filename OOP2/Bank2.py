class Bank:
    def __init__(self):
        print("Constructor method")
    
    def m1(self):
        print("Instance Method")
    
    @classmethod
    def m2(cls):
        print("class method")
    @staticmethod
    def m3():
        print("static method")
        
c1 = Bank()
c1.m1()
c1.m2()
Bank.m2()

c1.m3()
Bank.m3()