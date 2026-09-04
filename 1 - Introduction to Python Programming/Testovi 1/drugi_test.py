kupci_ponedeljak = int(input("Unesi broj kupaca za ponedeljak: "))
kupci_utorak = int(input("Unesi broj kupaca za utorak: "))
kupci_sreda = int(input("Unesi broj kupaca za sredu: "))
kupci_cetvrtak = int(input("Unesi broj kupaca za cetvrtak: "))
kupci_petak = int(input("Unesi broj kupaca za petak: "))
kupci_subota = int(input("Unesi broj kupaca za subotu: "))
kupci_nedelja = int(input("Unesi broj kupaca za nedelju: "))

ukupni_kupci = kupci_ponedeljak + kupci_utorak + kupci_sreda + kupci_cetvrtak + kupci_petak + kupci_subota + kupci_nedelja
print(f"Ukupan broj kupaca za celu nedelju je {ukupni_kupci}")

kupci_vikend = kupci_subota + kupci_nedelja
kupci_radni_dani = ukupni_kupci - kupci_vikend
print(f"Ukupan broj kupaca za radne dane je {kupci_radni_dani}")
print(f"Ukupan broj kupaca za vikend je {kupci_vikend}")

print("Nedelja je bila bolji prodajni dan od subote") if kupci_nedelja > kupci_subota else print("Subota je bila bolji prodajni dan od nedelje")
# Pise "koristiti jednolinijski if" pa je zato dugacka linija i nisam je presecao

if kupci_radni_dani > kupci_vikend:
    print("Ukupan broj kupaca za radne dane je veci nego za vikend")
else:
    print("Ukupan broj kupaca za vikend je veci nego za radne dane")

if kupci_subota > 100 and kupci_nedelja > 100:
    print("Oba dana vikenda su imala vise od 100 kupaca")
elif kupci_subota > 100 or kupci_nedelja > 100:
    print("Samo jedan dan vikenda je imao vise od 100 kupaca")
else:
    print("Nijedan dan vikenda nije imao vise od 100 kupaca")
