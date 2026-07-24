from abc import ABC,abstractmethod
class Shape:
    def execute(self):
        print("calculating area")
        self.area()
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        print(f"Area of Rectangle: {area}")
r=Rectangle(5,10)
r.area()
r.execute()
s=Shape()
s.area()