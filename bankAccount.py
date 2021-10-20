from random import randint
class BankAccount():
    def __init__(self, full_name, type = 'checking', account_number = randint(10000000,99999999), balance = 0):
        self.name = full_name
        self.account_number = account_number
        self.balance = balance
        self.type = type

        if len(str(self.account_number)) < 8:
            while len(str(self.account_number)) < 8:
                self.account_number *= 10
            print(f'Your account number must be 8 digits long, here is your new account number: {self.account_number}')
    
        if self.type != 'checking' and self.type != 'savings':
            self.type = 'checking'
            print(f'You chose an invalid account type, we have opened a checking account by default.')


    def deposit(self, amount):
        self.balance += amount
        print(f'Amount Deposited: ${amount}\nNew Balance: ${self.balance}\n')


    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient Funds')
        else:
            self.balance -= amount
            print(f'Amount withdrawn: ${amount}\nNew Balance: ${self.balance}\n')


    def get_balance(self):
        print(f'Hello {self.name}, your current account balance is ${self.balance}\n')
        return self.balance


    def add_interest(self):
        apy = 1

        if self.type == 'savings':
            apy = 1.2
            interest = self.balance * (apy/100)
            self.balance += interest
            print(f'Your new balance after this month\'s interest: ${self.balance}\n')
        else:
            interest = self.balance * (apy/100)
            self.balance += interest
            print(f'Your new balance after this month\'s interest: ${self.balance}\n')

        
    def print_statement(self):
        safeAccntNum = f'****{str(self.account_number)[slice(4, 8)]}'
        print(f'{self.name}\nAccount No.: {safeAccntNum}\nBalance: ${self.balance}\n')


kevinAccnt = BankAccount('Kevin McCarthy', 'savings')
kevinAccnt.deposit(1000)
kevinAccnt.add_interest()
kevinAccnt.get_balance()

mitchellAccnt = BankAccount('Mitchell', 'checking', 3141592)
mitchellAccnt.deposit(400000)
mitchellAccnt.print_statement()
mitchellAccnt.add_interest()
mitchellAccnt.print_statement()
mitchellAccnt.withdraw(150)
mitchellAccnt.print_statement()