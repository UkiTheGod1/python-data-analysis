import pandas as pd
df = pd.read_csv('books.csv')
df['last_borrowed_date'] = pd.to_datetime(df['last_borrowed_date'], format='%d_%b_%y', errors='coerce')
df.sort_values(by=["last_borrowed_date"], inplace=True)
print(df.filter(items=['title','author', 'last_borrowed_date']).head(30))

# 'years': df['last_borrowed_date'].dt.year,
# 'months': df['last_borrowed_date'].dt.month,
# 'days': df['last_borrowed_date'].dt.day

# Pristupanje samo godini, mesecu ili danu preko .dt