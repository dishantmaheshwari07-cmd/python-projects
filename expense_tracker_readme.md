# 📊 Advanced Multi-Account Expense Tracker

### 📝 Project Description
A powerful, interactive Command Line Interface (CLI) application built in Python to manage personal finances. Unlike basic trackers, this project supports **multiple user accounts**, dynamic account switching, and automated file-based data persistence.

### 🚀 Key Features
* **Multi-Account Support:** Create separate financial profiles/accounts for different users or purposes.
* **Smart Account Switching:** Easily switch between active profiles during runtime without losing current data.
* **File I/O Persistence:** Automatically creates and updates individual data files (`.txt` logs) for each user to save balance and transaction records.
* **Income & Expense Logs:** Track income, categorize expenses, and add custom short descriptions for every transaction.
* **Duplicate-Free History:** Displays a clean transaction history by filtering out redundant entries using uniqueness checks.
* **Robust Input Validation:** Uses custom exception handling to prevent crashes from invalid user inputs (e.g., entering text instead of numbers).

### 🛠️ Tech Stack & Concepts Used
* **Language:** Python 3 (Developed seamlessly on Pydroid 3)
* **Object-Oriented Programming (OOP):** Custom `expense_tracker` class utilizing constructors (`__init__`), instance variables, methods, and state updates.
* **File Handling:** Read/Write operations using context managers (`with open()`) to save data safely.
* **Error & Exception Handling:** Structured `try...except ValueError` blocks for bulletproof user inputs.
* **Data Management:** Efficient usage of lists, nested lists for histories, enumeration (`enumerate`), and dictionaries for tracking user-file mappings.
