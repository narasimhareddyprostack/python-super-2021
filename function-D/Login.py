def login():
    cust_Id = 101
    
    def get_Cust_Id():
        print("Inner function")
        return 10
    
    return get_Cust_Id
    
x = login()
x()