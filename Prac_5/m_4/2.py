import deal


class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self._invariant()

    @deal.inv(lambda self: self.balance >= 0)
    def _invariant(self):
        pass

    @deal.pre(lambda self, amount: amount > 0)
    @deal.post(lambda self, amount, result: result == self.balance - amount)
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    @deal.pre(lambda self, amount: amount > 0)
    @deal.post(lambda self, amount, result: result == self.balance + amount)
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    @deal.ensure(lambda self, amount, result: result >= amount)
    def get_balance(self):
        return self.balance
