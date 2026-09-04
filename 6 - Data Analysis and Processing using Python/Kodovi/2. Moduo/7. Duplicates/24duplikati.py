import pandas as pd
from preprocessing import *
data = pd.read_csv("books.csv")
df = prepare_data(data)
print(df.duplicated().sum()) # Suma svih duplikata - 7

print(df[df.duplicated()]) # Printujemo te duplikate (samo duplikate)

print(df[df.duplicated(keep=False)]) # Posto je keep=False onda printuje i originale i duplikate
# 'first' – prvo pojavljivanje reda se ignoriše, a sva ostala se markiraju kao duplikati (podrazumevana vrednost);
# 'last' – poslednje pojavljivanje reda se ignoriše, a sva ostala se markiraju kao duplikati.
# False – sva pojavljivanja se markiraju kao duplikati.
	
# df.drop_duplicates(keep='first', inplace=True, ignore_index=False) # Brisemo sve duplikate
# ignore_index = False znaci da se nece resetovati indexi nakon brisanja duplikata

print(df.duplicated(subset=['catalog_position']).sum()) # subset=['catalog_position'] proveravamo koliko se odredjena kolona

row1 = df.loc[546]
row2 = df.loc[1021]
differences = row1.compare(row2)
print(differences)

# Poredjenje dva reda

# df.drop_duplicates(subset=["catalog_position"],keep=first, inplace=True, ignore_index=False)
# brisanje duplikata po koloni