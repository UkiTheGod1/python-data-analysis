iznos = float(input("Unesi iznos porudzbine: "))

if iznos < 100:
    print("Ne dobijate poput")
else:
    if iznos <= 500:
        print("Dobijate 5% popusta")
    else:
        if iznos <= 1000:
            print("Dobijate 10% popusta")
        else:  
            if iznos <= 2000:
                print("Dobijate 15% popusta")
            else:
                print("Dobijate 20% popusta")


# if iznos < 100:
    # print("Ne dobijate poput")
# elif iznos <= 500:
    # print("Dobijate 5% popusta")
# elif iznos <= 1000:
    # print("Dobijate 10% popusta")
# elif iznos <= 2000:
    # print("Dobijate 15% popusta")
# else:
    # print("Dobijate 20% popusta")

# Kod bi mogao i ovako da se napise, a da bude ispravan, ugnezditi nije potrebno ovde jer nemamo dva faktora