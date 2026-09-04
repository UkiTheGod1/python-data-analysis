import pandas as pd
from preprocessing import prepare_data
data = pd.read_csv('books.csv')
df = prepare_data(data)

times_borrowd_per_author = df.groupby("author")["times_borrowed"].sum().sort_values(ascending=False)
print(times_borrowd_per_author.head(1).to_string())



times_borrowd_per_author = df.groupby("author").agg(
    all_borrowed = ('times_borrowed', 'sum'),
    avg_borrowed = ('times_borrowed', 'mean'),
    max_borrowed = ('times_borrowed', 'max'),
    max_rating = ('rating', 'max'),
    all_ratings = ('ratings_count', 'count'),
    avg_price = ('price', 'mean')
)

print(times_borrowd_per_author)