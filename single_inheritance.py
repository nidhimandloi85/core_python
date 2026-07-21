class Shape:
    def __init__(self):
        self.color=None
        self.border=0
    def set_color(self,color):
        self.color=color
    def get_color(self):
        return self.color
    def set_border(self,border):
        self.border=border
    def get_border(self):
        return self.border
class rectangle(Shape):
    def __init__(self):
        self.length=0
        self.width=0
    def set_length(self,length):
        self.length=length
    def get_length(self):
        return self.length
    def set_width(self,width):
        self.width=width
    def get_width(self):
        return self.width
r=rectangle()
r.set_color("black")
r.set_border(12)
r.set_length(5)
r.set_width(4)
print(r.get_color())
print(r.get_border())
print(r.get_length())
print(r.get_width())





