import pandas as pd
from preprocessing import prepare_data
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
p99 = df['page_count'].quantile(0.99)
 
longest_1_percent = df[df['page_count'] >= p99]
 
print(longest_1_percent.filter(items=['title', 'page_count']).sort_values(by=['page_count'], ascending=False).to_string())