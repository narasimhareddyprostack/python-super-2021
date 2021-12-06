class Bank:
    min_Bal = 500     # static variable
    def __init__(self,name):
        self.name =name      #instance 
       
        #print("Constructor executing automatically")
    def deposit(self, amount):
        self.amount =  amount # instace variable
        Bank.BranchName = "Marathahalli"
c1 = Bank("Rahul")
c2 = Bank("Priyanka")
c1.loc ="New Delhi"
c1.deposit(50000)
print(c1.__dict__)
print(c2.__dict__)


print(Bank.min_Bal)
print(Bank.BranchName)
print(Bank.__dict__)