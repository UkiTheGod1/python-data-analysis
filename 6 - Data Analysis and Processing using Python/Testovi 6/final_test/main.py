import pandas as pd
import numpy as np
df = pd.read_csv("fit_trackr_data.csv")

print(df.dtypes) # Provera

# Pretprocessing:
# 1. Ekstrahovanje numerickih podataka iz Duration i Calories

def parse_numeric(text):
    if pd.isna(text):
        return np.nan
    
    parts = str(text).split()

    try:
        return float(parts[0])
    except (ValueError, IndexError):
        return np.nan
    
df['Duration'] = df['Duration'].apply(parse_numeric)
df['Calories'] = df['Calories'].apply(parse_numeric)
# Ovaj nacin sam najbolje savladao i iskoristio sam ga za ekstrahovanje

# 2. Uklanjanje potpunih duplikata

# print(df.duplicated().sum()) # Provera koliko ih ima
# print(df[df.duplicated()])   # Provera koji su to duplikati

df.drop_duplicates(keep="first", inplace=True) # keep="first" se podrazumeva, ali zarad preglednosti


# 3. Uklanjanje redova bez vrednosti u koloni Username

df.dropna(subset=['Username'],how='all', inplace=True)
print(df['Username'].isna().sum()) # Izbrisali smo nedostajuce vrednosti


# 4. Standardizovanje vrednosti u koloni Activity

print(df['Activity'].unique())
# Vidimo da postoje yoga-Yoga; walking-Walking-walk-Walk; swimm-swim-swimming
mapping = {
    "Yoga": "yoga",
    "Walking": "walking",
    "walk": "walking",
    "Walk": "walking",
    "swimm": "swimming",
    "swim": "swimming"
}

df['Activity'] = df['Activity'].replace(mapping).astype('category') # Zamenili i pretvorili u tip kategorije
# print(df['Activity'].unique()) Provera


# Zadaci:
# 1. Koliko je prosečno trajanje aktivnosti?

avg_activity_duration = df['Duration'].mean()
print(f"\nProsecno trajanje aktivnosti je {avg_activity_duration:.2f} minuta.")


# 2. Koje je najčešće raspoloženje korisnika nakon aktivnosti?
most_common_mood = df['Mood'].mode()
print(f"Najcesce raspolozenje nakon aktivnosti je '{", ".join(most_common_mood.astype(str))}'")

# 3. Koliko varira broj potrošenih kalorija?
calories_std = df['Calories'].std()
print(f"Variranje potrosenih kalorija je {calories_std:.2f}")


# 4. Kolika je razlika u broju godina između najstarijeg i najmlađeg korisnika iz središnjih 50% podataka?

q1 = df['Age'].quantile(0.25)
q3 = df['Age'].quantile(0.75)
iqr = q3 - q1

print(f"Razlika u godinama izmedju najmladjeg i najstarijeg korisnika je {iqr:.0f}")
