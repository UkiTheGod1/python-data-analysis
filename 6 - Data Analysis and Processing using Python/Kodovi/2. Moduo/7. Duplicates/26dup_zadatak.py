import pandas as pd

df = pd.read_csv("books.csv")
print(df.duplicated(subset=['title', 'author']).sum())
duplicate_rows = df[df.duplicated(subset=['title', 'author'], keep=False)]
print(duplicate_rows.filter(items=['catalog_position', 'title', 'author']).sort_values(by='title'))

