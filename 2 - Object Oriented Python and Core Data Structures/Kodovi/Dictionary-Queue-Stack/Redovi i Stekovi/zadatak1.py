q = []

def add_to_queue(name):
    q.append(name)

def serve_customer():
    if q:
        next_customer = q.pop(0)
        print(f'Usluzen/a je {next_customer}.')
    else:
        print('Nema vise kupaca u redu.')

def display_queue():
    if q:
        print('Kupci koji su i dalje u redi su:', q)
    else:
        print('Nema vise kupaca u redu.')

def main_program():
    while True:
       print('\nBirajte opciju za rad sa redom: ')
       print('1. Dodavanje kupca u red')
       print('2. Usluzivanje kupca')
       print('3. Prikazivanje trenutnog reda')
       print('4. Zaustavljanje programa')
       odabir_opcije = int(input("Unesite zeljeni broj: "))
       if odabir_opcije == 1:
           ime = input('Unesite ime kupca: ')
           add_to_queue(ime)
           print('Dodat je kupac', ime)
       elif odabir_opcije == 2:
           serve_customer()
       elif odabir_opcije == 3:
           display_queue()
       elif odabir_opcije == 4:
           print("Program prekinut.")
           break
       else:
           print("Molim vas unesite ispravnu opciju")


add_to_queue("Marko")
add_to_queue("Milica")
add_to_queue("Zivojin")

main_program()
