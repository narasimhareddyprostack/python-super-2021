# Write a python program to read CLA and print sum
#argv
from sys import argv
sum=0
argv = argv[1:]
for a in argv:
    sum = sum +int(a)
    
print(sum)

