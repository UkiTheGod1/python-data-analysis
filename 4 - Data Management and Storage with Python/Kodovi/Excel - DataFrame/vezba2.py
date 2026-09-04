import pandas as pd

df = pd.read_excel("user_rentals.xlsx")

df["id"] = df["id"].astype("int16")

print(df.dtypes)