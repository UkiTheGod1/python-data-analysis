import pandas as pd
import numpy as np

df = pd.read_csv("books.csv")

def parse_ratings_counts(text):
    if pd.isna(text) or str(text).strip().lower() == "no reviews":
        return np.nan
    
    parts = str(text).split()

    try:
        return int(parts[0])
    except (ValueError, IndexError):
        return np.nan
    
df['ratings_count'] = df['ratings_count'].apply(parse_ratings_counts)
filtered_df = df.filter(items=['title', 'author', 'ratings_count'])
print(filtered_df.head(50))

def parse_price(text):
    if pd.isna(text) or str(text).strip().lower() == "price not available":
        return np.nan
    try:
        price_str = str(text).replace('$', '').strip()
        return float(price_str)
    except ValueError:
        return np.nan
df['price'] = df['price'].apply(parse_price)
print(df.filter(items=['title', 'price']).head(30))