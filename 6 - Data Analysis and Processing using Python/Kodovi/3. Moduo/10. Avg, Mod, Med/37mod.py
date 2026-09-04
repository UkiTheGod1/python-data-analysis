import pandas as pd
from preprocessing import prepare_data
data = pd.read_csv('books.csv')
df = prepare_data(data)

genre_mode = df["genre"].mode()
print(f"Genre mode: {", ".join(genre_mode.astype(str))}")

author_mode = df["author"].mode()
print(f"Author mode: {", ".join(author_mode.astype(str))}")