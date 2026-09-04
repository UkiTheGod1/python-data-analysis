import pandas as pd
import difflib 
df = pd.read_csv('books.csv')


genres = df["genre"].dropna().unique()

list = {}

for genre in genres:
    matches = difflib.get_close_matches(genre, genres)
    if len(matches) > 1:
        list[genre] = sorted(matches)
 
for key, value in list.items():
    print(f"'{key}' : {value}")
