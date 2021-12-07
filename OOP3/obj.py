class Test:
    counter = 0
  
    def __init__(self):
        Test.counter = Test.counter + 1
        

t1 = Test()
t2=  Test()
t3= Test()
print(Test.counter)
