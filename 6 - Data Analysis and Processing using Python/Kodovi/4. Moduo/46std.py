import pandas as pd
from preprocessing import prepare_data
df= pd.read_csv('books.csv')


std_year = df['year_published'].std()
mean_year = df['year_published'].mean()
 
print(std_year)
print(mean_year)

# Prosek 1871, devijacija 115, znaci od 1756 do 1986 se nalaze vrednosti najvise