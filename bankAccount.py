from random import randint
class BankAccount():
    def __init__(self, full_name, account_number = randint(00000000,99999999), balance = 0):
        self.name = full_name
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

    def get_balance(self):
        print(f'Hello, your current account balance is ${self.balance}\n')
        return self.balance

    def add_interest(self):
        apy = .083
        interest = self.balance * (apy/100)
        self.balance += interest
        print(f'Your new balance after this month\'s interest: ${self.balance}\n')

    def print_statement(self):
        safeAccntNum = f'****{str(self.account_number)[slice(4, 8)]}'
        print(f'{self.name}\nAccount No.: {safeAccntNum}\nBalance: ${self.balance}')


# kevinAccnt = BankAccount('Kevin McCarthy')
# kevinAccnt.deposit(1000)
# kevinAccnt.add_interest()
# print(kevinAccnt.account_number)
# kevinAccnt.print_statement()