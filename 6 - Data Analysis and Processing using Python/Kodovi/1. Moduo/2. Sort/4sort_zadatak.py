import pandas as pd
df = pd.read_csv('books.csv')

sorted_df_max = df.sort_values(by='page_count', ascending=False).iloc[0]['page_count']
sorted_df_min = df.sort_values(by='page_count').iloc[0]['page_count']
print("Najvise stranica koje knjiga ima:\n", sorted_df_max)
print("Najmanje stranica koje knjiga ima:\n", sorted_df_min)