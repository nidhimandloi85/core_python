from abc import ABC,abstractmethod
class Shape(ABC):
    def execute(self):
        print("calculating area")
        self.area()
    @abstractmethod
    def area(self):
        print("shape method")

class Rectangle(Shape):
    def hello(self):
        print("hello nidhi")
    def area(self):
        print("hy")
r=Rectangle()
r.execute()
