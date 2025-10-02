import csv, os
import datetime

FILENAME = "Expense.csv"

# This will create a file if it doesn't exist.

if not os.path.exists(FILENAME):
    with open(FILENAME,'w',newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date","Category","Amount","Description"])

# To add expenses

def add_expenses():
    Date = datetime.datetime.now().strftime("%Y-%m-%d")
    Category = input("Category (Food🍜/Travel✈️/Shopping🏬/Others): ")
    Amount = int(input("Enter the amount💵: "))
    Description = input("Description📄: ")
    with open(FILENAME,'a',newline="")as f:
        writer = csv.writer(f) 
        writer.writerow([Date, Category, Amount, Description])
print("Add Your Expenses👇")

add_expenses()

# To view Expenses

def view_expenses():
    with open("Expense.csv",'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

view_expenses()

# To total the expenses

def total_expenses():
    total = 0 # inititalize the total
    with open("Expense.csv",'r') as f:
        reader = csv.reader(f)
        next(reader) # skips the header
        for row in reader:
            if row: # avoids the empty line
                total+= int(row[2])
    print(f"total expenses💰: {total}\n")

total_expenses()

# To Filter category 

def filter_category():
    category = input("Enter a Category to filter (Food/Travel/Shopping/Others): ")
    found = False
    with open(FILENAME,'r') as f:
        reader = csv.reader(f)
        next(reader) #Skips the header
        for row in reader:
            if row and row[1].lower()== category.lower():
                print(row)
                found = True
    if not found:
        print(f"No expense found in category: {category}")


filter_category()
        

# Menu function

while True:
    print("=============EXPENSE TRACKER=================\n")
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3. Show Total Expenses")
    print("4. Filter Category")
    print("5. Exit")

    choice = int(input("Enter a choice between 1 to 5: "))
    match choice:
        case 1:
            add_expenses()
        case 2:
            view_expenses()
        case 3:
            total_expenses()
        case 4:
            filter_category()
        case 5:
            print("Exiting.......Goodbye!")
        case _ :
            print("Invalid choice, try again!\n")





