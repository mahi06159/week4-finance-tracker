from expense import Expense
from expense_manager import ExpenseManager
from file_handler import load_expenses, save_expenses, export_to_csv
from reports import monthly_report, category_report
from utils import get_float_input

class FinanceTracker:
    def __init__(self):
        self.manager = ExpenseManager()
        for e in load_expenses():
            self.manager.expenses.append(
                Expense(e["date"], e["amount"], e["category"], e["description"])
            )

    def add_expense(self):
        date = input("Date (YYYY-MM-DD): ")
        amount = get_float_input("Amount: ")
        category = input("Category: ")
        desc = input("Description: ")

        expense = Expense(date, amount, category, desc)
        if self.manager.add_expense(expense):
            save_expenses([e.to_dict() for e in self.manager.get_all()])
            print("Expense added successfully!")
        else:
            print("Invalid expense data.")

    def view_expenses(self):
        for e in self.manager.get_all():
            print(e.date, e.amount, e.category, e.description)

    def run(self):
        while True:
            print("\n1.Add 2.View 3.Export 0.Exit")
            ch = input("Choice: ")
            if ch == "1":
                self.add_expense()
            elif ch == "2":
                self.view_expenses()
            elif ch == "3":
                export_to_csv([e.to_dict() for e in self.manager.get_all()])
                print("Exported to CSV.")
            elif ch == "0":
                break

def main():
    FinanceTracker().run()
