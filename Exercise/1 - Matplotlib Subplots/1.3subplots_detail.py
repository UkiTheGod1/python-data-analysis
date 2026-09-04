import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Dan': ['Pon', 'Uto', 'Sre', 'Čet', 'Pet', 'Sub', 'Ned'],
    'Temp_C': [22, 25, 28, 15, 18, 32, 35],
    'Sladoled_Prodato': [120, 150, 200, 50, 70, 300, 450],
    'Tip_Dana': ['Radni', 'Radni', 'Radni', 'Radni', 'Radni', 'Vikend', 'Vikend']
}

df = pd.DataFrame(data)

fig, axs = plt.subplots(1, 2, figsize=(15,7))

sns.lineplot(df, x = "Dan", y = "Temp_C", color="red", marker="v", ax=axs[0])
axs[0].tick_params(axis='y', labelcolor='red') # Pravimo zasebnu y osu
axs[0].set_ylabel("Temperatura") 
axs2 = axs[0].twinx() # Pravimo "klona"
sns.lineplot(df, x = "Dan", y = "Sladoled_Prodato", color="blue", marker="o", ax=axs2)
axs2.tick_params(axis='y', labelcolor='blue') # Pravimo zasebnu y osu
axs2.set_ylabel("Broj prodatih sladoleda")

axs[0].set_title("Odnos temperature i broja prodatih sladoleda sa danom", color="purple", fontsize=15)
axs[0].set_xlabel("Dan u nedelji")
axs[0].grid(axis="y", linestyle="--", alpha=0.5)

df_group = df.groupby("Tip_Dana").agg(
    prosek = ("Sladoled_Prodato", "mean")).reset_index().sort_values(by="prosek", ascending=False)

sns.barplot(df_group, x = "Tip_Dana", y = "prosek", color="green", edgecolor="black", width=0.5, ax=axs[1])
axs[1].set_title("Prosecan broj prodatih sladoleda po tipu dana", color="green", fontsize=15)
axs[1].set_xlabel("Tip dana (Radni vs Vikend)")
axs[1].set_ylabel("Prosecan broj brodatih sladoleda")
axs[1].bar_label(axs[1].containers[0], padding=3) # Prikazuje vrednosti

plt.tight_layout(pad=3.0, w_pad=5.0)
plt.show()