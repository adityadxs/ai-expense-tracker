import csv
import os

print("=== Expense Tracker - Add Expense ===")

# Get expense name
expense_name = input("Enter expense name: ").strip()
if not expense_name:
    print("Expense name cannot be empty.")
    exit()

# Get expense amount
try:
    expense_amount = float(input("Enter amount: "))
    if expense_amount <= 0:
        print("Amount must be positive.")
        exit()
except ValueError:
    print("Invalid amount. Please enter a number.")
    exit()

# Define CSV file
csv_file = "expenses.csv"
file_exists = os.path.exists(csv_file)

# Open in append mode (creates file if it doesn't exist? Actually 'a' creates if missing, but we need header)
# Using 'a' will create the file if it doesn't exist, but then we write header only if file is new.
with open(csv_file, mode='a', newline='') as file:
    writer = csv.writer(file)
    
    # If file is new (didn't exist before opening), write header
    if not file_exists:
        writer.writerow(["name", "amount"])
        print("Created new expenses.csv file with headers.")
    
    # Write the expense data
    writer.writerow([expense_name, expense_amount])

print(f"✓ Saved: {expense_name} - ${expense_amount:.2f} to {csv_file}")
print(f"File location: {os.path.abspath(csv_file)}")