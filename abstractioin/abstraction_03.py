from abc import ABC,abstractmethod
from operator import length_hint


class Shape:
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
r=Rectangle(12,13)
print("rectangle area ",r.area())
shape:Shape=Rectangle(5,10)
print("area of rectangle :",shape.area())