from expense import Expense

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        if expense.is_valid():
            self.expenses.append(expense)
            return True
        return False

    def get_all(self):
        return self.expenses

    def search_by_category(self, category):
        return [e for e in self.expenses if e.category.lower() == category.lower()]
