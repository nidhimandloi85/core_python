class Car:
    def __init__(self):
        self.color=None
        self.price=0
        self.model=None
    def set_color(self,color):
        self.color=color
    def get_color(self):
        return self.color
    def set_price(self,price):
        self.price=price
    def get_price(self):
        return self.price
    def set_model(self,model):
        self.model=model
    def get_model(self):
        return self.model
class Maruti(Car) :
    def display(self):
        self.fuel_type=input("fuel_type:")
        self.mileage=input("mileage:")
        self.warranty=input("warranty:")

m=Maruti()
m.set_color("red")
m.set_price(1000000)
m.set_model("swift")
m.display()
print(m.get_color())
print(m.get_price())
print(m.get_model())