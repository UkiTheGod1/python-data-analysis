import pandas as pd
import numpy as np

df = pd.read_csv("D:/Python/libraries/smart_city_sensors_raw.csv")

# 1. Pretvaranje vrednosti
df["Datum_Očitavanja"] = pd.to_datetime(df["Datum_Očitavanja"], errors="coerce")

# 2. Proveravanje NaN
df.dropna(axis=0, how="any", inplace=True, ignore_index=True)

# 3. Proveravanje negativnih vrednosti
df_positive = df[(df["Vrednost"] > 0) & (df["Status_Baterije"] > 0)].copy() # Filtiranjem pravimo novi dataframe - .copy()

# 4. Proveravanje duplikata
df_positive.drop_duplicates(keep="first", inplace=True, ignore_index=True)

# 5. Ostalo

# 5.1 Parsiranje ID-a
def parse_text(text):
    parts = str(text).split("-")
     
    try:
        return int(parts[1]) 
    except (ValueError, IndexError):
        return np.nan
    
df_positive["Senzor_ID"] = df_positive["Senzor_ID"].apply(parse_text)
print(df_positive["Senzor_ID"].head())

# 5.2 Sortiranje vrednosti
df_sorted = df_positive.sort_values(by="Senzor_ID").reset_index(drop=True)

# 5.3 Promena naziva kolona
df_sorted.columns = ["id", "type", "value", "battery", "date", "location"]

# 5.4 Zaokruzivanje na 2 decimale kolone sa float vrednostima
df_sorted["value"] = df_sorted["value"].round(2)

df_sorted["battery"] = df_sorted["battery"].round(2)

# 5.5 Pretvaranje kolona u "category" zbog ustede memorije i ispravka ponavljajucih vrednosti kolona
df_sorted["location"] = df_sorted["location"].astype("category")

df_sorted["type"] = df_sorted["type"].astype("category").replace({"TEMP" : "Temperatura"})

# 6. Eksportovanje
df_sorted.to_csv("smart_city_sensors.csv", index=False)