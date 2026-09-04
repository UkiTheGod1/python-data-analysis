import pandas as pd
 
df = pd.read_csv('books.csv')
print(df['title'].to_string())   # Nakon df se ubaci u zagradi i navodnicima naziv kolone
print(" ")
print(df.title.to_string())      # Moze i na nacin odnosenja prema objektima