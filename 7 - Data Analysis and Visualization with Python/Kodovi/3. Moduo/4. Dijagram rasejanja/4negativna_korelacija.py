import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("student_performance_data.csv")
sns.regplot(data=df, x="missed_classes", y="grade", line_kws={"color": "red"})
plt.title("Relationship Between Missed Classes and Grade")
plt.xlabel("Missed Classes")
plt.ylabel("Grade")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()