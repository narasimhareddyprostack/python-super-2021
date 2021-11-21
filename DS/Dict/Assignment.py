input1 = int(input("Enter Number of numbers:"))
input2 = set()
i = 1
while i <= input1:
    v = int(input("Enter Number:"))
    input2.add(v)
    i=i+1
input3=sorted(input2)
print(input3)
    