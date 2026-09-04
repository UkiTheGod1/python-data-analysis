import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
 
df = pd.DataFrame({
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Rentals': [34, 45, 50, 47, 60, 75, 38]
})
 
plt.figure(figsize=(10, 5))
 
sns.set_style(style="whitegrid")
sns.lineplot(data=df, x='Day', y='Rentals', marker='o', color='green')
 
plt.title("Book Rentals Throughout the Week")
plt.xlabel("Day")
plt.ylabel("Number of Books Rented")
plt.tight_layout()
plt.show()