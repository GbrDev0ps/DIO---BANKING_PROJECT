class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"You deposited ${amount:.2f}. Your balance now is: ${self.balance:.2f}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrew the value of ${amount:.2f}. Your balance now is: ${self.balance:.2f}"
    
    def bank_statement(self):
        return f"Actual balance: ${self.balance:.2f}"


account = BankAccount()
print(account.deposit(100))
print(account.withdraw(50))
print(account.bank_statement())