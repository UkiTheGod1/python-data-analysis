import pandas as pd
from preprocessing import prepare_data

data = pd.read_csv("books.csv")
df = prepare_data(data)

rows = df.shape[0]
df.dropna(axis=1, thresh=(rows*0.3), inplace=True)
print(df.dtypes)
