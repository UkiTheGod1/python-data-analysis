import pandas as pd
df = pd.read_csv('books.csv')
df['total_copies'] = pd.to_numeric(df['total_copies'], errors='coerce') #
mask = (df['genre'] == 'Science') & (df['total_copies'] < 4)
filtered_books = df[mask]
print(filtered_books.filter(items=['title', 'total_copies']))

# Konvertovanje u int ili float kada postoje celije koje ne mogu da se promene sa .astype