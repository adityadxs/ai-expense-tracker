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
