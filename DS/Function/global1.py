#how to access local variable out side the function

def get_Price():
    global price  #global variable - price
    price = 599   # global variable
    
get_Price()

def update_Price():
    print(price)
    
update_Price()

print(price)