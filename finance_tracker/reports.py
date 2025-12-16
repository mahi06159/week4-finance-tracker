def monthly_report(expenses, month):
    total = 0
    for e in expenses:
        if e["date"].startswith(month):
            total += e["amount"]
    return total

def category_report(expenses):
    summary = {}
    for e in expenses:
        cat = e["category"]
        summary[cat] = summary.get(cat, 0) + e["amount"]
    return summary
