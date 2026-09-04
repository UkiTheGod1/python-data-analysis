import pandas as pd
from preprocessing import prepare_data
data = pd.read_csv('books.csv')
df = prepare_data(data)

print(df["section"].unique())
print(df["section"].value_counts())
print(df["section"].cat.categories)

# Children - Children's - Children's Fiction & Young Adult (YA) - Young Adult

mapping = {
    "Children's": "Children",
    "Children's Fiction": "Children",
    "Young Adult (YA)": "Young Adult"
}

df["section"] = df["section"].astype(object).replace(mapping).astype("category")

print(df["section"].value_counts())