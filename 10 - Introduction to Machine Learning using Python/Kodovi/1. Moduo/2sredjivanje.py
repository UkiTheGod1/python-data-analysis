import pandas as pd

df = pd.read_csv("reviews_labeled.csv")

df = df.dropna()

df['sentiment'] = df['sentiment'].str.strip().str.lower()
 
print("Unique sentiment values after standardization:", df['sentiment'].unique())

df.to_csv("reviews_labeled_cleaned.csv", index=False)