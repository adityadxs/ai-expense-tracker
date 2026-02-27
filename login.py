import csv
import os
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login():
    print("\n--- Log In ---")
    username = input("Username: ").strip()
    password = input("Password: ")

    if not os.path.exists("users.csv"):
        print("No users registered yet. Please sign up first.")
        return None

    with open("users.csv", "r") as file:
        reader = csv.reader(file)
        # Debug: print all rows
        rows = list(reader)
        print("Rows in users.csv:", rows)
        
        # Check if first row is header
        if rows and rows[0] and rows[0][0] == "username":
            print("Header found, skipping...")
            data_rows = rows[1:]
        else:
            data_rows = rows
        
        for row in data_rows:
            print("Checking row:", row)  # Debug
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

if __name__ == "__main__":
    user = login()
    if user:
        print(f"Logged in as: {user}")
    else:
        print("Login failed.")
        