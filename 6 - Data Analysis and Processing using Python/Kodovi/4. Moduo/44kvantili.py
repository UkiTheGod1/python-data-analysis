import pandas as pd
from preprocessing import prepare_data
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
# 1% najgore ocenjenih knjiga
p01 = df['rating'].quantile(0.01)
 
bottom_1_percent_books = df[df['rating'] <= p01]
 
print(bottom_1_percent_books.filter(items=['title', 'rating']).sort_values(by=['rating'], ascending=False).to_string())


# 5% najbolje ocenjenih knjiga
p95 = df['rating'].quantile(0.95)
 
top_5_percent_books = df[df['rating'] >= p95]
 
print(top_5_percent_books.filter(items=['title', 'rating']).sort_values(by=['rating'], ascending=False).to_string())
