import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
df = pd.read_csv("health_data.csv")
 
features = ['age', 'height', 'weight', 'bmi', 'daily_steps', 'sleep_hours', 'alcohol_units', 'exercise_minutes']
 
fig, axs = plt.subplots(2, 4, figsize=(20, 10))
axs = axs.flatten()
 
for i, feature in enumerate(features):
    sns.regplot(data=df, x=feature, y='blood_pressure', ax=axs[i], scatter_kws={'alpha': 0.6}, line_kws={'color': 'red'}, lowess=True)
    axs[i].set_title(f"Blood Pressure vs {feature}")
    axs[i].grid(True, linestyle='--', alpha=0.4)
 
plt.suptitle("How Patient Characteristics Affect Blood Pressure", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()