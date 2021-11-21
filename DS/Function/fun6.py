def add(a,b,c):
    return a,b,c,True,"Hello"

result = add(10,20,30)
print(result)
print(type(result))

for value in result:
    print(value)