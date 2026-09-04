import pandas as pd

df = pd.read_csv("online_shop_with_duplicates.csv")
print(df.duplicated().sum())
print(df[df.duplicated()])

df.drop_duplicates(keep="first", inplace=True, ignore_index=False)

print(df[df.duplicated()])
