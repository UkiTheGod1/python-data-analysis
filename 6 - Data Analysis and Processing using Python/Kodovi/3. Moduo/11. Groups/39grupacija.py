import pandas as pd
from preprocessing import prepare_data
 
data= pd.read_csv('books.csv')
df = prepare_data(data)
 
grouped_data = df.groupby("genre")
 
for genre, group in grouped_data:
    print(f"Genre: {genre}")
    print(group)
    print("-" * 60)

# Pokazuje nam sve knjige svakog zanra odvojeno