import pandas as pd
import numpy as np
from preprocessing import *
data = pd.read_csv("books.csv")
df = prepare_data(data)

mask = (df['times_borrowed'] == 0) & (df['last_borrowed_date'].notna() | df['rating'].notna() | df['ratings_count'].notna())
df.loc[mask, 'last_borrowed_date'] = pd.NaT
df.loc[mask, 'rating'] = np.nan
df.loc[mask, 'ratings_count'] = np.nan

mask = (df['times_borrowed'] == 0) & (df['last_borrowed_date'].notna() | df['rating'].notna() | df['ratings_count'].notna())
suspicious_values  = df[mask]
print(suspicious_values.filter(items=['catalog_position', 'title', 'times_borrowed', 'last_borrowed_date', 'rating', 'ratings_count']))