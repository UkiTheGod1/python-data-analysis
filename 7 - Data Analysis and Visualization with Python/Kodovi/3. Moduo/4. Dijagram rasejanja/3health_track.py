import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("health_data.csv")

plt.figure(figsize=(10,6))
sns.regplot(data=df, x="age", y="blood_pressure", color="red", line_kws={"color": "purple"})
plt.title("Blood pressure based on age")
plt.xlabel("Age")
plt.ylabel("Blood pressure")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()