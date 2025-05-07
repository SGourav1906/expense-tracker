import pandas as pd
import matplotlib.pyplot as plt
import os

# Check if the CSV file exists
if os.path.exists("expenses.csv"):
    expenses = pd.read_csv("expenses.csv")
else:
    expenses = pd.DataFrame(columns=["Date", "Category", "Amount"])

def add_expense(date, category, amount):
    global expenses
    new_expense = {"Date": date, "Category": category, "Amount": amount}
    expenses = pd.concat([expenses, pd.DataFrame([new_expense])], ignore_index=True)

    expenses.to_csv("expenses.csv", index=False)
    print(f"Added: {new_expense}")

def view_expenses():
    print(expenses)

def plot_expenses():
    category_sum = expenses.groupby("Category")["Amount"].sum()
    plt.figure(figsize=(8,6))
    category_sum.plot(kind='bar')
    plt.title("Expenses by Category")
    plt.ylabel("Amount Spent")
    plt.xlabel("Category")
    plt.savefig("expenses_chart.png")
    print("Chart saved as expenses_chart.png")

# Example interaction
while True:
    print("\nChoose an option:")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Plot expenses")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        add_expense(date, category, amount)
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        plot_expenses()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")


 
