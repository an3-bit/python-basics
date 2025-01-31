class Account:
    def __init__(self, full_name, phone_number, balance, account_number):
        self.full_name = full_name
        self.phone_number = phone_number
        self.balance = float(balance)  # Ensure balance is numeric
        self.account_number = account_number

    def deposit(self, amount):
        amount = float(amount)  # Ensure amount is numeric
        self.balance += amount
        print(f"Amount {amount} deposited successfully to account {self.account_number}")

    def withdraw(self, amount):
        amount = float(amount)  # Ensure amount is numeric
        if self.balance < amount:
            print(f"Insufficient funds. Balance is {self.balance}")
        else:
            self.balance -= amount
            print(f"Amount {amount} withdrawn successfully from account {self.account_number}")

    def check_balance(self):
        print(f"Balance for account {self.account_number} is: {self.balance}")


kevo_acc = Account("Kevo Smith", "+1234567890", 0, "ACC12345")
kevo_acc.deposit(2000)
kevo_acc.withdraw(500)
kevo_acc.check_balance()





