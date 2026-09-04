import pandas as pd
 
url = "https://music-top-charts-preview.s3.eu-north-1.amazonaws.com/itunes_top_20_2025-06-01.csv"
df = pd.read_csv(url)

print(df)