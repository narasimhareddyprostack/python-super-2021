def sum():
    print('Hello')
    
sum()

print(type(sum))  #<class 'function'>

# lambda argument : expression

incr = lambda counter  : counter+1
print(incr(10))

print(type(incr))