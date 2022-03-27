'''
methods
'''
class Bank():
    def __init__(self, bank_number, bank_name):
        self.bankNumber = bank_number
        self.bankName = bank_name
        self.bankAgencies = []

    def createAgency(self, agency_number, agency_name, agency_adress):
        new_agency = Agency(agency_number, agency_name, agency_adress)
        self.bankAgencies.append(new_agency)

    def __repr__(self):
        return "{} - {}".format(self.bankNumber, self.bankName)        

class Agency():
    def __init__(self, agency_number, agency_name, agency_adress):
        self.agencyNumber = agency_number
        self.agencyName = agency_name
        self.agencyAdress = agency_adress
        
    def __repr__(self):
        return "{} - {}".format(self.agencyNumber, self.agencyName)


class Account():

    #constructor, initializes model variables
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
        Account.balance = Account.balance + amt 
        return Account.balance


def begin():
    print("\n\nBEGIN\n\n")

def end():
    print("\n\nEND\n\n")

if __name__ == "__main__":
    begin()
    
    BB =  Bank(bank_name = "Banco do Brasil", bank_number = 1)
    
    NU =  Bank(bank_name = "NuBank", bank_number = 2)

    NU.createAgency(1, "Nu Digital", "n/a")

    print("Bank: {} | Agencies: {}".format(NU.bankName, NU.bankAgencies))

    

    end()