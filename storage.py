import pandas as pd

from config import COLUMNS, DATE_FORMAT


def create_empty_file(file_path):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(columns=COLUMNS).to_csv(file_path, index=False)


def sort_expenses(df):
    return df.sort_values("date", kind="stable").reset_index(drop=True)


def clean_expenses(df):
    df.columns = df.columns.str.strip().str.lower()
    missing = [col for col in COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"CSV is missing column(s): {', '.join(missing)}")

    df = df[COLUMNS].copy()
    df["description"] = df["description"].fillna("").astype(str).str.strip()
    df["category"] = df["category"].fillna("").astype(str).str.strip().str.title()
    dates = pd.to_datetime(df["date"], format=DATE_FORMAT, errors="coerce")
    amounts = pd.to_numeric(df["amount"], errors="coerce")

    valid = (
        dates.notna()
        & amounts.notna()
        & (amounts > 0)
        & (df["description"] != "")
        & (df["category"] != "")
    )
    issues = [f"Skipped CSV line {index + 2}: missing or invalid data." for index in df.index[~valid]]

    df["date"] = dates
    df["amount"] = amounts.astype(float)
    return sort_expenses(df[valid]), issues


def load_expenses(file_path):
    if not file_path.exists():
        create_empty_file(file_path)
    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        df = pd.DataFrame(columns=COLUMNS)
    except pd.errors.ParserError:
        raise ValueError("The CSV file is corrupted and cannot be read.")
    return clean_expenses(df)


def save_expenses(df, file_path):
    output = df.copy()
    output["date"] = output["date"].dt.strftime(DATE_FORMAT)
    output.to_csv(file_path, index=False)


def add_expense(df, date, description, category, amount):
    row = pd.DataFrame([{
        "date": pd.Timestamp(date),
        "description": description,
        "category": category,
        "amount": float(amount),
    }])
    if df.empty:
        return row
    return sort_expenses(pd.concat([df, row], ignore_index=True))


def delete_expense(df, number):
    return df.drop(df.index[number - 1]).reset_index(drop=True)
