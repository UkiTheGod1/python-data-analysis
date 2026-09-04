import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("student_performance_data.csv")
 
sns.scatterplot(data=df, x="study_hours", y="grade")
 
plt.title("Relationship Between Study Hours and Grade")
plt.xlabel("Study hours")
plt.ylabel("Grade")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()