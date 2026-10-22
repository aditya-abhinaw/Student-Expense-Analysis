import matplotlib.pyplot as plt

from config import OUTPUT_DIR


def save_and_show(fig, filename):
    OUTPUT_DIR.mkdir(exist_ok=True)
    path = OUTPUT_DIR / filename
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"Chart saved to: {path}")
    plt.show()
    plt.close(fig)


def plot_category_bar(totals):
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(totals["Category"], totals["Total"], color="steelblue")
    ax.bar_label(bars, fmt="%.0f")
    ax.set_title("Category-wise Spending")
    ax.set_xlabel("Category")
    ax.set_ylabel("Amount (Rs.)")
    save_and_show(fig, "category_spending.png")


def plot_expense_pie(totals):
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(totals["Total"], labels=totals["Category"], autopct="%1.1f%%", startangle=90)
    ax.set_title("Expense Distribution")
    save_and_show(fig, "expense_distribution.png")
