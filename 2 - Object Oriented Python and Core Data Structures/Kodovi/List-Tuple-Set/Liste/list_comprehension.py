# Define the initial list of prices
prices = [23.99, 19.50, 55.00, 48.75, 102.00, 33.40, 12.30]
 
# Create an empty list to store prices below 50
prices_below_50 = []
prices_below_50 = [price for price in prices if price < 50]

# U LISTU prices_below_50 mi dodajemo jednu vrednost (price) za svaki item u drugoj listi (for price in prices) pod uslovom (if price<50)
# Kod recnika, mora se navesti i kljuc i vrednost (key for key, value in dictionary.items() if value...) ako je kriterijum vezan za vrednost

# Print the list of prices below 50
print(prices_below_50)

