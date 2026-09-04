import pandas as pd
from functions import *

df = pd.read_csv("movies.csv")
print(df.dtypes) 
# Proveravamo koji su tipovi kolona i vidimo da je box_office object i moracemo ga pretvoriti u broj (functions.py)

df_usa = extract_data("movies.csv").pipe(sort_data).pipe(filter_usa).pipe(remove_columns)
df_usa.to_excel("top10usa.xlsx", index=False)

df_russia = extract_data("movies.csv").pipe(sort_data).pipe(filter_russia).pipe(remove_columns)
df_russia.to_excel("top10russia.xlsx", index=False)

df_uk = extract_data("movies.csv").pipe(sort_data).pipe(filter_uk).pipe(remove_columns)
df_uk.to_excel("top10uk.xlsx", index=False)

df_korea = extract_data("movies.csv").pipe(sort_data).pipe(filter_korea).pipe(remove_columns)
df_korea.to_excel("top10korea.xlsx", index=False)