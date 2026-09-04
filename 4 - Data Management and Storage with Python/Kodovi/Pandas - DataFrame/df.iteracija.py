import pandas as pd
 
df = pd.read_csv('books.csv')
 
#for index, row in df.iterrows():   # Sve
 #   print(row.to_string())

#for index, row in df.iterrows():   # Odredjeni podatak
  #  print(row["title"])

for index, row in df.iterrows():   # Moze i ovako
    print(row[1])
