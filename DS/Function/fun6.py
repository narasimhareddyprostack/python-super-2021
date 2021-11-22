def add(a,b,c):
    return a,b,c,True,"Hello"

result = add(10,20,30)
print(result)        #(10,20,30, True, "Hello")
print(type(result))  # tuple data type

for value in result:
    print(value)