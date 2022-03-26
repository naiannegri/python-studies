class Category:
    @classmethod
    def createChart(self):
        header = self.description.center(30,'*') +'\n'
        ledger = []

    def __init__(self,description):
        self.description = description
        
        self.ledger = []
        self.balance = 0.0

    def deposit(self,amount,desc):
        self.ledger.append({"amount": amount, "description": desc})
        self.balance += amount
    
    def withdraw(self,amount,desc):
        if self.balance >= amount:
            self.ledger.append({"amount": - amount, "description": desc})
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, account):
        if self.withdraw(amount,"Transfer to {}".format(account.description)):
            account.deposit(amount, "Transfer to {}".format(self.description))
            return True
        else:
            return False

    def check_funds(amount):
        if self.balance >= amount:
            return True
        else:
            return False




def create_spend_chart(categories):
