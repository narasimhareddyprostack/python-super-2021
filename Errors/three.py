try:
    f1 = open("one.txt", "r")
    fileData = f1.read()
    print(fileData)
    print(10/0)
except:
    print("Good Evening")
    
except FileNotFoundError as message:
    #print("File Not Founder Error in specified folder", message)
    print("File Not Founder Error in specified folder")


