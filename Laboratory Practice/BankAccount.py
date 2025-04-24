from abc import ABC, abstractmethod

class BankAccount(ABC):
    _accounts={
        "CA":0,
        "SA":0
    }
    def __init__(self):
        self._balance=0
        
    @property
    def balance(self):
        return self._balance
    
    @property
    def account_number(self):
        return self._account_number
    
    @abstractmethod
    def deposit(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    @abstractmethod
    def display_account_type(self):
        pass

class CurrentAccount(BankAccount):
    def __init__(self):
        super().__init__()
        BankAccount._accounts["CA"]+=1
        self._account_number="CA"+str(BankAccount._accounts["CA"])
    
    def deposit(self, amount):
        self._balance+=amount
        
    def withdraw(self, amount):
        if (self._balance-amount) >= (-5000):
            self._balance-=amount
        else:
            print("\nOverdraft limit exceeded!\n")
    
    def display_account_type(self):
        return "Type: Current Account"

class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()
        BankAccount._accounts["SA"]+=1
        self._account_number="SA"+str(BankAccount._accounts["SA"])
        
    def deposit(self, amount):
        self._balance+=amount
        
    def withdraw(self, amount):
        if (self._balance-amount) >= 0:
            self._balance-=amount
        else:
            print("\nInsufficient Balance!\n")
            
    
    def display_account_type(self):
        return "Type: Savings Account"


def print_account_details(account):
    print(f"Account Number: {account.account_number}")
    print(f"Balance: {account.balance}")
    print(account.display_account_type())
    print("-"*25)
    
new_savings_account=SavingsAccount()
new_current_account=CurrentAccount()
new_savings_account.deposit(1200)
new_current_account.deposit(1200)
new_current_account.withdraw(1400)
print_account_details(new_savings_account)
print_account_details(new_current_account)
