class Account:
    def __init__(self):
        print("constructor calling")
        self._ac_type = None
        self._balance = 0.0

    def set_ac_type(self, ac_type):
        self._ac_type = ac_type

    def get_ac_type(self):
        return self._ac_type

    def set_balance(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def withdrawal(self, amt):
        if amt < 5000:
            self._balance = self._balance - amt
            print("total balance after withdrawal :", self._balance)
        else:
            print("you cannot withdrawal more than 5000 in one time")

a = Account()
a.set_ac_type("saving")
a.set_balance(7000)
print(a.get_ac_type())
print(a.get_balance())
#a.deposit(1)
a.withdrawal(6000)















