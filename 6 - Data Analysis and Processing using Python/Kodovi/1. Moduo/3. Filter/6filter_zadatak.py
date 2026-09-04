import pandas as pd
df = pd.read_csv('books.csv')

df = df.set_index('catalog_position')
filtered = df.filter(like="A2", axis=0).filter(items=['title', 'page_count'])
print(filtered)

print(df['page_count'].median())