class Calculate:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print("Please atleast two argument")

c= Calculate()

c.sum(10,20,30)
c.sum(10,20)