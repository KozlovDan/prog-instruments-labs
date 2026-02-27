class Transaction:
    def __init__(self, description: str, amount: float):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")
        self.description = description
        self.amount = amount
