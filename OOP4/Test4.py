class A:
    def __init__(self):
        print("A - Constructor")
class B:
    def __init__(self):
        print("B - Constructor")
        
class C(A,B):
    def __init__(self):
        print("C - Constructor")
        super().__init__()
        B.__init__(self)
c= C()