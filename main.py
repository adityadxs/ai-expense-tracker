import csv
import os
import hashlib
from datetime import date

# ---------- User Authentication ----------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def user_exists(username):
    if not os.path.exists("users.csv"):
        return False
    with open("users.csv", "r") as file:
        reader = csv.reader(file)
        next(reader, None)  # skip header
        for row in reader:
            if row and row[0] == username:
                return True
    return False

def signup():
    print("\n--- Sign Up ---")
    username = input("Choose a username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return None
    if user_exists(username):
        print("Username already taken.")
        return None
    password = input("Choose a password: ")
    if not password:
        print("Password cannot be empty.")
        return None
    password_hash = hash_password(password)

    file_exists = os.path.exists("users.csv")
    with open("users.csv", "a", newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["username", "password_hash"])
        writer.writerow([username, password_hash])
    print(f"User '{username}' created successfully!")
    return username

def login():
    print("\n--- Log In ---")
    username = input("Username: ").strip()
    password = input("Password: ")
    if not os.path.exists("users.csv"):
        print("No users registered yet. Please sign up first.")
        return None
    with open("users.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            if row and row[0] == username:
                stored_hash = row[1]
                if hash_password(password) == stored_hash:
                    print(f"Login successful! Welcome, {username}.")
                    return username
                else:
                    print("Incorrect password.")
                    return None
    print("Username not found.")
    return None

# ---------- Expense Functions ----------
def add_expense(username):
    print("\n--- Add Expense ---")
    expense_name = input("Enter expense name: ").strip()
    if not expense_name:
        print("Expense name cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    # Automatically set date to today
    expense_date = date.today().isoformat()  # Format: YYYY-MM-DD

    csv_file = "expenses.csv"
    file_exists = os.path.exists(csv_file)

    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            # Write header with date column
            writer.writerow(["username", "date", "name", "amount"])
        writer.writerow([username, expense_date, expense_name, amount])

    print(f"✓ Saved: {expense_date} - {expense_name} - ${amount:.2f}")

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
        header = next(reader, None)  # skip header (we don't rely on it for parsing)

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
                # Unexpected format – skip
                continue

            total += amount
            count += 1
            print(f"{expense_date:<12} {name:<20} ${amount:>9.2f}")

    if count == 0:
        print("No expenses yet.")
    else:
        print("-" * 45)
        print(f"{'TOTAL':<34} ${total:>9.2f}")

# ---------- Main Menu ----------
def expense_menu(username):
    while True:
        print(f"\n=== Expense Tracker (Logged in as {username}) ===")
        print("1. Add an expense")
        print("2. View my expenses")
        print("3. Logout")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_expense(username)
        elif choice == '2':
            view_expenses(username)
        elif choice == '3':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def main():
    while True:
        print("\n=== Welcome to Expense Tracker ===")
        print("1. Login")
        print("2. Sign Up")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            user = login()
            if user:
                expense_menu(user)
        elif choice == '2':
            user = signup()
            if user:
                print(f"Auto-login successful! Welcome, {user}.")
                expense_menu(user)  # Directly go to expense menu
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
