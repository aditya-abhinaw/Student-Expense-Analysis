def total_expenses(df):
    return df["amount"].sum()


def monthly_spending(df):
    months = df["date"].dt.strftime("%Y-%m")
    totals = df.groupby(months)["amount"].sum().reset_index()
    totals.columns = ["Month", "Total"]
    return totals


def category_totals(df):
    totals = df.groupby("category")["amount"].sum().sort_values(ascending=False)
    return totals.reset_index().rename(columns={"category": "Category", "amount": "Total"})


def highest_expense(df):
    return df.loc[df["amount"].idxmax()]


def lowest_expense(df):
    return df.loc[df["amount"].idxmin()]
