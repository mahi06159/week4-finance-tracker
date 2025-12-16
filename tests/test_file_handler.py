from finance_tracker.file_handler import save_expenses, load_expenses

def test_save_and_load():
    sample_data = [
        {
            "date": "2025-01-10",
            "amount": 100,
            "category": "Transport",
            "description": "Bus"
        }
    ]

    save_expenses(sample_data)
    data = load_expenses()

    assert len(data) >= 1
    assert data[-1]["category"] == "Transport"
