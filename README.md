# Student Expense Analysis System

A Python-based application to record, manage, analyze, and visualize daily student expenses using Pandas, Matplotlib, and CSV file storage.

## Overview

The Student Expense Analysis System helps students track their daily spending, understand monthly expenses, and identify where their money goes. It provides a simple menu-driven interface and generates charts for category-wise expense analysis.

## Features

- Add, view, and delete expenses
- Store expense records in a CSV file
- Calculate total, highest, and lowest expenses
- Analyze monthly spending
- Calculate category-wise expense totals
- Generate bar charts and pie charts
- Validate user input and handle invalid CSV records
- Save generated charts as image files

## Technologies Used

- **Python** — application logic
- **Pandas** — data handling and analysis
- **Matplotlib** — data visualization
- **CSV** — expense data storage

## Project Structure

```text
student_expense_system/
├── main.py
├── config.py
├── storage.py
├── analysis.py
├── charts.py
├── menu.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   └── expenses.csv
└── output/
```

## Requirements

- Python 3.12 recommended
- pip
- Pandas
- Matplotlib

## Installation and Setup

### 1. Clone the repository

```powershell
git clone https://github.com/aditya-abhinaw/Student-Expense-Analysis.git
cd Student-Expense-Analysis
```

### 2. Create a virtual environment

```powershell
python -m venv venv
```

### 3. Activate the environment on Windows

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run this command in the current terminal and try again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### 4. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 5. Run the application

```powershell
python main.py
```

## How to Use

Choose an option from the application menu:

| Option | Operation |
|---|---|
| 1 | Add an expense |
| 2 | View all expenses |
| 3 | Delete an expense |
| 4 | View total, highest, and lowest expenses |
| 5 | View monthly spending |
| 6 | View category-wise totals |
| 7 | Generate a category-wise bar chart |
| 8 | Generate an expense distribution pie chart |
| 9 | Exit the application |

Enter dates in `YYYY-MM-DD` format and amounts as positive numbers.

## CSV Data Format

Expense records are stored in `data/expenses.csv`.

```csv
date,description,category,amount
2026-10-20,Lunch,Food,150
2026-10-20,Bus fare,Travel,40
2026-10-21,Notebook,Books,80
```

The application validates records and warns about invalid or incomplete rows.

## Output

The application displays expense summaries in the terminal and generates:

- `category_spending.png` — category-wise bar chart
- `expense_distribution.png` — expense distribution pie chart

Generated charts are saved in the `output/` directory.

## Learning Outcomes

This project demonstrates:

- Python functions, modules, loops, and conditional statements
- File handling and CSV data storage
- Input validation and exception handling
- Pandas DataFrames and data aggregation
- Matplotlib charts and data visualization
- Modular program design

## Future Enhancements

- Monthly budget limits and alerts
- Exportable expense reports
- A graphical user interface
- Expense search and filtering
- NumPy-based numerical analysis

## Author

**Abhinaw Aditya**

## License

This project was developed for educational purposes as part of the ITL-5 Python laboratory PBL.