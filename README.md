# Student Expense Analysis System

Menu-driven terminal project to record and analyse daily student expenses using Python, Pandas, Matplotlib and a CSV file.

## Folder Structure

student_expense_system/
├── main.py            entry point
├── config.py          paths and constants
├── storage.py         load, clean, save, add, delete (CSV)
├── analysis.py        totals, monthly, category-wise, highest/lowest
├── charts.py          bar chart and pie chart
├── menu.py            input validation and menu
├── requirements.txt
├── README.md
├── data/
│   └── expenses.csv   sample data
└── output/            charts are saved here

## Setup and Run (Windows 11)

1. Install Python 3.9+  (tick "Add Python to PATH").
2. Open Command Prompt and go to the project folder:

   cd path\to\student_expense_system

3. Create and activate a virtual environment:

   python -m venv venv
   venv\Scripts\activate

   (PowerShell: if blocked, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` first.)

4. Install libraries and run:

   pip install -r requirements.txt
   python main.py

## CSV Format

date,description,category,amount
2026-10-03,Auto fare,Travel,220

## Validation

- Date must be `YYYY-MM-DD`; amount must be a number greater than 0.
- Description cannot be empty; category is chosen from a numbered list.
- Invalid or incomplete CSV rows are skipped with a warning and are removed from the file the next time you add or delete an expense.
- A missing or empty CSV file is created automatically.
