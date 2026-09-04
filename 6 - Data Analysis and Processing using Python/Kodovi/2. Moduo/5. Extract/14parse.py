import pandas as pd
import numpy as np
df = pd.read_csv('books.csv')

# Ako je vrednost Na ili je kada se napise malim slovima i bez whitespace na pocetku i kraju jednaka
# "no rating available", vratice nan (ignorise je)
def parse_rating(text):
    if pd.isna(text) or str(text).strip().lower() == "no rating available":
        return np.nan
     
    parts = str(text).split() # Splituje vrednost na delove teksta npr ["4.14", "out", "of", "5", "stars"]
     
    try:
        return float(parts[0]) # Uzmimamo prvi clan te liste parts i stavljamo ga da je float
    except (ValueError, IndexError): # Ako se desi neki error da isto vrati NaN
        return np.nan
df['rating'] = df['rating'].apply(parse_rating)  # Aplajujemo ovu celu funkciju na df['rating']
print(df.filter(items=['title', 'author', 'rating']).head(30))