# Metoda drop() se koristi za uklanjanje redova ili kolona iz DataFramea. 
# Poziva se nad DataFrame objektom, a može da prihvati sledeće parametre kojima se konfiguriše njeno ponašanje:

# columns – lista kolona ili redova koje je potrebno ukloniti;
# axis – podatak koji definiše da li se uklanjaju redovi ili kolone; postavljamo 0 za uklanjanje redova,
# a 1 za uklanjanje kolona;

# inplace – definiše da li će se promena obaviti nad izvornom strukturom ili nad njenom kopijom.

import pandas as pd

df = pd.read_excel("user_rentals.xlsx")

mask = (pd.Timestamp.today() - df['rental_date']) > pd.Timedelta(days=31)
new_df = df[mask]

new_df2 = new_df.sort_values(by='rental_date', ascending=True)

new_df2['overdue_days'] = (pd.Timestamp.today() - new_df2['rental_date']).dt.days - 31 

new_df2.drop(['address', 'gender', 'city', 'active'], axis = 1, inplace = True)
print(new_df2)