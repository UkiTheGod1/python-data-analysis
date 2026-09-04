import pandas as pd
from preprocessing import prepare_data
data = pd.read_csv('books.csv')
df = prepare_data(data)

median_price = df["price"].median()
print(f"Median book price: ${median_price:.2f}")

median_page_count = df["page_count"].median()
print(f"Median page count: {median_page_count:.2f}")