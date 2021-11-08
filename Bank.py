class Account(object):
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount

    def deposit(self, amount):
        self.balance = self.balance+amount
    def withdraw(self, amount):
        self.balance = self.balance - amount

    def dump(self):
        print('NAME...',self.name),
        print("Account no....",self.no)
        print("Remaining balance....",self.balance)
a1=Account('Will',2040,10000)
a1.deposit(1000000)
a1.withdraw(10)
a1.dump()
