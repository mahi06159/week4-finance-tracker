from finance_tracker.expense import Expense

def test_valid_expense():
    e = Expense("2025-01-10", 500, "Food", "Lunch")
    assert e.is_valid() == True

def test_invalid_amount():
    e = Expense("2025-01-10", -100, "Food", "Invalid")
    assert e.is_valid() == False

def test_invalid_date():
    e = Expense("10-01-2025", 200, "Food", "Wrong date")
    assert e.is_valid() == False
