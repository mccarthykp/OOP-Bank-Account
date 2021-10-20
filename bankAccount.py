from random import randint
class BankAccount():
    def __init__(self, full_name, account_number = randint(00000000,99999999), balance = 0):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Amount Deposited: ${amount}\nNew Balance: ${self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient Funds')
        else:
            self.balance -= amount
            print(f'Amount withdrawn: ${amount}\nNew Balance: ${self.balance}')

# kevinAccnt = BankAccount('Kevin')
# kevinAccnt.deposit(1000)
# kevinAccnt.withdraw(500)