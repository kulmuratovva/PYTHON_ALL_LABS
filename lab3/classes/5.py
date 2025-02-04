class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"You have deposited {amount}."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        else:
            self.balance -= amount
            return f"You're balance: {self.balance}, and you withdrew {amount}."

    def get_balance(self):
        return self.balance

    def get_owner(self):
        return self.owner

bank = Bank("Chanel", 1000)

print(bank.get_balance())
print(bank.get_owner())
print(bank.deposit(1000))
print(bank.withdraw(3000))
print(bank.withdraw(2000))