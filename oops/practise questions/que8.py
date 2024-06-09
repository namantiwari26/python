'''Implement a Python class named BankAccount representing a bank account, 
incorporating attributes such as accountNumber, name, and balance. Provide
 a complete code for the BankAccount class with various methods.
'''
class BankAccount:
    def __init__(self, account_number, name, balance=10000):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

# Example usage:
while True:
    acc = BankAccount("123456", "Alice")
    uc=int(input("""
1 get balance
2 deposit
3 withdraw
4 exit                 
                      
""" ))  
    if uc==1:
        print("current balance:",acc.get_balance())
    elif uc==2:
        n=int(input("Enter the amount:---"))
        acc.deposit(n)
        print("current balance:",acc.get_balance())

        
    elif uc==3:
        m=int(input("Enter the amount:---"))
        acc.withdraw(m)
        print("current balance:",acc.get_balance())
    else:
        break    

#oooorrrrrrr

class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} successful. Current balance: ${self.balance}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. Current balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.balance

    def display_info(self):
        print(f"Account Holder: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance}")

# Example usage:
account1 = BankAccount("123456", "John Doe", 1000)
account1.display_info()  # Display account info
account1.deposit(500)    # Deposit $500
account1.withdraw(200)   # Withdraw $200
account1.withdraw(2000)  # Try to withdraw $2000 (not enough balance)



