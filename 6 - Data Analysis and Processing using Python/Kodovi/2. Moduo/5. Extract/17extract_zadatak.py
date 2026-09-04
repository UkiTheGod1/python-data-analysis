import pandas as pd

df = pd.read_csv("books.csv")

df[['catalog_shelf', 'catalog_row', 'catalog_number']] = df['catalog_position'].str.split("-", expand=True)

df.drop(['catalog_position'], axis=1, inplace=True)

print(df.head(30))