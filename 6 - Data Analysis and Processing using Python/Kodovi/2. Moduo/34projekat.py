import pandas as pd
import numpy as np
import difflib
from preprocessing import *

data = pd.read_csv("books.csv")
df = prepare_data(data)

df["borrowing_per_copy"] = df["times_borrowed"] / df["total_copies"]
sorted_df = df.sort_values(by="borrowing_per_copy", ascending=False)
top_50 = sorted_df.head(50).to_string(columns=['title', 'times_borrowed', 'total_copies', 'borrowing_per_copy'])
print(top_50)