import pandas as pd
df = pd.read_csv("books.csv")

df['times_borrowed'] = df['times_borrowed'].astype('Int32')
df['page_count'] = df['page_count'].astype('Int32')

print(df.dtypes)
