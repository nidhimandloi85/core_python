class Shape:
    def __init__(self,color,borderwidth):
        self.color=color
        self.borderwidth=borderwidth
    def get_color(self):
        return self.color
    def get_borderwidth(self):
        return self.borderwidth
class Circle(Shape):
    def __init__(self,radius=0,color=None,borderwidth=0):
        self.radius=radius
        super().__init__(color,borderwidth)
    def get_radius(self):
        return self.radius
class Rectangle(Shape) :
    def __init__(self,length=0,width=0,color=None,borderwidth=0):
        self.length=length
        self.width=width
    def get_length(self):
        return self.length
    def get_width(self):
        return  self.width
class Triangle(Shape)  :
    def __init__(self,height=0,base=0,color="",borderwidth=0):
        self.height=height
        self.base=base
    def  get_height(self):
        return self.height
    def get_base(self):
        return self.base
c=Circle(5,"black",12)
print("circle")
print("radius :",c.get_radius())
print("color :",c.get_color())
print("borderwidth: ",c.get_borderwidth())

print("-----------------------------------------")
r=Rectangle(4,5,"red",11)
print("Rectangle")
print("length:",r.get_length())
print("width:",r.get_width())
print("color :",c.get_color())
print("borderwidth: ",c.get_borderwidth())
print("------------------------------------------------")
t=Triangle(5,4,"yellow",8)
print("triangle")
print("height:",t.get_height())
print("base :",t.get_base())
print("color :",c.get_color())
print("borderwidth: ",c.get_borderwidth())

























