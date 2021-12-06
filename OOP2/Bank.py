class Bank:
    min_Bal = 500
    

c1 = Bank()
print(c1.__dict__)    # {}  - no instance variable
print(Bank.__dict__)  # displaying Bank Class info as dict format