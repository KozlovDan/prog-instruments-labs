import json
from lab_6.transaction import Transaction

class Account:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount: float):
        self._validate_amount(amount)
        self.balance += amount
        self._record_transaction("Deposit", amount)

    def withdraw(self, amount: float):
        self._validate_amount(amount)
        self._validate_funds(amount)
        self.balance -= amount
        self._record_transaction("Withdraw", amount)

    def get_balance(self):
        return self.balance

    def _validate_amount(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be positive")

    def _validate_funds(self, amount: float):
        if amount > self.balance:
            raise ValueError("Insufficient funds")

    def _record_transaction(self, description: str, amount: float):
        self.transactions.append(Transaction(description, amount))

    def save_transactions(self, filepath: str):
        data = [{"description": t.description, "amount": t.amount} for t in self.transactions]
        self._write_file(filepath, data)

    def load_transactions(self, filepath: str):
        data = self._read_file(filepath)
        self.transactions = [Transaction(d["description"], d["amount"]) for d in data]


    @staticmethod
    def _write_file(filepath: str, data):
        with open(filepath, "w") as f:
            json.dump(data, f)

    @staticmethod
    def _read_file(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)
