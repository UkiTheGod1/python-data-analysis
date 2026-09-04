import pandas as pd
from preprocessing import *
data = pd.read_csv("books.csv")
df = prepare_data(data)

suspicious_values = df[(df['year_published'] < 1450) | (df['year_published'] > 2025)]
print(suspicious_values.filter(items=['catalog_position', 'title', 'author', 'year_published']))

suspicious_values = df[(df['total_copies'] < 0)]
print(suspicious_values.filter(items=['title', 'author', 'total_copies']))

suspicious_values = df[(df['times_borrowed'] < 0)]
print(suspicious_values.filter(items=['title', 'author', 'times_borrowed']))