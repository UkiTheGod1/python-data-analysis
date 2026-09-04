import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_distribution(df, column, title=None, xlabel=None):
    plt.figure(figsize=(10, 5))
    sns.kdeplot(df[column], fill=True, color="skyblue")
    plt.title(title or f"Distribution of {column}")
    plt.xlabel(xlabel or column)
    plt.ylabel("Count")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()
    return None

    

