import pandas as pd

df = pd.read_csv('books.csv')

missing_per_row = df.isna().sum(axis=1)
missing_per_row_sorted = missing_per_row.sort_values(ascending=False)
print(missing_per_row_sorted.head(30))

selected_df = df.iloc[[212, 75, 698, 152]]
print(selected_df)

df.drop([212, 75, 698, 152], axis=0, inplace=True)

missing_rows=df[df[['title', 'author']].isna().all(axis=1)]
print(missing_rows)

df.drop([113, 926, 1394], axis=0, inplace=True)


# Sve smo ovo mogli sa 
# df.dropna(axis=0, thresh=df.shape[1] - 18, inplace=True)
# df.dropna(subset=['title','author'],how='all', inplace=True)