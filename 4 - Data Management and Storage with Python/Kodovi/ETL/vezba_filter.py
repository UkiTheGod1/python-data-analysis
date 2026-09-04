import pandas as pd

df = pd.read_excel("user_rentals.xlsx")

mask = (df['gender'] == "female") & (df['active'] == 'Y')
new_df = df[mask]
print(new_df.to_string())