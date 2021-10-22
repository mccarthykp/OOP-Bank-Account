from random import randint

bank = []
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

        bank.append(self)

    def deposit(self, amount):
        self.balance += amount
        print(f'\nAmount Deposited: ${amount}\nNew Balance: ${self.balance}\n')


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
            print(f'Hello {self.name}, your new balance after this month\'s interest: ${self.balance}\n')
        else:
            interest = self.balance * (apy/100)
            self.balance += interest
            print(f'Hello {self.name}, your new balance after this month\'s interest: ${self.balance}\n')

        
    def print_statement(self):
        safeAccntNum = f'****{str(self.account_number)[slice(4, 8)]}'
        print(f'{self.name}\nAccount No.: {safeAccntNum}\nBalance: ${self.balance}\n')

def monthly_interest(financial_institution):
    for account in financial_institution:
        account.add_interest()
    return


kevin_accnt = BankAccount('Kevin McCarthy', 'savings')
kevin_accnt.deposit(1000)
# kevin_accnt.add_interest()
# kevin_accnt.get_balance()
# kevin_accnt.withdraw(2000)
# kevin_accnt.print_statement()

mitchell_accnt = BankAccount('Mitchell', 'checking', 3141592)
mitchell_accnt.deposit(400000)
# mitchell_accnt.print_statement()
# mitchell_accnt.add_interest()
# mitchell_accnt.print_statement()
# mitchell_accnt.withdraw(150)
# mitchell_accnt.print_statement()

emily_accnt = BankAccount('Emily Weyda')
emily_accnt.deposit(38000)
# emily_accnt.add_interest()
# emily_accnt.get_balance()
# emily_accnt.withdraw(2500)
# emily_accnt.print_statement()

# bank.append(kevin_accnt)
# bank.append(mitchell_accnt)
# bank.append(emily_accnt)
monthly_interest(bank)