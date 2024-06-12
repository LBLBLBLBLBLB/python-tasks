class CheckingAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < 0:
            raise Exception('withdraw failed')
        self.balance -= amount

    def __str__(self):
        return f"CheckingAccount(name={self.name},balance={self.balance})"


class SavingAccount:
    def __init__(self, name, balance, interest_rate):
        self.name = name
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount

    def apply_daily_interest(self):
        daily_interest_balance = self.interest_rate / 365
        daily_interest = self.balance * daily_interest_balance
        self.balance += daily_interest

    def __str__(self):
        return f"SavingAccount(name={self.name}, interest_rate={self.interest_rate}, balance={self.balance})"


class CreditAccount:
    def __init__(self, name, balance, interest_rate, credit_limit):
        self.name = name
        self.balance = balance
        self.interest_rate =interest_rate
        self.credit_limit = credit_limit

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < 0:
            raise Exception('withdraw failed')
        self.balance -= amount

    def apply_daily_interest(self):
        if self.balance < 0:
            daily_interest = (self.interest_rate / 100) / 365
            self.balance -= abs(self.balance) * daily_interest

    def __str__(self):
        return f"CreditAccount(name={self.name}, interest_rate={self.interest_rate}%, credit_limit={self.credit_limit}, balance={self.balance})"


class Bank:
    def __init__(self):
        self.accounts = []

    def open_account(self, account):
        self.accounts.append(account)

    def display_accounts(self):
        for account in self.accounts:
            print(account)

    def apply_daily_interest(self):
        for account in self.accounts:
            if isinstance(account, (SavingAccount, CreditAccount)):
                account.apply_daily_interest()

    def total_cash(self):
        total_cash = sum(account.balance for account in self.accounts if account.balance > 0)
        return total_cash

    def total_credit(self):
        total_credit = sum(abs(account.balance) for account in self.accounts if account.balance < 0)
        return total_credit


checking = CheckingAccount(name="John Doe", balance=1000)
savings = SavingAccount(name="Jane Doe", interest_rate=1.5, balance=5000)
credit = CreditAccount(name="Jack Doe", interest_rate=5, credit_limit=2000, balance=-500)

bank = Bank()
bank.open_account(checking)
bank.open_account(savings)
bank.open_account(credit)

bank.display_accounts()
bank.apply_daily_interest()

print("\nAfter applying daily interest:")
bank.display_accounts()

print("\nTotal cash in the bank:", bank.total_cash())
print("Total credit on loan by the bank:", bank.total_credit())