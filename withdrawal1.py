class Account:
    def __init__(self):
        print("constructor calling")
        self._ac_type = None
        self._balance = 0.0
        self._count=0

    def set_ac_type(self, ac_type):
        self._ac_type = ac_type

    def get_ac_type(self):
        return self._ac_type

    def set_balance(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def withdrawal(self, amt):
        if self._count < 5:
            self._balance = self._balance - amt
            self._count+=1
            print("total balance after withdrawal :", self._balance)
            print("withdrawal successful",self._count)

        else:
            print("you cannot withdrawal more than 5  times in a day ")

a = Account()
a.set_ac_type("saving")
a.set_balance(7000)
print(a.get_ac_type())
print(a.get_balance())
a.withdrawal(600)
a.withdrawal(1000)
a.withdrawal(200)
a.withdrawal(500)
a.withdrawal(700)
a.withdrawal(1600)











