import os
import csv

def view_expenses(username):
    print(f"\n--- {username}'s Expenses ---")
    if not os.path.exists("expenses.csv"):
        print("No expenses found.")
        return

    total = 0.0
    count = 0
    print(f"{'Date':<12} {'Name':<20} {'Amount':>10}")
    print("-" * 45)

    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        next(reader, None)  # skip header

        for row in reader:
            if not row or row[0] != username:
                continue

            # Determine format based on row length
            if len(row) == 4:   # New format: username, date, name, amount
                expense_date = row[1]
                name = row[2]
                try:
                    amount = float(row[3])
                except ValueError:
                    continue
            elif len(row) == 3:  # Old format: username, name, amount (no date)
                expense_date = "N/A"
                name = row[1]
                try:
                    amount = float(row[2])
                except ValueError:
                    continue
            else:
                continue  # Skip any malformed rows

            total += amount
            count += 1
            print(f"{expense_date:<12} {name:<20} ${amount:>9.2f}")

    if count == 0:
        print("No expenses yet.")
    else:
        print("-" * 45)
        print(f"{'TOTAL':<34} ${total:>9.2f}")
