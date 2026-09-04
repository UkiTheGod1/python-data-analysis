import matplotlib.pyplot as plt
 
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
rentals = [34, 45, 50, 47, 60, 75, 38]
 
plt.figure(figsize=(10, 5)) # Definišemo širinu i visinu kompletnog grafikona (u inčima).
plt.plot(days, rentals, marker='o', color='green') # Dodajemo kružiće kao prikaz vrednosti podataka, postavljamo boju linije na zelenu.
 
plt.title("Book Rentals Throughout the Week") # Definišemo da naziv kompletnog grafika bude Book Rentals Throughout the Week.
plt.xlabel("Day") # Postavljamo da oznaka X-ose bude Day.
plt.ylabel("Number of Books Rented") # Određujemo da oznaka Y-ose bude Number of Books Rented.
plt.grid(True) # Prikazujemo mrežu u pozadini grafikona, radi bolje čitljivosti.
plt.tight_layout() # Automatski raspoređujemo elemente (naslova, osa, oznaka) da se ne preklapaju.
plt.show() # Prikazujemo grafikon unutar zasebnog prozora.