try:
    x = int(input("Please Enter First Number:"))
    y = int(input("Please Enter Second Number:"))
    print(x/y)
except :
    print("Please Enter Rigth Info")
    
except ZeroDivisionError:
    print("Please Enter proper value - except zero")

except ValueError :
    print("Enter only Digits")
