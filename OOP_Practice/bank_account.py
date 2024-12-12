class BankAccount:
    def __init__(self,holder_name, balance, acc_number):
        self.holder_name = holder_name
        self.balance = balance
        self.acc_number = acc_number
    
    def current_balance(self):
        return self.balance
    
    def deposit_money(self,amount):
        if amount <= 0:
            print('Error: Amount must be positive')
        self.balance += amount
    
    def withdraw_money(self, amount):
        if amount <=0:
            print('Error: Amount must be positive')
        if amount > self.balance:
            print('Error: Insufficient funds')
        self.balance -= amount
    
    def get_account_details(self):
        return f"Account Holder: {self.holder_name}, Account Number: {self.acc_number}, Balance: ${self.balance}"


# Example usage
account = BankAccount("John Doe", 1000, "12345")

# Depositing money
account.deposit_money(500)
print(account.current_balance())  # Will print 1500

# Trying to deposit negative amount
account.deposit_money(-100)  # Will print error message

# Withdrawing money
account.withdraw_money(200)
print(account.current_balance())  # Will print 1300

# Trying to withdraw more than balance
account.withdraw_money(2000)  # Will print error message