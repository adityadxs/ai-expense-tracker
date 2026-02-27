# signup.py – User Registration
import csv
import os
import hashlib

def hash_password(password):
    """Return SHA-256 hash of the password (as hex string)."""
    return hashlib.sha256(password.encode()).hexdigest()

def user_exists(username):
    """Check if username already exists in users.csv."""
    if not os.path.exists("users.csv"):
        return False
    with open("users.csv", "r") as file:
        reader = csv.reader(file)
        next(reader, None)  # skip header if exists
        for row in reader:
            if row and row[0] == username:
                return True
    return False

def signup():
    print("\n--- Sign Up ---")
    username = input("Choose a username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return

    if user_exists(username):
        print("Username already taken. Please choose another.")
        return

    password = input("Choose a password: ")
    if not password:
        print("Password cannot be empty.")
        return

    password_hash = hash_password(password)

    # Append to users.csv
    file_exists = os.path.exists("users.csv")
    with open("users.csv", "a", newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["username", "password_hash"])
        writer.writerow([username, password_hash])

    print(f"User '{username}' created successfully!")

if __name__ == "__main__":
    signup()