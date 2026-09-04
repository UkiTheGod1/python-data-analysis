import pandas as pd
import numpy as np
df = pd.read_csv('online_store_data.csv')

# 1. Kolika je prosečna ocena proizvoda u online trgovini?
# Prvo mora extract da bismo mogli ostale funkcije
print(df['rating'].unique(), "\n")
def parse_rating(text):
    if pd.isna(text) or str(text).strip().lower() == "no value":
        return np.nan
    
    parts = str(text).split()

    try:
        return float(parts[0])
    except (ValueError, IndexError):
        return np.nan
df['rating'] = df['rating'].apply(parse_rating)

avg_rating = df['rating'].mean()
print(f"1. Average rating for products is {avg_rating:.2f}") # Formatirali radi izgleda

# 2. Koji je najčešći brend u online trgovini?
most_common_brand = df['brand'].mode()
print(f"2. Most common brand is {", ".join(most_common_brand.astype(str))}")


# 3. Koji je najprodavaniji brend u online trgovini?
most_sold_per_brand = df.groupby("brand")['quantity_sold'].sum().sort_values(ascending=False) # Grupisali i sortirali
brand_name = most_sold_per_brand.index[0]
brand_quantity = most_sold_per_brand.iloc[0]  # Izvukli ime i vrednost radi lepseg ispisa
print(f"3. Most sold brand is {brand_name} with {brand_quantity:.0f} units sold.")


# 4. Kolika je prosečna ocena proizvoda po kategorijama?
avg_category_rating = df.groupby("category")["rating"].mean()
print(f"\n4. Average ratings per categories:\n {avg_category_rating.to_string()}")


# 5. Kako izgleda popularnost proizvoda po bojama?
popularity_by_color = df.groupby("color")['quantity_sold'].sum().sort_values(ascending=False)
print(f"\n5. Popularity of products per color: \n {popularity_by_color.to_string()}")


# 6. Kojih su 5 najefikasnijih brendova po pitanju prodaje?
print("\n", df.dtypes) # quantity_in_stock je object, mora konverzija
df['quantity_in_stock'] = pd.to_numeric(df['quantity_in_stock'], errors="coerce")
grouped_brands = df.groupby("brand").agg({
    'quantity_sold': 'sum',
    'quantity_in_stock': 'sum'
})

grouped_brands['efficiency_ratio'] = grouped_brands['quantity_sold'] / (grouped_brands['quantity_sold'] + grouped_brands['quantity_in_stock'])
print(grouped_brands.sort_values(by='efficiency_ratio', ascending=False).head(5).to_string())

