from config import DATA_FILE
from menu import run_menu
from storage import load_expenses


def main():
    try:
        expenses, issues = load_expenses(DATA_FILE)
    except (OSError, ValueError) as error:
        print(f"Error: {error}")
        return
    print(f"Loaded {len(expenses)} valid expense(s).")
    for issue in issues:
        print(f"  Warning: {issue}")
    run_menu(expenses, issues)


if __name__ == "__main__":
    main()
