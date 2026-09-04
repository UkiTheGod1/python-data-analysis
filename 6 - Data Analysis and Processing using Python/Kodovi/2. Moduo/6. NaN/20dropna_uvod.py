import pandas as pd
from preprocessing import prepare_data
 
data = pd.read_csv('books.csv')
 
df = prepare_data(data)

# axis – određuje osu po kojoj se uklanjaju nedostajuće vrednosti: axis=0 za redove, axis=1 za kolone;
# how – uslov za uklanjanje; any znači da se red ili kolona uklanjaju ukoliko poseduju makar jednu nedostajuću vrednost; all znači da sve vrednosti moraju biti nedostajuće da bi se red ili kolona uklonili;
# thresh – definiše minimalan broj nenedostajućih vrednosti koji red ili kolona mora imati da ne bi bio uklonjen; ne može se kombinovati sa parametrom how;
# subset – lista kolona koje je potrebno proveriti pri odlučivanju o uklanjanju reda;
# inplace – određuje da li se modifikacija izvršava direktno nad originalnim skupom ili ne.

df.dropna(axis=1, thresh=1500, inplace=True) # Brisu se kolone koje imaju manje od 1500 NEnedostajucih vrednosti (vrednosti koje postoje)

rows_count = df.shape[0]
df.dropna(axis=1, thresh=(rows_count*0.75), inplace=True) # Brise kolone koje imaju manje od 75% nenedostajucih vrednosti