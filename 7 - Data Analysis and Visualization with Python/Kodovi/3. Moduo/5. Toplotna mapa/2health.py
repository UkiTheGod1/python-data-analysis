import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("health_data.csv")

corr_matrix = df.corr()

plt.figure(figsize=(10,6))
sns.heatmap(data=corr_matrix, cmap="coolwarm", annot=True, linewidths=0.5)
plt.title("Correlation Heatmap of Health Data")
plt.tight_layout()
plt.show()
