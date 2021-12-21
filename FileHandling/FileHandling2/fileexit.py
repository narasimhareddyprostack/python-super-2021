import os,sys
filename = input("Enter File Name:")
if os.path.isfile(filename):
    print("File Exists")
else:
    print("File Not Exits")
    sys.exit(0)
