import os,sys
filename = input("Enter File Name:")
if os.path.isfile(filename):
    print("File Exists")
    f = open(filename)
else:
    print("File Not Exits")
    sys.exit(0)  #for normal termination
    
data = f.read()
print(data)
print(f.closed)

f.close()

print(f.closed)
