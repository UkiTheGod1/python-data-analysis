import pandas as pd
from preprocessing import prepare_data

data = pd.read_csv('books.csv')
df = prepare_data(data)

# print(df.describe(include='all')) # Pokazuje sve 

average_price = df["price"].mean() # Average
print(f"Average book price: ${average_price:.2f}")

average_page_count = df["page_count"].mean()
print(f"Average amount of pages per book: {average_page_count:.2f}") 