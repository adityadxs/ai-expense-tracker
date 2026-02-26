import csv
import os

csv_file = "expenses.csv"

if not os.path.exists(csv_file):
    print("No expenses found. Please add some expenses first.")
    exit()

print("\n=== Your Expenses ===")
print(f"{'Name':<20} {'Amount':>10}")
print("-" * 32)

total = 0.0
valid_rows = 0

with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    
    for row in reader:
        # Skip empty lines or lines that don't have two fields
        if len(row) != 2:
            continue
        
        name = row[0]
        try:
            amount = float(row[1])
        except ValueError:
            print(f"Skipping invalid amount in row: {row}")
            continue
            
        total += amount
        valid_rows += 1
        print(f"{name:<20} ${amount:>9.2f}")

if valid_rows == 0:
    print("No valid expense entries found.")

print("-" * 32)
print(f"{'TOTAL':<20} ${total:>9.2f}")