import pandas as pd

df = pd.read_excel('user_rentals.xlsx')

# Prikaz podataka 10. korisnika
print("Stats for the 10. user:\n", df.iloc[9].to_string())
print("")

# Prikaz prezimena 56. clana
print("Last name of the 56. user:", df.loc[55, 'lastname'])
print("")

# Prikaz broja telefona prvog clana
print("Phone number of the first user:", df.loc[0, 'phone'])
print("")

# Prikaz kolone broja telefona
print("All phone numbers:\n", df.phone.to_string())