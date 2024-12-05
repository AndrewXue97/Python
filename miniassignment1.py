# Student ID: 101004154
# Name: Andrew Xue

class BankAccount:
    def __init__(self, owner, balance):
        self._owner = owner
        self._balance = balance
        self.transactions = []

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, name):
        if isinstance(name, str) and len(name) > 10:
            self._owner = name
        else:
            raise ValueError("Name isn't a string or not 10 characters.")

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self._balance = value
        else:
            raise ValueError("Balance can't be a negative number, must be positive.")

    def __str__(self):
        return f"Owner: {self.owner}, Balance: {self.balance}"

    def deposit(self, amount):
        if isinstance(amount, (int, float)) and amount > 1:
            self.balance += amount
            self.transactions.append(f"Deposit: ${amount}")
        else:
            raise ValueError("Deposit has to be greater than 1")

    def withdraw(self, amount):
        if isinstance(amount, (int, float)) and amount < self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdraw: ${amount}")
        else:
            raise ValueError("Withdrawal can't be more than balance")

    def display_balance(self):
        print(f"Balance: {self.balance}")

    def display_transactions(self):
        for num, transaction in enumerate(self.transactions, start=1):
            print(f"{num}) {transaction}")
