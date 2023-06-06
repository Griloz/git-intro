class Bank_Account:

    # constructor
    def __init__(self, account_number, account_holder, balance=0) -> None:
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    # create obj method
    def deposit(self, amount):
        self.balance += amount
        print(
            f'Your deposited {amount}$. Your current balance is {self.balance}')

    # create obj method
    def withdraw(self, amount):
        if self.balance >= amount:
            print(
                f'Your withdraw {amount}$. Your current balance is {self.balance}')
        else:
            print(
                f'Sorry, you do not have sufficient funds to withdraw {amount}, your balance is {self.balance}')

    # create obj method
    def check_balance(self):
        print(f'Account holder is {self.account_holder}')
        print(f'Account number is {self.account_number}')
        print(f'Current balance is {self.balance}')


Greg = Bank_Account(3224, 'Greg Loz', 1000)
Radii = Bank_Account(322134, 'Radii Tem', 50)

Greg.deposit(120)
Greg.withdraw(50)
Greg.check_balance()

Radii.deposit(130)
Radii.withdraw(500)
Radii.check_balance()
