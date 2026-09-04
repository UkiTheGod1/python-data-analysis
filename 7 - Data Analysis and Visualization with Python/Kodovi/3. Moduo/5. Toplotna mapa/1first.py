import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("student_performance_raw_data.csv")
 
corr_matrix = df.corr()
 
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap of Student Performance Data")
plt.tight_layout()
plt.show()