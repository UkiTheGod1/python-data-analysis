import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Monitor:
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size
    
    def to_dict(self):
        return {"Ime": self.name, "Cena": self.price, "Velicina": self.size}

class Proba: # Moj nacin resavanja

    monitor1 = Monitor("Samsung", 25000, 24)
    monitor2 = Monitor("Asus", 20000, 24)
    monitor3 = Monitor("Apple", 50000, 21)
    monitor4 = Monitor("DLL", 20000, 27)
    monitor5 = Monitor("JVC", 500000, 27)

    lista = [monitor1.to_dict(), monitor2.to_dict(), monitor3.to_dict(), monitor4.to_dict(), monitor5.to_dict()]

    df = pd.DataFrame(lista)

lista = [Monitor("Samsung", 35000, 24), Monitor("Asus", 18000, 24), Monitor("Apple", 50000, 21), \
         Monitor("Dell", 25000, 27), Monitor("JVC", 500000, 27)]

df = pd.DataFrame([x.to_dict() for x in lista])

fig, axs = plt.subplots(1, 2, figsize=(14,5))

sns.boxplot(data=df, x="Cena", ax=axs[0], color="skyblue")
axs[0].set_title("Sa outlierima (JVC dominira)")

sns.boxplot(data=df, x="Cena", ax=axs[1], color="lightgreen", showfliers=False)
axs[1].set_title("Bez outliera (Jasna kutija)")

plt.tight_layout()
plt.show()