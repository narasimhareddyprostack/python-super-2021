from abc import *

class Calculate(metaclass=ABC):
    @abstractmethod
    def sum(self):
        pass

    @abstractmethod
    def sub(self):
        pass

    @abstractmethod
    def multi(self):
        pass

class Child(Calculate):
    def sum(self):
        print("sum method - child")
    def sub(self):
        print("sub method - Child")
    def multi(self):
        print("multi method - Child")

c = Child()
print(c)
c.sum()
c.sub()
c.multi()