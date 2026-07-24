class Shape:
    def area(self):
        print("Shape area")
        print("shape class area method")
class Rectangle(Shape):
    def area(self):
        print("rectangle area")
        print("rectangle class area method")
r=Rectangle()
r.area()
s:Shape=Rectangle()
s.area()