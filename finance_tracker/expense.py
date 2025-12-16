from datetime import datetime

class Expense:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

    def is_valid(self):
        try:
            datetime.strptime(self.date, "%Y-%m-%d")
            if self.amount <= 0:
                return False
            if not self.category:
                return False
            return True
        except ValueError:
            return False

    def to_dict(self):
        return {
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "description": self.description
        }
