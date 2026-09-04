import pandas as pd

df = pd.read_excel("user_rentals.xlsx")

mask = (pd.Timestamp.today() - df['rental_date']) > pd.Timedelta(days=31)
new_df = df[mask]

new_df2 = new_df.sort_values(by="rental_date", ascending = False) # Naglasili od nazad
print(new_df2)