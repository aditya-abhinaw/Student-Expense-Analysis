from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "expenses.csv"
OUTPUT_DIR = BASE_DIR / "output"

COLUMNS = ["date", "description", "category", "amount"]
DATE_FORMAT = "%Y-%m-%d"
CATEGORIES = ["Food", "Travel", "Books", "Entertainment", "Rent", "Other"]
MAX_AMOUNT = 1000000
