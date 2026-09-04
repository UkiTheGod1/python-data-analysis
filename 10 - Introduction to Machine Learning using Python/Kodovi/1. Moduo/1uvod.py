import pandas as pd

df = pd.read_csv("D:/Python/libraries/reviews_unlabeled.csv")

print("Dataset shape (rows, columns):", df.shape)
 
print("\nMissing values per column:")
print(df.isna().sum())
 
print("\nSample reviews:")
print(df['review'].sample(5, random_state=42))
 
  
df['review_length'] = df['review'].astype(str).apply(lambda x: len(x.split()))
average_length = df['review_length'].mean()
print(f"\nAverage review length (in words): {average_length:.2f}")