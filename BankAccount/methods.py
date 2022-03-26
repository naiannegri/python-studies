'''
methods
'''


class account():
    name=""
    balance=0.0

    #constructor, initializes global variables
    def __init__(self, name, balance):
        self.name=name
        self.balance=balance

    def deposit(self, amt):
        self.balance += amt 
        return self.balance

    def withdraw(self, amt):
        self.balance -= amt
        return self.balance
    
    def transfer(self, amt, acount):
        self.balance = self.balance - amt
        account.balance = account.balance + amt 
        return account.balance