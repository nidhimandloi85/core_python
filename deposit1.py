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
    def deposit(self, amt):
        if self._count<5:
            self._balance=self._balance+amt
            self._count+=1
            print("deposit successful")
        else:
            print("you cannot deposit more then 5 times in a day")
    #def withdrawal(self, amt):
        #if amt < self._balance:
         #   self._balance = self._balance - amt
            #print("total balance after withdrawal :", self._balance)
        #else:
            #print("Insufficient fund transfer")
a = Account()
a.set_ac_type("saving")
a.set_balance(1000)
print(a.get_ac_type())
print(a.get_balance())
a.deposit(30)
a.deposit(50)
a.deposit(40)
a.deposit(60)
a.deposit(100)
a.deposit(150)
#a.withdrawal(1300)















