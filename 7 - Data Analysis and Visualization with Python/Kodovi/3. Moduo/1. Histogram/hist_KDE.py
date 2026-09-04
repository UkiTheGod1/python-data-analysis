import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("call_durations.csv")

plt.figure(figsize=(10,6))
sns.histplot(df['call_duration_min'], bins=20, kde=True, color='red', edgecolor='maroon')

plt.xlabel("Call duration (in minutes)")
plt.ylabel("Number of call with that duration")
plt.tight_layout()
plt.show()

# Najcesca trajanja poziva - oko 6 minuta

# Ponekad je najbolji izbor – kombinacija oba. Onda znamo i koliko, i kako – u jednom potezu.