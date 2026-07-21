class Account:
    def __init__(self):
        print("constructor calling")
        self._ac_type = None
        #self._ac_no = None
        #self._ac_mode = None
        self._balance = 0.0

    def set_ac_type(self, ac_type):
        self._ac_type = ac_type

    def get_ac_type(self):
        return self._ac_type

    def set_balance(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance
    def deposit(self, amt):
        if amt<=50000:
            self_balance = self._balance + amt
            print("deposit successful ", self._balance)
        else:
            print("you cannot deposit more than 50000")


    def withdrawal(self, amt):
        if amt < self._balance:
            self._balance = self._balance - amt
            print("total balance after withdrawal :", self._balance)
        else:
            print("Insufficient fund transfer")

a = Account()
a.set_ac_type("saving")
a.set_balance(1000)
print(a.get_ac_type())
print(a.get_balance())
a.deposit(51000)
a.withdrawal(1300)




