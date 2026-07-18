class Person:
    def __init__(self):
        print("constructor is call")
        self_name=None
        self_dob=None
        self_address=None
    def set_name(self,name):
        self._name=name
    def get_name(self):
        return self._name
    def set_dob(self,dob):
        self._dob=dob
    def get_dob(self):
        return self._dob
    def set_address(self,address):
        self._address=address
    def get_address(self):
        return self._address
p=Person()
p.set_name("nidhi")
p.set_dob("2007-1-19")
p.set_address("indore")
print(p.get_name())
print(p.get_dob())
print(p.get_address())