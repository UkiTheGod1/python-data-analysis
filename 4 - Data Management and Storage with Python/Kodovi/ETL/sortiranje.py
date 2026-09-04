import pandas as pd
 
# Extract data
df = pd.read_excel('user_rentals.xlsx')
 
# Filter data
mask = (pd.Timestamp.today() - df['rental_date']) > pd.Timedelta(days=31)
new_df = df[mask]
 
# Sort data
new_df2 = new_df.sort_values(by='rental_date', ascending=True) # Ne moramo staviti ascending jer je podrazumevano
 
print(new_df2)