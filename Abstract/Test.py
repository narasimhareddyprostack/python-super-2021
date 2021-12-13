from abc import *
class Test:
    @abstractmethod
    def m1(self):
        pass

t = Test()
print(t)