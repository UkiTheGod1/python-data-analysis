# Lista preferencija kupaca
kupci_preferencije = ['sport', 'tehnologija', 'kućni uređaji', 'sport', 'kućni uređaji', 'knjige']
 
for preferencija in kupci_preferencije:
    if preferencija == 'sport':
        print("Posebna ponuda za sportsku opremu!")
    elif preferencija == 'kućni uređaji':
        print("Specijalna ponuda za kućne uređaje!")
    elif preferencija == 'tehnologija':
        print("Posebna ponuda za tehnologiju!")
    else:
        print("Pogledajte naše nove proizvode!")