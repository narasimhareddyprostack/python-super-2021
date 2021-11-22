#variable Lenght Argument
#Invoking a fun, reciving rest of values -

def sum(*varg):
    
    total = 0
    for value in varg:
        total = total +value
    
    print(total)
   
        
sum()         # 0
sum(10)       # 10
sum(10,20)    # 30
sum(10,20,30)
sum(10,20,30,40)
