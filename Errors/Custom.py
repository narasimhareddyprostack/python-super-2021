class NEFMarriage(Exception):
    def __init__(self,msg):
        self.msg = msg
        

salary = int(input("Please Enter your Net Salary :"))
if salary < 75000:
    raise NEFMarriage("Your Not Eligible for Marriage")
