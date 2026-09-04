import pandas as pd
df = pd.read_csv('books.csv')
df.drop(0, axis=0, inplace=True)

print(df.head(10))