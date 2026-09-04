import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
df = prepare_data(data)
 
Q1 = df['page_count'].quantile(0.25)
Q2 = df['page_count'].quantile(0.50)
Q3 = df['page_count'].quantile(0.75)
 
def assign_quartile(pages):
    if pages <= Q1:
        return '1st quartile'
    elif pages <= Q2:
        return '2nd quartile'
    elif pages <= Q3:
        return '3rd quartile'
    else:
        return '4th quartile'
 
df['page_quartile'] = df['page_count'].apply(assign_quartile)
 
total_borrowed_per_quartile = df.groupby('page_quartile')['times_borrowed'].sum().reset_index()
 
print(total_borrowed_per_quartile)