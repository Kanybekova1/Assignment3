from amount import Amount

# Creating a class with parametrized constructor
class PersonalAccount:
    def __init__(self,account_number:int ,account_holder:str):
        self.__account_number = account_number 
        self.__account_holder = account_holder
        self.__balance = 0.0 
        self.transactions = [] 

    def deposit(self,amount:float):
       if amount > 0:
            transaction = Amount(amount, 'Deposit')
            self.transactions.append(transaction)
            self.__balance += amount
            print('Deposit: ', amount, ', Balance:', self.__balance)
            return

    def withdraw(self,amount:float):
        if amount > 0:
            if self.__balance >= amount:
                transaction = Amount(amount, 'Withdrawal')
                self.transactions.append(transaction)
                self.__balance -= amount
                print('Withdraw: ', amount, ', Balance:', self.__balance)
            else:
                print('Withdraw: ', amount, ', Not enough balance.')
                return

    def print_transaction_history(self):
        for transaction in self.transactions:
            print(transaction)

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number
    def set_account_number(self, account_number):
        self.__account_number=account_number
    def get_account_holder(self):
        return self.__account_holder
    def set_account_holder(self,account_holder):
        self.__account_holder=account_holder

    def __str__(self):
        return f"Account Number: {self.__account_number}, Account Holder: {self.__account_holder}, Balance: ${self.__balance}"
    
    def __add__(self, amount):
        self.deposit(amount)
        return self
    
    def __sub__(self, amount):
        self.withdraw(amount)
        return self











