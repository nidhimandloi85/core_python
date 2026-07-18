class Account:
    def __init__(self):
        print("constructor calling")
        self._ac_type = None
        self._ac_no = None
        self._ac_mode = None
        self._balance = .0

    def set_ac_type(self, ac_type):
        self._ac_type = ac_type

    def get_ac_type(self):
        return self._ac_type

    def set_ac_no(self, ac_no):
        self._ac_no = ac_no

    def get_ac_no(self):
        return self._ac_no

    def set_ac_mode(self, ac_mode):
        self._ac_mode = ac_mode

    def get_ac_mode(self):
        return self._ac_mode

    def set_balance(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance
a = Account()
a.set_ac_type("saving")
a.set_ac_no("12456789")
a.set_ac_mode("self")
a.set_balance(35000)
print(a.get_ac_type())
print(a.get_ac_no())
print(a.get_ac_mode())
print(a.get_balance())





