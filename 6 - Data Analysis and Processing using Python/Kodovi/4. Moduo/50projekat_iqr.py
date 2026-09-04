import pandas as pd
from preprocessing import prepare_data
data = pd.read_csv('books.csv')
df = prepare_data(data)

q1 = df['times_borrowed'].quantile(0.25)
q3 = df['times_borrowed'].quantile(0.75)
iqr = q3 - q1

iqr_books = df[(df['times_borrowed'] >= q1) & (df['times_borrowed'] <= q3)]

print("Typical:", iqr)
print("Books:", len(iqr_books))
print("Range:", q1, "-", q3)