import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)

avg_price_per_genre = df.groupby("genre")["price"].mean().sort_values(ascending=False)
 
print(avg_price_per_genre)