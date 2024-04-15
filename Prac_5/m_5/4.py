class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"{amount} средств успешно зачислены на счет {self.account_number}"

    def withdraw(self, amount):
        self.balance -= amount
        return f"{amount} средств успешно сняты с счета {self.account_number}"

    def check_balance(self):
        return f"Баланс счета {self.account_number}: {self.balance}"

import unittest

class TestBankAccount(unittest.TestCase):
    def test_create_account(self):
        account = BankAccount("12345", 100)
        self.assertEqual(account.account_number, "12345")
        self.assertEqual(account.balance, 100)

    def test_deposit(self):
        account = BankAccount("12345")
        message = account.deposit(50)
        self.assertEqual(account.balance, 50)
        self.assertEqual(message, "50 средств успешно зачислены на счет 12345")

    def test_withdraw_sufficient_funds(self):
        account = BankAccount("12345", 100)
        message = account.withdraw(50)
        self.assertEqual(account.balance, 50)
        self.assertEqual(message, "50 средств успешно сняты с счета 12345")

    def test_withdraw_insufficient_funds(self):
        account = BankAccount("12345", 50)
        message = account.withdraw(100)
        self.assertEqual(account.balance, 50)
        self.assertEqual(message, "Недостаточно средств на счете 12345")

    def test_check_balance(self):
        account = BankAccount("12345", 100)
        balance_message = account.check_balance()
        self.assertEqual(balance_message, "Баланс счета 12345: 100")

    def test_deposit_negative_amount(self):
        account = BankAccount("12345", 100)
        message = account.deposit(-50)
        self.assertEqual(account.balance, 100)
        self.assertEqual(message, "Сумма для зачисления должна быть положительной")

    def test_withdraw_negative_amount(self):
        account = BankAccount("12345", 100)
        message = account.withdraw(-50)
        self.assertEqual(account.balance, 100)
        self.assertEqual(message, "Сумма для снятия должна быть положительной")

    def test_withdraw_from_zero_balance(self):
        account = BankAccount("12345")
        message = account.withdraw(50)
        self.assertEqual(account.balance, 0)
        self.assertEqual(message, "Недостаточно средств на счете 12345")

    def test_default_balance(self):
        account = BankAccount("12345")
        self.assertEqual(account.balance, 0)

    def test_account_equality(self):
        account1 = BankAccount("12345", 100)
        account2 = BankAccount("54321", 100)
        self.assertNotEqual(account1, account2)

    def test_transfer(self):
        account1 = BankAccount("12345", 100)
        account2 = BankAccount("54321", 50)
        account1.transfer(account2, 25)
        self.assertEqual(account1.balance, 75)
        self.assertEqual(account2.balance, 75)

    def test_transfer_invalid_account(self):
        account1 = BankAccount("12345", 100)
        message = account1.transfer(None, 50)
        self.assertEqual(account1.balance, 100)
        self.assertEqual(message, "Невозможно выполнить перевод: недопустимый счет")

if __name__ == '__main__':
    unittest.main()
