
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

DATA_FILE = 'expenses.csv'

if not os.path.exists(DATA_FILE):
    df_init = pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Description'])
    df_init.to_csv(DATA_FILE, index=False)

def add_expense(date, category, amount, description):
    new_expense = {
        'Date': date,
        'Category': category,
        'Amount': amount,
        'Description': description
    }
    df = pd.read_csv(DATA_FILE)
    df = pd.concat([df, pd.DataFrame([new_expense])], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)
    print("\n✅ Expense added successfully!")

def view_total_expenses():
    df = pd.read_csv(DATA_FILE)
    total = df['Amount'].sum()
    print(f"\n💰 Total expenses: ₹{total:.2f}")

def plot_category_spending():
    df = pd.read_csv(DATA_FILE)
    if df.empty:
        print("\n⚠️ No data to plot.")
        return
    category_sum = df.groupby('Category')['Amount'].sum()
    category_sum.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title('Spending by Category')
    plt.ylabel('')
    plt.show()

def plot_monthly_spending():
    df = pd.read_csv(DATA_FILE)
    if df.empty:
        print("\n⚠️ No data to plot.")
        return
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])
    df['Month'] = df['Date'].dt.to_period('M')
    monthly_sum = df.groupby('Month')['Amount'].sum()
    monthly_sum.plot(kind='bar')
    plt.title('Monthly Spending Trend')
    plt.xlabel('Month')
    plt.ylabel('Amount Spent')
    plt.show()

def main():
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Total Expenses")
        print("3. Plot Category Spending")
        print("4. Plot Monthly Spending")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            date = input("Date (YYYY-MM-DD): ")
            category = input("Category: ")
            try:
                amount = float(input("Amount: "))
            except ValueError:
                print("❌ Invalid amount. Please enter a number.")
                continue
            description = input("Description: ")
            add_expense(date, category, amount, description)

        elif choice == '2':
            view_total_expenses()

        elif choice == '3':
            plot_category_spending()

        elif choice == '4':
            plot_monthly_spending()

        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1-5.")

if __name__ == "__main__":
    main()
