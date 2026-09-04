import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("student_performance_data.csv")
 
fig, axs = plt.subplots(2, 2, figsize=(14, 7))
 
# Scatter plot: study_hours vs grade
sns.regplot(data=df, x="study_hours", y="grade", line_kws={"color": "green"}, lowess=True, ax=axs[0, 0])
axs[0, 0].set_title("Study Hours vs Grade")
 
# Scatter plot: missed classes vs grade
sns.regplot(data=df, x="missed_classes", y="grade", line_kws={"color": "green"}, lowess=True, ax=axs[0, 1])
axs[0, 1].set_title("Missed Classes vs Grade")
 
# Scatter plot: sleep_hours vs grade
sns.regplot(data=df, x="sleep_hours", y="grade", line_kws={"color": "green"}, lowess=True, ax=axs[1, 0])
axs[1, 0].set_title("Sleep Hours vs Grade")
 
# Scatter plot: shoe_size vs grade
sns.regplot(data=df, x="shoe_size", y="grade", line_kws={"color": "green"}, lowess=True, ax=axs[1, 1])
axs[1, 1].set_title("Shoe Size vs Grade")
 
plt.suptitle("Relationships Between Student Characteristics and Grade", fontsize=16)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()