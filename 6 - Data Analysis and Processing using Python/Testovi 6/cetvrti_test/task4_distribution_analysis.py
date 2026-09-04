import pandas as pd
import numpy as np
df = pd.read_csv('online_store_data.csv')

# 1. Kolika je razlika između najbolje i najlošije ocenjenog televizora?

# print(df['rating'].unique()) - Moramo da ekstrahujemo
def parse_rating(text):
    if pd.isna(text) or str(text).strip().lower() == "no value":
        return np.nan
    
    parts = str(text).split()

    try:
        return float(parts[0])
    except (ValueError, IndexError):
        return np.nan
    
df['rating'] = df['rating'].apply(parse_rating) 
category_tv = df[df['category'] == 'TVs'] # Filtriramo samo televizore
max_rating = category_tv['rating'].max()
min_rating = category_tv['rating'].min()
print(f"1. Best TV rating: {max_rating}, worst TV rating: {min_rating}")
print(f"Difference in rating between best and worst rated TV is {(max_rating - min_rating):.2f}") 


# 2. U kom cenovnog rangu se nalazi najveći broj prodatih pametnih telefona?
smartphones = df[df['category'] == 'Smartphones'] # Filtriramo samo pametne telefone
q1 = smartphones['quantity_sold'].quantile(0.25)
q3 = smartphones['quantity_sold'].quantile(0.75)
iqr = q3 - q1

print(f"\n2. Smartphones quantity sold range: {q1} - {q3}")
print(f"IQR is {iqr}")


# 3. Kojih 5 brendova imaju najujednačenije ocene?
std_brand_ratings = df.groupby('brand')['rating'].std() # Grupisemo po brendu, a STD racunamo nad ocenama
top_5_brand = std_brand_ratings.sort_values().head(5)
print("\nTop 5 brands:\n", top_5_brand.to_string())


# 4. Da li broj dobijenih ocena (recenzija) zavisi od broja prodatih jedinica? 
# Da li više prodatih komada znači i veći broj recenzija ili obrnuto?

Q1 = df['quantity_sold'].quantile(0.25)
Q2 = df['quantity_sold'].quantile(0.50)
Q3 = df['quantity_sold'].quantile(0.75)

def assign_quartile_sold(sold):
    if sold <= Q1:
        return '1st quartile'
    elif sold <= Q2:
        return '2nd quartile'
    elif sold <= Q3:
        return '3rd quartile'
    else:
        return '4th quartile'
    
df['sold_quartile'] = df['quantity_sold'].apply(assign_quartile_sold)
total_ratings_per_quartile = df.groupby('sold_quartile')['num_of_ratings'].sum().reset_index()
print("\nNumber of ratings per quantity sold:\n", total_ratings_per_quartile)

# Obrnuto
Q1 = df['num_of_ratings'].quantile(0.25)
Q2 = df['num_of_ratings'].quantile(0.50)
Q3 = df['num_of_ratings'].quantile(0.75)

def assign_quartile_ratings(ratings):
    if ratings <= Q1:
        return '1st quartile'
    elif ratings <= Q2:
        return '2nd quartile'
    elif ratings <= Q3:
        return '3rd quartile'
    else:
        return '4th quartile'
    
df['rating_quartile'] = df['num_of_ratings'].apply(assign_quartile_ratings)
total_sold_per_quartile = df.groupby('rating_quartile')['quantity_sold'].sum().reset_index()
print("\nQuantity sold per number of ratings:\n", total_sold_per_quartile)

# Pristupio sam na oba nacina i prema ispisu zakljucujem da su oba tacna:
# Vise ocena -> Vise prodatih komada ; Vise prodatih komada -> Vise ocena
