# AI Expense Tracker (Python)

A terminal-based expense tracking application built step by step while learning Python, Data Structures, and Machine Learning concepts.

This project is part of my journey as a 3rd Year B.Tech CSE (AI & ML) student focused on building real-world projects from scratch.

---

## 📅 Day 01 Progress

### ✅ Expense Input System Implemented

- Created Python program to accept expense details from user
- Implemented input validation:
  - Prevent empty expense name
  - Ensure amount is numeric
  - Ensure amount is positive
- Designed structured user interaction in terminal

---

### 💾 CSV File Storage Implemented

- Implemented persistent storage using CSV file
- Automatically creates `expenses.csv` if not present
- Writes header row when file is created
- Appends new expense entries safely

---

### 📊 Expense Viewing Feature

- Reads stored expenses from CSV file
- Displays formatted expense table
- Calculates and displays total expense amount
- Handles invalid or corrupted rows gracefully

---

### 🧩 Program Structure Setup

- Created modular file structure:
  - `expense_tracker.py` → Add expense logic
  - `view_expenses.py` → View expense logic
  - `main.py` → Menu system (skeleton)

- Designed foundation for scalable project structure

---

### 🧠 Concepts Learned

- File handling in Python
- CSV read/write operations
- Input validation techniques
- Error handling using try/except
- Basic program structuring

---

### 🚧 Next Step (Day 02 Goal)

- Connect menu system with real functions
- Refactor code into reusable functions
- Improve project structure

- ## 📅 Day 02 Progress

### 🔐 User Authentication System

- Implemented user signup functionality
- Passwords stored securely using SHA-256 hashing
- Implemented login verification system
- Automatic login after successful signup

---

### 👤 Per-User Expense Management

- Updated expense storage to include username
- Each user can view only their own expenses
- Established user-specific data handling logic

CSV format updated:
username,date,name,amount

---

### 📅 Automatic Date Tracking

- Added automatic date stamp when expense is recorded
- Removed need for manual date input
- Ensured consistent record structure

---

### 🧩 Robust Data Handling

- Updated viewing logic to support:
  - Old records without date
  - New records with date
- Legacy data displays "N/A" for missing date

---

### 🔄 Application Flow Completed

Structured program flow implemented:

Welcome Screen  
→ Login / Signup  
→ Expense Menu  
→ Add Expense / View Expenses / Logout  
→ Return to Welcome

---

### 🧠 Concepts Learned

- Authentication fundamentals
- Password hashing for security
- Multi-user data management
- CSV structure evolution handling
- Real-world application flow design

---

🚧 Next Step: Add expense categories and spending analysis
