
class InvalidAmountError(Exception):
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"Invalid Transaction Amount : {self.amount}"


class InsufficientBalanceError(Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance

    def __str__(self):
        return f"Insufficient balance {self.balance} for transaction amount {self.amount}"

class SavingsAccount:
    def __init__(self, acno, ahname, balance):
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0 :
            raise InvalidAmountError(amount)

        if amount > self.balance:
            raise InsufficientBalanceError(amount, self.balance)

        self.balance -= amount


a = SavingsAccount(1, "Mike", 10000)
a.withdraw(-10)
#a.withdraw(15000)