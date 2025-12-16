import json
import csv
import os
from datetime import datetime

DATA_FILE = "data/expenses.json"
BACKUP_DIR = "data/backup/"
EXPORT_DIR = "data/exports/"

def load_expenses():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    os.makedirs(BACKUP_DIR, exist_ok=True)
    if os.path.exists(DATA_FILE):
        backup_name = BACKUP_DIR + "backup_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".json"
        os.rename(DATA_FILE, backup_name)

    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def export_to_csv(expenses):
    os.makedirs(EXPORT_DIR, exist_ok=True)
    with open(EXPORT_DIR + "expenses.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "amount", "category", "description"])
        writer.writeheader()
        for exp in expenses:
            writer.writerow(exp)
