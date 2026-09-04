vreme = "sunce"
temperatura = 20


if vreme == "kiša":
    print("Ponesi kišobran!")
    if temperatura < 15:
        print("Obuci jaknu, hladno je!")
    else:
        print("Kiša pada, ali je toplo, jakna ti nije potrebna.")
elif vreme == "sunce":
        if temperatura > 25:
            print("Stavi naočare za sunce i obuci laganu odeću!")
        else:
            print("Uživaj u suncu, ali obuci nešto udobno!")
else:
    print("Vreme je oblačno, ne treba ti ništa specijalno.")