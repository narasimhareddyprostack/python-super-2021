emp ={'name':"Narasimha",'sal':45000,'loc':"Bangalore"}
emp.pop('loc')  # remove and return

print(emp)
value =emp.popitem()
# remove last element and return element key and value
# as a tuple
print(emp)
print(type(value))

emp.clear()
print(emp)