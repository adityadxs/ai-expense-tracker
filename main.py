# main.py – Expense Tracker Menu (Skeleton)

def add_expense():
    print("Add expense feature (to be implemented)")

def view_expenses():
    print("View expenses feature (to be implemented)")

def main():
    while True:
        print("\n=== Expense Tracker Menu ===")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()