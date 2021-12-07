class Bank:
    min_Bal = 500
    @classmethod
    def updateMin_Bal(cls):
        print(cls)
        cls.min_Bal = 700
    
Bank.updateMin_Bal()
print(Bank.__dict__)
        