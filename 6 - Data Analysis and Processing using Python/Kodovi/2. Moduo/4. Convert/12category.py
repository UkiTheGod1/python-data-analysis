import pandas as pd
df = pd.read_csv('books.csv')
print(df.memory_usage(deep=True))
df['genre'] = df['genre'].astype('category')
df['section'] = df['section'].astype('category')
df['language'] = df['language'].astype('category')
print(df.memory_usage(deep=True)) # Pregled dokaz da se manje memorije koristi na ovaj nacin