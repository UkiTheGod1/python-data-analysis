import pandas as pd
from preprocessing import prepare_data
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
price_stats = df.groupby('genre').agg(
    avg_price=('price', 'mean'),
    median_price=('price', 'median')
)
 
print(price_stats)