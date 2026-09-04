import pandas as pd
from preprocessing import prepare_data
data = pd.read_csv('books.csv')
df = prepare_data(data)

missing_count = df['title'].isna().sum()
print("Missing values count in the column 'title':", missing_count)
df['title'] = df['title'].fillna("Unknown Title")