import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
data = {
    'mean': df['ratings_count'].mean(),
    'median':df['ratings_count'].median(),
    'mode':df['ratings_count'].mode().tolist(),
    'sum':df['ratings_count'].sum(),
    'count':df['ratings_count'].count(),
    'min':df['ratings_count'].min(),
    'max':df['ratings_count'].max()
}
 
for key, value in data.items():
    print(f"{key}: {value}")