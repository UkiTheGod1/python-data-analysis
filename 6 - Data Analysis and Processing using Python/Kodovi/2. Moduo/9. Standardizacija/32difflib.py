import difflib
 
products = [
    "Apple iPhone 12",
    "Apple iPhone 12 Pro",
    "Samsung Galaxy S21",
    "Samsung Galaxy S21 Ultra",
    "Google Pixel 5",
    "Gooogle Pixel 5", #input error
    "Google Pixl 5", #input error
    "OnePlus 9",
    "OnePlus 9 Pro"
]
 
query = "Google Pixel 5"
matches = difflib.get_close_matches(query, products, n=3, cutoff=0.8)
# n – maksimalan broj sličnih zapisa koje funkcija treba da vrati; podrazumevana vrednost je 3 (n mora biti veći od 0);
# cutoff – prag sličnosti koji određuje osetljivost pretrage; može imati vrednosti između 0 i 1, gde 0 označava potpunu različitost, 
# a vrednost 1 potpunu sličnost, odnosno identičnost; ukoliko, recimo, navedemo vrednost 0.8, to praktično znači da će se u finalnom 
# rezultatu naći samo oni elementi čija je sličnost za zadatom rečju 0.8 ili veća; podrazumevana vrednost je 0.6.
print(matches)