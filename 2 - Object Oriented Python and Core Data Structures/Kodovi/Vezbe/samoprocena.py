customers = [
    
    {
    
        "first_name": "Jovana",
        "last_name": "Sarcevic",
        "purhcases": [
            ("Laptop", 1200.0),
            ("Mouse", 50.0)

        ]
    },
    {
        "first_name": "Uros",
        "last_name": "Djordjic",
        "purhcases": [
            ("Phone", 500.0),
            ("TV", 700.0)
        ]
    },
    {
        "first_name": "Matija",
        "last_name": "Budincevic",
        "purhcases": [
            ("Soccer Ball", 40.0),
            ("Computer", 1000.0),
            ("T-Shirt", 100.0)
        ]
    },
    {
        "first_name": "Damjan",
        "last_name": "Lazic",
        "purhcases": [
            ("Xbox", 400.0),
            ("TV", 500.0)
        ]
    },
    {
        "first_name": "Nikola",
        "last_name": "Gutesa",
        "purhcases": [
            ("Phone", 1400.0),
            ("Keyboard", 120.0)
        ]
    },
]


def calculate_total_spent(customers):
    for customer in customers: 
        ime = customer["first_name"]
        prezime = customer["last_name"]
        kupovine = customer["purhcases"] 

        ukupno_potroseno = 0
        for kupovina in kupovine:
            naziv_prozivoda = kupovina[0]
            cena_proizvoda = kupovina[1]
            ukupno_potroseno += cena_proizvoda
        print(f"Kupac: {ime} {prezime}")
        print(f"Potrosen novac: ${ukupno_potroseno:.2f}")
        print(" ")

def total_items_purchased(customers):
    for customer in customers: 
        ukupno_kupovina = len(customer["purhcases"] )
        print(f"Kupac: {customer["first_name"]} {customer["last_name"]}")
        print(f"Ukupno kupovina: {ukupno_kupovina}")
        print(" ")

def most_expensive_purchase(customers):
    for customer in customers: 
        najskuplja_kupovina = max(customer["purhcases"], key=lambda x: x[1])
        print(f"Kupac: {customer["first_name"]} {customer["last_name"]}")
        print(f"Ukupno kupovina: {najskuplja_kupovina}")
        print(" ")

def report(customers):
    print("Ukupan potrosen novac za svakog kupca:")

    calculate_total_spent(customers)

    print("Ukupan kupovina svakog kupca:")

    total_items_purchased(customers)

    print("Najskuplja kupovina svakog kupca:")

    most_expensive_purchase(customers)

report(customers)
