class Shape:
    def execute(self):
        print("Shape execute  method ")
        self.area()
    def area(self):
        print("shape area method")
class Rectangle(Shape) :
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        rectangle_area=self.length*self.width
        print("Rectangle area",rectangle_area)
        return rectangle_area
class Circle(Shape):
    PI=3.141
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        circle_area=self.PI*self.radius*self.radius
        print("circle area :",circle_area)
        return circle_area
class Test(Shape):
    pass
r=Rectangle(10,12)
r.execute()
c=Circle(2)
c.execute()
t=Test()
t.execute()