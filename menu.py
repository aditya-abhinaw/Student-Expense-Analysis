from datetime import datetime

from analysis import category_totals, highest_expense, lowest_expense, monthly_spending, total_expenses
from charts import plot_category_bar, plot_expense_pie
from config import CATEGORIES, DATA_FILE, DATE_FORMAT, MAX_AMOUNT
from storage import add_expense, delete_expense, save_expenses

MENU_TEXT = """
========== Student Expense Analysis System ==========
1. Add expense
2. View all expenses
3. Delete expense
4. Summary (total, highest, lowest)
5. Monthly spending
6. Category-wise totals
7. Bar chart: category-wise spending
8. Pie chart: expense distribution
9. Exit
"""


def input_date():
    while True:
        text = input("Date (YYYY-MM-DD, press Enter for today): ").strip()
        if not text:
            return datetime.today()
        try:
            return datetime.strptime(text, DATE_FORMAT)
        except ValueError:
            print("Invalid date. Use the format YYYY-MM-DD.")


def input_description():
    while True:
        text = input("Description: ").strip()
        if text:
            return text
        print("Description cannot be empty.")


def input_category():
    for number, name in enumerate(CATEGORIES, start=1):
        print(f"  {number}. {name}")
    while True:
        text = input(f"Choose category (1-{len(CATEGORIES)}): ").strip()
        if text.isdigit() and 1 <= int(text) <= len(CATEGORIES):
            return CATEGORIES[int(text) - 1]
        print("Invalid category number.")


def input_amount():
    while True:
        text = input("Amount (Rs.): ").strip()
        try:
            amount = float(text)
        except ValueError:
            print("Amount must be a number.")
            continue
        if 0 < amount <= MAX_AMOUNT:
            return round(amount, 2)
        print(f"Amount must be greater than 0 and at most {MAX_AMOUNT}.")


def show_table(df):
    table = df.copy()
    table["date"] = table["date"].dt.strftime(DATE_FORMAT)
    table.index = range(1, len(table) + 1)
    table.index.name = "No"
    print(table.to_string())


def add_new_expense(df):
    date = input_date()
    description = input_description()
    category = input_category()
    amount = input_amount()
    df = add_expense(df, date, description, category, amount)
    save_expenses(df, DATA_FILE)
    print("Expense added successfully.")
    return df


def delete_existing_expense(df):
    show_table(df)
    text = input("Enter the No of the expense to delete: ").strip()
    if not (text.isdigit() and 1 <= int(text) <= len(df)):
        print("Invalid number.")
        return df
    if input("Delete this expense? (y/n): ").strip().lower() != "y":
        print("Deletion cancelled.")
        return df
    df = delete_expense(df, int(text))
    save_expenses(df, DATA_FILE)
    print("Expense deleted.")
    return df


def print_expense(label, row):
    print(f"{label}: Rs. {row['amount']:.2f} - {row['description']} "
          f"({row['category']}, {row['date'].strftime(DATE_FORMAT)})")


def show_summary(df):
    print(f"\nTotal expenses : Rs. {total_expenses(df):.2f}")
    print(f"Entries        : {len(df)}")
    print_expense("Highest expense", highest_expense(df))
    print_expense("Lowest expense ", lowest_expense(df))


def run_menu(df, issues):
    needs_data = {"2", "3", "4", "5", "6", "7", "8"}
    while True:
        print(MENU_TEXT)
        try:
            choice = input("Enter your choice (1-9): ").strip()
            if choice == "9":
                print("Thank you for using the system. Goodbye!")
                break
            if choice == "1":
                df = add_new_expense(df)
            elif choice not in needs_data:
                print("Invalid choice. Please enter a number from 1 to 9.")
            elif df.empty:
                print("No expenses recorded yet. Add an expense first.")
            elif choice == "2":
                show_table(df)
            elif choice == "3":
                df = delete_existing_expense(df)
            elif choice == "4":
                show_summary(df)
            elif choice == "5":
                print(monthly_spending(df).to_string(index=False))
            elif choice == "6":
                print(category_totals(df).to_string(index=False))
            elif choice == "7":
                plot_category_bar(category_totals(df))
            elif choice == "8":
                plot_expense_pie(category_totals(df))
        except (EOFError, KeyboardInterrupt):
            print("\nExiting. Goodbye!")
            break
