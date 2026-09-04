import pandas as pd
from preprocessing import prepare_data
data = pd.read_csv('books.csv')
df = prepare_data(data)

sections_grouped = df.groupby('section', observed=True).agg(
    times_borrowed_std = ('times_borrowed', 'std'),
    titles_counts = ('title', 'count')
)

sections_filtered = sections_grouped[sections_grouped['titles_counts'] >= 20]
sections_sorted = sections_filtered.sort_values(by='times_borrowed_std')
print(sections_sorted)