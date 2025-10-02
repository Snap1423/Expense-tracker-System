# 🧾 Expense Tracker (Python CLI)

A simple **command-line Expense Tracker** built using Python and CSV.  
This program allows you to **add, view, and calculate total expenses** with ease.  

---

## 📌 Features
- ✅ Add expenses with **date, category, amount, and description**  
- ✅ View all your expenses in a clean tabular format  
- ✅ Get the **total of all expenses** instantly 
- ✅ **Filter expenses** by category (e.g., only Food or Travel) 
- ✅ Data is stored in a **CSV file (Expense.csv)** for persistence  
- ✅ Simple **menu-based CLI** with options  

---

## 🛠️ Tech Stack
- Python 3  
- CSV module (for file handling)  
- OS & Datetime libraries  

---

## 📂 File Structure
📦 Expense-Tracker
┣ 📜 Expense.csv # Stores your expenses (auto-created)
┣ 📜 main.py # Main program file
┗ 📜 README.md # Project documentation

---

## 🚀 How to Run
1. Clone this repository  
 git clone https://github.com/Snap-1423/Expense-Tracker.git
Navigate into the project folder

cd Expense-Tracker

Run the Python program:

python main.py

---

## 📖 Usage
Once you run the program, you’ll see a menu:

=============EXPENSE TRACKER=================

1. Add Expenses
2. View Expenses
3. Show Total Expenses
4. Exit
Option 1 → Add new expense (Category, Amount, Description)

Option 2 → View all expenses stored in Expense.csv

Option 3 → Show total sum of all expenses

Option 4 → Exit the program

---

## 📸 Example
=============EXPENSE TRACKER=================

1. Add Expenses
2. View Expenses
3. Show Total Expenses
4. Filter by Category
5. Exit

## Adding an Expense
Enter a choice between 1 to 5: 1
Category (Food🍜/Travel✈️/Shopping🏬/Others): Food
Enter the amount💵: 200
Description📄: Lunch at cafe
Added Expenses!✅

## Viewing Expenses
['Date', 'Category', 'Amount', 'Description']
['2025-10-02', 'Food', '250', 'Lunch with friends']
['2025-10-02', 'Travel', '100', 'Bus ticket']

## Filtering by Category (Food)
Expenses in category: food
['2025-10-02', 'Food', '250', 'Lunch with friends']
Total in category 'food': 250

---

## 💡Future Improvements
Add monthly/weekly reports

Export expenses as Excel or PDF

Add income tracking

GUI/Flask web version

