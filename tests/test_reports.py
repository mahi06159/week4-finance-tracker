from finance_tracker.reports import monthly_report, category_report

def test_monthly_report():
    expenses = [
        {"date": "2025-01-05", "amount": 200, "category": "Food"},
        {"date": "2025-02-10", "amount": 300, "category": "Food"}
    ]

    total = monthly_report(expenses, "2025-01")
    assert total == 200

def test_category_report():
    expenses = [
        {"category": "Food", "amount": 100},
        {"category": "Food", "amount": 200},
        {"category": "Travel", "amount": 300}
    ]

    result = category_report(expenses)
    assert result["Food"] == 300
    assert result["Travel"] == 300
