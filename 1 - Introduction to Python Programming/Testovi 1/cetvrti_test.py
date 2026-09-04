ime_kupca = input("Unesite ime kupca: ")
samoglasnici = "aeiouAEIOU" 

def broj_samoglasnika(ime):
    broj = 0
    for slovo in ime:
        if slovo in samoglasnici:
            broj += 1
    return broj

while True:
    if broj_samoglasnika(ime_kupca) == 0:
        print("Ime ne sadrži samoglasnike.")
        break
    else:
        print(f"Broj samoglasnika u imenu {ime_kupca} je {broj_samoglasnika(ime_kupca)}")
        ime_kupca = input("Unesite ime kupca: ")
