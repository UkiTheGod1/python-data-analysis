import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("student_performance_data.csv")
sns.regplot(data=df, x="sleep_hours", y="grade", lowess=True, line_kws={"color": "purple"})
plt.title("Relationship Between Sleep Hours and Grade")
plt.xlabel("Sleep Hours")
plt.ylabel("Grade")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()